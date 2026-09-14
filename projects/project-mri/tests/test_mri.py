import json
import os
import subprocess
import sys
import tempfile
import time
import unittest
import urllib.error
import urllib.request
import zipfile
from pathlib import Path

from mri.golden_eval import run_golden_eval
from mri.nutrient import NutrientAdapter, NutrientConfig, NutrientIntegrationError
from mri.pipeline import scan, write_outputs
from mri.review import apply_review
from mri.validation import SchemaValidationError, validate_model_findings_payload, validate_scan_result


ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "fixtures" / "demo_corpus"
CLEAN_FIXTURE = ROOT / "fixtures" / "clean_corpus"
NORTHSTAR = ROOT / "fixtures" / "northstar"


class ProjectMRITest(unittest.TestCase):
    def test_end_to_end_finds_required_failure_modes(self):
        result = scan(FIXTURE)
        types = {finding.finding_type for finding in result.findings}
        self.assertTrue({
            "duplicate",
            "near_duplicate",
            "contradiction",
            "stale_authority",
            "unclear_authority",
            "orphaned_decision",
            "scope_jurisdiction_leak",
        }.issubset(types))
        self.assertGreaterEqual(len(result.documents), 7)
        self.assertGreaterEqual(len(result.objects), 7)

    def test_evidence_points_to_existing_fixture_fragments(self):
        result = scan(FIXTURE)
        documents = {document.path: document for document in result.documents}
        for finding in result.findings:
            for evidence in finding.evidence:
                self.assertIn(evidence.source.path, documents)
                self.assertGreaterEqual(evidence.source.line_start, 1)
                self.assertLessEqual(evidence.source.line_end, documents[evidence.source.path].line_count)

    def test_repair_plan_is_proposal_only(self):
        result = scan(FIXTURE)
        self.assertTrue(result.repair_plan)
        self.assertTrue(all(item["requires_human_approval"] for item in result.repair_plan))
        self.assertTrue(all(not item["mutation_applied"] for item in result.repair_plan))
        self.assertTrue(all(item["status"] == "unresolved" for item in result.review_ledger))

    def test_before_after_changes_storage_answer_and_reports_fixed_questions(self):
        result = scan(FIXTURE)
        self.assertTrue(result.before_after["changed"])
        self.assertIn("PostgreSQL", result.before_after["before"]["answer"])
        self.assertIn("SQLite", result.before_after["after"]["answer"])
        self.assertEqual(result.before_after["metrics"]["question_count"], 2)
        self.assertGreaterEqual(result.before_after["metrics"]["evidence_attached_after"], 1)

    def test_zip_ingestion_is_bounded(self):
        with tempfile.TemporaryDirectory() as temp:
            archive = Path(temp) / "corpus.zip"
            with zipfile.ZipFile(archive, "w") as handle:
                for path in FIXTURE.rglob("*.md"):
                    handle.write(path, path.relative_to(FIXTURE))
            result = scan(archive)
            self.assertEqual(len(result.documents), len(list(FIXTURE.rglob("*.md"))))

    def test_directory_symlinks_are_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp) / "corpus"
            outside = Path(temp) / "outside.md"
            root.mkdir()
            outside.write_text("# outside\nClaim: should not be followed\n", encoding="utf-8")
            try:
                (root / "linked.md").symlink_to(outside)
            except (OSError, NotImplementedError) as exc:
                self.skipTest(f"symlinks unavailable: {exc}")
            with self.assertRaisesRegex(ValueError, "Symlink"):
                scan(root)

    def test_zip_path_traversal_is_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            archive = Path(temp) / "unsafe.zip"
            with zipfile.ZipFile(archive, "w") as handle:
                handle.writestr("../escape.md", "# escape\n")
            with self.assertRaisesRegex(ValueError, "Unsafe ZIP member"):
                scan(archive)

    def test_malformed_zip_and_empty_or_unsupported_corpora_fail_clearly(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            malformed = root / "broken.zip"
            malformed.write_bytes(b"not a zip")
            with self.assertRaisesRegex(ValueError, "Malformed ZIP"):
                scan(malformed)
            empty = root / "empty"
            empty.mkdir()
            with self.assertRaisesRegex(ValueError, "empty"):
                scan(empty)
            unsupported = root / "unsupported"
            unsupported.mkdir()
            (unsupported / "data.json").write_text("{}", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "No supported"):
                scan(unsupported)

    def test_clean_corpus_is_a_real_negative_case(self):
        result = scan(CLEAN_FIXTURE)
        self.assertEqual(result.findings, [])
        self.assertEqual(result.validation["valid"], True)

    def test_schema_validation_rejects_malformed_model_output(self):
        with self.assertRaises(SchemaValidationError):
            validate_model_findings_payload({"findings": [{"finding_type": "contradiction"}]})
        self.assertTrue(validate_scan_result(scan(FIXTURE))["valid"])

    def test_human_review_states_keep_audit_history_and_no_mutation(self):
        result = scan(FIXTURE)
        finding_id = result.findings[0].finding_id
        item = apply_review(result.review_ledger, finding_id, "rejected", "Evidence is insufficient.")
        self.assertEqual(item["status"], "rejected")
        self.assertFalse(item["mutation_applied"])
        self.assertGreaterEqual(len(item["history"]), 2)
        apply_review(result.review_ledger, finding_id, "unresolved", "Needs authority confirmation.")
        self.assertEqual(result.review_ledger[0]["status"], "unresolved")

    def test_export_contains_schema_review_and_report(self):
        with tempfile.TemporaryDirectory() as temp:
            output = Path(temp) / "out"
            write_outputs(scan(FIXTURE), output)
            payload = json.loads((output / "scan.json").read_text(encoding="utf-8"))
            report = (output / "report.md").read_text(encoding="utf-8")
            self.assertEqual(payload["validation"]["valid"], True)
            self.assertIn("Human review ledger", report)
            self.assertIn("Before / After", report)

    def test_northstar_golden_eval_reports_fixture_recovery_not_model_accuracy(self):
        with tempfile.TemporaryDirectory() as temp:
            payload = run_golden_eval(NORTHSTAR, temp)
            self.assertEqual(payload["recovered"], payload["expected"])
            self.assertTrue(payload["not_model_accuracy"])
            self.assertTrue((Path(temp) / "northstar_eval.json").exists())

    def test_nutrient_adapter_is_explicitly_blocked_without_credentials(self):
        adapter = NutrientAdapter(NutrientConfig(api_key="", mode="disabled"))
        self.assertFalse(adapter.status()["configured"])
        with self.assertRaises(NutrientIntegrationError):
            adapter.convert_markdown_to_pdf("# evidence")

    def test_web_routes_and_review_endpoint(self):
        port = "8765"
        process = subprocess.Popen(
            [sys.executable, "server.py"],
            cwd=ROOT,
            env={**os.environ, "MRI_PORT": port},
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        try:
            url = f"http://127.0.0.1:{port}/api/scan"
            for _ in range(30):
                try:
                    with urllib.request.urlopen(url, timeout=0.2) as response:
                        payload = json.loads(response.read())
                    break
                except OSError:
                    time.sleep(0.05)
            else:
                self.fail("server did not become ready")
            with urllib.request.urlopen(f"http://127.0.0.1:{port}/api/health", timeout=1) as response:
                health = json.loads(response.read())
            self.assertEqual(health["service"], "project-mri")
            self.assertIn("review_ledger", payload)
            finding_id = payload["findings"][0]["finding_id"]
            body = json.dumps({"finding_id": finding_id, "status": "rejected"}).encode("utf-8")
            request = urllib.request.Request(
                f"http://127.0.0.1:{port}/api/review",
                data=body,
                headers={"Content-Type": "application/json"},
                method="POST",
            )
            with urllib.request.urlopen(request, timeout=1) as response:
                reviewed = json.loads(response.read())
            self.assertEqual(reviewed["review"]["status"], "rejected")
            with urllib.request.urlopen(f"http://127.0.0.1:{port}/api/report.md", timeout=1) as response:
                self.assertIn(b"Human review ledger", response.read())
            oversized = urllib.request.Request(
                f"http://127.0.0.1:{port}/api/review",
                data=b"x" * 8001,
                headers={"Content-Type": "application/json", "Content-Length": "8001"},
                method="POST",
            )
            with self.assertRaises(urllib.error.HTTPError) as error_context:
                urllib.request.urlopen(oversized, timeout=1)
            self.assertEqual(error_context.exception.code, 413)
        finally:
            process.terminate()
            process.wait(timeout=3)


if __name__ == "__main__":
    unittest.main()

# MOON-SOURCE-PUBLIC-STAMP
# 🌙 Moon Source · Lua Helena Moon Martins Cardoso (Moon) + Áurion (AI-assisted) · Licensing: https://github.com/luahelenammc/Moon-Source/blob/main/LICENSING.md · Use & attribution: https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md · Full source: https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip · Questions, suggestions, or proposals? Feel free to contact me at LuaHelenaMMC@gmail.com.
