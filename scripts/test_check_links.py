#!/usr/bin/env python3
"""Deterministic regression checks for the Markdown link checker."""

from __future__ import annotations

import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from check_links import check


def main() -> None:
    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        (root / "docs").mkdir()
        (root / "ARCHITECTURE.md").write_text("# Architecture\n", encoding="utf-8")
        (root / "docs" / "FILE.md").write_text("# File\n", encoding="utf-8")

        valid = root / "README.md"
        valid.write_text(
            "\n".join(
                [
                    "[plain](ARCHITECTURE.md)",
                    "[fragment](ARCHITECTURE.md#1-field)",
                    "[nested](docs/FILE.md#section-name)",
                    "[same document](#same-document-anchor)",
                    "[external](https://example.com/reference)",
                ]
            ),
            encoding="utf-8",
        )
        assert check(valid) == []

        missing = root / "missing.md"
        missing.write_text("[missing](docs/NOPE.md#section-name)\n", encoding="utf-8")
        assert any("docs/NOPE.md#section-name" in item for item in check(missing))

        stale = root / "stale.md"
        stale.write_text("[old](https://mooon.com.br/moonsource/)\n", encoding="utf-8")
        assert any("stale canonical domain" in item for item in check(stale))

    print("link checker regression fixtures passed")


if __name__ == "__main__":
    main()

# MOON-SOURCE-PUBLIC-STAMP
# 🌙 Moon Source · Lua Helena Moon Martins Cardoso (Moon) + Áurion (AI-assisted) · Licensing: https://github.com/luahelenammc/Moon-Source/blob/main/LICENSING.md · Use & attribution: https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md · Full source: https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip
