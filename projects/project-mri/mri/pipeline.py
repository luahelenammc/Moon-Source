from __future__ import annotations

import json
from pathlib import Path

from .blueprint import build_blueprint, build_repair_plan
from .diagnostics import run_diagnostics
from .evaluation import evaluate_before_after
from .extract import extract_all
from .ingest import load_corpus
from .models import ScanResult
from .report import render_markdown
from .review import initial_review_ledger
from .validation import validate_scan_result
from . import __version__


def scan(source: str | Path, output_dir: str | Path | None = None) -> ScanResult:
    documents = load_corpus(source)
    objects = extract_all(documents)
    findings = run_diagnostics(documents, objects)
    blueprint = build_blueprint(documents, objects, findings)
    repair_plan = build_repair_plan(findings)
    before_after = evaluate_before_after(objects)
    result = ScanResult(
        source=str(source),
        documents=documents,
        objects=objects,
        findings=findings,
        blueprint=blueprint,
        repair_plan=repair_plan,
        before_after=before_after,
        engine={
            "name": "Project MRI bounded prototype",
            "version": __version__,
            "schema_version": "project-mri.scan.v1",
            "competition_track": "Open Source",
            "competition_surface": "InfraJam 2026",
            "deterministic_ingestion": True,
            "deterministic_diagnostics": True,
            "model_assisted_extraction": "optional extension point; not required for the demo fixture",
            "mutation": "proposal_only",
            "review_boundary": "human_review_required",
        },
        review_ledger=initial_review_ledger(findings),
    )
    result.validation = validate_scan_result(result)
    if output_dir is not None:
        write_outputs(result, output_dir)
    return result


def write_outputs(result: ScanResult, output_dir: str | Path) -> None:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    (output_path / "scan.json").write_text(
        json.dumps(result.to_dict(), indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    (output_path / "report.md").write_text(render_markdown(result), encoding="utf-8")
