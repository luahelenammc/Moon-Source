#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Small regression tests for the title/version separation guard."""

from __future__ import annotations

import copy
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from check_title_version_separation import (  # noqa: E402
    contains_version_marker,
    first_h1,
    normalize_heading,
    validation_errors,
)

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    assert contains_version_marker("Preflight V2")
    assert contains_version_marker("Be My Eyes 1.0-public")
    assert contains_version_marker("Moon Source Language 4.3")
    assert not contains_version_marker("Preflight")
    assert not contains_version_marker("Chat–Work Routing Protocol")
    assert first_h1("intro\n# Stable Name\n") == "Stable Name"
    assert normalize_heading("# 🧭 Moon Source Setup") == "Moon Source Setup"

    data = json.loads(
        (ROOT / "registry" / "public-capabilities.json").read_text(encoding="utf-8")
    )
    assert not validation_errors(data)

    fixture = copy.deepcopy(data)
    fixture["capabilities"][0]["title"] = "Be My Eyes 1.0-public"
    errors = validation_errors(
        fixture,
        root=ROOT,
        human_registry=(ROOT / "registry" / "PUBLIC_CAPABILITIES.md").read_text(
            encoding="utf-8"
        ),
    )
    assert any("title contains a version marker" in error for error in errors)
    print("title/version separation tests passed")


if __name__ == "__main__":
    main()

# MOON-SOURCE-PUBLIC-STAMP
# 🌙 Moon Source · Lua Helena Moon Martins Cardoso (Moon) + Áurion (AI-assisted) · Licensing: https://github.com/luahelenammc/Moon-Source/blob/main/LICENSING.md · Use & attribution: https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md · Full source: https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip · Questions, suggestions, or proposals? Feel free to contact me at LuaHelenaMMC@gmail.com.
