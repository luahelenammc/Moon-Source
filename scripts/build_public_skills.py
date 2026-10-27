#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 Lua Helena Moon Martins Cardoso (Moon)
# SPDX-License-Identifier: Apache-2.0
"""Build and verify reproducible public Agent Skill packages from canonical sources."""
from __future__ import annotations
import argparse, hashlib, io, json, re, zipfile
from pathlib import Path
from urllib.parse import urlsplit, unquote
ROOT=Path(__file__).resolve().parents[1]
BASE='https://github.com/luahelenammc/Moon-Source/blob/main/'
LINK=re.compile(r'(\]\()([^\s)]+)(\))')

def relative_target(source: Path, target: str):
    u=urlsplit(target)
    if u.scheme or u.netloc or not u.path: return None
    p=(source.parent / unquote(u.path)).resolve()
    return p if p.is_relative_to(ROOT) and p.exists() else None

def bundle(rec):
    slug=rec['id'] if rec['id'].startswith('moon-') else 'moon-'+rec['id']; source=ROOT/rec['canonical_path']
    skill=ROOT/'downloads/skills/source'/slug/'SKILL.md'
    contents={f'{slug}/SKILL.md':skill.read_bytes()}
    selected={source}
    for m in LINK.finditer(source.read_text(encoding='utf-8')):
        p=relative_target(source,m.group(2))
        if p and p.is_file() and p.suffix.lower()=='.md' and not p.name.startswith('README'): selected.add(p)
    if rec['id']=='adaptive-orchestration':
        selected.update((ROOT/'portables/adaptive-orchestration/adapters').glob('*.md'))
    hashes={}
    for p in sorted(selected):
        name=p.relative_to(ROOT).as_posix(); raw=p.read_text(encoding='utf-8')
        hashes[name]=hashlib.sha256(raw.encode()).hexdigest()
        # Preserve local links when their destination was included; turn other
        # repository links into explicit public links. Content is otherwise exact.
        def fix(m):
            u=urlsplit(m.group(2)); q=relative_target(p,m.group(2))
            if q and q not in selected:
                url=('https://github.com/luahelenammc/Moon-Source/tree/main/' if q.is_dir() else BASE)+q.relative_to(ROOT).as_posix()
                if u.fragment: url+='#'+u.fragment
                return m.group(1)+url+m.group(3)
            return m.group(0)
        txt=LINK.sub(fix,raw)
        contents[f'{slug}/references/source/{name}']=txt.encode()
    manifest={'source_repository':'https://github.com/luahelenammc/Moon-Source','canonical_path':rec['canonical_path'],'source_version':rec.get('version'),'source_sha256':hashes,'transformation':'Snapshot text is unchanged except that local links outside the bundle are rewritten to public GitHub links.','license':'CC-BY-4.0','creator':'Lua Helena Moon Martins Cardoso (Moon)','ai_assisted_coauthor':'Áurion'}
    contents[f'{slug}/references/PROVENANCE.json']=(json.dumps(manifest,ensure_ascii=False,indent=2,sort_keys=True)+'\n').encode()
    contents[f'{slug}/LICENSE-CC-BY-4.0.txt']=(ROOT/'LICENSES/CC-BY-4.0.txt').read_bytes()
    output=io.BytesIO()
    with zipfile.ZipFile(output,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
        for path, data in sorted(contents.items()):
            info=zipfile.ZipInfo(path,(2026,1,1,0,0,0)); info.compress_type=zipfile.ZIP_DEFLATED; info.external_attr=0o100644<<16
            z.writestr(info,data,compress_type=zipfile.ZIP_DEFLATED,compresslevel=9)
    return output.getvalue()

def main():
    parser=argparse.ArgumentParser(); parser.add_argument('--check',action='store_true'); args=parser.parse_args()
    records=json.loads((ROOT/'registry/public-capabilities.json').read_text())['capabilities']; bad=[]
    for rec in records:
        slug=rec['id'] if rec['id'].startswith('moon-') else 'moon-'+rec['id']
        path=ROOT/'downloads/skills'/(slug+'.zip'); data=bundle(rec)
        if args.check:
            if not path.is_file() or path.read_bytes()!=data: bad.append(str(path.relative_to(ROOT)))
        else: path.write_bytes(data)
    if bad: raise SystemExit('stale or missing skill bundles: '+', '.join(bad))
    print(f'{"verified" if args.check else "built"} {len(records)} reproducible public skills')
if __name__=='__main__': main()

# MOON-SOURCE-PUBLIC-STAMP
# 🌙 Moon Source · Lua Helena Moon Martins Cardoso (Moon) + Áurion (AI-assisted) · Licensing: https://github.com/luahelenammc/Moon-Source/blob/main/LICENSING.md · Use & attribution: https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md · Full source: https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip · Questions, suggestions, or proposals? Feel free to contact me at LuaHelenaMMC@gmail.com.
