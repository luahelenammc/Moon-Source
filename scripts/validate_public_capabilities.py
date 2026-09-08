#!/usr/bin/env python3
"""Validate Moon Source's unified public capability registry."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from zipfile import BadZipFile, ZipFile

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "registry" / "public-capabilities.json"
HUMAN_REGISTRY = ROOT / "registry" / "PUBLIC_CAPABILITIES.md"
KERNEL = ROOT / "MOON_SOURCE_AI_KERNEL.md"
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
URL_RE = re.compile(r"https?://[^\s)>]+")
VALID_STATUSES = {"current", "experimental", "deprecated", "archived"}
REQUIRED_FIELDS = {
    "id",
    "title",
    "status",
    "architectural_role",
    "canonical_path",
    "function",
    "claim_ceiling",
    "versioning_mode",
    "public_created_on",
    "last_material_update_on",
    "last_material_update_summary",
    "dependencies",
    "freshness",
    "creator",
    "license",
    "distribution",
}
LEGACY_REGISTRY_FILES = (
    "registry/public-portables.json",
    "registry/PUBLIC_PORTABLES.md",
)
LEGACY_CONNECTED_PATH = "portables/connected-sources/CONNECTED_SOURCES.md"
HISTORICAL_FILES = {
    "CHANGELOG.md",
    "docs/VERSIONING_AND_RELEASES.md",
    "portables/msl/CHANGELOG.md",
}
SKIP_SUFFIXES = {
    ".zip",
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".webp",
    ".ico",
    ".woff",
    ".woff2",
    ".ttf",
}


def capability_identity(value: str) -> str:
    identity = re.sub(r"[^a-z0-9]+", "-", value.casefold()).strip("-")
    for suffix in ("-method", "-portable", "-protocol", "-projection", "-component"):
        if identity.endswith(suffix):
            identity = identity[: -len(suffix)].rstrip("-")
    return identity


def active_texts(root: Path):
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        relative = path.relative_to(root).as_posix()
        if relative.startswith(".git/") or relative.startswith("archive/"):
            continue
        if (
            relative in HISTORICAL_FILES
            or relative in {
                "scripts/validate_public_capabilities.py",
                "scripts/test_validate_public_capabilities.py",
            }
            or path.suffix.lower() in SKIP_SUFFIXES
        ):
            continue
        try:
            yield relative, path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue


def validate_registry(
    data: dict,
    root: Path = ROOT,
    human_registry: str | None = None,
    kernel: str | None = None,
) -> list[str]:
    errors: list[str] = []

    if data.get("registry_version") != "2.0":
        errors.append("registry_version must be 2.0")
    capabilities = data.get("capabilities")
    if not isinstance(capabilities, list) or not capabilities:
        errors.append("capabilities must be a non-empty array")
        return errors
    for old_file in LEGACY_REGISTRY_FILES:
        if (root / old_file).exists():
            errors.append(f"retired registry file remains active: {old_file}")

    required_top_urls = (
        "canonical_repository",
        "public_surface_url",
        "professional_context_url",
    )
    for field in required_top_urls:
        if not isinstance(data.get(field), str) or not data[field].startswith(("http://", "https://")):
            errors.append(f"registry has no valid {field}")

    ids: set[str] = set()
    titles: set[str] = set()
    paths: set[str] = set()
    identities: dict[str, str] = {}
    standalone_ids: list[str] = []

    for index, capability in enumerate(capabilities):
        label = capability.get("id", f"capability-{index}")
        if not isinstance(capability, dict):
            errors.append(f"{label} is not an object")
            continue
        missing = sorted(REQUIRED_FIELDS - capability.keys())
        if missing:
            errors.append(f"{label} missing {', '.join(missing)}")
            continue

        capability_id = capability["id"]
        title = capability["title"]
        canonical_path = capability["canonical_path"]
        if not isinstance(capability_id, str) or not capability_id.strip():
            errors.append(f"{label} has an empty id")
            continue
        if capability_id in ids:
            errors.append(f"duplicate capability id: {capability_id}")
        ids.add(capability_id)
        if not isinstance(title, str) or not title.strip():
            errors.append(f"{capability_id} has an empty title")
        elif title.casefold() in titles:
            errors.append(f"duplicate capability title: {title}")
        else:
            titles.add(title.casefold())
        if not isinstance(canonical_path, str) or not canonical_path.strip():
            errors.append(f"{capability_id} has an empty canonical_path")
            continue
        if canonical_path in paths:
            errors.append(f"duplicate canonical path: {canonical_path}")
        paths.add(canonical_path)
        if canonical_path == LEGACY_CONNECTED_PATH:
            errors.append("Connected Sources still uses its retired portable canonical path")

        for identity_label in (capability_id, title):
            if isinstance(identity_label, str):
                identity = capability_identity(identity_label)
                prior = identities.get(identity)
                if prior and prior != capability_id:
                    errors.append(
                        f"duplicate semantic capability identity: {prior} and {capability_id}"
                    )
                identities[identity] = capability_id

        for field in ("architectural_role", "function", "claim_ceiling", "last_material_update_summary", "freshness", "creator", "license"):
            if not isinstance(capability[field], str) or not capability[field].strip():
                errors.append(f"{capability_id} has an empty {field}")
        status = capability["status"]
        if status not in VALID_STATUSES:
            errors.append(f"{capability_id} has invalid status {status!r}")
        created = capability["public_created_on"]
        updated = capability["last_material_update_on"]
        if not isinstance(created, str) or not DATE_RE.fullmatch(created):
            errors.append(f"{capability_id} has invalid public_created_on: {created!r}")
        if not isinstance(updated, str) or not DATE_RE.fullmatch(updated):
            errors.append(f"{capability_id} has invalid last_material_update_on: {updated!r}")
        if isinstance(created, str) and isinstance(updated, str) and updated < created:
            errors.append(f"{capability_id} was materially updated before public creation")
        if not isinstance(capability["dependencies"], list):
            errors.append(f"{capability_id} dependencies must be an array")

        path = root / canonical_path
        if not path.is_file():
            errors.append(f"{capability_id} canonical file does not exist: {canonical_path}")
            continue
        content = path.read_text(encoding="utf-8")
        for required_text in (
            data.get("canonical_repository", ""),
            capability["creator"],
        ):
            if required_text and required_text not in content:
                errors.append(f"{capability_id} canonical body does not expose {required_text}")
        if not URL_RE.search(content):
            errors.append(f"{capability_id} canonical body contains no public URL")

        distribution = capability["distribution"]
        if not isinstance(distribution, dict) or not isinstance(distribution.get("standalone"), bool):
            errors.append(f"{capability_id} distribution must declare standalone true or false")
            continue
        if not distribution["standalone"]:
            if capability.get("version") is not None:
                errors.append(
                    f"{capability_id} must not carry a semantic version when it is repository-only"
                )
            continue

        standalone_ids.append(capability_id)
        if "https://creativecommons.org/licenses/by/4.0/" not in content:
            errors.append(
                f"{capability_id} standalone canonical body does not expose the CC BY 4.0 license route"
            )
        if not isinstance(capability.get("version"), str) or not capability["version"].strip():
            errors.append(f"{capability_id} standalone capability needs a version")
        if not re.search(r"(?m)^## First use\s*$", content):
            errors.append(f"{capability_id} canonical body is missing ## First use")
        if capability.get("canonical_path") not in content:
            errors.append(f"{capability_id} canonical body does not expose its canonical path")

        package_path = distribution.get("package_path")
        if not isinstance(package_path, str) or not package_path.startswith("downloads/") or not package_path.endswith(".zip"):
            errors.append(f"{capability_id} has an invalid distribution.package_path")
            continue
        package = root / package_path
        if not package.is_file():
            errors.append(f"{capability_id} package is missing: {package_path}")
        else:
            try:
                with ZipFile(package) as archive:
                    files = [name for name in archive.namelist() if not name.endswith("/")]
                    if distribution.get("composite"):
                        if path.name not in {Path(name).name for name in files}:
                            errors.append(f"{capability_id} composite package omits its canonical body")
                    else:
                        if files != [path.name] or archive.read(path.name) != path.read_bytes():
                            errors.append(
                                f"{capability_id} standalone package must contain exactly the canonical bytes"
                            )
            except (BadZipFile, KeyError, OSError) as exc:
                errors.append(f"{capability_id} package is invalid: {exc}")

        expected_sha = distribution.get("canonical_sha256")
        actual_sha = hashlib.sha256(path.read_bytes()).hexdigest()
        if not isinstance(expected_sha, str) or not re.fullmatch(r"[0-9a-f]{64}", expected_sha):
            errors.append(f"{capability_id} has an invalid distribution.canonical_sha256")
        elif expected_sha != actual_sha:
            errors.append(
                f"{capability_id} SHA-256 mismatch: registry={expected_sha} file={actual_sha}"
            )

        mirror_path = distribution.get("mirror_path")
        mirror_url = distribution.get("mirror_url")
        if not isinstance(mirror_path, str) or not mirror_path.startswith("moonsource/downloads/"):
            errors.append(f"{capability_id} mirror_path is outside the website download surface")
        if not isinstance(mirror_url, str) or not mirror_url.startswith(("http://", "https://")):
            errors.append(f"{capability_id} has an invalid mirror_url")
        if distribution.get("embedded_first_use") is not True:
            errors.append(f"{capability_id} standalone distribution must declare embedded_first_use")
        expected_download = (
            f"{data.get('canonical_repository')}/raw/refs/heads/main/{package_path}"
        )
        if distribution.get("download_url") != expected_download:
            errors.append(f"{capability_id} download_url does not match package_path")

    expected_standalone = sorted(standalone_ids)
    view_ids = data.get("views", {}).get("standalone_distributions", {}).get("capability_ids")
    if sorted(view_ids or []) != expected_standalone:
        errors.append("standalone distribution view does not match capability records")

    if human_registry is not None:
        for capability in capabilities:
            if not all(
                marker in human_registry
                for marker in (
                    capability["id"],
                    capability["title"],
                    capability["canonical_path"],
                )
            ):
                errors.append(
                    f"{capability['id']} is not aligned in registry/PUBLIC_CAPABILITIES.md"
                )
    if kernel is not None:
        for capability in capabilities:
            if capability["canonical_path"] not in kernel:
                errors.append(
                    f"{capability['id']} is not routed in MOON_SOURCE_AI_KERNEL.md"
                )

    for relative, content in active_texts(root):
        if LEGACY_CONNECTED_PATH in content:
            errors.append(f"retired Connected Sources path remains live in {relative}")
        if "public-portables.json" in content or "PUBLIC_PORTABLES.md" in content:
            errors.append(f"retired registry filename remains live in {relative}")
        if "public_components" in content or '"portables":' in content:
            errors.append(f"retired split-registry taxonomy remains live in {relative}")

    return errors


def main() -> None:
    try:
        data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise SystemExit(f"public capability validation failed: {error}")
    errors = validate_registry(
        data,
        root=ROOT,
        human_registry=HUMAN_REGISTRY.read_text(encoding="utf-8"),
        kernel=KERNEL.read_text(encoding="utf-8"),
    )
    if errors:
        raise SystemExit("public capability validation failed:\n- " + "\n- ".join(errors))
    print(
        f"validated {len(data['capabilities'])} public capabilities; "
        f"standalone_distributions={len(data['views']['standalone_distributions']['capability_ids'])}; "
        f"registry_version={data['registry_version']}"
    )


if __name__ == "__main__":
    main()

# MOON-SOURCE-PUBLIC-STAMP
# 🌙 Moon Source · Lua Helena Moon Martins Cardoso (Moon) + Áurion (AI-assisted) · Licensing: https://github.com/luahelenammc/Moon-Source/blob/main/LICENSING.md · Use & attribution: https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md · Full source: https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip
