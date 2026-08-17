#!/usr/bin/env python3
"""Validate the public portable registry and its canonical files."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "registry" / "public-portables.json"
REQUIRED = {
    "id",
    "title",
    "slug",
    "version",
    "status",
    "class",
    "language",
    "difficulty",
    "function",
    "best_for",
    "canonical_path",
    "download_url",
    "public_surface_url",
    "professional_context_url",
    "dependencies",
    "freshness",
    "claim_ceiling",
    "supersedes",
    "archive_paths",
}
URL_RE = re.compile(r"https?://[^)\s>]+")


def fail(message: str) -> None:
    raise SystemExit(f"validation failed: {message}")


def main() -> None:
    data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    if not isinstance(data.get("portables"), list) or not data["portables"]:
        fail("registry has no portables")

    seen_paths: set[str] = set()
    for portable in data["portables"]:
        missing = REQUIRED - portable.keys()
        if missing:
            fail(f"{portable.get('id', '<unknown>')} missing {sorted(missing)}")

        path = ROOT / portable["canonical_path"]
        if not path.is_file():
            fail(f"canonical file missing: {portable['canonical_path']}")

        if portable["canonical_path"] in seen_paths:
            fail(f"duplicate canonical path: {portable['canonical_path']}")
        seen_paths.add(portable["canonical_path"])

        content = path.read_text(encoding="utf-8")
        for required_url in (
            data["public_surface_url"],
            data["professional_context_url"],
            portable["download_url"].replace(
                "https://raw.githubusercontent.com/luahelenammc/Moon-Source/main/",
                "https://github.com/luahelenammc/Moon-Source/blob/main/",
            ),
        ):
            if required_url not in content and required_url not in portable["download_url"]:
                fail(f"{portable['id']} does not expose {required_url}")

        if "mooon.com.br" in content:
            fail(f"{portable['id']} contains a stale canonical mooon.com.br URL")

        if not content.lstrip().startswith("#"):
            fail(f"{portable['id']} does not start with a Markdown heading")

        if not URL_RE.search(content):
            fail(f"{portable['id']} contains no public metadata URL")

    print(f"validated {len(data['portables'])} public portables")


if __name__ == "__main__":
    main()
