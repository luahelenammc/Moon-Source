#!/usr/bin/env python3
"""Check local Markdown links and stale canonical references."""

from __future__ import annotations

import re
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
FAILURES: list[str] = []


def check(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    if "https://" + "www.mooon.com.br" in text or "https://" + "mooon.com.br" in text:
        FAILURES.append(f"{path}: stale canonical domain")
    for target in LINK_RE.findall(text):
        if target.startswith(("http://", "https://", "#")):
            continue
        target_path = (path.parent / target).resolve()
        if not target_path.exists():
            FAILURES.append(f"{path}: missing relative link {target}")


for markdown in ROOT.rglob("*.md"):
    check(markdown)

if FAILURES:
    print("\n".join(FAILURES))
    raise SystemExit(1)

print("local Markdown links and canonical domains validated")
