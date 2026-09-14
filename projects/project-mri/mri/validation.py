from __future__ import annotations

from collections.abc import Mapping
from typing import Any


ALLOWED_FINDING_TYPES = {
    "duplicate",
    "near_duplicate",
    "contradiction",
    "stale_authority",
    "unclear_authority",
    "missing_owner",
    "orphaned_decision",
    "scope_jurisdiction_leak",
}
ALLOWED_SEVERITIES = {"low", "medium", "high"}
ALLOWED_DETECTION_MODES = {"deterministic", "heuristic", "model_assisted"}
ALLOWED_REVIEW_STATUSES = {"unresolved", "approved", "rejected"}


class SchemaValidationError(ValueError):
    """Raised when a model-shaped or exported payload violates the MRI schema."""

    def __init__(self, issues: list[str]):
        self.issues = issues
        super().__init__("Schema validation failed: " + "; ".join(issues))


def _text(value: Any, field_name: str, issues: list[str]) -> None:
    if not isinstance(value, str) or not value.strip():
        issues.append(f"{field_name} must be a non-empty string")


def _source_ref(value: Any, field_name: str, issues: list[str]) -> None:
    if not isinstance(value, Mapping):
        issues.append(f"{field_name} must be an object")
        return
    _text(value.get("path"), f"{field_name}.path", issues)
    for key in ("line_start", "line_end"):
        number = value.get(key)
        if not isinstance(number, int) or number < 1:
            issues.append(f"{field_name}.{key} must be a positive integer")
    if isinstance(value.get("line_start"), int) and isinstance(value.get("line_end"), int):
        if value["line_end"] < value["line_start"]:
            issues.append(f"{field_name}.line_end must be >= line_start")


def validate_finding_payload(value: Any, field_name: str = "finding") -> None:
    issues: list[str] = []
    if not isinstance(value, Mapping):
        raise SchemaValidationError([f"{field_name} must be an object"])
    for key in ("finding_id", "title", "reason", "proposed_action"):
        _text(value.get(key), f"{field_name}.{key}", issues)
    finding_type = value.get("finding_type")
    if finding_type not in ALLOWED_FINDING_TYPES:
        issues.append(f"{field_name}.finding_type is not a supported finding family")
    if value.get("severity") not in ALLOWED_SEVERITIES:
        issues.append(f"{field_name}.severity must be one of {sorted(ALLOWED_SEVERITIES)}")
    mode = value.get("detection_mode", "deterministic")
    if mode not in ALLOWED_DETECTION_MODES:
        issues.append(f"{field_name}.detection_mode is not supported")
    confidence = value.get("confidence")
    if confidence is not None and (not isinstance(confidence, (int, float)) or not 0 <= confidence <= 1):
        issues.append(f"{field_name}.confidence must be a number between 0 and 1")
    evidence = value.get("evidence")
    if not isinstance(evidence, list) or not evidence:
        issues.append(f"{field_name}.evidence must contain at least one item")
    else:
        for index, item in enumerate(evidence):
            if not isinstance(item, Mapping):
                issues.append(f"{field_name}.evidence[{index}] must be an object")
                continue
            _source_ref(item.get("source"), f"{field_name}.evidence[{index}].source", issues)
            _text(item.get("role"), f"{field_name}.evidence[{index}].role", issues)
    if issues:
        raise SchemaValidationError(issues)


def validate_model_findings_payload(value: Any) -> list[dict[str, Any]]:
    """Validate the narrow shape accepted from an optional model adapter."""

    if not isinstance(value, Mapping) or not isinstance(value.get("findings"), list):
        raise SchemaValidationError(["model payload must be an object with a findings list"])
    findings = value["findings"]
    for index, finding in enumerate(findings):
        validate_finding_payload(finding, f"findings[{index}]")
    return list(findings)


def validate_scan_payload(value: Any) -> None:
    issues: list[str] = []
    if not isinstance(value, Mapping):
        raise SchemaValidationError(["scan payload must be an object"])
    for key in ("source", "documents", "objects", "findings", "blueprint", "repair_plan", "before_after", "engine"):
        if key not in value:
            issues.append(f"scan payload is missing {key}")
    if not isinstance(value.get("documents"), list):
        issues.append("scan.documents must be a list")
    documents = value.get("documents")
    documents_by_path: dict[str, Any] = {}
    if isinstance(documents, list):
        for index, document in enumerate(documents):
            if not isinstance(document, Mapping):
                issues.append(f"scan.documents[{index}] must be an object")
                continue
            path = document.get("path")
            line_count = document.get("line_count")
            if not isinstance(path, str) or not path.strip():
                issues.append(f"scan.documents[{index}].path must be a non-empty string")
            elif path in documents_by_path:
                issues.append(f"scan.documents contains duplicate path: {path}")
            else:
                documents_by_path[path] = line_count
    if not isinstance(value.get("objects"), list):
        issues.append("scan.objects must be a list")
    findings = value.get("findings")
    if not isinstance(findings, list):
        issues.append("scan.findings must be a list")
    ledger = value.get("review_ledger", [])
    if not isinstance(ledger, list):
        issues.append("scan.review_ledger must be a list")
    else:
        for index, item in enumerate(ledger):
            if not isinstance(item, Mapping):
                issues.append(f"scan.review_ledger[{index}] must be an object")
                continue
            _text(item.get("finding_id"), f"scan.review_ledger[{index}].finding_id", issues)
            if item.get("status") not in ALLOWED_REVIEW_STATUSES:
                issues.append(f"scan.review_ledger[{index}].status is not supported")
    finding_ids: set[str] = set()
    if isinstance(findings, list):
        for index, finding in enumerate(findings):
            if not isinstance(finding, Mapping):
                issues.append(f"scan.findings[{index}] must be an object")
                continue
            validate_finding_payload(finding, f"scan.findings[{index}]")
            for evidence_index, item in enumerate(finding.get("evidence", [])):
                if not isinstance(item, Mapping):
                    continue
                source = item.get("source", {})
                if not isinstance(source, Mapping):
                    continue
                path = source.get("path")
                if path not in documents_by_path:
                    issues.append(f"scan.findings[{index}].evidence[{evidence_index}] references unknown path: {path}")
                    continue
                line_end = source.get("line_end")
                line_count = documents_by_path[path]
                if isinstance(line_count, int) and isinstance(line_end, int) and line_end > line_count:
                    issues.append(f"scan.findings[{index}].evidence[{evidence_index}] ends beyond {path} line count")
            finding_id = finding.get("finding_id")
            if finding_id in finding_ids:
                issues.append(f"scan.findings contains duplicate finding_id: {finding_id}")
            finding_ids.add(finding_id)
    ledger_ids = [item.get("finding_id") for item in ledger if isinstance(item, Mapping)]
    if len(ledger_ids) != len(set(ledger_ids)):
        issues.append("scan.review_ledger contains duplicate finding_id values")
    unknown_ledger_ids = set(ledger_ids) - finding_ids
    if unknown_ledger_ids:
        issues.append(f"scan.review_ledger references unknown findings: {sorted(unknown_ledger_ids)}")
    if issues:
        raise SchemaValidationError(issues)


def validate_scan_result(result: Any) -> dict[str, Any]:
    """Validate the serialized result and return a small audit summary."""

    payload = result.to_dict() if hasattr(result, "to_dict") else result
    validate_scan_payload(payload)
    return {
        "schema": "project-mri.scan.v1",
        "valid": True,
        "finding_count": len(payload["findings"]),
        "evidence_count": sum(len(item["evidence"]) for item in payload["findings"]),
    }
