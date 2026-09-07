#!/usr/bin/env python3
"""Validate the public Moon Source component registry contract."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "registry" / "public-portables.json"
HUMAN_REGISTRY = ROOT / "registry" / "PUBLIC_PORTABLES.md"
KERNEL = ROOT / "MOON_SOURCE_AI_KERNEL.md"
IMPLEMENTATIONS = ROOT / "docs" / "EXISTING_IMPLEMENTATIONS.md"
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
AUTHORITY_START = "<!-- MOON-SOURCE-CANONICAL-AUTHORITY:START -->"
AUTHORITY_END = "<!-- MOON-SOURCE-CANONICAL-AUTHORITY:END -->"
IDENTITY_SUFFIX_RE = re.compile(r"(?:[-_\s]+)(?:method|portable|protocol|projection|component)$", re.IGNORECASE)
VALID_STATUSES = {"current", "experimental", "deprecated", "archived"}
REQUIRED_FIELDS = {
    "id",
    "title",
    "class",
    "canonical_path",
    "function",
    "claim_ceiling",
    "public_created_on",
    "last_material_update_on",
    "last_material_update_summary",
    "status",
}


def fail(message: str) -> None:
    raise SystemExit(f"public component validation failed: {message}")


def text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def capability_identity(value: str) -> str:
    """Normalize registry labels without attempting semantic prose classification."""

    identity = re.sub(r"[^a-z0-9]+", "-", value.casefold()).strip("-")
    while True:
        reduced = IDENTITY_SUFFIX_RE.sub("", identity).strip("-")
        if reduced == identity:
            return identity
        identity = reduced


def declared_authorities(kernel: str) -> dict[str, str]:
    if AUTHORITY_START not in kernel or AUTHORITY_END not in kernel:
        fail("kernel is missing the canonical-authority map")

    block = kernel.split(AUTHORITY_START, 1)[1].split(AUTHORITY_END, 1)[0]
    entries = re.findall(r"^- ([^→\n]+?) → `([^`]+)`", block, flags=re.MULTILINE)
    if not entries:
        fail("kernel canonical-authority map has no entries")

    authorities: dict[str, str] = {}
    for title, path in entries:
        identity = capability_identity(title.strip())
        if identity in authorities:
            fail(f"kernel declares more than one active authority for {title.strip()}")
        authorities[identity] = path
    return authorities


def main() -> None:
    if not REGISTRY.is_file():
        fail("registry/public-portables.json is missing")

    try:
        data = json.loads(text(REGISTRY))
    except json.JSONDecodeError as error:
        fail(f"registry JSON is invalid: {error}")

    components = data.get("public_components")
    portables = data.get("portables")
    if not isinstance(components, list) or not components:
        fail("public_components must be a non-empty array")
    if not isinstance(portables, list):
        fail("portables must be an array")

    human_registry = text(HUMAN_REGISTRY)
    kernel = text(KERNEL)
    implementations = text(IMPLEMENTATIONS)
    component_ids: set[str] = set()
    component_paths: set[str] = set()
    portable_ids = {entry.get("id") for entry in portables}
    portable_paths = {entry.get("canonical_path") for entry in portables}
    portable_identities: dict[str, str] = {}
    for index, portable in enumerate(portables):
        if not isinstance(portable, dict):
            fail(f"portable {index} is not an object")
        entry_identities: set[str] = set()
        for label in (portable.get("id"), portable.get("title")):
            if not isinstance(label, str) or not label.strip():
                fail(f"portable {index} has an empty identity label")
            identity = capability_identity(label)
            if identity in entry_identities:
                continue
            entry_identities.add(identity)
            previous = portable_identities.get(identity)
            if previous is not None:
                fail(f"portable identity {identity} is duplicated by {previous} and {label}")
            portable_identities[identity] = label

    kernel_authorities = declared_authorities(kernel)
    for portable in portables:
        identity = capability_identity(portable["title"])
        declared_path = kernel_authorities.get(identity)
        if declared_path != portable["canonical_path"]:
            fail(
                f"kernel authority for {portable['title']} must name only "
                f"{portable['canonical_path']}; found {declared_path!r}"
            )

    for index, component in enumerate(components):
        if not isinstance(component, dict):
            fail(f"component {index} is not an object")
        missing = sorted(REQUIRED_FIELDS - component.keys())
        if missing:
            fail(f"component {index} is missing: {', '.join(missing)}")

        component_id = component["id"]
        canonical_path = component["canonical_path"]
        if not isinstance(component_id, str) or not component_id.strip():
            fail(f"component {index} has an empty id")
        if component_id in component_ids:
            fail(f"duplicate component id: {component_id}")
        component_ids.add(component_id)

        if not isinstance(canonical_path, str) or not canonical_path.strip():
            fail(f"{component_id} has an empty canonical_path")
        if canonical_path in component_paths:
            fail(f"duplicate component canonical_path: {canonical_path}")
        component_paths.add(canonical_path)

        if canonical_path in portable_paths:
            fail(f"component {component_id} is silently duplicated in the portable array")
        if component_id in portable_ids:
            fail(f"component id {component_id} is duplicated in the portable array")
        component_identity = capability_identity(component_id)
        title_identity = capability_identity(component["title"])
        duplicate_identities = {
            identity
            for identity in (component_identity, title_identity)
            if identity in portable_identities
        }
        if duplicate_identities:
            fail(
                f"component {component_id} duplicates current portable capability identity: "
                f"{', '.join(sorted(duplicate_identities))}"
            )

        for field in ("function", "claim_ceiling", "last_material_update_summary"):
            value = component[field]
            if not isinstance(value, str) or not value.strip():
                fail(f"{component_id} has an empty {field}")

        status = component["status"]
        if status not in VALID_STATUSES:
            fail(f"{component_id} has invalid status {status!r}")

        created = component["public_created_on"]
        updated = component["last_material_update_on"]
        if not isinstance(created, str) or not DATE_RE.fullmatch(created):
            fail(f"{component_id} has invalid public_created_on: {created!r}")
        if not isinstance(updated, str) or not DATE_RE.fullmatch(updated):
            fail(f"{component_id} has invalid last_material_update_on: {updated!r}")
        if updated < created:
            fail(f"{component_id} was materially updated before public creation")

        path = ROOT / canonical_path
        if not path.is_file():
            fail(f"{component_id} canonical path does not exist: {canonical_path}")

        if canonical_path not in human_registry and component_id not in human_registry:
            fail(f"{component_id} is not represented in registry/PUBLIC_PORTABLES.md")

        if canonical_path not in kernel and component["title"] not in kernel:
            fail(f"{component_id} is not routed or represented in MOON_SOURCE_AI_KERNEL.md")

        implementation_markers = {
            canonical_path,
            Path(canonical_path).name,
            component["title"],
        }
        if not any(marker in implementations for marker in implementation_markers):
            fail(f"{component_id} is not represented in docs/EXISTING_IMPLEMENTATIONS.md")

    print(
        f"validated {len(components)} non-portable public components; "
        f"registry_version={data.get('registry_version', 'missing')}"
    )


if __name__ == "__main__":
    main()

# MOON-SOURCE-PUBLIC-STAMP
# 🌙 Moon Source · Lua Helena Moon Martins Cardoso (Moon) + Áurion (AI-assisted) · Licensing: https://github.com/luahelenammc/Moon-Source/blob/main/LICENSING.md · Use & attribution: https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md · Full source: https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip
