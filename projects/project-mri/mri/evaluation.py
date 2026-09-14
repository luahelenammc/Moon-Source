from __future__ import annotations

from .diagnostics import _date_key, _norm
from .models import ObjectRecord

TASK = "Which storage choice should an AI assistant follow, and who currently owns that decision?"
FIXED_QUESTIONS = [
    {
        "id": "storage-authority",
        "question": TASK,
        "scope": "decision records with decision_key=storage",
    },
    {
        "id": "retention-owner",
        "question": "Who owns the 30-day customer event-log retention fact?",
        "scope": "Fact ID FACT-RETENTION",
    },
]


def _storage_decisions(objects: list[ObjectRecord]) -> list[ObjectRecord]:
    return [obj for obj in objects if obj.kind == "decision" and obj.object_key == "storage"]


def evaluate_before_after(objects: list[ObjectRecord]) -> dict:
    decisions = _storage_decisions(objects)
    if not decisions:
        return {
            "task": TASK,
            "questions": FIXED_QUESTIONS,
            "before": {"answer": "No storage decision found", "evidence": []},
            "after": {"answer": "No storage decision found", "evidence": []},
            "changed": False,
            "metrics": {"fixed_question_count": 0, "question_count": len(FIXED_QUESTIONS), "evidence_attached_before": 0, "evidence_attached_after": 0},
            "method": "deterministic proxy; no benchmark claim",
        }
    # The pre-MRI proxy intentionally models a naive historical lookup: it
    # selects the oldest matching record. The post-MRI proxy selects the
    # latest dated decision and keeps the evidence/authority fields attached.
    before = min(decisions, key=lambda item: _date_key(item.date))
    after = sorted(decisions, key=lambda item: _date_key(item.date))[-1]
    before_answer = {
        "answer": before.value,
        "owner": before.owner or "unknown",
        "authority": before.authority or "unknown",
        "evidence": [before.source.to_dict()],
    }
    after_answer = {
        "answer": after.value,
        "owner": after.owner or "unknown",
        "authority": after.authority or "unknown",
        "evidence": [after.source.to_dict()],
    }
    retention = next((item for item in objects if item.object_id == "FACT-RETENTION"), None)
    retention_answer = {
        "answer": retention.value if retention else "Retention fact not found",
        "owner": retention.owner if retention and retention.owner else "unresolved",
        "authority": retention.authority if retention and retention.authority else "unresolved",
        "evidence": [retention.source.to_dict()] if retention else [],
    }
    before_questions = [before_answer, retention_answer]
    after_questions = [after_answer, retention_answer]
    unique_values = {_norm(item.value) for item in decisions}
    return {
        "task": TASK,
        "questions": FIXED_QUESTIONS,
        "before": before_answer,
        "after": after_answer,
        "question_results": {
            "before": before_questions,
            "after": after_questions,
        },
        "changed": before.value != after.value or before.source.path != after.source.path,
        "metrics": {
            "fixed_question_count": 1 if before.value != after.value else 0,
            "question_count": len(FIXED_QUESTIONS),
            "evidence_attached_before": sum(bool(item["evidence"]) for item in before_questions),
            "evidence_attached_after": sum(bool(item["evidence"]) for item in after_questions),
            "unresolved_owner_after": sum(item["owner"] == "unresolved" for item in after_questions),
            "candidate_decisions_before": len(decisions),
            "candidate_decisions_after": 1,
            "distinct_decision_values_before": len(unique_values),
            "distinct_decision_values_after": 1,
        },
        "why": "Before uses the first matching source; after uses the latest dated decision and preserves its evidence and authority fields.",
        "method": "deterministic proxy; not a benchmark or proof of general model improvement",
    }
