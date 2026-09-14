from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .pipeline import scan


def _matches(expected: dict[str, Any], finding: dict[str, Any]) -> bool:
    if expected.get("finding_type") != finding.get("finding_type"):
        return False
    evidence_paths = {
        item.get("source", {}).get("path")
        for item in finding.get("evidence", [])
    }
    required_paths = set(expected.get("evidence_paths", []))
    return required_paths.issubset(evidence_paths)


def run_golden_eval(fixture: str | Path, output_dir: str | Path | None = None) -> dict[str, Any]:
    fixture_path = Path(fixture)
    expected_path = fixture_path / "expected_findings.json"
    expected = json.loads(expected_path.read_text(encoding="utf-8"))
    result = scan(fixture_path)
    findings = [item.to_dict() for item in result.findings]
    used: set[str] = set()
    cases: list[dict[str, Any]] = []
    for item in expected.get("findings", []):
        match = next(
            (
                finding
                for finding in findings
                if finding["finding_id"] not in used and _matches(item, finding)
            ),
            None,
        )
        if match:
            used.add(match["finding_id"])
        cases.append(
            {
                "id": item.get("id", item.get("finding_type", "unknown")),
                "expected": item,
                "recovered": match is not None,
                "finding_id": match["finding_id"] if match else None,
            }
        )
    recovered = sum(case["recovered"] for case in cases)
    total = len(cases)
    payload = {
        "fixture": str(fixture_path),
        "metric": "fixture_recovery_rate",
        "metric_definition": "expected diagnostic families recovered with required evidence paths",
        "recovered": recovered,
        "expected": total,
        "rate": round(recovered / total, 4) if total else 1.0,
        "not_model_accuracy": True,
        "not_generalization_proof": True,
        "cases": cases,
        "observed_finding_types": sorted({finding["finding_type"] for finding in findings}),
        "scan_validation": result.validation,
    }
    if output_dir is not None:
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
        (output_path / "northstar_eval.json").write_text(
            json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
        )
        lines = [
            "# Northstar Golden Eval",
            "",
            f"Fixture recovery rate: **{recovered}/{total} ({payload['rate']:.0%})**",
            "",
            "> This is fixture recovery, not model accuracy, benchmark superiority or evidence of generalization.",
            "",
            "| Case | Recovered | Finding |",
            "|---|---:|---|",
        ]
        lines.extend(
            f"| {case['id']} | {'yes' if case['recovered'] else 'no'} | {case['finding_id'] or '—'} |"
            for case in cases
        )
        (output_path / "northstar_eval.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return payload
