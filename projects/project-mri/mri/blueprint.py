from __future__ import annotations

from collections import defaultdict

from .diagnostics import _date_key
from .models import DocumentRecord, Finding, ObjectRecord


def build_blueprint(documents: list[DocumentRecord], objects: list[ObjectRecord], findings: list[Finding]) -> dict:
    decisions: defaultdict[str, list[ObjectRecord]] = defaultdict(list)
    for obj in objects:
        if obj.kind == "decision":
            decisions[obj.object_key or obj.object_id].append(obj)

    historical_paths = {
        evidence.source.path
        for finding in findings
        if finding.finding_type == "stale_authority"
        for evidence in finding.evidence
    }
    duplicate_paths = {
        evidence.source.path
        for finding in findings
        if finding.finding_type in {"duplicate", "near_duplicate"}
        for evidence in finding.evidence
    }
    governing_sources = []
    human_decisions = []
    for key, group in sorted(decisions.items()):
        latest = sorted(group, key=lambda item: _date_key(item.date))[-1]
        if latest.authority and latest.authority.lower() not in {"unknown", "tbd"}:
            governing_sources.append(
                {
                    "decision_key": key,
                    "candidate": latest.source.path,
                    "authority": latest.authority,
                    "owner": latest.owner or "unassigned",
                    "basis": "latest dated decision with a named authority",
                    "approval_required": True,
                }
            )
        else:
            human_decisions.append(
                {
                    "decision_key": key,
                    "candidate": latest.source.path,
                    "question": "Who owns and governs this decision?",
                    "approval_required": True,
                }
            )

    for obj in objects:
        if obj.kind in {"claim", "fact", "rule"} and (
            not obj.authority or obj.authority.lower() in {"unknown", "tbd"}
        ):
            human_decisions.append(
                {
                    "object_id": obj.object_id,
                    "candidate": obj.source.path,
                    "question": "Should this object enter active context, and under which authority?",
                    "approval_required": True,
                }
            )

    return {
        "governing_sources": governing_sources,
        "historical_sources": sorted(historical_paths),
        "merge_candidates": sorted(duplicate_paths),
        "human_decisions": human_decisions,
        "principle": "The blueprint proposes authority and history; it never silently rewrites the corpus.",
        "document_count": len(documents),
        "object_count": len(objects),
    }


def build_repair_plan(findings: list[Finding]) -> list[dict]:
    return [
        {
            "finding_id": finding.finding_id,
            "finding_type": finding.finding_type,
            "action": "propose",
            "target": sorted({item.source.path for item in finding.evidence}),
            "change": finding.proposed_action,
            "requires_human_approval": True,
            "mutation_applied": False,
        }
        for finding in findings
    ]

# MOON-SOURCE-PUBLIC-STAMP
# 🌙 Moon Source · Lua Helena Moon Martins Cardoso (Moon) + Áurion (AI-assisted) · Licensing: https://github.com/luahelenammc/Moon-Source/blob/main/LICENSING.md · Use & attribution: https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md · Full source: https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip · Questions, suggestions, or proposals? Feel free to contact me at LuaHelenaMMC@gmail.com.
