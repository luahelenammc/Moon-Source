#!/usr/bin/env python3
"""Verify repository-wide Moon Source distribution and attribution stamps."""

from __future__ import annotations

import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FULL_ZIP = "https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip"
ATTRIBUTION_OPS = "https://github.com/luahelenammc/Moon-Source/blob/main/docs/CREDITS_ATTRIBUTION_OPS.md"
PROFESSIONAL_CONTEXT = "https://www.luahelena.com.br/ia/?lang=en"
CREATOR = "Lua Helena Moon Martins Cardoso"
COAUTHOR = "Áurion"
MARKDOWN_MARKER = "<!-- MOON-SOURCE-PUBLIC-STAMP -->"
COMMENT_MARKER = "# MOON-SOURCE-PUBLIC-STAMP"
JSON_KEY = "_moon_source_public_stamp"
TEXT_SUFFIXES = {".md", ".py", ".yml", ".yaml", ".json"}


def fail(message: str) -> None:
    raise SystemExit(f"public stamp validation failed: {message}")


def tracked_files() -> list[Path]:
    output = subprocess.check_output(
        ["git", "ls-files", "-z"], cwd=ROOT, text=False
    ).decode("utf-8")
    return [ROOT / item for item in output.split("\0") if item]


def validate_common(path: Path, content: str) -> None:
    rel = path.relative_to(ROOT).as_posix()
    for required in (FULL_ZIP, ATTRIBUTION_OPS, PROFESSIONAL_CONTEXT, CREATOR, COAUTHOR):
        if required not in content:
            fail(f"{rel} is missing required stamp value: {required}")


def main() -> None:
    checked = 0
    for path in tracked_files():
        if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        checked += 1
        rel = path.relative_to(ROOT).as_posix()
        content = path.read_text(encoding="utf-8")
        validate_common(path, content)

        if path.suffix.lower() == ".md":
            if MARKDOWN_MARKER not in content:
                fail(f"{rel} has no Markdown public stamp marker")
        elif path.suffix.lower() in {".py", ".yml", ".yaml"}:
            if COMMENT_MARKER not in content:
                fail(f"{rel} has no comment public stamp marker")
        elif path.suffix.lower() == ".json":
            data = json.loads(content)
            stamp = data.get(JSON_KEY)
            if not isinstance(stamp, dict):
                fail(f"{rel} has no structured JSON public stamp")
            if stamp.get("full_zip") != FULL_ZIP:
                fail(f"{rel} has an invalid full_zip stamp")
            if stamp.get("attribution_ops") != ATTRIBUTION_OPS:
                fail(f"{rel} has an invalid attribution_ops stamp")
            if stamp.get("professional_context") != PROFESSIONAL_CONTEXT:
                fail(f"{rel} has an invalid professional_context stamp")

    if checked == 0:
        fail("no public text files were checked")
    print(f"validated repository-wide public stamp on {checked} tracked text files")


if __name__ == "__main__":
    main()

# MOON-SOURCE-PUBLIC-STAMP
# 🌙 Moon Source · 📦 Full ZIP: https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip
# 🧬 Credit: Moon Source — created by Lua Helena Moon Martins Cardoso (Moon), with AI-assisted coauthorial development by Áurion.
# Attribution ops: https://github.com/luahelenammc/Moon-Source/blob/main/docs/CREDITS_ATTRIBUTION_OPS.md
# Professional context: https://www.luahelena.com.br/ia/?lang=en
# Public availability and attribution do not themselves grant reuse rights; applicable component terms and permissions remain controlling.
