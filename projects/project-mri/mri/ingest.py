from __future__ import annotations

import hashlib
import os
import re
import tempfile
import zipfile
from datetime import datetime
from pathlib import Path
from pathlib import PurePosixPath

from .models import DocumentRecord

SUPPORTED_SUFFIXES = {".md", ".markdown", ".txt"}
MAX_CORPUS_BYTES = 5_000_000
MAX_DOCUMENT_BYTES = 1_000_000
MAX_DOCUMENTS = 500


def _title(text: str, path: Path) -> str:
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return path.stem.replace("_", " ").replace("-", " ").strip().title()


def _headings(text: str) -> list[str]:
    return [line.lstrip("#").strip() for line in text.splitlines() if line.startswith("#")]


def _safe_members(root: Path, names: list[str]) -> list[Path]:
    output: list[Path] = []
    for name in names:
        if not name or "\x00" in name:
            raise ValueError(f"Unsafe ZIP member: {name!r}")
        posix_name = PurePosixPath(name)
        if posix_name.is_absolute() or ".." in posix_name.parts:
            raise ValueError(f"Unsafe ZIP member: {name}")
        candidate = (root / name).resolve()
        if root.resolve() not in candidate.parents and candidate != root.resolve():
            raise ValueError(f"Unsafe ZIP member: {name}")
        output.append(candidate)
    return output


def _visible_files(root: Path) -> list[Path]:
    """Walk a directory without following symlinks or hidden branches."""

    files: list[Path] = []
    root = root.resolve()
    for current, dirnames, filenames in os.walk(root, topdown=True, followlinks=False):
        current_path = Path(current)
        for dirname in list(dirnames):
            path = current_path / dirname
            if path.is_symlink():
                raise ValueError(f"Symlink directory is not allowed: {path}")
            if dirname.startswith("."):
                dirnames.remove(dirname)
        for filename in filenames:
            path = current_path / filename
            if path.is_symlink():
                raise ValueError(f"Symlink file is not allowed: {path}")
            if filename.startswith("."):
                continue
            if not any(part.startswith(".") for part in path.relative_to(root).parts):
                files.append(path)
    return files


def _read_directory(root: Path, display_root: Path) -> list[DocumentRecord]:
    records: list[DocumentRecord] = []
    visible_files = _visible_files(root)
    if len(visible_files) > MAX_DOCUMENTS:
        raise ValueError(f"Corpus contains more than {MAX_DOCUMENTS} visible files")
    paths = sorted(
        path for path in visible_files
        if path.suffix.lower() in SUPPORTED_SUFFIXES
    )
    if len(paths) > MAX_DOCUMENTS:
        raise ValueError(f"Corpus contains {len(paths)} supported documents; limit is {MAX_DOCUMENTS}")
    if not visible_files:
        raise ValueError("Corpus is empty: no visible files were found")
    if not paths:
        raise ValueError("No supported Markdown/text documents found in corpus")
    total_bytes = 0
    for path in paths:
        data = path.read_bytes()
        total_bytes += len(data)
        if len(data) > MAX_DOCUMENT_BYTES:
            raise ValueError(f"Document exceeds {MAX_DOCUMENT_BYTES} bytes: {path.name}")
        if total_bytes > MAX_CORPUS_BYTES:
            raise ValueError(f"Corpus exceeds {MAX_CORPUS_BYTES} bytes")
        try:
            text = data.decode("utf-8")
        except UnicodeDecodeError as exc:
            raise ValueError(f"Document is not valid UTF-8: {path}") from exc
        relative = path.relative_to(display_root).as_posix() if display_root in path.parents else path.name
        modified = datetime.fromtimestamp(path.stat().st_mtime).isoformat(timespec="seconds")
        records.append(
            DocumentRecord(
                path=relative,
                title=_title(text, path),
                text=text,
                sha256=hashlib.sha256(data).hexdigest(),
                size_bytes=len(data),
                line_count=len(text.splitlines()),
                modified_time=modified,
                headings=_headings(text),
            )
        )
    return records


def load_corpus(source: str | Path) -> list[DocumentRecord]:
    """Load a bounded folder or ZIP without invoking a model."""

    source_path = Path(source).expanduser().resolve()
    if source_path.is_dir():
        return _read_directory(source_path, source_path)
    if source_path.suffix.lower() != ".zip":
        raise ValueError("Corpus input must be a folder or .zip file")
    try:
        archive = zipfile.ZipFile(source_path)
    except (zipfile.BadZipFile, OSError) as exc:
        raise ValueError(f"Malformed ZIP corpus: {source_path.name}") from exc
    with archive:
        members = [item for item in archive.infolist() if not item.is_dir()]
        if not members:
            raise ValueError("Corpus ZIP is empty")
        if len(members) > MAX_DOCUMENTS:
            raise ValueError(f"Corpus ZIP contains more than {MAX_DOCUMENTS} members")
        total_bytes = sum(item.file_size for item in members)
        if any(item.file_size < 0 for item in members):
            raise ValueError("Corpus ZIP contains an invalid member size")
        if total_bytes > MAX_CORPUS_BYTES:
            raise ValueError(f"Corpus ZIP expands beyond {MAX_CORPUS_BYTES} bytes")
        for item in members:
            if item.file_size > MAX_DOCUMENT_BYTES:
                raise ValueError(f"ZIP member exceeds {MAX_DOCUMENT_BYTES} bytes: {item.filename}")
            mode = (item.external_attr >> 16) & 0o170000
            if mode == 0o120000:
                raise ValueError(f"ZIP symlink member is not allowed: {item.filename}")
        names = [item.filename for item in members]
        with tempfile.TemporaryDirectory(prefix="mri-corpus-") as temp:
            root = Path(temp).resolve()
            _safe_members(root, names)
            archive.extractall(root)
            return _read_directory(root, root)

# MOON-SOURCE-PUBLIC-STAMP
# 🌙 Moon Source · Lua Helena Moon Martins Cardoso (Moon) + Áurion (AI-assisted) · Licensing: https://github.com/luahelenammc/Moon-Source/blob/main/LICENSING.md · Use & attribution: https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md · Full source: https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip · Questions, suggestions, or proposals? Feel free to contact me at LuaHelenaMMC@gmail.com.
