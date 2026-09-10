#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Guard stable public capability identities, summary labels and surface titles."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "registry" / "public-capabilities.json"
HUMAN_REGISTRY = ROOT / "registry" / "PUBLIC_CAPABILITIES.md"

VERSION_MARKER_RE = re.compile(
    r"(?i)(?<![A-Za-z])(?:v\d+(?:\.\d+)*|\d+\.\d+(?:\.\d+)*(?:-[a-z0-9.-]+)?|(?:alpha|beta|rc)\d*)(?![A-Za-z])"
)
H1_RE = re.compile(r"^\s*#\s+(?!#)(.*?)\s*$", re.MULTILINE)


def contains_version_marker(value: str) -> bool:
    return bool(VERSION_MARKER_RE.search(value))


def first_h1(markdown: str) -> str | None:
    match = H1_RE.search(markdown)
    return match.group(1).strip() if match else None


def normalize_heading(value: str) -> str:
    value = value.replace(chr(96), "")
    value = re.sub(r"[*_~]", "", value)
    value = re.sub(r"^[^\w]+(?=[A-Za-z])", "", value)
    return re.sub(r"\s+", " ", value).strip()


def validation_errors(
    data: dict[str, object], *, root: Path = ROOT, human_registry: str | None = None
) -> list[str]:
    errors: list[str] = []
    if human_registry is None:
        human_registry = HUMAN_REGISTRY.read_text(encoding="utf-8")

    capabilities = data.get("capabilities", [])
    if not isinstance(capabilities, list):
        return ["registry must contain a capabilities array"]

    for capability in capabilities:
        if not isinstance(capability, dict):
            errors.append("capability entry is not an object")
            continue

        identity = capability.get("id", "<unknown>")
        title = capability.get("title")
        summary_title = capability.get("summary_title")
        surface_title = capability.get("surface_title")
        canonical_path = capability.get("canonical_path")
        distribution = capability.get("distribution", {})
        standalone = isinstance(distribution, dict) and distribution.get("standalone") is True
        version = capability.get("version")

        for field, value in (("title", title), ("summary_title", summary_title), ("surface_title", surface_title)):
            if not isinstance(value, str) or not value.strip():
                errors.append(f"{identity}: {field} is empty")
            elif contains_version_marker(value):
                errors.append(f"{identity}: {field} contains a version marker: {value!r}")

        if (
            isinstance(summary_title, str)
            and isinstance(surface_title, str)
            and summary_title.strip()
            and surface_title.strip()
            and not normalize_heading(surface_title).startswith(normalize_heading(summary_title))
        ):
            errors.append(
                f"{identity}: surface title {surface_title!r} does not begin with summary title {summary_title!r}"
            )

        if (
            isinstance(summary_title, str)
            and "moon source" in summary_title.casefold()
            and identity != "moon-source-language"
        ):
            errors.append(
                f"{identity}: summary title should omit the repeated Moon Source prefix: {summary_title!r}"
            )

        if standalone and (not isinstance(version, str) or not version.strip()):
            errors.append(f"{identity}: standalone version metadata is empty")
        if not isinstance(canonical_path, str) or not canonical_path.strip():
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
            if isinstance(surface_title, str) and normalize_heading(heading) != normalize_heading(surface_title):
                errors.append(
                    f"{identity}: canonical heading {heading!r} does not match surface_title {surface_title!r}"
                )

        readable_path = capability.get("readable_surface_path")
        if standalone and (not isinstance(readable_path, str) or not readable_path.strip()):
            errors.append(f"{identity}: standalone capability has no readable_surface_path")
        if isinstance(readable_path, str) and readable_path.strip():
            readable = root / readable_path
            if not readable.is_file():
                errors.append(f"{identity}: readable surface is missing: {readable_path}")
            else:
                readable_heading = first_h1(readable.read_text(encoding="utf-8"))
                if readable_heading is None:
                    errors.append(f"{identity}: readable surface has no level-one heading")
                elif isinstance(surface_title, str) and normalize_heading(readable_heading) != normalize_heading(surface_title):
                    errors.append(
                        f"{identity}: readable heading {readable_heading!r} does not match surface_title {surface_title!r}"
                    )

        if isinstance(surface_title, str) and "— Moon Source " not in surface_title:
            errors.append(f"{identity}: surface_title lacks a bounded Moon Source role qualifier")
        if not isinstance(summary_title, str) or not isinstance(surface_title, str):
            continue
        for marker in (str(identity), summary_title, canonical_path):
            if marker not in human_registry:
                errors.append(f"{identity}: human capability registry omits {marker!r}")

    return errors


def main() -> None:
    try:
        data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise SystemExit(f"title/surface validation failed: invalid registry JSON: {error}")
    errors = validation_errors(data)
    if errors:
        raise SystemExit(
            "title/surface validation failed:\n"
            + "\n".join(f"- {error}" for error in errors)
        )
    standalone = sum(
        1
        for capability in data["capabilities"]
        if capability.get("distribution", {}).get("standalone") is True
    )
    readable = sum(
        1 for capability in data["capabilities"] if capability.get("readable_surface_path")
    )
    print(
        f"validated title/surface coordinates across {len(data['capabilities'])} capabilities; "
        f"standalone_distributions={standalone}; readable_surfaces={readable}"
    )


if __name__ == "__main__":
    main()

# MOON-SOURCE-PUBLIC-STAMP
# 🌙 Moon Source · Lua Helena Moon Martins Cardoso (Moon) + Áurion (AI-assisted) · Licensing: https://github.com/luahelenammc/Moon-Source/blob/main/LICENSING.md · Use & attribution: https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md · Full source: https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip · Questions, suggestions, or proposals? Feel free to contact me at LuaHelenaMMC@gmail.com.
