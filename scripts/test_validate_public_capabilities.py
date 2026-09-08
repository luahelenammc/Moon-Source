#!/usr/bin/env python3
"""Regression tests for the unified public capability registry validator."""

from __future__ import annotations

import copy
import hashlib
import sys
import tempfile
import unittest
from pathlib import Path
from zipfile import ZipFile

sys.path.insert(0, str(Path(__file__).resolve().parent))

from validate_public_capabilities import LEGACY_CONNECTED_PATH, validate_registry


REPOSITORY = "https://github.com/example/moon-source"
CREATOR = "Example Creator"


class PublicCapabilityRegistryTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tempdir = tempfile.TemporaryDirectory()
        self.root = Path(self.tempdir.name)
        (self.root / "docs").mkdir()
        (self.root / "downloads").mkdir()
        (self.root / "registry").mkdir()

        connected = """# Connected Sources

## First use

Use this capability for governed living-source work.

Canonical repository: https://github.com/example/moon-source
Creator: Example Creator
Canonical path: `docs/CONNECTED_SOURCES.md`
License: https://creativecommons.org/licenses/by/4.0/
"""
        repository_only = """# Source Operations

Canonical repository: https://github.com/example/moon-source
Creator: Example Creator
"""
        (self.root / "docs/CONNECTED_SOURCES.md").write_text(connected, encoding="utf-8")
        (self.root / "docs/SOURCE_OPERATIONS.md").write_text(repository_only, encoding="utf-8")
        self._write_package("CONNECTED_SOURCES.md", connected)

        connected_capability = {
            "id": "connected-sources",
            "title": "Connected Sources",
            "status": "current",
            "architectural_role": "structural_crown_jewel",
            "canonical_path": "docs/CONNECTED_SOURCES.md",
            "function": "Govern living-source authority.",
            "claim_ceiling": "No guaranteed freshness or universal connector behavior.",
            "versioning_mode": "public_semantic_version",
            "version": "1.1-public",
            "public_created_on": "2026-09-07",
            "last_material_update_on": "2026-09-08",
            "last_material_update_summary": "Registry rebase.",
            "dependencies": [],
            "freshness": "Recheck source state before consequential mutation.",
            "creator": CREATOR,
            "license": "CC BY 4.0",
            "distribution": {
                "standalone": True,
                "composite": False,
                "package_path": "downloads/connected-sources.zip",
                "download_url": f"{REPOSITORY}/raw/refs/heads/main/downloads/connected-sources.zip",
                "canonical_sha256": hashlib.sha256(connected.encode()).hexdigest(),
                "mirror_path": "moonsource/downloads/CONNECTED_SOURCES.md",
                "mirror_url": "https://example.com/moonsource/downloads/CONNECTED_SOURCES.md",
                "embedded_first_use": True,
            },
        }
        repository_only_capability = {
            "id": "source-operations",
            "title": "Source Operations",
            "status": "current",
            "architectural_role": "source_operations_method",
            "canonical_path": "docs/SOURCE_OPERATIONS.md",
            "function": "Govern source transformations.",
            "claim_ceiling": "No guaranteed source outcome.",
            "versioning_mode": "material_change_only",
            "version": None,
            "public_created_on": "2026-09-04",
            "last_material_update_on": "2026-09-08",
            "last_material_update_summary": "Registry rebase.",
            "dependencies": [],
            "freshness": "Read back after material transformation.",
            "creator": CREATOR,
            "license": "CC BY 4.0",
            "distribution": {"standalone": False},
        }
        self.data = {
            "registry_version": "2.0",
            "canonical_repository": REPOSITORY,
            "public_surface_url": f"{REPOSITORY}/blob/main/README.md",
            "professional_context_url": f"{REPOSITORY}/blob/main/LICENSING.md",
            "capabilities": [connected_capability, repository_only_capability],
            "views": {"standalone_distributions": {"capability_ids": ["connected-sources"]}},
        }
        self.human_registry = (
            "connected-sources Connected Sources docs/CONNECTED_SOURCES.md\n"
            "source-operations Source Operations docs/SOURCE_OPERATIONS.md\n"
        )
        self.kernel = "docs/CONNECTED_SOURCES.md\ndocs/SOURCE_OPERATIONS.md\n"

    def tearDown(self) -> None:
        self.tempdir.cleanup()

    def _write_package(self, filename: str, content: str) -> None:
        with ZipFile(self.root / "downloads/connected-sources.zip", "w") as archive:
            archive.writestr(filename, content.encode("utf-8"))

    def errors(self, data=None, human=None, kernel=None):
        return validate_registry(
            copy.deepcopy(data if data is not None else self.data),
            root=self.root,
            human_registry=self.human_registry if human is None else human,
            kernel=self.kernel if kernel is None else kernel,
        )

    def assert_error(self, fragment: str, errors: list[str]) -> None:
        self.assertTrue(any(fragment in error for error in errors), errors)

    def test_baseline_registry_is_valid(self):
        self.assertEqual(self.errors(), [])

    def test_architectural_role_and_standalone_distribution_are_independent(self):
        data = copy.deepcopy(self.data)
        data["capabilities"][0]["architectural_role"] = "transversal_interface_method"
        self.assertEqual(self.errors(data), [])

    def test_repository_only_capability_has_no_version_or_package_requirement(self):
        data = copy.deepcopy(self.data)
        data["capabilities"][1]["distribution"] = {"standalone": False}
        data["capabilities"][1]["version"] = None
        self.assertEqual(self.errors(data), [])

    def test_duplicate_id_is_rejected(self):
        data = copy.deepcopy(self.data)
        data["capabilities"].append(copy.deepcopy(data["capabilities"][1]))
        self.assert_error("duplicate capability id", self.errors(data))

    def test_duplicate_semantic_identity_is_rejected(self):
        data = copy.deepcopy(self.data)
        extra = copy.deepcopy(data["capabilities"][1])
        extra["id"] = "connected-sources-method"
        extra["title"] = "Another capability"
        extra["canonical_path"] = "docs/ANOTHER.md"
        (self.root / extra["canonical_path"]).write_text(
            "# Another capability\nhttps://github.com/example/moon-source\nExample Creator\n",
            encoding="utf-8",
        )
        data["capabilities"].append(extra)
        self.assert_error("duplicate semantic capability identity", self.errors(data))

    def test_duplicate_canonical_path_is_rejected(self):
        data = copy.deepcopy(self.data)
        data["capabilities"][1]["canonical_path"] = data["capabilities"][0]["canonical_path"]
        self.assert_error("duplicate canonical path", self.errors(data))

    def test_missing_first_use_is_rejected(self):
        data = copy.deepcopy(self.data)
        path = self.root / data["capabilities"][0]["canonical_path"]
        path.write_text(path.read_text(encoding="utf-8").replace("## First use\n", ""), encoding="utf-8")
        self.assert_error("missing ## First use", self.errors(data))

    def test_package_must_contain_exact_canonical_bytes(self):
        data = copy.deepcopy(self.data)
        self._write_package("CONNECTED_SOURCES.md", "different bytes")
        self.assert_error("exactly the canonical bytes", self.errors(data))

    def test_canonical_sha_is_checked(self):
        data = copy.deepcopy(self.data)
        data["capabilities"][0]["distribution"]["canonical_sha256"] = "0" * 64
        self.assert_error("SHA-256 mismatch", self.errors(data))

    def test_retired_connected_path_is_rejected(self):
        data = copy.deepcopy(self.data)
        data["capabilities"][0]["canonical_path"] = LEGACY_CONNECTED_PATH
        legacy_path = self.root / LEGACY_CONNECTED_PATH
        legacy_path.parent.mkdir(parents=True)
        legacy_path.write_text(
            "# Connected Sources\n## First use\nhttps://github.com/example/moon-source\nExample Creator\n",
            encoding="utf-8",
        )
        self.assert_error("retired portable canonical path", self.errors(data))

    def test_human_registry_alignment_is_checked(self):
        human = self.human_registry.replace("connected-sources", "missing-capability")
        self.assert_error("is not aligned in registry", self.errors(human=human))

    def test_standalone_view_must_match_capability_records(self):
        data = copy.deepcopy(self.data)
        data["views"]["standalone_distributions"]["capability_ids"] = []
        self.assert_error("standalone distribution view", self.errors(data))

    def test_missing_canonical_file_is_rejected(self):
        data = copy.deepcopy(self.data)
        data["capabilities"][1]["canonical_path"] = "docs/MISSING.md"
        self.assert_error("canonical file does not exist", self.errors(data))


if __name__ == "__main__":
    unittest.main()

# MOON-SOURCE-PUBLIC-STAMP
# 🌙 Moon Source · Lua Helena Moon Martins Cardoso (Moon) + Áurion (AI-assisted) · Licensing: https://github.com/luahelenammc/Moon-Source/blob/main/LICENSING.md · Use & attribution: https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md · Full source: https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip
