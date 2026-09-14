from __future__ import annotations

import json

from .models import Finding, ScanResult
from .review import review_summary


def _evidence(finding: Finding) -> str:
    return "; ".join(
        f"{item.source.path}:{item.source.line_start} ({item.role})"
        for item in finding.evidence
    )


def render_markdown(result: ScanResult) -> str:
    lines = [
        "# Project MRI — Governed Context Scan Report",
        "",
        "> InfraJam 2026 Open Source track reference build. Findings are evidence-backed proposals for human review; no corpus mutation was applied.",
        "",
        f"- **Engine:** `{result.engine.get('name', 'unknown')}` `{result.engine.get('version', 'unknown')}`",
        f"- **Track:** {result.engine.get('competition_track', 'not specified')}",
        f"- **Input:** `{result.source}`",
        f"- **Documents:** {len(result.documents)}",
        f"- **Extracted objects:** {len(result.objects)}",
        f"- **Findings:** {len(result.findings)}",
        f"- **Schema:** `{result.validation.get('schema', 'unknown')}` ({'valid' if result.validation.get('valid') else 'invalid'})",
        "",
        "## Human review ledger",
        "",
        f"Current states: `{review_summary(result.review_ledger)}`. Approval records an intent; `mutation_applied` remains false.",
        "",
        "## Findings",
        "",
    ]
    if not result.findings:
        lines.append("No findings.")
    for finding in result.findings:
        lines.extend(
            [
                f"### {finding.finding_id} · {finding.title} · {finding.severity}",
                "",
                finding.reason,
                "",
                f"**Evidence:** {_evidence(finding)}",
                f"**Proposed action:** {finding.proposed_action}",
                f"**Uncertainty:** {finding.uncertainty or 'none recorded'}",
                f"**Detection:** {finding.detection_mode}"
                + (f" (confidence {finding.confidence:.2f})" if finding.confidence is not None else ""),
                "",
            ]
        )
    lines.extend(["## Source-of-Truth Blueprint", "", "```json", json.dumps(result.blueprint, indent=2, ensure_ascii=False), "```", ""])
    lines.extend(["## Repair Plan", "", "```json", json.dumps(result.repair_plan, indent=2, ensure_ascii=False), "```", ""])
    lines.extend(["## Before / After", "", "```json", json.dumps(result.before_after, indent=2, ensure_ascii=False), "```", ""])
    lines.extend(
        [
            "## Claim ceiling",
            "",
            "This report demonstrates a bounded, deterministic scan over a synthetic corpus. It does not establish autonomous repair, benchmark superiority, production readiness, external adoption, secure handling of regulated data or general model accuracy.",
            "",
        ]
    )
    return "\n".join(lines)

# MOON-SOURCE-PUBLIC-STAMP
# 🌙 Moon Source · Lua Helena Moon Martins Cardoso (Moon) + Áurion (AI-assisted) · Licensing: https://github.com/luahelenammc/Moon-Source/blob/main/LICENSING.md · Use & attribution: https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md · Full source: https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip · Questions, suggestions, or proposals? Feel free to contact me at LuaHelenaMMC@gmail.com.
