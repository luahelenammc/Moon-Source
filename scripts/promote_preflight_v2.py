#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

ROOT = Path(__file__).resolve().parents[1]
STAMP = """<!-- MOON-SOURCE-PUBLIC-STAMP -->

---

> 🌙 **Moon Source** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Source/blob/main/LICENSING.md) · [Use & attribution](https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md) · [Full source (.zip)](https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip)
"""

OLD_CANON = "docs/PREFLIGHT.md"
NEW_CANON = "portables/preflight/PREFLIGHT_V2.md"
DOWNLOAD = "downloads/preflight-v2.zip"
MIRROR_PATH = "moonsource/downloads/PREFLIGHT_V2.md"
MIRROR_URL = "https://www.luahelena.com.br/moonsource/downloads/PREFLIGHT_V2.md"


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, content: str) -> None:
    p = ROOT / path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8", newline="\n")


def must_replace(text: str, old: str, new: str, label: str, count: int | None = None) -> str:
    found = text.count(old)
    if found == 0:
        raise SystemExit(f"migration failed: missing replacement target for {label}")
    if count is not None and found != count:
        raise SystemExit(f"migration failed: {label} expected {count}, found {found}")
    return text.replace(old, new)


source = read(OLD_CANON)
portable = source
portable = must_replace(
    portable,
    "**Status:** current public Moon Source component  \n**Public since:** 2026-08-23  \n**V2 rebase:** 2026-09-07  \n**Canonical path:** `docs/PREFLIGHT.md`",
    "**Status:** current public portable  \n**Public since:** 2026-08-23  \n**V2 rebase:** 2026-09-07  \n**Portable promotion:** 2026-09-07  \n**Canonical path:** `portables/preflight/PREFLIGHT_V2.md`  \n**Language:** English; execution should follow the user's language  \n**Audience:** general AI users, power users, writers, teams and builders  \n**Creator and final human authority:** Lua Helena Moon Martins Cardoso (Moon)  \n**AI-assisted coauthorial development:** Moon + Áurion  \n**License:** CC-BY-4.0 — https://creativecommons.org/licenses/by/4.0/  \n**Moon Source public surface:** https://www.luahelena.com.br/moonsource/?lang=en",
    "portable metadata",
    1,
)
portable = must_replace(
    portable,
    "Preflight is a public Moon Source component, not a new portable family. It is directly usable as a method and is specialized by [Moon Source Setup 3.0](../portables/setup/MOON_SOURCE_SETUP.md) for personal and project-context setup.",
    "Preflight V2 is a standalone public Moon Source portable. Its reconstruction core is independently usable without the rest of the repository. When the full Moon Source body is available, it may route to specialized components for consequence-sensitive governance. [Moon Source Setup 3.0](../setup/MOON_SOURCE_SETUP.md) specializes the same reconstruction principle for personal and project-context setup.",
    "portable identity paragraph",
    1,
)

start_here = """
## 1. Start here

Paste this portable into an AI conversation and say:

```text
Execute Preflight V2 on my requests.
```

The AI should not summarize the portable back to the user unless asked. It should use the method as an operating layer.

For one request only:

```text
Apply Preflight V2 to the request below, then execute.

Request:
[...]
```

### Operating modes

- **Preflight** — reconstruct the intended task, then execute it.
- **Silent Preflight** — reconstruct internally and return only the result unless an assumption must be surfaced.
- **Preflight only** — reconstruct the intended task but do not execute it.
- **Show reconstructed task** — show the compact working task, then execute unless the user says not to.
- **Deep Preflight** — use deeper reconstruction for long, tangled, contradictory or multi-stage human expression; still avoid unnecessary questions.

If no mode is named, use ordinary **Preflight**. For clear low-ambiguity requests, behave like **Silent Preflight** by default.

## 2. Why Preflight exists
"""
portable = must_replace(portable, "## 1. Why Preflight exists\n", start_here, "start-here insertion", 1)
for n in range(19, 1, -1):
    portable = portable.replace(f"## {n}. ", f"## {n+1}. ")

replacements = {
    "../portables/setup/MOON_SOURCE_SETUP.md": "../setup/MOON_SOURCE_SETUP.md",
    "../portables/chat-work/CHAT_WORK_ROUTING_PROTOCOL_V4.md": "../chat-work/CHAT_WORK_ROUTING_PROTOCOL_V4.md",
    "../portables/msl/MSL_4_3.md": "../msl/MSL_4_3.md",
}
for old, new in replacements.items():
    portable = portable.replace(old, new)
for name in [
    "CONNECTED_SOURCES.md", "SOURCE_OPERATIONS.md", "RESPONSIBILITY_MAP.md",
    "SOURCE_HYGIENE.md", "CREDITS_ATTRIBUTION_OPS.md", "OPERATIONAL_RELIABILITY.md",
    "SIGNAL_CALIBRATION.md", "FIELD_TO_FORM.md",
]:
    portable = portable.replace(f"]({name})", f"](../../docs/{name})")

portable = must_replace(
    portable,
    "The superseded V1 body remains recoverable through Git history. The canonical path now carries V2.\n\nThis is a component-version rebase. It does not create a new portable family, change MSL 4.3 or require a Setup 3.0 version bump.",
    "The superseded V1 body remains recoverable through Git history. On 2026-09-07, V2 was promoted from a repository component into a standalone public portable. Its current canonical identity is `portables/preflight/PREFLIGHT_V2.md`. The former `docs/PREFLIGHT.md` body is superseded; that path now exists only as a lightweight succession pointer, while historical bodies remain recoverable through Git history.\n\nThis promotion creates the Preflight portable family at version 2.0. It does not change MSL 4.3, Setup 3.0 or Chat–Work V4.",
    "lineage promotion",
    1,
)
portable = must_replace(
    portable,
    "The public claim is narrower and useful: Moon Source provides an inspectable method for reconstructing a human's intended task before execution and for activating heavier execution governance only when the task's consequences require it.",
    "The public claim is narrower and useful: Moon Source provides an inspectable, independently usable portable for reconstructing a human's intended task before execution and for activating heavier execution governance only when the task's consequences require it.",
    "claim ceiling portable wording",
    1,
)

reuse = """

## Reuse and attribution

This portable is Moon-authored open content under **CC-BY-4.0**. You may share and adapt it under that license. Preserve appropriate credit, a license link and an indication of material changes; do not imply endorsement.

For repository-wide licensing details, use https://github.com/luahelenammc/Moon-Source/blob/main/LICENSING.md. For broader content identity, lineage, transformations and permission boundaries, use the current Moon Source Credits & Attribution Ops component when relevant.
"""
portable = portable.replace("\n<!-- MOON-SOURCE-PUBLIC-STAMP -->", reuse + "\n<!-- MOON-SOURCE-PUBLIC-STAMP -->", 1)
write(NEW_CANON, portable)

readme = f"""# Preflight V2

**Human Intent Reconstruction Before AI Execution**

Preflight V2 is the Moon Source portable for reconstructing what a person is actually trying to accomplish before an AI acts on the literal wording of their message.

> Humans should not have to prompt like machines.

## Use it

- Open the canonical portable: [`PREFLIGHT_V2.md`](PREFLIGHT_V2.md)
- Download the packaged current portable: [`preflight-v2.zip`](../../{DOWNLOAD})

The ZIP contains only the exact canonical `PREFLIGHT_V2.md` bytes.

## Quick commands

```text
Preflight
Silent Preflight
Preflight only
Show reconstructed task
Deep Preflight
```

The portable is independently usable. The larger Moon Source repository adds optional routes for source governance, Field to Form, operational reliability, lineage and other consequence-sensitive tasks.

## Family relationship

- **Setup 3.0** helps AI understand a person or project across time.
- **Preflight V2** helps AI understand what the human means now.
- **MSL 4.3** structures context that has earned persistence.
- **Chat–Work V4** routes sustained execution across surfaces and models.

## Canonical identity

- Version: **2.0**
- Canonical repository: https://github.com/luahelenammc/Moon-Source
- Canonical path: `{NEW_CANON}`
- Public surface: https://www.luahelena.com.br/moonsource/?lang=en
- Professional context: https://www.luahelena.com.br/ia/?lang=en
- Creator and final human authority: Lua Helena Moon Martins Cardoso (Moon)
- AI-assisted coauthorial development: Moon + Áurion
- License: CC-BY-4.0

The former `{OLD_CANON}` body was the component home before portable promotion. It remains as a lightweight succession pointer; historical bodies remain recoverable through Git history.

{STAMP}"""
write("portables/preflight/README.md", readme)

canonical_bytes = (ROOT / NEW_CANON).read_bytes()
package = ROOT / DOWNLOAD
package.parent.mkdir(parents=True, exist_ok=True)
with ZipFile(package, "w", compression=ZIP_DEFLATED) as zf:
    zi = ZipInfo("PREFLIGHT_V2.md")
    zi.date_time = (2026, 9, 7, 0, 0, 0)
    zi.compress_type = ZIP_DEFLATED
    zf.writestr(zi, canonical_bytes)
canonical_sha = hashlib.sha256(canonical_bytes).hexdigest()

stub = f"""# Preflight V2 — canonical portable moved

Preflight V2 is now a standalone Moon Source public portable.

**Current canonical path:** [`{NEW_CANON}`](../{NEW_CANON})  
**Current version:** 2.0  
**Portable promotion:** 2026-09-07

This file is a succession pointer, not a second semantic body. The former component body and Preflight V1 lineage remain recoverable through Git history. For current use, load the canonical portable above.

> Humans should not have to prompt like machines.

{STAMP}"""
write(OLD_CANON, stub)

registry_path = ROOT / "registry/public-portables.json"
data = json.loads(registry_path.read_text(encoding="utf-8"))
preflight_components = [c for c in data["public_components"] if c.get("id") == "preflight"]
if len(preflight_components) != 1:
    raise SystemExit(f"migration failed: expected one preflight component, found {len(preflight_components)}")
data["public_components"] = [c for c in data["public_components"] if c.get("id") != "preflight"]
if any(p.get("id") == "preflight" for p in data["portables"]):
    raise SystemExit("migration failed: preflight portable already registered")
preflight_portable = {
    "id": "preflight",
    "title": "Preflight V2",
    "slug": "preflight",
    "version": "2.0",
    "status": "current",
    "class": "human-intent-reconstruction",
    "language": "English with language-sensitive execution",
    "difficulty": "beginner to advanced",
    "function": "Reconstruct a human's intended task from ordinary, incomplete, conversational or self-correcting expression before execution, activating heavier authority, freshness, provenance, safety, destination, mutation and readback guardrails only when consequence requires them",
    "best_for": "People who want to speak naturally to AI without translating themselves into prompt-engineering language, especially when a request contains examples, corrections, implicit constraints, negative requirements or tangled context",
    "canonical_path": NEW_CANON,
    "download_url": f"https://github.com/luahelenammc/Moon-Source/raw/refs/heads/main/{DOWNLOAD}",
    "mirror_url": MIRROR_URL,
    "public_surface_url": "https://www.luahelena.com.br/moonsource/?lang=en",
    "professional_context_url": "https://www.luahelena.com.br/ia/?lang=en",
    "license": "CC-BY-4.0",
    "license_class": "open-content",
    "license_url": "https://creativecommons.org/licenses/by/4.0/",
    "licensing_url": "https://github.com/luahelenammc/Moon-Source/blob/main/LICENSING.md",
    "creator": "Lua Helena Moon Martins Cardoso (Moon)",
    "adaptation_policy": "Share or adapt with appropriate credit, a license link and an indication of changes; do not imply endorsement.",
    "dependencies": [],
    "freshness": "general interpretation method; external facts and product-specific routes remain date-sensitive when a reconstructed task requires them",
    "claim_ceiling": "Published human-intent reconstruction portable; not mind-reading, scientific validation, uniqueness, adoption, measured improvement, universal superiority or independent validation",
    "supersedes": None,
    "archive_paths": [],
    "mirror_path": MIRROR_PATH,
    "canonical_sha256": canonical_sha,
}
data["portables"].insert(1, preflight_portable)
data["as_of"] = "2026-09-07"
note = data.get("mirror_contract", {}).get("current_rebase_note", "")
preflight_note = "Preflight V2 2.0 is now a current standalone portable; the former docs/PREFLIGHT.md component body is superseded by a succession pointer, while the canonical portable is mirrored at moonsource/downloads/PREFLIGHT_V2.md."
if preflight_note not in note:
    data["mirror_contract"]["current_rebase_note"] = preflight_note + (" " + note if note else "")
registry_path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")

human = read("registry/PUBLIC_PORTABLES.md")
portable_header = "| ID | Title | Version | Status | License | Function | Canonical file | Download |\n|---|---|---:|---|---|---|---|---|\n"
preflight_row = f"| preflight | Preflight V2 | 2.0 | current | [CC BY 4.0](../LICENSES/CC-BY-4.0.txt) | Human-intent reconstruction before execution, with consequence-triggered guardrails | [PREFLIGHT_V2.md](../{NEW_CANON}) | [⬇️ package (`.zip`)](https://github.com/luahelenammc/Moon-Source/raw/refs/heads/main/{DOWNLOAD}) |\n"
if preflight_row not in human:
    human = must_replace(human, portable_header, portable_header + preflight_row, "human registry portable row", 1)
human = re.sub(r"^\| \[Preflight[^\n]*\n", "", human, flags=re.M)
human = human.replace("These are public components, not portable registry entries.", "These are public components outside the portable registry. Preflight moved into the portable registry on 2026-09-07; its earlier component-only lineage remains in Git history.")
mirror_bullet = "- https://www.luahelena.com.br/moonsource/downloads/PREFLIGHT_V2.md\n"
anchor = "- https://www.luahelena.com.br/moonsource/downloads/MOON_SOURCE_SETUP.md\n"
if mirror_bullet not in human:
    human = must_replace(human, anchor, mirror_bullet + anchor, "human registry mirror bullet", 1)
human = human.replace("Setup and MSL are general public documents, but their wording can evolve.", "Preflight V2, Setup and MSL are general public documents, but their wording can evolve.")
write("registry/PUBLIC_PORTABLES.md", human)

downloads = read("DOWNLOADS.md")
row_anchor = "| **Moon Source Setup 3.0** | Adaptive routing for proportionate personal and project AI context | [⬇️ Download package (`.zip`)](https://github.com/luahelenammc/Moon-Source/raw/refs/heads/main/downloads/moon-source-setup-3.0.zip) |\n"
row = f"| **Preflight V2** | Human-intent reconstruction before execution without requiring prompt-engineering language | [⬇️ Download package (`.zip`)](https://github.com/luahelenammc/Moon-Source/raw/refs/heads/main/{DOWNLOAD}) |\n"
if row not in downloads:
    downloads = must_replace(downloads, row_anchor, row_anchor + row, "download hub row", 1)
downloads = re.sub(
    r"\n## Open a public component\n\n\[\*\*Preflight[^\n]+\n\n",
    "\n## Preflight is now a portable\n\n[**Preflight V2 — Human Intent Reconstruction Before AI Execution**](portables/preflight/PREFLIGHT_V2.md) is now a standalone public portable with its own packaged download above. The former `docs/PREFLIGHT.md` path remains only as a succession pointer.\n\n",
    downloads,
    count=1,
)
downloads = downloads.replace("- [🛫 Preflight](docs/PREFLIGHT.md)", "- [🛫 Preflight V2](portables/preflight/PREFLIGHT_V2.md)\n- [Preflight V2 guide](portables/preflight/README.md)")
choose_anchor = "- **Just want AI to understand you better?** Download **Moon Source Setup 3.0**.\n"
choose = "- **Want AI to reconstruct what you mean before it acts?** Download **Preflight V2**.\n"
if choose not in downloads:
    downloads = must_replace(downloads, choose_anchor, choose_anchor + choose, "download chooser", 1)
write("DOWNLOADS.md", downloads)

root_readme = read("README.md")
root_readme = root_readme.replace("[Preflight V2](docs/PREFLIGHT.md)", "[Preflight V2](portables/preflight/PREFLIGHT_V2.md)")
root_readme = root_readme.replace("[Preflight](docs/PREFLIGHT.md)", "[Preflight V2](portables/preflight/PREFLIGHT_V2.md)")
root_readme = root_readme.replace("Setup, MSL and Chat–Work are separately versioned public projections", "Setup, Preflight, MSL and Chat–Work are separately versioned public projections")
portable_anchor = "- 🧭 [**Moon Source Setup 3.0**](portables/setup/MOON_SOURCE_SETUP.md) — adaptive routing to the smallest useful personal or project context setup.\n"
portable_bullet = "- 🛫 [**Preflight V2**](portables/preflight/PREFLIGHT_V2.md) — human-intent reconstruction before execution, with heavier guardrails only when consequence requires them.\n"
if portable_bullet not in root_readme:
    root_readme = must_replace(root_readme, portable_anchor, portable_anchor + portable_bullet, "README portable bullet", 1)
root_readme = re.sub(r"^\| \[Preflight V2\].*\n", "", root_readme, flags=re.M)
root_readme = root_readme.replace(
    "Current structural grammar: **MSL 4.3**. Current public portables: **Setup 3.0**, **MSL 4.3** and **Chat–Work 4.2-public**.",
    "Current structural grammar: **MSL 4.3**. Current public portables: **Setup 3.0**, **Preflight 2.0**, **MSL 4.3** and **Chat–Work 4.2-public**.",
)
write("README.md", root_readme)

kernel = read("MOON_SOURCE_AI_KERNEL.md")
kernel = kernel.replace("docs/PREFLIGHT.md", NEW_CANON)
kernel = kernel.replace(
    "adaptive task shaping before execution: intent, authority, missing facts, risk, destination, form and question threshold.",
    "standalone human-intent reconstruction before execution; heavier authority, freshness, provenance, safety, destination, mutation and readback checks are conditional routes.",
)
kernel = kernel.replace("Preflight is the general before-execution gate.", "Preflight V2 is the general human-intent reconstruction portable before execution.")
write("MOON_SOURCE_AI_KERNEL.md", kernel)

architecture = read("ARCHITECTURE.md")
architecture = architecture.replace("docs/PREFLIGHT.md", NEW_CANON)
architecture = architecture.replace("[Preflight](portables/preflight/PREFLIGHT_V2.md)", "[Preflight V2](portables/preflight/PREFLIGHT_V2.md)")
write("ARCHITECTURE.md", architecture)

evidence = read("EVIDENCE_AND_CLAIMS.md")
evidence = evidence.replace(
    "Moon Source includes independently readable public portables for setup, adaptive structural grammar and Chat–Work routing.",
    "Moon Source includes independently readable public portables for setup, human-intent reconstruction, adaptive structural grammar and Chat–Work routing.",
)
evidence = evidence.replace(
    "The public body includes a documented Preflight V2 method for human-intent reconstruction before execution, integrated with the AI Kernel, Architecture and Setup 3.0.",
    "The public body includes a standalone Preflight V2 portable for human-intent reconstruction before execution, integrated with the AI Kernel, Architecture and Setup 3.0.",
)
if "documented Preflight method for adaptive task shaping" in evidence:
    evidence = evidence.replace("documented Preflight method for adaptive task shaping", "standalone Preflight V2 portable for human-intent reconstruction")
write("EVIDENCE_AND_CLAIMS.md", evidence)

impl = read("docs/EXISTING_IMPLEMENTATIONS.md")
impl = impl.replace("| Human-intent reconstruction before execution | [Preflight V2](PREFLIGHT.md)", "| Human-intent reconstruction before execution | [Preflight V2](../portables/preflight/PREFLIGHT_V2.md)")
impl = impl.replace("| Adaptive task shaping before execution | [Preflight](PREFLIGHT.md)", "| Human-intent reconstruction before execution | [Preflight V2](../portables/preflight/PREFLIGHT_V2.md)")
impl = impl.replace("A documented public method is integrated with the AI Kernel, Architecture and Setup 3.0", "A standalone public portable is integrated with the AI Kernel, Architecture and Setup 3.0")
write("docs/EXISTING_IMPLEMENTATIONS.md", impl)

boundary = read("PUBLIC_BOUNDARY.md")
boundary = boundary.replace("[Preflight](docs/PREFLIGHT.md)", "[Preflight V2](portables/preflight/PREFLIGHT_V2.md)")
write("PUBLIC_BOUNDARY.md", boundary)

setup = read("portables/setup/MOON_SOURCE_SETUP.md")
setup = setup.replace("https://github.com/luahelenammc/Moon-Source/blob/main/docs/PREFLIGHT.md", "https://github.com/luahelenammc/Moon-Source/blob/main/portables/preflight/PREFLIGHT_V2.md")
setup = setup.replace("The general mechanism shapes any request before execution", "The general portable reconstructs human intent before execution")
write("portables/setup/MOON_SOURCE_SETUP.md", setup)

terms = read("docs/TERMINOLOGY.md")
terms = terms.replace(
    "| Preflight | Adaptive human-intent reconstruction before execution",
    "| Preflight V2 | Standalone portable for adaptive human-intent reconstruction before execution",
)
terms = terms.replace("broader Preflight mechanism", "broader Preflight V2 portable")
write("docs/TERMINOLOGY.md", terms)

changelog = read("CHANGELOG.md")
entry = """## 2026-09-07 — Preflight V2 portable promotion

- Promoted Preflight V2 from a repository component into a standalone public portable at `portables/preflight/PREFLIGHT_V2.md`.
- Added explicit operating modes (`Preflight`, `Silent Preflight`, `Preflight only`, `Show reconstructed task`, `Deep Preflight`) while preserving the human-intent reconstruction core and consequence-triggered guardrails.
- Added a deterministic `.zip` download package containing the exact canonical Markdown bytes, plus canonical SHA-256 identity and website mirror mapping in the portable registry.
- Replaced the former `docs/PREFLIGHT.md` body with a lightweight succession pointer so the active tree keeps one semantic source while historical bodies remain recoverable through Git history.
- Reconciled README, download hub, AI Kernel, Architecture, evidence, implementation map, public boundary, terminology and Setup routing without changing MSL 4.3, Setup 3.0 or Chat–Work V4.

"""
marker = "Historical entries describe the repository state at their recorded date. The current licensing authority is [LICENSING.md](LICENSING.md).\n\n"
if entry not in changelog:
    changelog = must_replace(changelog, marker, marker + entry, "changelog insertion", 1)
write("CHANGELOG.md", changelog)

for path in ["README.md", "ARCHITECTURE.md", "MOON_SOURCE_AI_KERNEL.md", "PUBLIC_BOUNDARY.md", "EVIDENCE_AND_CLAIMS.md", "registry/PUBLIC_PORTABLES.md"]:
    text = read(path)
    if "docs/PREFLIGHT.md" in text:
        raise SystemExit(f"migration failed: stale current Preflight path remains in {path}")

print(f"promoted Preflight V2 portable; canonical_sha256={canonical_sha}")
