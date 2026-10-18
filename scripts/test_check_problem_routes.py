#!/usr/bin/env python3
"""Regression checks for multilingual problem-to-method table navigation."""
from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from check_problem_routes import DOCS, TABLE_RULE, audit


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
        for filename, (inspect, limit) in DOCS.items():
            rows = (
                "| Problem | Method | First move | Evidence and boundary |\n"
                + TABLE_RULE + "\n"
                + "| Synthetic problem | <!-- problem-route: sample-route -->"
                  "<a id=\"sample-route\"></a>[Sample](../portables/sample/CANONICAL.md) "
                  f"| Try the method | {inspect} Result {limit} Not a runtime |\n"
            )
            # Four category tables, one containing the route and three empty.
            rows += ("| Problem | Method | First move | Evidence and boundary |\n"
                     + TABLE_RULE + "\n") * 3
            (self.root / filename).write_text(rows, encoding="utf-8")

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
        path = self.root / "docs/PROBLEM_TO_METHOD.es.md"
        path.write_text(path.read_text(encoding="utf-8").replace(
            "../portables/sample/CANONICAL.md", "wrong.md"), encoding="utf-8")
        self.assertTrue(any("must link" in e for e in audit(self.root)))

    def test_unstructured_row_detected(self):
        path = self.root / "docs/PROBLEM_TO_METHOD.zh-CN.md"
        path.write_text(path.read_text(encoding="utf-8").replace(
            "| Try the method |", "| Try the method | EXTRA |"), encoding="utf-8")
        self.assertTrue(any("malformed" in e for e in audit(self.root)))

    def test_missing_result_or_boundary_detected(self):
        path = self.root / "docs/PROBLEM_TO_METHOD.ru.md"
        path.write_text(path.read_text(encoding="utf-8").replace(
            "**Граница:**", "**No-limit:**"), encoding="utf-8")
        self.assertTrue(any("missing **Граница:**" in e for e in audit(self.root)))

    def test_missing_table_detected(self):
        path = self.root / "docs/PROBLEM_TO_METHOD.md"
        path.write_text(path.read_text(encoding="utf-8").replace(
            TABLE_RULE, "|---|---|---|", 1), encoding="utf-8")
        self.assertTrue(any("four-column thematic" in e for e in audit(self.root)))


if __name__ == "__main__":
    unittest.main()

# MOON-SOURCE-PUBLIC-STAMP
# 🌙 Moon Source · Lua Helena Moon Martins Cardoso (Moon) + Áurion (AI-assisted) · Licensing: https://github.com/luahelenammc/Moon-Source/blob/main/LICENSING.md · Use & attribution: https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md · Full source: https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip · Questions, suggestions, or proposals? Feel free to contact me at LuaHelenaMMC@gmail.com.
