#!/usr/bin/env python3
"""Apply the Moon Source distribution and attribution stamp across tracked public text files.

This script is intentionally idempotent. It stamps Markdown, Python and YAML files,
adds structured stamp metadata to JSON files, and refreshes canonical SHA-256 values
for registered public portables after their bytes change.
"""

from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FULL_ZIP = "https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip"
ATTRIBUTION_OPS = "https://github.com/luahelenammc/Moon-Source/blob/main/docs/CREDITS_ATTRIBUTION_OPS.md"
PROFESSIONAL_CONTEXT = "https://www.luahelena.com.br/ia/?lang=en"
CREDIT = (
    "Moon Source — created by Lua Helena Moon Martins Cardoso (Moon), "
    "with AI-assisted coauthorial development by Áurion."
)
PERMISSION_NOTE = (
    "Public availability and attribution do not themselves grant reuse rights; "
    "applicable component terms and permissions remain controlling."
)
MARKDOWN_MARKER = "<!-- MOON-SOURCE-PUBLIC-STAMP -->"
COMMENT_MARKER = "# MOON-SOURCE-PUBLIC-STAMP"
TEXT_SUFFIXES = {".md", ".py", ".yml", ".yaml", ".json"}

MARKDOWN_STAMP = f"""{MARKDOWN_MARKER}

---

> 🌙 **Moon Source public stamp**  
> 📦 **Full repository:** [Download the complete Moon Source (.zip)]({FULL_ZIP})  
> 🧬 **Credit & attribution:** **{CREDIT}** [Credits & Attribution Ops]({ATTRIBUTION_OPS}) · [Professional context]({PROFESSIONAL_CONTEXT})  
> {PERMISSION_NOTE}
"""

COMMENT_STAMP = f"""{COMMENT_MARKER}
# 🌙 Moon Source · 📦 Full ZIP: {FULL_ZIP}
# 🧬 Credit: {CREDIT}
# Attribution ops: {ATTRIBUTION_OPS}
# Professional context: {PROFESSIONAL_CONTEXT}
# {PERMISSION_NOTE}
"""

JSON_STAMP = {
    "full_zip": FULL_ZIP,
    "credit": CREDIT,
    "attribution_ops": ATTRIBUTION_OPS,
    "professional_context": PROFESSIONAL_CONTEXT,
    "permission_note": PERMISSION_NOTE,
}


def tracked_files() -> list[Path]:
    output = subprocess.check_output(
        ["git", "ls-files", "-z"], cwd=ROOT, text=False
    ).decode("utf-8")
    return [ROOT / item for item in output.split("\0") if item]


def append_stamp(path: Path, stamp: str, marker: str) -> bool:
    content = path.read_text(encoding="utf-8")
    if marker in content:
        return False
    normalized = content.rstrip() + "\n\n" + stamp.rstrip() + "\n"
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
            did_change = append_stamp(path, MARKDOWN_STAMP, MARKDOWN_MARKER)
        elif path.suffix.lower() in {".py", ".yml", ".yaml"}:
            did_change = append_stamp(path, COMMENT_STAMP, COMMENT_MARKER)
        else:
            did_change = stamp_json(path)
        if did_change:
            changed.append(rel)

    if refresh_portable_hashes():
        changed.append("registry/public-portables.json")

    print(f"public stamp applied; changed={len(changed)}")
    for item in changed:
        print(item)


if __name__ == "__main__":
    main()

# MOON-SOURCE-PUBLIC-STAMP
# 🌙 Moon Source · 📦 Full ZIP: https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip
# 🧬 Credit: Moon Source — created by Lua Helena Moon Martins Cardoso (Moon), with AI-assisted coauthorial development by Áurion.
# Attribution ops: https://github.com/luahelenammc/Moon-Source/blob/main/docs/CREDITS_ATTRIBUTION_OPS.md
# Professional context: https://www.luahelena.com.br/ia/?lang=en
# Public availability and attribution do not themselves grant reuse rights; applicable component terms and permissions remain controlling.
