#!/usr/bin/env python3
"""Regression checks for problem-to-method public navigation coverage."""
from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from check_problem_routes import DOCS, audit


class ProblemRoutesTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / "registry").mkdir()
        (self.root / "docs").mkdir()
        (self.root / "portables" / "sample").mkdir(parents=True)
        (self.root / "portables" / "sample" / "CANONICAL.md").write_text("# test", encoding="utf-8")
        registry = {"capabilities": [
            {"id": "sample-route", "canonical_path": "portables/sample/CANONICAL.md"}
        ]}
        (self.root / "registry/public-capabilities.json").write_text(
            json.dumps(registry), encoding="utf-8"
        )
        for filename, labels in DOCS.items():
            body = "\n".join(label + " Synthetic only." for label in labels[:-1])
            body += "\n" + labels[-1] + " [Source](../portables/sample/CANONICAL.md)"
            (self.root / filename).write_text(
                "<!-- problem-route: sample-route -->\n### Example\n" + body + "\n",
                encoding="utf-8",
            )

    def test_valid_one_to_one_routes(self):
        self.assertEqual(audit(self.root), [])

    def test_missing_record_detected(self):
        path = self.root / "docs/PROBLEM_TO_METHOD.md"
        path.write_text("# Missing", encoding="utf-8")
        self.assertTrue(any("missing=['sample-route']" in e for e in audit(self.root)))

    def test_duplicate_record_detected(self):
        path = self.root / "docs/PROBLEM_TO_METHOD.pt-BR.md"
        path.write_text(path.read_text(encoding="utf-8") + 
                        "\n<!-- problem-route: sample-route -->\n", encoding="utf-8")
        self.assertTrue(any("duplicates=['sample-route']" in e for e in audit(self.root)))

    def test_broken_canonical_link_detected(self):
        path = self.root / "docs/PROBLEM_TO_METHOD.md"
        path.write_text(path.read_text(encoding="utf-8").replace(
            "../portables/sample/CANONICAL.md", "wrong.md"), encoding="utf-8")
        self.assertTrue(any("must link" in e for e in audit(self.root)))


if __name__ == "__main__":
    unittest.main()
