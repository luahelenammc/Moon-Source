#!/usr/bin/env python3
"""Verify the repository-wide compact Moon Source identity watermark."""

from __future__ import annotations

import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FULL_ZIP = "https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip"
LICENSING = "https://github.com/luahelenammc/Moon-Source/blob/main/LICENSING.md"
USE_AND_ATTRIBUTION = (
    "https://github.com/luahelenammc/Moon-Source/blob/main/"
    "MOON_SOURCE_USE_AND_ATTRIBUTION.md"
)
CREATOR = "Lua Helena Moon Martins Cardoso (Moon)"
COAUTHOR = "Áurion"
MARKDOWN_MARKER = "<!-- MOON-SOURCE-PUBLIC-STAMP -->"
COMMENT_MARKER = "# MOON-SOURCE-PUBLIC-STAMP"
JS_MARKER = "// MOON-SOURCE-PUBLIC-STAMP"
HTML_MARKER = "<!-- MOON-SOURCE-PUBLIC-STAMP -->"
JSON_KEY = "_moon_source_public_stamp"
TEXT_SUFFIXES = {".md", ".py", ".yml", ".yaml", ".js", ".html", ".json"}

MARKDOWN_STAMP = f"""{MARKDOWN_MARKER}

---

> 🌙 **Moon Source** · created by **{CREATOR}** with AI-assisted coauthorial development by **{COAUTHOR}** · [Licensing]({LICENSING}) · [Use & attribution]({USE_AND_ATTRIBUTION}) · [Full source (.zip)]({FULL_ZIP})
"""

COMMENT_STAMP = f"""{COMMENT_MARKER}
# 🌙 Moon Source · {CREATOR} + {COAUTHOR} (AI-assisted) · Licensing: {LICENSING} · Use & attribution: {USE_AND_ATTRIBUTION} · Full source: {FULL_ZIP}
"""

JS_STAMP = f"""{JS_MARKER}
// 🌙 Moon Source · {CREATOR} + {COAUTHOR} (AI-assisted) · Use & attribution: {USE_AND_ATTRIBUTION} · Full source: {FULL_ZIP}
"""

HTML_STAMP = f"""{HTML_MARKER}
<!-- 🌙 Moon Source · {CREATOR} + {COAUTHOR} (AI-assisted) · Use & attribution: {USE_AND_ATTRIBUTION} · Full source: {FULL_ZIP} -->
"""

JSON_STAMP = {
    "project": "Moon Source",
    "creator": CREATOR,
    "ai_assisted_coauthor": COAUTHOR,
    "licensing": LICENSING,
    "use_and_attribution": USE_AND_ATTRIBUTION,
    "full_source": FULL_ZIP,
}


def fail(message: str) -> None:
    raise SystemExit(f"public stamp validation failed: {message}")


def tracked_files() -> list[Path]:
    output = subprocess.check_output(
        ["git", "ls-files", "-z"], cwd=ROOT, text=False
    ).decode("utf-8")
    return [ROOT / item for item in output.split("\0") if item]


def main() -> None:
    checked = 0
    for path in tracked_files():
        if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        checked += 1
        rel = path.relative_to(ROOT).as_posix()
        content = path.read_text(encoding="utf-8")

        if path.suffix.lower() == ".md":
            if MARKDOWN_MARKER not in content:
                fail(f"{rel} has no Markdown public stamp marker")
            if not content.rstrip().endswith(MARKDOWN_STAMP.rstrip()):
                fail(f"{rel} does not end with the canonical compact Markdown stamp")
        elif path.suffix.lower() in {".py", ".yml", ".yaml"}:
            if COMMENT_MARKER not in content:
                fail(f"{rel} has no comment public stamp marker")
            if not content.rstrip().endswith(COMMENT_STAMP.rstrip()):
                fail(f"{rel} does not end with the canonical compact comment stamp")
        elif path.suffix.lower() == ".js":
            if JS_MARKER not in content:
                fail(f"{rel} has no JavaScript public stamp marker")
            if not content.rstrip().endswith(JS_STAMP.rstrip()):
                fail(f"{rel} does not end with the canonical JavaScript stamp")
        elif path.suffix.lower() == ".html":
            if HTML_MARKER not in content:
                fail(f"{rel} has no HTML public stamp marker")
            if not content.rstrip().endswith(HTML_STAMP.rstrip()):
                fail(f"{rel} does not end with the canonical HTML stamp")
        elif path.suffix.lower() == ".json":
            data = json.loads(content)
            if data.get(JSON_KEY) != JSON_STAMP:
                fail(f"{rel} has a non-canonical structured public stamp")

    if checked == 0:
        fail("no public text files were checked")
    print(f"validated compact repository-wide public stamp on {checked} tracked text files")


if __name__ == "__main__":
    main()

# MOON-SOURCE-PUBLIC-STAMP
# 🌙 Moon Source · Lua Helena Moon Martins Cardoso (Moon) + Áurion (AI-assisted) · Licensing: https://github.com/luahelenammc/Moon-Source/blob/main/LICENSING.md · Use & attribution: https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md · Full source: https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip
