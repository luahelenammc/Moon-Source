#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Guard stable public titles against accidental release-marker coupling."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "registry" / "public-portables.json"
HUMAN_REGISTRY = ROOT / "registry" / "PUBLIC_PORTABLES.md"

# This is intentionally applied only to governed title and heading fields, not
# to historical prose, technical paths, package names or release records.
VERSION_MARKER_RE = re.compile(
    r"(?i)(?<![A-Za-z])(?:v\d+(?:\.\d+)*|\d+\.\d+(?:\.\d+)*(?:-[a-z0-9.-]+)?|(?:alpha|beta|rc)\d*)(?![A-Za-z])"
)
H1_RE = re.compile(r"^\s*#\s+(?!#)(.*?)\s*$", re.MULTILINE)


def contains_version_marker(value: str) -> bool:
    """Return whether a human-facing title contains a release marker."""

    return bool(VERSION_MARKER_RE.search(value))


def first_h1(markdown: str) -> str | None:
    """Return the first level-one Markdown heading, without its hash mark."""

    match = H1_RE.search(markdown)
    return match.group(1).strip() if match else None


def normalize_heading(value: str) -> str:
    """Normalize decorative Markdown/emoji around a stable title for comparison."""

    value = re.sub(r"[*_`~]", "", value)
    value = re.sub(r"^[^\w]+(?=[A-Za-z])", "", value)
    return re.sub(r"\s+", " ", value).strip()


def _registry_row_exists(human_registry: str, portable: dict[str, str]) -> bool:
    row_prefix = f"| {portable['id']} | {portable['title']} | {portable['version']} |"
    return any(line.startswith(row_prefix) for line in human_registry.splitlines())


def validation_errors(
    data: dict[str, object], *, root: Path = ROOT, human_registry: str | None = None
) -> list[str]:
    """Return scoped title/version errors for a registry payload."""

    errors: list[str] = []
    if human_registry is None:
        human_registry = (root / "registry" / "PUBLIC_PORTABLES.md").read_text(
            encoding="utf-8"
        )

    portables = data.get("portables", [])
    components = data.get("public_components", [])
    if not isinstance(portables, list) or not isinstance(components, list):
        return ["registry must contain list-valued portables and public_components"]

    for portable in portables:
        if not isinstance(portable, dict):
            errors.append("portable entry is not an object")
            continue
        identity = portable.get("id", "<unknown>")
        title = portable.get("title")
        version = portable.get("version")
        canonical_path = portable.get("canonical_path")
        if not isinstance(title, str) or not title.strip():
            errors.append(f"{identity}: title is empty")
            continue
        if contains_version_marker(title):
            errors.append(f"{identity}: title contains a version marker: {title!r}")
        if not isinstance(version, str) or not version.strip():
            errors.append(f"{identity}: version metadata is empty")
        if not isinstance(canonical_path, str):
            errors.append(f"{identity}: canonical_path is missing")
            continue
        path = root / canonical_path
        if not path.is_file():
            errors.append(f"{identity}: canonical file is missing: {canonical_path}")
            continue
        heading = first_h1(path.read_text(encoding="utf-8"))
        if heading is None:
            errors.append(f"{identity}: canonical file has no level-one heading")
        else:
            if contains_version_marker(heading):
                errors.append(f"{identity}: canonical heading contains a version marker: {heading!r}")
            if normalize_heading(heading) != normalize_heading(title):
                errors.append(
                    f"{identity}: canonical heading {heading!r} does not match title {title!r}"
                )
        if not _registry_row_exists(human_registry, {"id": str(identity), "title": title, "version": str(version)}):
            errors.append(f"{identity}: human registry row does not expose stable title plus version metadata")

    for component in components:
        if not isinstance(component, dict):
            errors.append("component entry is not an object")
            continue
        identity = component.get("id", "<unknown>")
        title = component.get("title")
        canonical_path = component.get("canonical_path")
        if not isinstance(title, str) or not title.strip():
            errors.append(f"{identity}: component title is empty")
            continue
        if contains_version_marker(title):
            errors.append(f"{identity}: component title contains a version marker: {title!r}")
        if not isinstance(canonical_path, str):
            errors.append(f"{identity}: component canonical_path is missing")
            continue
        path = root / canonical_path
        if not path.is_file():
            errors.append(f"{identity}: component canonical file is missing: {canonical_path}")
            continue
        heading = first_h1(path.read_text(encoding="utf-8"))
        if heading is not None and contains_version_marker(heading):
            errors.append(f"{identity}: component heading contains a version marker: {heading!r}")

    return errors


def main() -> None:
    try:
        data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        raise SystemExit(f"title/version separation validation failed: invalid registry JSON: {error}")

    errors = validation_errors(data)
    if errors:
        joined = "\n".join(f"- {error}" for error in errors)
        raise SystemExit(f"title/version separation validation failed:\n{joined}")
    print(f"validated title/version separation for {len(data['portables'])} portables and {len(data['public_components'])} components")


if __name__ == "__main__":
    main()

# MOON-SOURCE-PUBLIC-STAMP
# 🌙 Moon Source · Lua Helena Moon Martins Cardoso (Moon) + Áurion (AI-assisted) · Licensing: https://github.com/luahelenammc/Moon-Source/blob/main/LICENSING.md · Use & attribution: https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md · Full source: https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip
