#!/usr/bin/env python3
"""Reject private-project backstory and unpublished-feature inventories in public docs.

This is a narrow editorial smoke test, not a substitute for permissions review.
"""
from pathlib import Path
import re
import sys
import subprocess

ROOT = Path(__file__).resolve().parents[1]
PATTERNS = [
    re.compile(r"\bLocal Moon Source\b", re.IGNORECASE),
    re.compile(r"\bFinan[cç]as Moon\b", re.IGNORECASE),
    re.compile(r"\bDefensoria Social\b", re.IGNORECASE),
    re.compile(r"\bprivate donor (?:corpus|corpora|lineage|project|system)s?\b", re.IGNORECASE),
    re.compile(r"\bsource[- ]gap (?:candidate|route|engine)s?\b", re.IGNORECASE),
    re.compile(r"\bnot every local experiment\b", re.IGNORECASE),
]
SKIP = {"docs/PUBLIC_EDITORIAL_POLICY.md"}

def main() -> int:
    errors = []
    paths = subprocess.check_output(["git", "ls-files", "--cached", "-z"], cwd=ROOT).decode("utf-8").split(chr(0))
    for relative in sorted(p for p in paths if p.endswith(".md")):
        path = ROOT / relative
        if relative.startswith(("LICENSES/", ".git/")) or relative in SKIP or not path.is_file():
            continue
        for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if any(pattern.search(line) for pattern in PATTERNS):
                errors.append(f"{relative}:{number}: non-user-facing provenance or unpublished-work narrative")
    notice = ROOT / "NOTICE"
    if notice.is_file():
        for number, line in enumerate(notice.read_text(encoding="utf-8").splitlines(), 1):
            if any(pattern.search(line) for pattern in PATTERNS):
                errors.append(f"NOTICE:{number}: non-user-facing provenance narrative")
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print("Public editorial surface: no identified backstage disclosures.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

# MOON-SOURCE-PUBLIC-STAMP
# 🌙 Moon Source · Lua Helena Moon Martins Cardoso (Moon) + Áurion (AI-assisted) · Licensing: https://github.com/luahelenammc/Moon-Source/blob/main/LICENSING.md · Use & attribution: https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md · Full source: https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip · Questions, suggestions, or proposals? Feel free to contact me at LuaHelenaMMC@gmail.com.
