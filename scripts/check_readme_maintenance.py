#!/usr/bin/env python3
"""Check that README surfaces do not become changelogs."""

from __future__ import annotations

import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXCLUDED_DIRS = {".git", ".venv", "venv", "node_modules", "__pycache__"}
DIGEST_MARKER = "MOON-SOURCE-CAPABILITY-DIGEST:"
HISTORY_HEADINGS = tuple(
    re.compile(pattern)
    for pattern in (
        r"\b(?:recent|latest|newest)\s+(?:(?:public\s+)?capabilit(?:y|ies)\s+)?(?:changes?|updates?)\b",
        r"\bwhat\s+(?:(?:is|has|have)\s+)?new\b",
        r"\bwhat\s+changed(?:\s+in\s+(?:v?\d+(?:\.\d+)*(?:[-.][\w]+)?))?\b",
        r"\b(?:changes?|updates?|fixes?)\s+in\s+(?:v?\d+(?:\.\d+)*(?:[-.][\w]+)?)\b",
        r"\bversion\s+\d+(?:\.\d+)*(?:\s+(?:changes?|updates?|notes?))\b",
        r"\b(?:change|update|version)\s+history\b",
        r"\brelease\s+notes?\b|\bchangelog\b",
        r"\b(?:mudancas|atualizacoes|novidades)\s+recentes\b",
        r"\bo\s+que\s+mudou\b|\bhistorico\s+de\s+(?:mudancas|atualizacoes)\b",
        r"\bnotas?\s+de\s+versao\b|\bregistro\s+de\s+mudancas\b",
        r"\b(?:cambios|actualizaciones|novedades)\s+recientes\b",
        r"\bque\s+cambio\b|\bhistorial\s+de\s+(?:cambios|actualizaciones)\b",
        r"\bnotas?\s+de\s+version\b",
        r"(?:недавние|последние)\s+(?:изменения|обновления)|история\s+изменений|заметки\s+о\s+выпуске",
        r"近期(?:能力)?(?:变化|更新)|最新(?:能力)?(?:变化|更新)|(?:变更|更新)历史|发行说明",
    )
)
HEADING_RE = re.compile(r"^\s{0,3}#{1,6}\s+(.+?)\s*#*\s*$")
FENCE_RE = re.compile(r"^\s*(\x60{3,}|~{3,})(.*)$")


def normalize_heading(heading: str) -> str:
    heading = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", heading)
    heading = re.sub(r"<[^>]+>", " ", heading)
    heading = unicodedata.normalize("NFKD", heading).casefold()
    heading = "".join(char for char in heading if unicodedata.category(char) != "Mn")
    return re.sub(r"[\x60*_~]", "", heading)


def history_heading(heading: str) -> bool:
    normalized = normalize_heading(heading)
    return any(pattern.search(normalized) for pattern in HISTORY_HEADINGS)


def readme_maintenance_violations(root: Path = ROOT) -> list[str]:
    failures: list[str] = []
    for path in sorted(root.rglob("README*.md")):
        relative = path.relative_to(root)
        if any(part in EXCLUDED_DIRS for part in relative.parts):
            continue
        try:
            lines = path.read_text(encoding="utf-8").splitlines()
        except UnicodeDecodeError as error:
            failures.append(f"{relative}: could not read UTF-8 content ({error})")
            continue

        fence_char: str | None = None
        fence_length = 0
        for number, line in enumerate(lines, start=1):
            fence = FENCE_RE.match(line)
            if fence_char is not None:
                if (
                    fence
                    and fence.group(1)[0] == fence_char
                    and len(fence.group(1)) >= fence_length
                    and not fence.group(2).strip()
                ):
                    fence_char = None
                    fence_length = 0
                continue
            if fence:
                fence_char = fence.group(1)[0]
                fence_length = len(fence.group(1))
                continue
            if DIGEST_MARKER in line:
                failures.append(
                    f"{relative}:{number}: generated capability-history digests do not belong in README files"
                )
            heading = HEADING_RE.match(line)
            if heading and history_heading(heading.group(1)):
                failures.append(
                    f"{relative}:{number}: changelog-style README heading; put history in its changelog or registry: {heading.group(1).strip()}"
                )
    return failures


def main() -> int:
    failures = readme_maintenance_violations()
    if failures:
        print("README maintenance policy failed:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1
    print("README maintenance policy passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

# MOON-SOURCE-PUBLIC-STAMP
# 🌙 Moon Source · Lua Helena Moon Martins Cardoso (Moon) + Áurion (AI-assisted) · Licensing: https://github.com/luahelenammc/Moon-Source/blob/main/LICENSING.md · Use & attribution: https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md · Full source: https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip · Questions, suggestions, or proposals? Feel free to contact me at LuaHelenaMMC@gmail.com.
