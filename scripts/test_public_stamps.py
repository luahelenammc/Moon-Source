#!/usr/bin/env python3
"""Regression checks for public-stamp insertion, idempotency and validation."""

from __future__ import annotations

import json
import tempfile
from pathlib import Path

import apply_public_stamps as applicator
import check_public_stamps as checker


def check_valid(path: Path, root: Path) -> None:
    previous_root = checker.ROOT
    previous_tracked = checker.tracked_files
    checker.ROOT = root
    checker.tracked_files = lambda: [path]
    try:
        checker.main()
    finally:
        checker.ROOT = previous_root
        checker.tracked_files = previous_tracked


def check_invalid(path: Path, root: Path) -> None:
    previous_root = checker.ROOT
    previous_tracked = checker.tracked_files
    checker.ROOT = root
    checker.tracked_files = lambda: [path]
    try:
        try:
            checker.main()
        except SystemExit as error:
            assert "public stamp" in str(error)
        else:
            raise AssertionError("invalid stamp was accepted")
    finally:
        checker.ROOT = previous_root
        checker.tracked_files = previous_tracked


def main() -> None:
    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)

        js_path = root / "device.js"
        js_path.write_text("window.device = true;\n", encoding="utf-8")
        assert applicator.normalize_text_stamp(js_path, applicator.JS_STAMP, applicator.JS_MARKER)
        js_once = js_path.read_text(encoding="utf-8")
        assert not applicator.normalize_text_stamp(js_path, applicator.JS_STAMP, applicator.JS_MARKER)
        assert js_path.read_text(encoding="utf-8") == js_once
        check_valid(js_path, root)
        js_path.write_text(js_once.replace("Full source:", "Corrupted source:"), encoding="utf-8")
        check_invalid(js_path, root)

        html_path = root / "demo.html"
        html_path.write_text("<!doctype html>\n<html></html>\n", encoding="utf-8")
        assert applicator.normalize_text_stamp(html_path, applicator.HTML_STAMP, applicator.HTML_MARKER)
        html_once = html_path.read_text(encoding="utf-8")
        assert not applicator.normalize_text_stamp(html_path, applicator.HTML_STAMP, applicator.HTML_MARKER)
        assert html_path.read_text(encoding="utf-8") == html_once
        check_valid(html_path, root)

        json_path = root / "receipt.json"
        json_path.write_text(json.dumps({"items": []}), encoding="utf-8")
        assert applicator.stamp_json(json_path)
        assert not applicator.stamp_json(json_path)
        check_valid(json_path, root)

    print("public stamp regression fixtures passed")


if __name__ == "__main__":
    main()

# MOON-SOURCE-PUBLIC-STAMP
# 🌙 Moon Source · Lua Helena Moon Martins Cardoso (Moon) + Áurion (AI-assisted) · Licensing: https://github.com/luahelenammc/Moon-Source/blob/main/LICENSING.md · Use & attribution: https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md · Full source: https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip
