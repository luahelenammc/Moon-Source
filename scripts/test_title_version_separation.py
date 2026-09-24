#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Small regression tests for the public title/version coordinate guard."""

from __future__ import annotations

import copy
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from check_title_version_separation import (  # noqa: E402
    VERSIONED_CURRENT_PATH_EXCEPTIONS,
    contains_audience_version_label,
    contains_version_marker,
    contains_version_marker_in_path,
    current_path_error,
    first_h1,
    normalize_heading,
    validation_errors,
)

ROOT = Path(__file__).resolve().parents[1]
HUMAN_REGISTRY = (ROOT / "registry" / "PUBLIC_CAPABILITIES.md").read_text(encoding="utf-8")


def main() -> None:
    assert contains_version_marker("Preflight V2")
    assert contains_version_marker("Be My Eyes 1.0-public")
    assert contains_version_marker("Moon Source Language 4.3")
    assert not contains_version_marker("Preflight")
    assert not contains_version_marker("Chat–Work Routing Protocol")
    assert contains_audience_version_label("1.2-public")
    assert contains_audience_version_label("2.0_private")
    assert contains_audience_version_label("3.1.local")
    assert not contains_audience_version_label("1.2")
    assert not contains_audience_version_label("5.1-rc1")
    assert contains_version_marker_in_path("portables/msl/MSL_5_1.md")
    assert contains_version_marker_in_path("portables/msl/v5/MOON_SOURCE_LANGUAGE.md")
    assert contains_version_marker_in_path("downloads/preflight-v2.zip")
    assert contains_version_marker_in_path("moonsource/downloads/PREFLIGHT_V2.md")
    assert not contains_version_marker_in_path("portables/msl/MOON_SOURCE_LANGUAGE.md")
    assert current_path_error("msl", "canonical_path", "portables/msl/MSL_5_1.md")
    exception_path = "portables/preflight/PREFLIGHT_V2.md"
    VERSIONED_CURRENT_PATH_EXCEPTIONS[exception_path] = "parallel compatibility generation"
    assert current_path_error("preflight", "canonical_path", exception_path) is None
    VERSIONED_CURRENT_PATH_EXCEPTIONS[exception_path] = ""
    assert current_path_error("preflight", "canonical_path", exception_path)
    del VERSIONED_CURRENT_PATH_EXCEPTIONS[exception_path]
    assert first_h1("intro\n# Stable Name\n") == "Stable Name"
    assert normalize_heading("# 🧭 Setup — Moon Source portable") == "Setup — Moon Source portable"

    data = json.loads(
        (ROOT / "registry" / "public-capabilities.json").read_text(encoding="utf-8")
    )
    assert not validation_errors(data)

    fixture = copy.deepcopy(data)
    msl = next(item for item in fixture["capabilities"] if item["id"] == "moon-source-language")
    msl["canonical_path"] = "portables/msl/MOON_SOURCE_LANGUAGE_V5_1.md"
    errors = validation_errors(fixture, root=ROOT, human_registry=HUMAN_REGISTRY)
    assert any("current canonical_path contains a version marker" in error for error in errors)

    fixture = copy.deepcopy(data)
    preflight = next(item for item in fixture["capabilities"] if item["id"] == "preflight")
    preflight["distribution"]["package_path"] = "downloads/preflight-v2.zip"
    errors = validation_errors(fixture, root=ROOT, human_registry=HUMAN_REGISTRY)
    assert any("current package_path contains a version marker" in error for error in errors)

    fixture = copy.deepcopy(data)
    preflight = next(item for item in fixture["capabilities"] if item["id"] == "preflight")
    preflight["distribution"]["mirror_path"] = "moonsource/downloads/PREFLIGHT_V2.md"
    errors = validation_errors(fixture, root=ROOT, human_registry=HUMAN_REGISTRY)
    assert any("current mirror_path contains a version marker" in error for error in errors)

    fixture = copy.deepcopy(data)
    fixture["capabilities"][0]["title"] = "Be My Eyes 1.0-public"
    errors = validation_errors(fixture, root=ROOT, human_registry=HUMAN_REGISTRY)
    assert any("title contains a version marker" in error for error in errors)

    fixture = copy.deepcopy(data)
    fixture["capabilities"][0]["surface_title"] = "Wrong — Moon Source portable"
    errors = validation_errors(fixture, root=ROOT, human_registry=HUMAN_REGISTRY)
    assert any("canonical heading" in error for error in errors)

    fixture = copy.deepcopy(data)
    fixture["capabilities"][0]["summary_title"] = "Moon Source Be My Eyes"
    errors = validation_errors(fixture, root=ROOT, human_registry=HUMAN_REGISTRY)
    assert any("summary title should omit" in error for error in errors)

    # Legacy distributed labels are grandfathered only at their exact existing values.
    fixture = copy.deepcopy(data)
    be_my_eyes = next(item for item in fixture["capabilities"] if item["id"] == "be-my-eyes")
    be_my_eyes["version"] = "1.1-public"
    errors = validation_errors(fixture, root=ROOT, human_registry=HUMAN_REGISTRY)
    assert any("version contains an audience/surface label" in error for error in errors)

    fixture = copy.deepcopy(data)
    lwr = next(item for item in fixture["capabilities"] if item["id"] == "lifecycle-workspace-router")
    lwr["version"] = "1.2-public"
    errors = validation_errors(fixture, root=ROOT, human_registry=HUMAN_REGISTRY)
    assert any("version contains an audience/surface label" in error for error in errors)

    print("title/surface/version coordinate tests passed")


if __name__ == "__main__":
    main()

# MOON-SOURCE-PUBLIC-STAMP
# 🌙 Moon Source · Lua Helena Moon Martins Cardoso (Moon) + Áurion (AI-assisted) · Licensing: https://github.com/luahelenammc/Moon-Source/blob/main/LICENSING.md · Use & attribution: https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md · Full source: https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip · Questions, suggestions, or proposals? Feel free to contact me at LuaHelenaMMC@gmail.com.
