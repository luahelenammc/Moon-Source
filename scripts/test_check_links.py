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
# 🌙 Moon Source · 📦 Full ZIP: https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip
# 🧬 Credit: Moon Source — created by Lua Helena Moon Martins Cardoso (Moon), with AI-assisted coauthorial development by Áurion.
# Attribution ops: https://github.com/luahelenammc/Moon-Source/blob/main/docs/CREDITS_ATTRIBUTION_OPS.md
# Professional context: https://www.luahelena.com.br/ia/?lang=en
# Public availability and attribution do not themselves grant reuse rights; applicable component terms and permissions remain controlling.
