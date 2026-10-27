#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 Lua Helena Moon Martins Cardoso (Moon)
# SPDX-License-Identifier: Apache-2.0
"""Verify public Agent Skill archive structure, local links, provenance and bytes."""
import hashlib, io, json, posixpath, re, sys, zipfile
from pathlib import Path
from urllib.parse import unquote, urlsplit
sys.dont_write_bytecode = True
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from build_public_skills import bundle
records=json.loads((ROOT/'registry/public-capabilities.json').read_text())['capabilities']
for rec in records:
    slug=rec['id'] if rec['id'].startswith('moon-') else 'moon-'+rec['id']; p=ROOT/'downloads/skills'/f'{slug}.zip'
    data=p.read_bytes()
    assert data==bundle(rec), f'stale bundle: {slug}'
    with zipfile.ZipFile(io.BytesIO(data)) as z:
        assert z.testzip() is None
        names=set(z.namelist())
        assert f'{slug}/SKILL.md' in names
        assert f'{slug}/LICENSE-CC-BY-4.0.txt' in names
        front=z.read(f'{slug}/SKILL.md').decode()
        assert front.startswith(f'---\nname: {slug}\ndescription: ')
        assert f'references/source/{rec["canonical_path"]}' in front
        meta=json.loads(z.read(f'{slug}/references/PROVENANCE.json'))
        assert meta['canonical_path']==rec['canonical_path']
        for name,sha in meta['source_sha256'].items():
            assert hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==sha
            assert f'{slug}/references/source/{name}' in names
        for name in names:
            if not name.endswith('.md'): continue
            for target in re.findall(r'\]\(([^\s)]+)\)',z.read(name).decode()):
                u=urlsplit(target)
                if u.scheme or u.netloc or not u.path: continue
                resolved=posixpath.normpath(posixpath.join(posixpath.dirname(name),unquote(u.path)))
                assert resolved in names or any(n.startswith(resolved.rstrip('/')+'/') for n in names), (slug,name,target)
print(f'validated structure, integrity, source hashes and local links of {len(records)} skills')
