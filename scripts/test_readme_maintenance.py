#!/usr/bin/env python3
"""Regression tests for README/changelog separation."""

from __future__ import annotations

import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from check_readme_maintenance import readme_maintenance_violations


def main() -> None:
    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        readme = root / "README.md"
        readme.write_text(
            "# Example\n\n## Current identity\n\n## First use\n\n"
            + chr(96) * 3
            + "md\n## Recent changes\n"
            + chr(96) * 3
            + "\n",
            encoding="utf-8",
        )
        assert readme_maintenance_violations(root) == []

        cases = {
            "aop/README.md": "What changed in 6.1",
            "pt/README.md": "Mudanças recentes de capacidades",
            "es/README.md": "Cambios recientes en capacidades",
            "ru/README.md": "Недавние изменения возможностей",
            "zh/README.md": "近期能力变化",
        }
        for relative, heading in cases.items():
            path = root / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(f"# Example\n\n## {heading}\n", encoding="utf-8")
        failures = readme_maintenance_violations(root)
        assert len(failures) == len(cases), failures
        assert any("aop/README.md:3" in failure for failure in failures)

        readme.write_text(
            "# Example\n\n<!-- MOON-SOURCE-CAPABILITY-DIGEST:START -->\n",
            encoding="utf-8",
        )
        failures = readme_maintenance_violations(root)
        assert any("generated capability-history digests" in failure for failure in failures)

    print("README maintenance regression tests passed")


if __name__ == "__main__":
    main()

# MOON-SOURCE-PUBLIC-STAMP
# 🌙 Moon Source · Lua Helena Moon Martins Cardoso (Moon) + Áurion (AI-assisted) · Licensing: https://github.com/luahelenammc/Moon-Source/blob/main/LICENSING.md · Use & attribution: https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md · Full source: https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip · Questions, suggestions, or proposals? Feel free to contact me at LuaHelenaMMC@gmail.com.
