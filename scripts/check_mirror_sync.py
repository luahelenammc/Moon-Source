#!/usr/bin/env python3
"""Verify canonical portable bytes against the branded website mirrors."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "registry" / "public-portables.json"


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def read_mirror(portable: dict, mirror_root: Path | None) -> bytes:
    if mirror_root is not None:
        return (mirror_root / portable["mirror_path"]).read_bytes()
    request = Request(
        portable["mirror_url"],
        headers={"User-Agent": "Moon-Source-mirror-check/1.0"},
    )
    with urlopen(request, timeout=20) as response:
        return response.read()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mirror-root",
        type=Path,
        help="local LUAHELENA checkout; otherwise fetch each mirror_url",
    )
    args = parser.parse_args()

    data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    failures: list[str] = []

    for portable in data["portables"]:
        canonical_path = ROOT / portable["canonical_path"]
        canonical_bytes = canonical_path.read_bytes()
        actual_canonical = sha256(canonical_bytes)
        expected = portable["canonical_sha256"]

        if actual_canonical != expected:
            failures.append(
                f"{portable['id']}: canonical fingerprint mismatch "
                f"(registry={expected}, file={actual_canonical})"
            )

        try:
            mirror_bytes = read_mirror(portable, args.mirror_root)
        except Exception as error:
            failures.append(f"{portable['id']}: could not read mirror: {error}")
            continue

        actual_mirror = sha256(mirror_bytes)
        if actual_mirror != actual_canonical:
            failures.append(
                f"{portable['id']}: mirror drift "
                f"(canonical={actual_canonical}, mirror={actual_mirror})"
            )

    if failures:
        print("\n".join(failures))
        raise SystemExit(1)

    print(f"mirror synchronization validated for {len(data['portables'])} public portables")


if __name__ == "__main__":
    main()

# MOON-SOURCE-PUBLIC-STAMP
# 🌙 Moon Source · Lua Helena Moon Martins Cardoso (Moon) + Áurion (AI-assisted) · Licensing: https://github.com/luahelenammc/Moon-Source/blob/main/LICENSING.md · Use & attribution: https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md · Full source: https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip
