#!/usr/bin/env python3
"""Regression tests for the thin repository maintenance CLI."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parent))

import moon_source


def namespace(**values: object) -> argparse.Namespace:
    defaults = {"apply": False, "mirror_root": None}
    defaults.update(values)
    return argparse.Namespace(**defaults)


def main() -> None:
    validate = moon_source.command_steps("validate", namespace())
    assert validate[0][1][1].endswith("check_licensing.py")
    assert validate[-1][1][1].endswith("test_moon_source_cli.py")

    registry = moon_source.command_steps("registry", namespace())
    assert [step[1][1] for step in registry] == [
        str(moon_source.ROOT / "scripts" / "validate_public_capabilities.py"),
        str(moon_source.ROOT / "scripts" / "test_validate_public_capabilities.py"),
    ]

    stamps = moon_source.command_steps("stamps", namespace(apply=True))
    assert stamps[0][1][1].endswith("apply_public_stamps.py")
    assert stamps[-1][1][1].endswith("test_public_stamps.py")

    digest = moon_source.command_steps("digest", namespace())
    assert digest[0][1][-1] == "--check"
    digest_apply = moon_source.command_steps("digest", namespace(apply=True))
    assert "--check" not in digest_apply[0][1]

    mirror = moon_source.command_steps(
        "mirror", namespace(mirror_root=Path("../luahelena"))
    )
    assert mirror[0][1][-2:] == ["--mirror-root", "../luahelena"]

    with patch.object(moon_source, "run_step", return_value=0) as run_step:
        assert moon_source.execute("registry", namespace()) == 0
        assert run_step.call_count == 2

    with patch.object(moon_source, "run_step", side_effect=[0, 3]) as run_step:
        assert moon_source.execute("registry", namespace()) == 3
        assert run_step.call_count == 2

    print("maintenance CLI regression tests passed")


if __name__ == "__main__":
    main()

# MOON-SOURCE-PUBLIC-STAMP
# 🌙 Moon Source · Lua Helena Moon Martins Cardoso (Moon) + Áurion (AI-assisted) · Licensing: https://github.com/luahelenammc/Moon-Source/blob/main/LICENSING.md · Use & attribution: https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md · Full source: https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip · Questions, suggestions, or proposals? Feel free to contact me at LuaHelenaMMC@gmail.com.
