#!/usr/bin/env python3
"""Validate the complete, synchronized README translation set."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
LANGUAGES = {
    "pt-BR": {"path": "translations/README.pt-BR.md", "flag": "🇧🇷", "authority": "tradução completa do README canônico em inglês"},
    "es": {"path": "translations/README.es.md", "flag": "🇪🇸", "authority": "traducción completa del README canónico en inglés"},
    "zh-CN": {"path": "translations/README.zh-CN.md", "flag": "🇨🇳", "authority": "英文规范 README 的完整译文"},
    "ru": {"path": "translations/README.ru.md", "flag": "🇷🇺", "authority": "полный перевод канонического README на английском языке"},
}
ENGLISH = "🇬🇧"
SOURCE_PATH = "../README.md"
CONTRACT_PATH = "../docs/README_TRANSLATIONS.md"
NAV_START = "<!-- MOON-SOURCE-LANGUAGE-NAV:START -->"
NAV_END = "<!-- MOON-SOURCE-LANGUAGE-NAV:END -->"
PUBLIC_STAMP = "<!-- MOON-SOURCE-PUBLIC-STAMP -->"
LINK_RE = re.compile(r"\[([^\]\n]+)\]\(([^)\n]+)\)")
METADATA_RE = re.compile(
    r"<!--\s*MOON-SOURCE-README-TRANSLATION\s*\n"
    r"locale:\s*(?P<locale>[^\n]+)\n"
    r"source:\s*(?P<source>[^\n]+)\n"
    r"source_sha256:\s*(?P<sha>[0-9a-f]{64})\n"
    r"contract:\s*(?P<contract>[^\n]+)\n-->"
)
MARKER_RE = re.compile(r"<!--\s*(MOON-SOURCE-[A-Z0-9_-]+(?::(?:START|END))?)\s*-->")
INLINE_CODE_RE = re.compile(r"(?<!\x60)(\x60[^\x60\n]+\x60)(?!\x60)")
VERSION_RE = re.compile(r"\b\d+\.\d+\b")
FENCE_RE = re.compile(r"^((?:\x60){3,}|~{3,})(.*)$")


def language_nav(text: str) -> tuple[str | None, int]:
    matches = list(re.finditer(
        re.escape(NAV_START) + r"\s*(.*?)\s*" + re.escape(NAV_END),
        text, re.DOTALL
    ))
    if len(matches) != 1:
        return None, -1
    return matches[0].group(1), matches[0].start()


def expected_nav_targets(locale: str | None) -> list[str]:
    if locale is None:
        return [info["path"] for info in LANGUAGES.values()]
    return ["../README.md", *(Path(info["path"]).name for info in LANGUAGES.values())]


def check_nav(text: str, label: str, locale: str | None, failures: list[str]) -> None:
    block, offset = language_nav(text)
    if block is None:
        failures.append(f"{label}: language-navigation block is missing or repeated")
        return
    if offset > 1400:
        failures.append(f"{label}: language navigation is too far from the top")
    expected = Counter(expected_nav_targets(locale))
    actual = Counter(target.strip() for _, target in LINK_RE.findall(block))
    if actual != expected:
        failures.append(f"{label}: language-navigation routes do not match the required stable paths")
    flags = {info["flag"] for info in LANGUAGES.values()}
    if locale is not None:
        flags.add(ENGLISH)
    if any(flag not in block for flag in flags):
        failures.append(f"{label}: language navigation is missing a required flag")


def translated_target(target: str) -> str:
    target = target.strip()
    parsed = urlsplit(target)
    if parsed.scheme or parsed.netloc or not parsed.path or parsed.path.startswith("../"):
        return target
    return "../" + target


def markdown_targets(text: str) -> Counter[str]:
    if language_nav(text)[0] is not None:
        text = re.sub(
            re.escape(NAV_START) + r"\s*.*?\s*" + re.escape(NAV_END),
            "", text, count=1, flags=re.DOTALL
        )
    return Counter(target.strip() for _, target in LINK_RE.findall(text))


def line_block_signature(text: str, prefix: str) -> tuple[int, ...]:
    groups: list[int] = []
    count = 0
    inside = False
    for line in text.splitlines():
        if line.startswith(prefix):
            count += 1
            inside = True
        elif inside:
            groups.append(count)
            count = 0
            inside = False
    if inside:
        groups.append(count)
    return tuple(groups)


def heading_signature(text: str) -> tuple[int, ...]:
    return tuple(
        len(match.group(1))
        for line in text.splitlines()
        if (match := re.match(r"^(#{1,6})\s+", line))
    )


def fenced_blocks(text: str) -> list[tuple[str, str, str]]:
    blocks: list[tuple[str, str, str]] = []
    marker: str | None = None
    info = ""
    body: list[str] = []
    for line in text.splitlines():
        match = FENCE_RE.match(line)
        if marker is None:
            if match:
                marker = match.group(1)
                info = match.group(2).strip()
                body = []
            continue
        closing = re.match(r"^((?:\x60)+|~+)\s*$", line)
        if closing and closing.group(1)[0] == marker[0] and len(closing.group(1)) >= len(marker):
            blocks.append((marker, info, "\n".join(body)))
            marker = None
            info = ""
            body = []
        else:
            body.append(line)
    if marker is not None:
        blocks.append((marker, info, "\n".join(body)))
    return blocks


def mermaid_shape(body: str) -> tuple[tuple[str, ...], tuple[tuple[str, str, str], ...]]:
    nodes = tuple(
        match.group(1)
        for line in body.splitlines()
        if (match := re.match(r"^\s*([A-Za-z_]\w*)\s*\[", line))
    )
    edges = tuple(
        (match.group(1), match.group(2), match.group(3))
        for line in body.splitlines()
        if (match := re.match(r"^\s*([A-Za-z_]\w*)\s+(<-->|---)\s+([A-Za-z_]\w*)\s*$", line))
    )
    return nodes, edges


def check_structure(source: str, translated: str, label: str, failures: list[str]) -> None:
    if heading_signature(source) != heading_signature(translated):
        failures.append(f"{label}: heading hierarchy or section coverage differs from README.md")
    for prefix, description in (("|", "table rows"), ("- ", "list items"), (">", "block quotes")):
        if line_block_signature(source, prefix) != line_block_signature(translated, prefix):
            failures.append(f"{label}: {description} structure differs from README.md")

    source_blocks = fenced_blocks(source)
    translated_blocks = fenced_blocks(translated)
    signatures = [(marker, info) for marker, info, _ in source_blocks]
    translated_signatures = [(marker, info) for marker, info, _ in translated_blocks]
    if signatures != translated_signatures:
        failures.append(f"{label}: fenced-code structure differs from README.md")
        return
    for (_, info, source_body), (_, _, translated_body) in zip(source_blocks, translated_blocks):
        if info == "bash" and source_body != translated_body:
            failures.append(f"{label}: a protected shell command block was changed")
        elif info == "mermaid" and mermaid_shape(source_body) != mermaid_shape(translated_body):
            failures.append(f"{label}: the Mermaid diagram topology was changed")
        elif info not in {"text", "mermaid"} and source_body != translated_body:
            failures.append(f"{label}: a protected code block was changed")

    required_markers = set(MARKER_RE.findall(source))
    present_markers = set(MARKER_RE.findall(translated))
    if not required_markers.issubset(present_markers):
        failures.append(f"{label}: a required Moon Source automation marker is missing")

    for literal in INLINE_CODE_RE.findall(source):
        if literal not in translated:
            failures.append(f"{label}: protected inline literal is missing: {literal}")
    if Counter(VERSION_RE.findall(source)) != Counter(VERSION_RE.findall(translated)):
        failures.append(f"{label}: version or decimal literals differ from README.md")

    for name in ("Moon Source", "Moon Source Language", "Adaptive Orchestration Protocol", "Connected Sources", "Moon Cortex", "Áurion"):
        if name in source and name not in translated:
            failures.append(f"{label}: protected proper name is missing: {name}")

    expected = Counter(
        translated_target(target)
        for target, count in markdown_targets(source).items()
        for _ in range(count)
    )
    actual = markdown_targets(translated)
    if expected != actual:
        missing = list((expected - actual).elements())
        extra = list((actual - expected).elements())
        failures.append(
            f"{label}: Markdown targets differ after rebasing; missing={missing[:3]} extra={extra[:3]}"
        )


def cochange_failures(changed_paths: set[str] | None) -> list[str]:
    if changed_paths is None or "README.md" not in changed_paths:
        return []
    missing = sorted(info["path"] for info in LANGUAGES.values() if info["path"] not in changed_paths)
    if not missing:
        return []
    return ["README.md changed in this pull request without co-changing every translation: " + ", ".join(missing)]


def pull_request_changed_paths(root: Path) -> set[str] | None:
    if os.environ.get("GITHUB_EVENT_NAME") != "pull_request":
        return None
    event_path = os.environ.get("GITHUB_EVENT_PATH")
    if not event_path:
        raise RuntimeError("GITHUB_EVENT_PATH is missing in a pull-request validation")
    event = json.loads(Path(event_path).read_text(encoding="utf-8"))
    base_sha = event.get("pull_request", {}).get("base", {}).get("sha")
    if not base_sha:
        raise RuntimeError("pull-request base SHA is missing from the GitHub event")
    result = subprocess.run(
        ["git", "diff", "--name-only", f"{base_sha}...HEAD"],
        cwd=root, capture_output=True, text=True, check=False
    )
    if result.returncode:
        detail = result.stderr.strip() or "git diff failed"
        raise RuntimeError(f"could not inspect pull-request changes: {detail}")
    return {line.strip() for line in result.stdout.splitlines() if line.strip()}


def validate(root: Path = ROOT, changed_paths: set[str] | None = None) -> list[str]:
    failures: list[str] = []
    source_path = root / "README.md"
    if not source_path.is_file():
        return ["README.md is missing"]
    source_bytes = source_path.read_bytes()
    source = source_bytes.decode("utf-8")
    source_sha = hashlib.sha256(source_bytes).hexdigest()
    check_nav(source, "README.md", None, failures)
    if PUBLIC_STAMP not in source:
        failures.append("README.md: canonical public-stamp marker is missing")

    for locale, info in LANGUAGES.items():
        path = root / info["path"]
        label = info["path"]
        if not path.is_file():
            failures.append(f"{label}: required translation is missing")
            continue
        translated = path.read_text(encoding="utf-8")
        metadata = METADATA_RE.search(translated)
        if not metadata:
            failures.append(f"{label}: translation metadata block is missing or malformed")
        else:
            if metadata.group("locale").strip() != locale:
                failures.append(f"{label}: metadata locale is not {locale}")
            if metadata.group("source").strip() != SOURCE_PATH:
                failures.append(f"{label}: metadata source must be {SOURCE_PATH}")
            if metadata.group("sha").strip() != source_sha:
                failures.append(f"{label}: source_sha256 is stale")
            if metadata.group("contract").strip() != CONTRACT_PATH:
                failures.append(f"{label}: metadata contract must be {CONTRACT_PATH}")
        contract = (root / "translations" / CONTRACT_PATH).resolve()
        if not contract.is_file():
            failures.append(f"{label}: translation contract target is missing")
        if PUBLIC_STAMP not in translated:
            failures.append(f"{label}: canonical public-stamp marker is missing")
        if info["authority"] not in translated:
            failures.append(f"{label}: derived-translation authority statement is missing")
        check_nav(translated, label, locale, failures)
        check_structure(source, translated, label, failures)

    failures.extend(cochange_failures(changed_paths))
    return failures


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT, help="repository root for validation")
    args = parser.parse_args(argv)
    root = args.root.resolve()
    try:
        changed_paths = pull_request_changed_paths(root)
    except (OSError, ValueError, RuntimeError) as error:
        print(f"README translation validation failed: {error}", file=sys.stderr)
        return 1
    failures = validate(root, changed_paths)
    if failures:
        print("\n".join(failures), file=sys.stderr)
        return 1
    print("README translation mirrors are complete, current and structurally synchronized")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

# MOON-SOURCE-PUBLIC-STAMP
# 🌙 Moon Source · Lua Helena Moon Martins Cardoso (Moon) + Áurion (AI-assisted) · Licensing: https://github.com/luahelenammc/Moon-Source/blob/main/LICENSING.md · Use & attribution: https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md · Full source: https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip · Questions, suggestions, or proposals? Feel free to contact me at LuaHelenaMMC@gmail.com.
