#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 Lua Helena Moon Martins Cardoso (Moon)
# SPDX-License-Identifier: Apache-2.0
"""Read-only integrity checks for external Adaptive Orchestration projections."""
from __future__ import annotations
import argparse, hashlib, json, subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
MANIFEST=ROOT/"downloads/external-projections/aop-compatibility.json"
def sha(data: bytes) -> str: return hashlib.sha256(data).hexdigest()
def require(ok: bool, message: str) -> None:
    if not ok: raise SystemExit("AOP compatibility check failed: "+message)
def main() -> None:
    parser=argparse.ArgumentParser(); parser.add_argument("--source-root",type=Path); parser.add_argument("--site-root",type=Path); args=parser.parse_args()
    manifest=json.loads(MANIFEST.read_text(encoding="utf-8"))
    require(manifest["canonical_repository"]=="https://github.com/luahelenammc/Adaptive-Orchestration-Protocol","canonical repository mismatch")
    for rel in manifest["compatibility_composite_paths"]:
        path=ROOT/rel; require(path.is_file(),f"missing compatibility package {rel}"); require(sha(path.read_bytes())==manifest["composite_zip_sha256"],f"stale composite package {rel}")
    skill=ROOT/manifest["compatibility_skill_path"]; require(skill.is_file(),"missing compatibility Agent Skill ZIP"); require(sha(skill.read_bytes())==manifest["skill_zip_sha256"],"stale compatibility Agent Skill ZIP")
    for rel,target in manifest["pointer_paths"].items():
        path=ROOT/rel; require(path.is_file(),f"missing legacy pointer {rel}"); require(target in path.read_text(encoding="utf-8"),f"pointer target mismatch: {rel}")
    skill_pointer=ROOT/manifest["skill_source_pointer"]; require(skill_pointer.is_file(),"missing legacy skill source pointer"); require(manifest["canonical_repository"] in skill_pointer.read_text(encoding="utf-8"),"skill source pointer is not canonical")
    core=None
    if args.source_root:
        source=args.source_root.resolve(); head=subprocess.run(["git","rev-parse","HEAD"],cwd=source,capture_output=True,text=True,check=True).stdout.strip(); require(head==manifest["canonical_commit"],f"canonical source moved from pinned commit: {head}")
        core=(source/manifest["core_path"]).read_bytes(); require(sha(core)==manifest["core_sha256"],"canonical core fingerprint differs")
        composite=(source/manifest["composite_zip_path"]).read_bytes(); require(sha(composite)==manifest["composite_zip_sha256"],"canonical composite ZIP differs")
        canonical_skill=(source/manifest["skill_zip_path"]).read_bytes(); require(sha(canonical_skill)==manifest["skill_zip_sha256"],"canonical skill ZIP differs")
    if args.site_root:
        site=args.site_root.resolve()
        for rel in manifest["site_core_mirrors"]:
            path=site/rel; require(path.is_file(),f"missing website compatibility mirror {rel}"); content=path.read_bytes(); require(sha(content)==manifest["core_sha256"],f"website mirror differs from canonical AOP core: {rel}")
            if core is not None: require(content==core,f"website mirror bytes differ: {rel}")
        index=(site/manifest["site_index_path"]).read_text(encoding="utf-8"); require(manifest["canonical_repository"] in index,"site card does not link to the independent AOP repository"); require("Moon-Source/blob/main/portables/adaptive-orchestration/" not in index,"site card still links to the old Moon Source AOP body")
    print("AOP compatibility projections match the pinned canonical source and declared routes")
if __name__=="__main__": main()

# MOON-SOURCE-PUBLIC-STAMP
# 🌙 Moon Source · Lua Helena Moon Martins Cardoso (Moon) + Áurion (AI-assisted) · Licensing: https://github.com/luahelenammc/Moon-Source/blob/main/LICENSING.md · Use & attribution: https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md · Full source: https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip · Questions, suggestions, or proposals? Feel free to contact me at LuaHelenaMMC@gmail.com.
