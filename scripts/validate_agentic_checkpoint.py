#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 Lua Helena Moon Martins Cardoso (Moon)
# SPDX-License-Identifier: Apache-2.0
"""Bounded structural checks for the public, wholly synthetic Agentic Continuity fixture.

This validates a sample checkpoint and a few negative cases. It does not
authenticate a provider, check real permissions, prove privacy or run an agent.
"""

from __future__ import annotations

import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "examples" / "agentic-continuity" / "sample-state.json"
KINDS = {"OWNER_REPORT", "PLATFORM_RECEIPT", "PROVIDER_READBACK", "INDEPENDENT_READBACK"}
RUN_STATES = {
    "RUN_COMPLETED", "NO_DELTA", "BLOCKED", "STATE_NOT_RECOVERED",
    "RUN_INCOMPLETE", "PAUSED", "DECOMMISSIONED",
}
WRITE_STATES = {"NOT_REQUIRED", "SOURCE_WRITE_VERIFIED", "SOURCE_WRITE_NOT_VERIFIED", "UNVERIFIED"}
REPORT_STATES = {"REPORT_PERSISTED_VERIFIED", "UNVERIFIED", "NOT_PERSISTED"}
NOTIFICATION_STATES = {"NOT_REQUIRED", "NOTIFICATION_PENDING", "DELIVERED"}


def validate_checkpoint(data: dict) -> list[str]:
    """Return structural consistency failures; provider proof requires real adapters."""
    errors: list[str] = []
    required = (
        "schema", "agent_id", "mandate_version", "run_id", "run_status",
        "trigger", "source_manifest_version", "cursor", "coverage",
        "evidence", "source_write", "report_write", "notification",
        "next_action",
    )
    for key in required:
        if key not in data:
            errors.append(f"missing {key}")
    if errors:
        return errors
    if data["schema"] != "moon-agentic-continuity/1":
        errors.append("wrong checkpoint schema")
    for field in ("agent_id", "mandate_version", "run_id", "trigger", "source_manifest_version"):
        if not isinstance(data[field], str) or not data[field].strip():
            errors.append(f"{field} must be nonempty")
    if data["run_status"] not in RUN_STATES:
        errors.append("invalid run status")
    if data["source_write"] not in WRITE_STATES:
        errors.append("invalid source write status")
    if data["report_write"] not in REPORT_STATES:
        errors.append("invalid report write status")
    if data["notification"] not in NOTIFICATION_STATES:
        errors.append("invalid notification status")
    cursor = data["cursor"]
    if not isinstance(cursor, dict) or not isinstance(cursor.get("unit_key"), str):
        errors.append("cursor needs a unit_key")
    coverage = data["coverage"]
    if not isinstance(coverage, list):
        errors.append("coverage must be a list")
        coverage = []
    keys = [item.get("unit_key") for item in coverage if isinstance(item, dict)]
    if len(keys) != len(coverage) or any(not isinstance(k, str) or not k for k in keys):
        errors.append("each coverage item needs a stable unit_key")
    if len(keys) != len(set(keys)):
        errors.append("duplicate coverage key")
    if isinstance(cursor, dict) and cursor.get("next_unit_key") in keys:
        errors.append("next unit already covered: require new revision or explicit revalidation")
    evidences = data["evidence"]
    if not isinstance(evidences, list):
        errors.append("evidence must be a list")
        evidences = []
    for event in evidences:
        if not isinstance(event, dict) or event.get("kind") not in KINDS:
            errors.append("invalid evidence kind")
        elif not isinstance(event.get("target"), str) or not isinstance(event.get("verified"), bool):
            errors.append("evidence needs target and verified boolean")
    independent_workspace = any(
        isinstance(event, dict)
        and event.get("kind") in {"INDEPENDENT_READBACK", "PROVIDER_READBACK"}
        and event.get("target") == "workspace-state"
        and event.get("verified") is True
        for event in evidences
    )
    if data["report_write"] == "REPORT_PERSISTED_VERIFIED" and not independent_workspace:
        errors.append("report verified claim lacks workspace readback")
    if data["source_write"] == "SOURCE_WRITE_VERIFIED" and not any(
        isinstance(event, dict) and event.get("target") == "governing-source"
        and event.get("verified") is True and event.get("kind") in {"INDEPENDENT_READBACK", "PROVIDER_READBACK"}
        for event in evidences
    ):
        errors.append("source verified claim lacks source readback")
    if data["notification"] == "DELIVERED" and not any(
        isinstance(event, dict) and event.get("target") == "notification-delivery"
        and event.get("kind") == "PLATFORM_RECEIPT" and event.get("verified") is True
        for event in evidences
    ):
        errors.append("delivery claim lacks provider receipt")
    return errors


def run_fixture_checks() -> None:
    data = json.loads(FIXTURE.read_text(encoding="utf-8"))
    assert not validate_checkpoint(data), validate_checkpoint(data)

    duplicate = copy.deepcopy(data)
    duplicate["coverage"].append(copy.deepcopy(duplicate["coverage"][0]))
    assert "duplicate coverage key" in validate_checkpoint(duplicate)

    lost_receipt = copy.deepcopy(data)
    lost_receipt["evidence"] = []
    assert "report verified claim lacks workspace readback" in validate_checkpoint(lost_receipt)

    false_delivery = copy.deepcopy(data)
    false_delivery["notification"] = "DELIVERED"
    assert "delivery claim lacks provider receipt" in validate_checkpoint(false_delivery)

    false_source_write = copy.deepcopy(data)
    false_source_write["source_write"] = "SOURCE_WRITE_VERIFIED"
    assert "source verified claim lacks source readback" in validate_checkpoint(false_source_write)

    loop = copy.deepcopy(data)
    loop["cursor"]["next_unit_key"] = "unit-001"
    assert any("next unit already covered" in e for e in validate_checkpoint(loop))


if __name__ == "__main__":
    run_fixture_checks()
    print("PASS: synthetic agent checkpoint + five rejection probes")

# MOON-SOURCE-PUBLIC-STAMP
# 🌙 Moon Source · Lua Helena Moon Martins Cardoso (Moon) + Áurion (AI-assisted) · Licensing: https://github.com/luahelenammc/Moon-Source/blob/main/LICENSING.md · Use & attribution: https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md · Full source: https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip · Questions, suggestions, or proposals? Feel free to contact me at LuaHelenaMMC@gmail.com.
