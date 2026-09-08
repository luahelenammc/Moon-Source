#!/usr/bin/env python3
"""Verify that the standalone AI Kernel package carries the current canonical body."""

from pathlib import Path
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "MOON_SOURCE_AI_KERNEL.md"
PACKAGE = ROOT / "downloads" / "moon-source-ai-kernel.zip"
EXPECTED_NAME = SOURCE.name


def fail(message: str) -> None:
    print(f"AI Kernel package validation failed: {message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> None:
    if not SOURCE.is_file():
        fail(f"missing canonical body: {SOURCE.relative_to(ROOT)}")
    if not PACKAGE.is_file():
        fail(f"missing package: {PACKAGE.relative_to(ROOT)}")

    try:
        with zipfile.ZipFile(PACKAGE, "r") as archive:
            names = archive.namelist()
            if names != [EXPECTED_NAME]:
                fail(f"expected exactly [{EXPECTED_NAME!r}], found {names!r}")
            packaged = archive.read(EXPECTED_NAME)
    except zipfile.BadZipFile as exc:
        fail(f"invalid ZIP: {exc}")

    canonical = SOURCE.read_bytes()
    if packaged != canonical:
        fail("packaged MOON_SOURCE_AI_KERNEL.md bytes differ from the canonical body")

    print("AI Kernel package is current and byte-identical to MOON_SOURCE_AI_KERNEL.md.")


if __name__ == "__main__":
    main()
