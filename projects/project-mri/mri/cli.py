from __future__ import annotations

import argparse
import json
from pathlib import Path

from .pipeline import scan
from .golden_eval import run_golden_eval
from .nutrient import NutrientAdapter
from . import __version__


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="mri", description="Project MRI governed context scan")
    parser.add_argument("--version", action="version", version=f"project-mri {__version__}")
    subparsers = parser.add_subparsers(dest="command", required=True)
    scan_parser = subparsers.add_parser("scan", help="scan a folder or ZIP")
    scan_parser.add_argument("source", type=Path)
    scan_parser.add_argument("--output", type=Path, default=Path("out"))
    scan_parser.add_argument("--json", action="store_true", help="print the complete JSON result")
    demo_parser = subparsers.add_parser("demo", help="run the checked-in synthetic demo corpus")
    demo_parser.add_argument("--output", type=Path, default=Path("out/demo"))
    eval_parser = subparsers.add_parser("eval", help="run the Northstar golden fixture eval")
    eval_parser.add_argument("fixture", type=Path, default=Path("fixtures/northstar"), nargs="?")
    eval_parser.add_argument("--output", type=Path, default=Path("evals/northstar"))
    subparsers.add_parser("nutrient-status", help="show optional Nutrient DWS adapter state")
    args = parser.parse_args(argv)
    if args.command in {"scan", "demo"}:
        source = Path("fixtures/demo_corpus") if args.command == "demo" else args.source
        result = scan(source, args.output)
        summary = {
            "documents": len(result.documents),
            "objects": len(result.objects),
            "findings": len(result.findings),
            "finding_types": sorted({finding.finding_type for finding in result.findings}),
            "before_after_changed": result.before_after["changed"],
            "output": str(args.output),
            "track": result.engine.get("competition_track"),
        }
        print(json.dumps(result.to_dict() if getattr(args, "json", False) else summary, indent=2, ensure_ascii=False))
    elif args.command == "eval":
        print(json.dumps(run_golden_eval(args.fixture, args.output), indent=2, ensure_ascii=False))
    elif args.command == "nutrient-status":
        print(json.dumps(NutrientAdapter().status(), indent=2, ensure_ascii=False))
    return 0

# MOON-SOURCE-PUBLIC-STAMP
# 🌙 Moon Source · Lua Helena Moon Martins Cardoso (Moon) + Áurion (AI-assisted) · Licensing: https://github.com/luahelenammc/Moon-Source/blob/main/LICENSING.md · Use & attribution: https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md · Full source: https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip · Questions, suggestions, or proposals? Feel free to contact me at LuaHelenaMMC@gmail.com.
