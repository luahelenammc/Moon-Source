#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 Lua Helena Moon Martins Cardoso (Moon)
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import hashlib
import json
import re
import subprocess
import tempfile
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VISIBILITY = "-" + "public"
VERSION_SUFFIX = re.compile(r"(\d+(?:\.\d+)+)" + re.escape(VISIBILITY) + r"\b")


def tracked_files() -> list[str]:
    raw = subprocess.check_output(["git", "ls-files", "-z"], cwd=ROOT)
    return [p.decode("utf-8") for p in raw.split(b"\0") if p]


def normalize_paths() -> None:
    for old in sorted(tracked_files(), key=len, reverse=True):
        new = VERSION_SUFFIX.sub(r"\1", old)
        if new != old:
            subprocess.run(["git", "mv", old, new], cwd=ROOT, check=True)


def normalize_texts() -> None:
    for rel in tracked_files():
        path = ROOT / rel
        if not path.is_file() or path.suffix.lower() == ".zip":
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        normalized = VERSION_SUFFIX.sub(r"\1", text)
        if normalized != text:
            path.write_text(normalized, encoding="utf-8")


def add_meta_rules() -> None:
    rule = """## Visibility-neutral version tokens

Repository visibility is an orthogonal publication/distribution state, not part of a version token. Moon Source versions therefore use bare release state only. Public/private exposure belongs in repository location, status, boundary and distribution metadata; never append a visibility qualifier to the numeric version.

Removing a legacy visibility qualifier is a bookkeeping-only normalization and does not by itself advance the numeric release. Future accepted updates continue to follow the governing increment rule on the bare number itself.

"""
    for rel in (
        "docs/REPOSITORY_NAMING_AND_VERSIONING.md",
        "templates/REPOSITORY_NAMING_AND_VERSIONING.md",
        "docs/VERSIONING_AND_RELEASES.md",
    ):
        path = ROOT / rel
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        if "## Visibility-neutral version tokens" in text:
            continue
        marker = "<!-- MOON-SOURCE-PUBLIC-STAMP -->"
        if marker in text:
            text = text.replace(marker, rule + marker, 1)
        else:
            text = text.rstrip() + "\n\n" + rule
        path.write_text(text, encoding="utf-8")


def install_guard() -> None:
    guard = '''#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 Lua Helena Moon Martins Cardoso (Moon)
# SPDX-License-Identifier: Apache-2.0
"""Reject repository-visibility qualifiers encoded inside numeric versions."""

from __future__ import annotations

import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VISIBILITY = "-" + "public"
BAD = re.compile(r"\\d+(?:\\.\\d+)+" + re.escape(VISIBILITY) + r"\\b")
SKIP_SUFFIXES = {".zip", ".png", ".jpg", ".jpeg", ".gif", ".webp", ".ico", ".woff", ".woff2", ".ttf", ".pyc"}


def main() -> None:
    raw = subprocess.check_output(["git", "ls-files", "-z"], cwd=ROOT)
    violations = []
    for item in (p for p in raw.split(b"\\0") if p):
        rel = item.decode("utf-8")
        if BAD.search(rel):
            violations.append(f"path: {rel}")
        path = ROOT / rel
        if not path.is_file() or path.suffix.lower() in SKIP_SUFFIXES:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        if BAD.search(text):
            violations.append(f"text: {rel}")
    if violations:
        raise SystemExit("visibility-qualified numeric versions are forbidden:\\n- " + "\\n- ".join(violations))
    print("version visibility guard passed")


if __name__ == "__main__":
    main()
'''
    (ROOT / "scripts/check_version_visibility.py").write_text(guard, encoding="utf-8")


def rebuild_registered_packages() -> set[Path]:
    registry_path = ROOT / "registry/public-capabilities.json"
    registry = json.loads(registry_path.read_text(encoding="utf-8"))
    registered: set[Path] = set()
    for cap in registry["capabilities"]:
        dist = cap.get("distribution") or {}
        if not dist.get("standalone"):
            continue
        canonical = ROOT / cap["canonical_path"]
        dist["canonical_sha256"] = hashlib.sha256(canonical.read_bytes()).hexdigest()
        package = ROOT / dist["package_path"]
        registered.add(package.resolve())
        if not dist.get("composite"):
            package.parent.mkdir(parents=True, exist_ok=True)
            with zipfile.ZipFile(package, "w", compression=zipfile.ZIP_DEFLATED) as zf:
                info = zipfile.ZipInfo(canonical.name, date_time=(1980, 1, 1, 0, 0, 0))
                info.compress_type = zipfile.ZIP_DEFLATED
                info.external_attr = 0o644 << 16
                zf.writestr(info, canonical.read_bytes())
    registry_path.write_text(json.dumps(registry, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return registered


def normalize_other_zips(registered: set[Path]) -> None:
    for package in sorted((ROOT / "downloads").glob("*.zip")):
        if package.resolve() in registered:
            continue
        try:
            with zipfile.ZipFile(package, "r") as src:
                entries = [(i, src.read(i.filename)) for i in src.infolist()]
        except zipfile.BadZipFile:
            continue
        changed = False
        with tempfile.NamedTemporaryFile(delete=False, suffix=".zip") as tmp:
            tmp_path = Path(tmp.name)
        with zipfile.ZipFile(tmp_path, "w") as dst:
            for info, data in entries:
                name = VERSION_SUFFIX.sub(r"\1", info.filename)
                try:
                    text = data.decode("utf-8")
                except UnicodeDecodeError:
                    new_data = data
                else:
                    new_data = VERSION_SUFFIX.sub(r"\1", text).encode("utf-8")
                if name != info.filename or new_data != data:
                    changed = True
                new_info = zipfile.ZipInfo(name, date_time=info.date_time)
                new_info.compress_type = info.compress_type
                new_info.comment = info.comment
                new_info.extra = info.extra
                new_info.internal_attr = info.internal_attr
                new_info.external_attr = info.external_attr
                new_info.create_system = info.create_system
                dst.writestr(new_info, new_data)
        if changed:
            package.write_bytes(tmp_path.read_bytes())
        tmp_path.unlink(missing_ok=True)


def cleanup_one_shot() -> None:
    (ROOT / ".github/workflows/normalize-version-visibility.yml").unlink(missing_ok=True)
    Path(__file__).unlink(missing_ok=True)


def main() -> None:
    normalize_paths()
    normalize_texts()
    add_meta_rules()
    install_guard()
    registered = rebuild_registered_packages()
    normalize_other_zips(registered)
    cleanup_one_shot()


if __name__ == "__main__":
    main()
