#!/usr/bin/env python3
"""Check the public licensing contract and active authority language."""

from __future__ import annotations

import hashlib
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = (
    "LICENSE",
    "LICENSING.md",
    "NOTICE",
    "LICENSES/Apache-2.0.txt",
    "LICENSES/CC-BY-4.0.txt",
    "REUSE.toml",
    "CITATION.cff",
    "THIRD_PARTY_NOTICES.md",
)

ACTIVE_AUTHORITIES = (
    "README.md",
    "MOON_SOURCE_AI_KERNEL.md",
    "MOON_SOURCE_USE_AND_ATTRIBUTION.md",
    "docs/PORTABLE_DESIGN_CONTRACT.md",
    "docs/VERSIONING_AND_RELEASES.md",
    "PUBLIC_BOUNDARY.md",
    "EVIDENCE_AND_CLAIMS.md",
    "DOWNLOADS.md",
    "ARCHITECTURE.md",
    "registry/PUBLIC_PORTABLES.md",
    "portables/setup/MOON_SOURCE_SETUP.md",
    "portables/msl/MSL_4_3.md",
    "portables/chat-work/CHAT_WORK_ROUTING_PROTOCOL_V2.md",
)

STALE_PATTERNS = (
    re.compile(r"no repository-wide (?:open-source )?licen[cs]e is ratified", re.I),
    re.compile(r"no such broad licen[cs]e is ratified", re.I),
    re.compile(r"a repository-wide open-source licen[cs]e is not assumed", re.I),
    re.compile(r"no repository-wide licen[cs]e is created", re.I),
)

# Hashes of the official texts retrieved from the canonical sources named in the
# repository's third-party notice. The CC BY text uses one final newline rather
# than the source's extra empty EOF line; no operative legal text is changed.
EXPECTED_LICENSE_SHA256 = {
    "LICENSES/Apache-2.0.txt": "cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30",
    "LICENSES/CC-BY-4.0.txt": "9e5f1b3c610b9c2da5c313bf81d577a7d1acec686bdb0384edefa6df0f90cd94",
}


def fail(message: str) -> None:
    raise SystemExit(f"licensing validation failed: {message}")


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def main() -> None:
    for relative in REQUIRED_FILES:
        path = ROOT / relative
        if not path.is_file():
            fail(f"required file is missing: {relative}")

    for relative, expected in EXPECTED_LICENSE_SHA256.items():
        if expected.startswith("TODO_"):
            fail(f"official license hash is not pinned for {relative}")
        actual = hashlib.sha256((ROOT / relative).read_bytes()).hexdigest()
        if actual != expected:
            fail(f"{relative} is not the verified official text (expected {expected}, got {actual})")

    notice = read("NOTICE")
    for required in (
        "Lua Helena Moon Martins Cardoso",
        "Áurion",
        "https://github.com/luahelenammc/Moon-Source",
        "https://www.luahelena.com.br/moonsource/?lang=en",
        "https://www.luahelena.com.br/ia/?lang=en",
    ):
        if required not in notice:
            fail(f"NOTICE does not preserve {required}")

    licensing = read("LICENSING.md")
    for required in ("Apache-2.0", "CC-BY-4.0", "THIRD_PARTY_NOTICES.md", "CREDITS_ATTRIBUTION_OPS.md"):
        if required not in licensing:
            fail(f"LICENSING.md does not route {required}")

    reuse = read("REUSE.toml")
    if "SPDX-License-Identifier = \"Apache-2.0\"" not in reuse:
        fail("REUSE.toml has no Apache-2.0 annotation")
    if "SPDX-License-Identifier = \"CC-BY-4.0\"" not in reuse:
        fail("REUSE.toml has no CC-BY-4.0 annotation")

    citation = read("CITATION.cff")
    if "Lua Helena Moon" not in citation or "LICENSING.md" not in citation:
        fail("CITATION.cff is missing human authorship or mixed-license routing")

    for relative in ACTIVE_AUTHORITIES:
        text = read(relative)
        for pattern in STALE_PATTERNS:
            if pattern.search(text):
                fail(f"{relative} contains obsolete no-license language: {pattern.pattern}")

    print("licensing contract, official texts, attribution notice and active authority language validated")


if __name__ == "__main__":
    main()

# MOON-SOURCE-PUBLIC-STAMP
# 🌙 Moon Source · Lua Helena Moon Martins Cardoso (Moon) + Áurion (AI-assisted) · Licensing: https://github.com/luahelenammc/Moon-Source/blob/main/LICENSING.md · Use & attribution: https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md · Full source: https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip
