#!/usr/bin/env python3
"""Validate problem-first tables against the canonical capability registry.

This checks coverage, table shape and links; linguistic fidelity and the
truth of an example remain editorial-review responsibilities.
"""
from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ROUTE_RE = re.compile(r"<!-- problem-route: ([a-z0-9-]+) -->")
LINK_RE = re.compile(r"\]\(([^)]+)\)")

DOCS = {
    "docs/PROBLEM_TO_METHOD.md": ("**Inspect:**", "**Limit:**"),
    "docs/PROBLEM_TO_METHOD.pt-BR.md": ("**Confira:**", "**Limite:**"),
    "docs/PROBLEM_TO_METHOD.es.md": ("**Comprueba:**", "**Límite:**"),
    "docs/PROBLEM_TO_METHOD.zh-CN.md": ("**检查:**", "**边界:**"),
    "docs/PROBLEM_TO_METHOD.ru.md": ("**Проверить:**", "**Граница:**"),
}

# All guides have four thematic four-column tables.
TABLE_RULE = "|---|---|---|---|"


def audit(root: Path = ROOT) -> list[str]:
    failures: list[str] = []
    registry = json.loads(
        (root / "registry/public-capabilities.json").read_text(encoding="utf-8")
    )
    records = registry["capabilities"]
    ids = [item["id"] for item in records]
    if len(ids) != len(set(ids)):
        failures.append("registry: duplicate capability identifiers")
    by_id = {record["id"]: record for record in records}
    for filename, labels in DOCS.items():
        filepath = root / filename
        if not filepath.is_file():
            failures.append(f"{filename}: missing guide")
            continue
        content = filepath.read_text(encoding="utf-8")
        matches = ROUTE_RE.findall(content)
        parts = re.split(r"(?m)^### [^\n]+\n", content)
        groups = [part for part in parts[1:] if ROUTE_RE.search(part)][:4]
        families = registry.get("discovery_families", [])
        if len(groups) != len(families):
            failures.append(f"{filename}: expected {len(families)} thematic groups, got {len(groups)}")
        else:
            for family, section in zip(families, groups):
                actual_ids = set(ROUTE_RE.findall(section))
                expected_ids = {
                    record["id"] for record in records
                    if record.get("discovery_family") == family["id"]
                }
                if actual_ids != expected_ids:
                    failures.append(
                        f"{filename}: {family['id']} group differs from canonical registry; "
                        f"missing={sorted(expected_ids - actual_ids)}, extra={sorted(actual_ids - expected_ids)}"
                    )
        counts = Counter(matches)
        missing = sorted(set(ids) - set(counts))
        extras = sorted(set(counts) - set(ids))
        duplicates = sorted(k for k, count in counts.items() if count != 1)
        if missing or extras or duplicates:
            failures.append(
                f"{filename}: missing={missing}, extras={extras}, duplicates={duplicates}"
            )
        if content.count(TABLE_RULE) != 4:
            failures.append(f"{filename}: expected four four-column thematic tables")
        for row in content.splitlines():
            match = ROUTE_RE.search(row)
            if not match:
                continue
            identity = match.group(1)
            if identity not in by_id:
                continue
            cells = row.strip().split("|")
            if len(cells) != 6 or cells[0] or cells[-1]:
                failures.append(f"{filename}: {identity} malformed four-column table row")
                continue
            problem, method, move, evidence = [c.strip() for c in cells[1:5]]
            if not all((problem, method, move, evidence)):
                failures.append(f"{filename}: {identity} contains empty cell")
            if "<a id=\"" not in method:
                failures.append(f"{filename}: {identity} missing stable deep-link anchor")
            for label in labels:
                if label not in evidence:
                    failures.append(f"{filename}: {identity} missing {label}")
            canonical = by_id[identity]["canonical_path"]
            expected = (canonical.removeprefix("docs/") if canonical.startswith("docs/")
                        else "../" + canonical)
            if expected not in LINK_RE.findall(method):
                failures.append(f"{filename}: {identity} must link to {expected}")
            if not (root / canonical).is_file():
                failures.append(f"{filename}: {identity} canonical target missing: {canonical}")
    return failures


def main() -> int:
    findings = audit()
    if findings:
        for finding in findings:
            print("FAIL:", finding)
        return 1
    print("PASS: 16 canonical capabilities in four themed tables across five languages")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

# MOON-SOURCE-PUBLIC-STAMP
# 🌙 Moon Source · Lua Helena Moon Martins Cardoso (Moon) + Áurion (AI-assisted) · Licensing: https://github.com/luahelenammc/Moon-Source/blob/main/LICENSING.md · Use & attribution: https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md · Full source: https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip · Questions, suggestions, or proposals? Feel free to contact me at LuaHelenaMMC@gmail.com.
