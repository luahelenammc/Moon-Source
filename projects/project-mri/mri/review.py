from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from .models import Finding
from .validation import ALLOWED_REVIEW_STATUSES


def _event(status: str, note: str, actor: str, at: str | None = None) -> dict[str, Any]:
    return {
        "status": status,
        "note": note,
        "actor": actor,
        "at": at or datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "mutation_applied": False,
    }


def initial_review_ledger(findings: list[Finding]) -> list[dict[str, Any]]:
    return [
        {
            "finding_id": finding.finding_id,
            "status": "unresolved",
            "mutation_applied": False,
            "history": [_event("unresolved", "Awaiting human review.", "system", "not-reviewed")],
        }
        for finding in findings
    ]


def _entry(ledger: list[dict[str, Any]], finding_id: str) -> dict[str, Any]:
    for item in ledger:
        if item.get("finding_id") == finding_id:
            return item
    raise KeyError(f"Unknown finding_id: {finding_id}")


def apply_review(
    ledger: list[dict[str, Any]],
    finding_id: str,
    status: str,
    note: str = "",
    actor: str = "human",
) -> dict[str, Any]:
    if status not in ALLOWED_REVIEW_STATUSES:
        raise ValueError(f"Review status must be one of {sorted(ALLOWED_REVIEW_STATUSES)}")
    if len(note) > 500:
        raise ValueError("Review note must be 500 characters or fewer")
    item = _entry(ledger, finding_id)
    item["status"] = status
    item["mutation_applied"] = False
    item.setdefault("history", []).append(_event(status, note, actor))
    return item


def approve_plan(ledger: list[dict[str, Any]], actor: str = "human") -> int:
    changed = 0
    for item in ledger:
        if item.get("status") == "unresolved":
            apply_review(
                ledger,
                item["finding_id"],
                "approved",
                "Sandbox plan approval recorded; source mutation remains disabled.",
                actor,
            )
            changed += 1
    return changed


def review_summary(ledger: list[dict[str, Any]]) -> dict[str, int]:
    summary = {status: 0 for status in sorted(ALLOWED_REVIEW_STATUSES)}
    for item in ledger:
        status = item.get("status", "unresolved")
        summary[status] = summary.get(status, 0) + 1
    return summary

# MOON-SOURCE-PUBLIC-STAMP
# 🌙 Moon Source · Lua Helena Moon Martins Cardoso (Moon) + Áurion (AI-assisted) · Licensing: https://github.com/luahelenammc/Moon-Source/blob/main/LICENSING.md · Use & attribution: https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md · Full source: https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip · Questions, suggestions, or proposals? Feel free to contact me at LuaHelenaMMC@gmail.com.
