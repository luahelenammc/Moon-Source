from __future__ import annotations

import re
from collections import defaultdict

from .models import DocumentRecord, ObjectRecord, SourceRef

METADATA_RE = re.compile(r"^\s*([A-Za-z][A-Za-z0-9 _/-]*)\s*:\s*(.*?)\s*$")
OBJECT_RE = re.compile(r"^\s*(Claim|Rule|Decision|Fact|Scope leak)\s*:\s*(.+?)\s*$", re.I)
ID_KEYS = {
    "claim": "Claim ID",
    "rule": "Rule ID",
    "decision": "Decision ID",
    "fact": "Fact ID",
    "scope leak": "Scope Leak ID",
}


def _clean(value: str) -> str:
    return value.strip().strip("`")


def _metadata(lines: list[str]) -> dict[str, str]:
    result: dict[str, str] = {}
    for line in lines:
        match = METADATA_RE.match(line)
        if match:
            result[match.group(1).strip().lower()] = _clean(match.group(2))
    return result


def _get(meta: dict[str, str], *keys: str) -> str:
    for key in keys:
        value = meta.get(key.lower(), "")
        if value:
            return value
    return ""


def extract_objects(document: DocumentRecord) -> list[ObjectRecord]:
    lines = document.text.splitlines()
    meta = _metadata(lines)
    objects: list[ObjectRecord] = []
    section = ""
    counts: defaultdict[str, int] = defaultdict(int)
    for line_no, line in enumerate(lines, start=1):
        if line.startswith("#"):
            section = line.lstrip("#").strip()
        match = OBJECT_RE.match(line)
        if not match:
            continue
        label = match.group(1).strip().lower()
        value = _clean(match.group(2))
        counts[label] += 1
        object_id = _get(meta, ID_KEYS[label], f"{label} id")
        if not object_id or counts[label] > 1:
            object_id = f"{label.replace(' ', '-')}-{document.sha256[:8]}-{counts[label]}"
        if label == "scope leak":
            kind = "scope_jurisdiction_leak"
        else:
            kind = label
        key = _get(meta, "decision key", "object key", "topic")
        if not key and label == "decision":
            key = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")[:60]
        attributes = dict(meta)
        attributes["section"] = section
        source = SourceRef(
            path=document.path,
            line_start=line_no,
            line_end=line_no,
            section=section,
            quote=line.strip(),
        )
        objects.append(
            ObjectRecord(
                object_id=object_id,
                kind=kind,
                text=value,
                source=source,
                object_key=key,
                owner=_get(meta, "owner", "responsible", "decision owner"),
                authority=_get(meta, "authority", "governing source", "source of truth"),
                scope=_get(meta, "scope", "applies to"),
                status=_get(meta, "status", "state"),
                date=_get(meta, "decision date", "date", "last updated", "updated"),
                supersedes=_get(meta, "supersedes", "replaces"),
                value=value,
                attributes=attributes,
            )
        )
    return objects


def extract_all(documents: list[DocumentRecord]) -> list[ObjectRecord]:
    objects: list[ObjectRecord] = []
    for document in documents:
        objects.extend(extract_objects(document))
    return objects
