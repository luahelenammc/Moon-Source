#!/usr/bin/env python3
"""Check local Markdown links and stale canonical references."""

from __future__ import annotations

import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)\n]+)\)")


def local_target(path: Path, target: str) -> Path | None:
    """Return the filesystem target for a relative Markdown link."""

    target = target.strip()
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1]

    parsed = urlsplit(target)
    if parsed.scheme or parsed.netloc or not parsed.path:
        return None

    return (path.parent / unquote(parsed.path)).resolve()


def check(path: Path) -> list[str]:
    """Return validation failures for one Markdown file."""

    failures: list[str] = []
    text = path.read_text(encoding="utf-8")

    if "mooon.com.br" in text:
        failures.append(f"{path}: stale canonical domain")

    for target in LINK_RE.findall(text):
        target_path = local_target(path, target)
        if target_path is not None and not target_path.exists():
            failures.append(f"{path}: missing relative link {target}")

    return failures


def main() -> None:
    failures: list[str] = []
    for markdown in ROOT.rglob("*.md"):
        failures.extend(check(markdown))

    if failures:
        print("\n".join(failures))
        raise SystemExit(1)

    print("local Markdown links and canonical domains validated")


if __name__ == "__main__":
    main()

# MOON-SOURCE-PUBLIC-STAMP
# 🌙 Moon Source · 📦 Full ZIP: https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip
# 🧬 Credit: Moon Source — created by Lua Helena Moon Martins Cardoso (Moon), with AI-assisted coauthorial development by Áurion.
# Attribution ops: https://github.com/luahelenammc/Moon-Source/blob/main/docs/CREDITS_ATTRIBUTION_OPS.md
# Professional context: https://www.luahelena.com.br/ia/?lang=en
# Public availability and attribution do not themselves grant reuse rights; applicable component terms and permissions remain controlling.
