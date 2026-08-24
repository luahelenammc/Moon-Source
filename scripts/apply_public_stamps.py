#!/usr/bin/env python3
"""Normalize the compact Moon Source identity watermark across tracked public text files.

The operation is idempotent. Markdown, Python/YAML, JavaScript and HTML stamps are
replaced in place; JSON receives equivalent structured metadata. Portable SHA-256 values
are refreshed after stamp changes so registry fingerprints continue to describe the
canonical bytes.
"""

from __future__ import annotations

import hashlib
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


def tracked_files() -> list[Path]:
    output = subprocess.check_output(
        ["git", "ls-files", "-z"], cwd=ROOT, text=False
    ).decode("utf-8")
    return [ROOT / item for item in output.split("\0") if item]


def normalize_text_stamp(path: Path, stamp: str, marker: str) -> bool:
    content = path.read_text(encoding="utf-8")
    marker_line = f"\n{marker}\n"
    if marker_line in content:
        base = content.rsplit(marker_line, 1)[0].rstrip()
    elif content.startswith(marker + "\n"):
        base = ""
    else:
        base = content.rstrip()
    normalized = base + "\n\n" + stamp.rstrip() + "\n" if base else stamp.rstrip() + "\n"
    if normalized == content:
        return False
    path.write_text(normalized, encoding="utf-8", newline="\n")
    return True


def stamp_json(path: Path) -> bool:
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("_moon_source_public_stamp") == JSON_STAMP:
        return False
    data["_moon_source_public_stamp"] = JSON_STAMP
    path.write_text(
        json.dumps(data, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    return True


def refresh_portable_hashes() -> bool:
    registry_path = ROOT / "registry" / "public-portables.json"
    data = json.loads(registry_path.read_text(encoding="utf-8"))
    changed = False
    for portable in data.get("portables", []):
        canonical_path = ROOT / portable["canonical_path"]
        digest = hashlib.sha256(canonical_path.read_bytes()).hexdigest()
        if portable.get("canonical_sha256") != digest:
            portable["canonical_sha256"] = digest
            changed = True
    if data.get("_moon_source_public_stamp") != JSON_STAMP:
        data["_moon_source_public_stamp"] = JSON_STAMP
        changed = True
    if changed:
        registry_path.write_text(
            json.dumps(data, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
            newline="\n",
        )
    return changed


def main() -> None:
    changed: list[str] = []
    for path in tracked_files():
        if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        rel = path.relative_to(ROOT).as_posix()
        if rel == "registry/public-portables.json":
            continue
        if path.suffix.lower() == ".md":
            did_change = normalize_text_stamp(path, MARKDOWN_STAMP, MARKDOWN_MARKER)
        elif path.suffix.lower() in {".py", ".yml", ".yaml"}:
            did_change = normalize_text_stamp(path, COMMENT_STAMP, COMMENT_MARKER)
        elif path.suffix.lower() == ".js":
            did_change = normalize_text_stamp(path, JS_STAMP, JS_MARKER)
        elif path.suffix.lower() == ".html":
            did_change = normalize_text_stamp(path, HTML_STAMP, HTML_MARKER)
        else:
            did_change = stamp_json(path)
        if did_change:
            changed.append(rel)

    if refresh_portable_hashes():
        changed.append("registry/public-portables.json")

    print(f"compact public stamp normalized; changed={len(changed)}")
    for item in changed:
        print(item)


if __name__ == "__main__":
    main()

# MOON-SOURCE-PUBLIC-STAMP
# 🌙 Moon Source · Lua Helena Moon Martins Cardoso (Moon) + Áurion (AI-assisted) · Licensing: https://github.com/luahelenammc/Moon-Source/blob/main/LICENSING.md · Use & attribution: https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md · Full source: https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip
