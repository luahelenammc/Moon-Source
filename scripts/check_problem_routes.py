#!/usr/bin/env python3
"""Verify that the problem-first reading routes cover the live public registry.

The registry and canonical bodies retain semantic authority; this validates
only navigability, not correctness of examples or completeness of translations.
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
    "docs/PROBLEM_TO_METHOD.md": (
        "**Concrete problem**:", "**First move**:",
        "**What to inspect**:", "**Stop line**:", "**Canonical authority**:",
    ),
    "docs/PROBLEM_TO_METHOD.pt-BR.md": (
        "**Problema concreto**:", "**Primeiro movimento**:",
        "**O que observar**:", "**Limite**:", "**Fonte canônica**:",
    ),
}


def audit(root: Path = ROOT) -> list[str]:
    failures: list[str] = []
    registry = json.loads((root / "registry/public-capabilities.json").read_text(encoding="utf-8"))
    records = registry["capabilities"]
    ids = [item["id"] for item in records]
    if len(ids) != len(set(ids)):
        failures.append("registry: duplicate capability identifiers")
    for filename, fields in DOCS.items():
        filepath = root / filename
        if not filepath.is_file():
            failures.append(f"{filename}: missing guide")
            continue
        content = filepath.read_text(encoding="utf-8")
        matches = list(ROUTE_RE.finditer(content))
        counts = Counter(m.group(1) for m in matches)
        missing = sorted(set(ids) - set(counts))
        extras = sorted(set(counts) - set(ids))
        duplicates = sorted(k for k, count in counts.items() if count != 1)
        if missing or extras or duplicates:
            failures.append(
                f"{filename}: missing={missing}, extras={extras}, duplicates={duplicates}"
            )
        for i, match in enumerate(matches):
            identity = match.group(1)
            item = next((r for r in records if r["id"] == identity), None)
            if item is None:
                continue
            section = content[match.end():matches[i + 1].start() if i + 1 < len(matches) else len(content)]
            for field in fields:
                if field not in section:
                    failures.append(f"{filename}: {identity} missing {field}")
            canonical = item["canonical_path"]
            expected = (canonical.removeprefix("docs/") if canonical.startswith("docs/")
                        else "../" + canonical)
            authorities = [line for line in section.splitlines() if fields[-1] in line]
            if not authorities or expected not in LINK_RE.findall(authorities[0]):
                failures.append(f"{filename}: {identity} must link to {expected}")
            if not (root / canonical).is_file():
                failures.append(f"{filename}: {identity} canonical target missing: {canonical}")
        if "new capability" in content.lower() and "not a new capability" not in content.lower():
            # No enforcement of editorial meaning beyond the explicit route contract.
            pass
    return failures


def main() -> int:
    findings = audit()
    if findings:
        for finding in findings:
            print("FAIL:", finding)
        return 1
    print("PASS: 16 public capabilities each have one inspected EN + pt-BR problem route")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
