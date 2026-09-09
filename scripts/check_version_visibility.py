#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 Lua Helena Moon Martins Cardoso (Moon)
# SPDX-License-Identifier: Apache-2.0
"""Reject repository-visibility qualifiers encoded inside numeric versions."""

from __future__ import annotations

import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VISIBILITY = "-" + "public"
BAD = re.compile(r"\d+(?:\.\d+)+" + re.escape(VISIBILITY) + r"\b")
SKIP_SUFFIXES = {".zip", ".png", ".jpg", ".jpeg", ".gif", ".webp", ".ico", ".woff", ".woff2", ".ttf", ".pyc"}


def main() -> None:
    raw = subprocess.check_output(["git", "ls-files", "-z"], cwd=ROOT)
    violations = []
    for item in (p for p in raw.split(b"\0") if p):
        rel = item.decode("utf-8")
        if BAD.search(rel):
            violations.append(f"path: {rel}")
        path = ROOT / rel
        if not path.is_file() or path.suffix.lower() in SKIP_SUFFIXES:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        if BAD.search(text):
            violations.append(f"text: {rel}")
    if violations:
        raise SystemExit("visibility-qualified numeric versions are forbidden:\n- " + "\n- ".join(violations))
    print("version visibility guard passed")


if __name__ == "__main__":
    main()

# MOON-SOURCE-PUBLIC-STAMP
# 🌙 Moon Source · Lua Helena Moon Martins Cardoso (Moon) + Áurion (AI-assisted) · Licensing: https://github.com/luahelenammc/Moon-Source/blob/main/LICENSING.md · Use & attribution: https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md · Full source: https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip
