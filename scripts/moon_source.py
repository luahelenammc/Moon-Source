#!/usr/bin/env python3
"""Provide one transparent entry point for Moon Source maintenance checks."""

from __future__ import annotations

import argparse
import os
import shlex
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PYTHON = sys.executable


def python_script(name: str, *arguments: str) -> list[str]:
    return [PYTHON, str(ROOT / "scripts" / name), *arguments]


def local_validation_steps() -> list[tuple[str, list[str]]]:
    """Return the same bounded local checks used by the public CI job."""

    return [
        ("licensing contract", python_script("check_licensing.py")),
        ("REUSE lint", ["reuse", "lint"]),
        ("CITATION.cff", ["cffconvert", "--validate", "--infile", "CITATION.cff"]),
        ("Markdown links", python_script("check_links.py")),
        ("public capability registry", python_script("validate_public_capabilities.py")),
        (
            "public capability registry tests",
            python_script("test_validate_public_capabilities.py"),
        ),
        ("AI Kernel package", python_script("check_kernel_package.py")),
        ("title/version separation", python_script("check_title_version_separation.py")),
        (
            "title/version separation tests",
            python_script("test_title_version_separation.py"),
        ),
        ("Markdown link tests", python_script("test_check_links.py")),
        ("public stamps", python_script("check_public_stamps.py")),
        ("public stamp tests", python_script("test_public_stamps.py")),
        ("capability digest", python_script("update_capability_digest.py", "--check")),
        ("maintenance CLI tests", python_script("test_moon_source_cli.py")),
    ]


def command_steps(command: str, args: argparse.Namespace) -> list[tuple[str, list[str]]]:
    if command == "validate":
        return local_validation_steps()
    if command == "registry":
        return [
            ("public capability registry", python_script("validate_public_capabilities.py")),
            (
                "public capability registry tests",
                python_script("test_validate_public_capabilities.py"),
            ),
        ]
    if command == "licensing":
        return [
            ("licensing contract", python_script("check_licensing.py")),
            ("REUSE lint", ["reuse", "lint"]),
            ("CITATION.cff", ["cffconvert", "--validate", "--infile", "CITATION.cff"]),
        ]
    if command == "links":
        return [
            ("Markdown links", python_script("check_links.py")),
            ("Markdown link tests", python_script("test_check_links.py")),
        ]
    if command == "stamps":
        steps: list[tuple[str, list[str]]] = []
        if args.apply:
            steps.append(("apply public stamps", python_script("apply_public_stamps.py")))
        steps.extend(
            [
                ("public stamps", python_script("check_public_stamps.py")),
                ("public stamp tests", python_script("test_public_stamps.py")),
            ]
        )
        return steps
    if command == "digest":
        arguments = [] if args.apply else ["--check"]
        return [("capability digest", python_script("update_capability_digest.py", *arguments))]
    if command == "mirror":
        command_line = python_script("check_mirror_sync.py")
        if args.mirror_root is not None:
            command_line.extend(["--mirror-root", str(args.mirror_root)])
        return [("canonical/mirror synchronization", command_line)]
    raise ValueError(f"unknown maintenance command: {command}")


def run_step(label: str, command: list[str]) -> int:
    rendered = " ".join(shlex.quote(part) for part in command)
    print(f"==> {label}: {rendered}")
    environment = os.environ.copy()
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    try:
        completed = subprocess.run(command, cwd=ROOT, env=environment, check=False)
    except FileNotFoundError:
        print(f"required command not found: {command[0]}", file=sys.stderr)
        return 127
    return completed.returncode


def execute(command: str, args: argparse.Namespace) -> int:
    for label, command_line in command_steps(command, args):
        exit_code = run_step(label, command_line)
        if exit_code:
            print(f"maintenance command stopped after {label} (exit {exit_code})", file=sys.stderr)
            return exit_code
    print(f"maintenance command completed: {command}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Run Moon Source repository maintenance checks without changing source semantics."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("validate", help="run the complete offline/local validation contract")
    subparsers.add_parser("registry", help="validate the public capability registry")
    subparsers.add_parser("licensing", help="run licensing, REUSE and citation checks")
    subparsers.add_parser("links", help="run Markdown link checks and regression tests")

    stamps = subparsers.add_parser("stamps", help="check public stamps; use --apply to normalize them")
    stamps.add_argument("--apply", action="store_true", help="explicitly apply stamp normalization")

    digest = subparsers.add_parser("digest", help="check the generated README capability digest")
    digest.add_argument("--apply", action="store_true", help="explicitly refresh the generated digest")

    mirror = subparsers.add_parser("mirror", help="check current canonical-to-website mirror bytes")
    mirror.add_argument("--check", action="store_true", help="explicitly request the read-only check")
    mirror.add_argument("--mirror-root", type=Path, help="local LUAHELENA checkout for offline comparison")

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return execute(args.command, args)


if __name__ == "__main__":
    raise SystemExit(main())

# MOON-SOURCE-PUBLIC-STAMP
# 🌙 Moon Source · Lua Helena Moon Martins Cardoso (Moon) + Áurion (AI-assisted) · Licensing: https://github.com/luahelenammc/Moon-Source/blob/main/LICENSING.md · Use & attribution: https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md · Full source: https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip · Questions, suggestions, or proposals? Feel free to contact me at LuaHelenaMMC@gmail.com.
