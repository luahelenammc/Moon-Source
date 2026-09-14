from __future__ import annotations

import re
from collections import defaultdict
from difflib import SequenceMatcher

from .models import DocumentRecord, Evidence, Finding, ObjectRecord, SourceRef


def _norm(text: str) -> str:
    return re.sub(r"\W+", " ", text.lower()).strip()


def _tokens(text: str) -> set[str]:
    return set(_norm(text).split())


def _evidence(obj: ObjectRecord, role: str) -> Evidence:
    return Evidence(source=obj.source, role=role, object_id=obj.object_id)


def _date_key(value: str) -> str:
    match = re.search(r"(\d{4}-\d{2}-\d{2})", value)
    return match.group(1) if match else "0000-00-00"


def _finding(
    index: int,
    kind: str,
    severity: str,
    title: str,
    reason: str,
    evidence: list[Evidence],
    action: str,
    uncertainty: str = "",
    detection_mode: str = "deterministic",
    confidence: float | None = None,
) -> Finding:
    return Finding(
        finding_id=f"F-{index:03d}",
        finding_type=kind,
        severity=severity,
        title=title,
        reason=reason,
        evidence=evidence,
        proposed_action=action,
        uncertainty=uncertainty,
        detection_mode=detection_mode,
        confidence=confidence,
    )


def run_diagnostics(documents: list[DocumentRecord], objects: list[ObjectRecord]) -> list[Finding]:
    findings: list[Finding] = []
    number = 1

    by_hash: defaultdict[str, list[DocumentRecord]] = defaultdict(list)
    for document in documents:
        by_hash[document.sha256].append(document)
    for same_hash in by_hash.values():
        if len(same_hash) < 2:
            continue
        refs = [
            Evidence(
                source=_doc_source(document),
                role="exact duplicate document",
            )
            for document in same_hash
        ]
        findings.append(
            _finding(
                number,
                "duplicate",
                "medium",
                "Exact duplicate material",
                "Two files have identical content and should not both act as independent authority.",
                refs,
                "Keep one canonical source and demote the other to a linked mirror or archive after human review.",
            )
        )
        number += 1

    for left_index, left in enumerate(documents):
        for right in documents[left_index + 1 :]:
            if left.sha256 == right.sha256:
                continue
            left_tokens, right_tokens = _tokens(left.text), _tokens(right.text)
            if not left_tokens or not right_tokens:
                continue
            overlap = len(left_tokens & right_tokens) / max(1, len(left_tokens | right_tokens))
            ratio = SequenceMatcher(None, _norm(left.text), _norm(right.text)).ratio()
            if overlap >= 0.82 or ratio >= 0.92:
                findings.append(
                    _finding(
                        number,
                        "near_duplicate",
                        "low",
                        "Near-duplicate material",
                        f"The files share a high proportion of normalized content (token overlap {overlap:.2f}; sequence similarity {ratio:.2f}).",
                        [
                            Evidence(_doc_source(left), "near-duplicate document"),
                            Evidence(_doc_source(right), "near-duplicate document"),
                        ],
                        "Compare the two sources and merge or explicitly differentiate them after human review.",
                        "Similarity does not prove that every repeated sentence has the same authority.",
                        detection_mode="heuristic",
                        confidence=round(max(overlap, ratio), 2),
                    )
                )
                number += 1

    decisions: defaultdict[str, list[ObjectRecord]] = defaultdict(list)
    for obj in objects:
        if obj.kind == "decision":
            decisions[obj.object_key or obj.object_id].append(obj)
    for key, group in decisions.items():
        values = {_norm(obj.value) for obj in group}
        if len(group) < 2 or len(values) < 2:
            continue
        ordered = sorted(group, key=lambda item: _date_key(item.date))
        latest = ordered[-1]
        findings.append(
            _finding(
                number,
                "contradiction",
                "high",
                f"Conflicting decisions for {key}",
                "Multiple decision records use the same decision key but prescribe different values.",
                [_evidence(obj, "conflicting decision") for obj in group],
                f"Treat {latest.source.path} as the current candidate only if its authority is confirmed; mark the older decision historical rather than deleting it.",
                "Date ordering is a useful signal, not a substitute for explicit authority.",
                detection_mode="deterministic",
                confidence=0.92,
            )
        )
        number += 1
        for older in ordered[:-1]:
            if older.status.lower() in {"active", "current", "outdated", "stale"} or older.supersedes:
                findings.append(
                    _finding(
                        number,
                        "stale_authority",
                        "medium",
                        f"Older authority remains operational for {key}",
                        f"{older.source.path} is older than {latest.source.path} but is still marked or formatted as usable authority.",
                        [_evidence(older, "older decision"), _evidence(latest, "newer decision")],
                        "Demote the older source to historical context and link the current decision after approval.",
                    )
                )
                number += 1

    for obj in objects:
        authority_missing = obj.authority.strip().lower() in {"", "unknown", "tbd", "none", "unassigned"}
        owner_missing = obj.owner.strip().lower() in {"", "unknown", "tbd", "none", "unassigned"}
        if authority_missing:
            findings.append(
                _finding(
                    number,
                    "unclear_authority",
                    "medium",
                    f"Authority unclear for {obj.object_id}",
                    "The extracted object has no identifiable governing source or names an unknown authority.",
                    [_evidence(obj, "object without authority")],
                    "Route the object to a human decision and record the governing source before treating it as current instruction.",
                )
            )
            number += 1
        if owner_missing:
            findings.append(
                _finding(
                    number,
                    "missing_owner",
                    "low" if obj.kind != "decision" else "medium",
                    f"Owner unclear for {obj.object_id}",
                    "The object has no accountable owner in the extracted corpus.",
                    [_evidence(obj, "object without owner")],
                    "Assign an accountable owner or explicitly record that the ownership decision is unresolved.",
                )
            )
            number += 1
        if obj.kind == "decision" and obj.attributes.get("orphaned", "").lower() in {"yes", "true"}:
            findings.append(
                _finding(
                    number,
                    "orphaned_decision",
                    "high",
                    f"Orphaned decision {obj.object_id}",
                    "The corpus explicitly marks this decision as orphaned, so it has no safe route into current source-of-truth context.",
                    [_evidence(obj, "orphaned decision")],
                    "Keep the decision visible as unresolved history and require a human owner/authority decision before activation.",
                )
            )
            number += 1
        if obj.kind == "scope_jurisdiction_leak":
            findings.append(
                _finding(
                    number,
                    "scope_jurisdiction_leak",
                    "high",
                    f"Scope leak in {obj.object_id}",
                    "The corpus contains an instruction that crosses the stated responsibility boundary.",
                    [_evidence(obj, "scope leak")],
                    "Quarantine the instruction, define the owning scope and require explicit approval before propagation.",
                )
            )
            number += 1

    return findings

def _doc_source(document: DocumentRecord):
    return SourceRef(path=document.path, line_start=1, line_end=1, section=document.title, quote=document.title)
