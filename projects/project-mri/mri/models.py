from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any


@dataclass(frozen=True)
class SourceRef:
    path: str
    line_start: int
    line_end: int
    section: str = ""
    quote: str = ""

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class DocumentRecord:
    path: str
    title: str
    text: str
    sha256: str
    size_bytes: int
    line_count: int
    modified_time: str | None = None
    headings: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "path": self.path,
            "title": self.title,
            "sha256": self.sha256,
            "size_bytes": self.size_bytes,
            "line_count": self.line_count,
            "modified_time": self.modified_time,
            "headings": self.headings,
        }


@dataclass
class ObjectRecord:
    object_id: str
    kind: str
    text: str
    source: SourceRef
    object_key: str = ""
    owner: str = ""
    authority: str = ""
    scope: str = ""
    status: str = ""
    date: str = ""
    supersedes: str = ""
    value: str = ""
    attributes: dict[str, str] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return {
            "object_id": self.object_id,
            "kind": self.kind,
            "text": self.text,
            "source": self.source.to_dict(),
            "object_key": self.object_key,
            "owner": self.owner,
            "authority": self.authority,
            "scope": self.scope,
            "status": self.status,
            "date": self.date,
            "supersedes": self.supersedes,
            "value": self.value,
            "attributes": self.attributes,
        }


@dataclass
class Evidence:
    source: SourceRef
    role: str
    object_id: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "source": self.source.to_dict(),
            "role": self.role,
            "object_id": self.object_id,
        }


@dataclass
class Finding:
    finding_id: str
    finding_type: str
    severity: str
    title: str
    reason: str
    evidence: list[Evidence] = field(default_factory=list)
    uncertainty: str = ""
    proposed_action: str = ""
    detection_mode: str = "deterministic"
    confidence: float | None = None

    def to_dict(self) -> dict[str, Any]:
        return {
            "finding_id": self.finding_id,
            "finding_type": self.finding_type,
            "severity": self.severity,
            "title": self.title,
            "reason": self.reason,
            "evidence": [item.to_dict() for item in self.evidence],
            "uncertainty": self.uncertainty,
            "proposed_action": self.proposed_action,
            "detection_mode": self.detection_mode,
            "confidence": self.confidence,
        }


@dataclass
class ScanResult:
    source: str
    documents: list[DocumentRecord]
    objects: list[ObjectRecord]
    findings: list[Finding]
    blueprint: dict[str, Any]
    repair_plan: list[dict[str, Any]]
    before_after: dict[str, Any]
    engine: dict[str, Any]
    review_ledger: list[dict[str, Any]] = field(default_factory=list)
    validation: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return {
            "source": self.source,
            "documents": [item.to_dict() for item in self.documents],
            "objects": [item.to_dict() for item in self.objects],
            "findings": [item.to_dict() for item in self.findings],
            "blueprint": self.blueprint,
            "repair_plan": self.repair_plan,
            "before_after": self.before_after,
            "engine": self.engine,
            "review_ledger": self.review_ledger,
            "validation": self.validation,
        }

# MOON-SOURCE-PUBLIC-STAMP
# 🌙 Moon Source · Lua Helena Moon Martins Cardoso (Moon) + Áurion (AI-assisted) · Licensing: https://github.com/luahelenammc/Moon-Source/blob/main/LICENSING.md · Use & attribution: https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md · Full source: https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip · Questions, suggestions, or proposals? Feel free to contact me at LuaHelenaMMC@gmail.com.
