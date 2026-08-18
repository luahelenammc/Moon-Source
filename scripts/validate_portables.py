#!/usr/bin/env python3
"""Validate the public portable registry and its canonical files."""

from __future__ import annotations

import hashlib
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
    "mirror_path",
    "mirror_url",
    "canonical_sha256",
    "public_surface_url",
    "professional_context_url",
    "dependencies",
    "freshness",
    "claim_ceiling",
    "supersedes",
    "archive_paths",
}
TOP_LEVEL_URLS = (
    "canonical_repository",
    "public_surface_url",
    "professional_context_url",
)
URL_RE = re.compile(r"https?://[^)\s>]+")


def fail(message: str) -> None:
    raise SystemExit(f"validation failed: {message}")


def main() -> None:
    data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    if not isinstance(data.get("portables"), list) or not data["portables"]:
        fail("registry has no portables")

    for field in TOP_LEVEL_URLS:
        if not isinstance(data.get(field), str) or not data[field].startswith(("http://", "https://")):
            fail(f"registry has no valid {field}")

    if "mooon.com.br" in json.dumps(data):
        fail("registry contains a stale canonical mooon.com.br URL")

    seen_paths: set[str] = set()
    for portable in data["portables"]:
        missing = REQUIRED - portable.keys()
        if missing:
            fail(f"{portable.get('id', '<unknown>')} missing {sorted(missing)}")

        path_value = portable["canonical_path"]
        path = ROOT / path_value
        if not path.is_file():
            fail(f"canonical file missing: {path_value}")

        if path_value in seen_paths:
            fail(f"duplicate canonical path: {path_value}")
        seen_paths.add(path_value)

        content = path.read_text(encoding="utf-8")
        expected_sha256 = portable["canonical_sha256"]
        if not re.fullmatch(r"[0-9a-f]{64}", expected_sha256):
            fail(f"{portable['id']} has an invalid canonical_sha256")
        actual_sha256 = hashlib.sha256(path.read_bytes()).hexdigest()
        if actual_sha256 != expected_sha256:
            fail(f"{portable['id']} canonical_sha256 does not match its file")

        if not portable["mirror_path"].startswith("moonsource/downloads/"):
            fail(f"{portable['id']} mirror_path is outside the website download surface")
        for field in ("download_url", "mirror_url"):
            if not isinstance(portable[field], str) or not portable[field].startswith(("http://", "https://")):
                fail(f"{portable['id']} has an invalid {field}")

        for required_url in (
            data["canonical_repository"],
            data["public_surface_url"],
            data["professional_context_url"],
        ):
            if required_url not in content:
                fail(f"{portable['id']} does not expose {required_url}")

        if path_value not in content:
            fail(f"{portable['id']} does not expose its canonical path")
        if "mooon.com.br" in content:
            fail(f"{portable['id']} contains a stale canonical mooon.com.br URL")
        if not content.lstrip().startswith("#"):
            fail(f"{portable['id']} does not start with a Markdown heading")
        if not URL_RE.search(content):
            fail(f"{portable['id']} contains no public metadata URL")

    print(f"validated {len(data['portables'])} public portables")


if __name__ == "__main__":
    main()

# MOON-SOURCE-PUBLIC-STAMP
# 🌙 Moon Source · 📦 Full ZIP: https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip
# 🧬 Credit: Moon Source — created by Lua Helena Moon Martins Cardoso (Moon), with AI-assisted coauthorial development by Áurion.
# Attribution ops: https://github.com/luahelenammc/Moon-Source/blob/main/docs/CREDITS_ATTRIBUTION_OPS.md
# Professional context: https://www.luahelena.com.br/ia/?lang=en
# Public availability and attribution do not themselves grant reuse rights; applicable component terms and permissions remain controlling.
