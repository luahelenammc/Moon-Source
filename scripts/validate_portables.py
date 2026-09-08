#!/usr/bin/env python3
"""Validate the public portable registry and its canonical files."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from zipfile import BadZipFile, ZipFile

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
    "license",
    "license_class",
    "license_url",
    "licensing_url",
    "creator",
    "adaptation_policy",
    "supersedes",
    "archive_paths",
}
TOP_LEVEL_URLS = (
    "canonical_repository",
    "public_surface_url",
    "professional_context_url",
)
URL_RE = re.compile(r"https?://[^)\s>]+")
REQUIRED_PORTABLE_SUPPORT_FILES = {"README.md", "FIRST_USE.md"}
OPTIONAL_PORTABLE_SUPPORT_FILES = {"CHANGELOG.md"}
PORTABLE_SUPPORT_FILES = REQUIRED_PORTABLE_SUPPORT_FILES | OPTIONAL_PORTABLE_SUPPORT_FILES


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

        if portable["status"] != "current":
            fail(f"{portable['id']} is not current; the live registry exposes only current generations")
        if portable["archive_paths"]:
            fail(f"{portable['id']} exposes superseded archive paths in the live registry")

        family_dir = ROOT / "portables" / portable["slug"]
        if not family_dir.is_dir():
            fail(f"portable family directory missing: {portable['slug']}")

        missing_support = sorted(
            support_name
            for support_name in REQUIRED_PORTABLE_SUPPORT_FILES
            if not (family_dir / support_name).is_file()
        )
        if missing_support:
            fail(
                f"{portable['id']} is missing required support files: {missing_support}"
            )

        allowed_names = PORTABLE_SUPPORT_FILES | {path.name}
        extra_markdown = sorted(
            candidate.name
            for candidate in family_dir.glob("*.md")
            if candidate.name not in allowed_names
        )
        if extra_markdown:
            fail(
                f"{portable['id']} exposes non-current portable markdown files: {extra_markdown}"
            )

        content = path.read_text(encoding="utf-8")
        expected_sha256 = portable["canonical_sha256"]
        if not re.fullmatch(r"[0-9a-f]{64}", expected_sha256):
            fail(f"{portable['id']} has an invalid canonical_sha256")
        actual_sha256 = hashlib.sha256(path.read_bytes()).hexdigest()
        if actual_sha256 != expected_sha256:
            fail(
                f"{portable['id']} canonical_sha256 does not match its file: "
                f"expected={expected_sha256} actual={actual_sha256}"
            )

        download_prefix = f"{data['canonical_repository']}/raw/refs/heads/main/"
        download_url = portable["download_url"]
        if not isinstance(download_url, str) or not download_url.startswith(download_prefix):
            fail(
                f"{portable['id']} download_url must use the canonical GitHub package route: "
                f"{download_prefix}downloads/<package>.zip"
            )

        package_value = download_url[len(download_prefix):]
        if (
            "?" in package_value
            or "#" in package_value
            or not package_value.startswith("downloads/")
            or not package_value.endswith(".zip")
        ):
            fail(f"{portable['id']} download_url must point to a .zip package under downloads/")

        package_path = ROOT / package_value
        if not package_path.is_file():
            fail(f"{portable['id']} download package missing: {package_value}")

        try:
            with ZipFile(package_path) as package:
                package_files = [name for name in package.namelist() if not name.endswith("/")]
                package_file_set = set(package_files)
                required_package_files = {path.name} | REQUIRED_PORTABLE_SUPPORT_FILES
                allowed_package_files = {path.name} | PORTABLE_SUPPORT_FILES
                missing_package_files = sorted(required_package_files - package_file_set)
                unexpected_files = sorted(package_file_set - allowed_package_files)
                if (
                    len(package_file_set) != len(package_files)
                    or missing_package_files
                    or unexpected_files
                ):
                    fail(
                        f"{portable['id']} download package must contain the canonical file, "
                        f"README.md and FIRST_USE.md, with no unexpected files: {package_files}"
                    )
                packaged_bytes = package.read(path.name)
                for support_name in sorted(set(package_files) - {path.name}):
                    support_path = family_dir / support_name
                    if not support_path.is_file():
                        fail(
                            f"{portable['id']} package support file is missing from the "
                            f"portable directory: {support_name}"
                        )
                    if package.read(support_name) != support_path.read_bytes():
                        fail(
                            f"{portable['id']} package support file does not match the "
                            f"portable directory: {support_name}"
                        )
        except (BadZipFile, KeyError, OSError) as exc:
            fail(f"{portable['id']} has an invalid download package: {exc}")

        if packaged_bytes != path.read_bytes():
            fail(
                f"{portable['id']} download package does not contain the exact canonical bytes"
            )

        if not portable["mirror_path"].startswith("moonsource/downloads/"):
            fail(f"{portable['id']} mirror_path is outside the website download surface")
        for field in ("download_url", "mirror_url"):
            if not isinstance(portable[field], str) or not portable[field].startswith(("http://", "https://")):
                fail(f"{portable['id']} has an invalid {field}")

        for required_url in (
            data["canonical_repository"],
            data["public_surface_url"],
            data["professional_context_url"],
            portable["license_url"],
            portable["licensing_url"],
        ):
            if required_url not in content:
                fail(f"{portable['id']} does not expose {required_url}")

        if path_value not in content:
            fail(f"{portable['id']} does not expose its canonical path")
        if "mooon.com.br" in content:
            fail(f"{portable['id']} contains a stale canonical mooon.com.br URL")
        if portable["license"] != "CC-BY-4.0":
            fail(f"{portable['id']} is not classified as CC-BY-4.0")
        if portable["license_class"] != "open-content":
            fail(f"{portable['id']} is not classified as open-content")
        if portable["creator"] not in content:
            fail(f"{portable['id']} does not expose its creator")
        if "adapt" not in content.lower() or "change" not in content.lower():
            fail(f"{portable['id']} does not expose an adaptation/change expectation")
        if not content.lstrip().startswith("#"):
            fail(f"{portable['id']} does not start with a Markdown heading")
        if not URL_RE.search(content):
            fail(f"{portable['id']} contains no public metadata URL")

    print(f"validated {len(data['portables'])} current public portables")


if __name__ == "__main__":
    main()

# MOON-SOURCE-PUBLIC-STAMP
# 🌙 Moon Source · Lua Helena Moon Martins Cardoso (Moon) + Áurion (AI-assisted) · Licensing: https://github.com/luahelenammc/Moon-Source/blob/main/LICENSING.md · Use & attribution: https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md · Full source: https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip
