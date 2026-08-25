#!/usr/bin/env python3
"""Render the bounded README digest from the public component registry."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "registry" / "public-portables.json"
README = ROOT / "README.md"
START = "<!-- MOON-SOURCE-COMPONENT-DIGEST:START -->"
END = "<!-- MOON-SOURCE-COMPONENT-DIGEST:END -->"
DEFAULT_LIMIT = 5


def fail(message: str) -> None:
    raise SystemExit(f"component digest update failed: {message}")


def render() -> str:
    try:
        data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        fail(f"registry JSON is invalid: {error}")

    components = data.get("public_components")
    if not isinstance(components, list):
        fail("public_components is not an array")

    ordered = sorted(
        components,
        key=lambda component: (
            component.get("last_material_update_on", ""),
            component.get("id", ""),
        ),
        reverse=True,
    )
    lines = []
    for component in ordered[:DEFAULT_LIMIT]:
        title = component["title"].split(" — ", 1)[0]
        lines.append(
            f"- **{component['last_material_update_on']} — {title}:** "
            f"{component['last_material_update_summary']}"
        )
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="fail when README is stale")
    args = parser.parse_args()

    current = README.read_text(encoding="utf-8")
    if START not in current or END not in current:
        fail("README digest markers are missing or incomplete")
    if current.count(START) != 1 or current.count(END) != 1:
        fail("README digest markers must occur exactly once")

    expected = f"{START}\n{render()}\n{END}"
    before, remainder = current.split(START, 1)
    _, after = remainder.split(END, 1)
    actual = f"{START}{remainder.split(END, 1)[0]}{END}"
    rendered = before + expected + after

    if args.check:
        if actual != expected:
            fail("README component digest is stale; run python scripts/update_component_digest.py")
        print("README component digest is current")
        return

    if rendered != current:
        README.write_text(rendered, encoding="utf-8", newline="\n")
        print("updated README component digest")
    else:
        print("README component digest already current")


if __name__ == "__main__":
    main()

# MOON-SOURCE-PUBLIC-STAMP
# 🌙 Moon Source · Lua Helena Moon Martins Cardoso (Moon) + Áurion (AI-assisted) · Licensing: https://github.com/luahelenammc/Moon-Source/blob/main/LICENSING.md · Use & attribution: https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md · Full source: https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip
