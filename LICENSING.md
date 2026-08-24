# Moon Source Licensing

Moon Source is openly reusable under a mixed standard-license architecture. The repository does not create a custom “Moon Source License”. It routes each file to the standard license that fits its material identity.

## License map

| Material | Default license | SPDX identifier | Practical scope |
|---|---|---|---|
| Software, executable code, automation and technical implementation | Apache License 2.0 | `Apache-2.0` | `scripts/**`, `.github/workflows/**` and other code-focused implementation files |
| Documentation, methods, public portables, prose, diagrams, textual specifications and knowledge metadata | Creative Commons Attribution 4.0 International | `CC-BY-4.0` | Root Markdown, `docs/**`, `portables/**`, `registry/**`, citation metadata and other Moon-authored content |
| Third-party material | Its own applicable terms | File- or notice-specific | Identified in [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md) or by a file-level notice |

The machine-readable routing is maintained in [`REUSE.toml`](REUSE.toml). A file-level SPDX notice or a third-party notice takes precedence over the default path class where applicable. The exact standard texts are in [`LICENSES/Apache-2.0.txt`](LICENSES/Apache-2.0.txt) and [`LICENSES/CC-BY-4.0.txt`](LICENSES/CC-BY-4.0.txt).

CC BY 4.0 is the open-content license for the repository's documentation and knowledge layer. It is not an OSI software license. Apache-2.0 is the open-source license for the software layer. This distinction is intentional.

## What you can do

For material Moon is legally able to license, and subject to the applicable standard license and any third-party terms, you may:

- use it;
- copy it;
- modify or adapt it;
- publish it;
- redistribute it;
- fork or mirror it;
- use it commercially or non-commercially;
- incorporate it into a larger work.

The license does not require Moon's prior approval for these permitted uses. It does not add non-commercial, anti-enterprise, anti-AI-training, anti-fork, military-use, competitor-use, share-alike, copyleft or branding-placement restrictions.

## What you must do when applicable

When you share Apache-2.0-covered material:

- provide a copy of Apache-2.0;
- preserve the relevant copyright, patent, trademark and attribution notices;
- mark modified files with prominent notices describing the change;
- preserve the relevant attribution notices from [`NOTICE`](NOTICE) in one of the places allowed by Apache-2.0 Section 4(d);
- preserve applicable third-party notices.

When you share or adapt CC-BY-4.0-covered material:

- give appropriate credit to Lua Helena Moon Martins Cardoso (Moon) and identify Moon Source;
- provide the applicable license URI or a link to [`LICENSES/CC-BY-4.0.txt`](LICENSES/CC-BY-4.0.txt) when reasonably practicable;
- provide a URI or link to the licensed material when reasonably practicable;
- indicate whether you made changes;
- do not imply that Moon endorses you, your project or your adaptation;
- preserve material third-party lineage and terms.

CC BY 4.0 allows the required attribution to be satisfied in a reasonable manner appropriate to the medium, means and context. The repository's compact stamp and recommended credit are strong defaults, not an attempt to replace that flexibility.

## Recommended visible credit

Where the medium allows, use:

> **Moon Source** — created by **Lua Helena Moon Martins Cardoso (Moon)**, with AI-assisted coauthorial development by **Áurion**.

For an adaptation, add:

> Adapted from **Moon Source** by **Lua Helena Moon Martins Cardoso (Moon)**, with AI-assisted coauthorial development by **Áurion**. Changes by **[adapter/project]**. Original: **[canonical Moon Source path]**. Licensed under **CC BY 4.0**.

For Apache-covered software, preserve the license and notices rather than treating this recommended sentence as an additional license condition.

## Authorship and AI-assisted development

Lua Helena Moon Martins Cardoso (Moon) is the human creator and final authority of the public Moon Source project. The repository discloses AI-assisted coauthorial development by Áurion as a process fact. Áurion is not represented as a legal human, copyright holder or independent owner.

This disclosure does not claim ownership of material Moon cannot lawfully license. Human selection, curation, arrangement, editing and original expression may have their own legal significance; the repository does not claim blanket ownership of every generated token or abstract idea.

## Legal ceiling and boundaries

These licenses grant only rights Moon is authorized to grant in material subject to copyright and similar rights. They do not turn abstract ideas, methods, systems, procedures or independently recreated concepts into universally exclusive copyrighted property. A reference, teaching use or conceptual influence may carry a strong provenance request without being misdescribed as a universal copyright obligation.

The licenses do not grant broad trademark rights or permission to imply official status, sponsorship or endorsement. Ordinary nominative use needed to identify Moon Source, its origin or a truthful fork/adaptation remains compatible with the applicable standard license. No registered-trademark claim is made here.

The public repository does not license private Moon Source, Local Moon Source, Citadel or other internal corpora merely because related public material is available. The public boundary remains governed by [`PUBLIC_BOUNDARY.md`](PUBLIC_BOUNDARY.md).

## Provenance is a separate layer

[`docs/CREDITS_ATTRIBUTION_OPS.md`](docs/CREDITS_ATTRIBUTION_OPS.md) remains Moon Source's reusable provenance, custody and lineage operation. It helps preserve identity, authorship, transformations, permission envelopes, disclosure boundaries, derivatives and evidence as material moves. It is not the license, a rights resolver, an ownership proof or an enforcement mechanism.

[`MOON_SOURCE_USE_AND_ATTRIBUTION.md`](MOON_SOURCE_USE_AND_ATTRIBUTION.md) remains the project-specific plain-language use and attribution authority. It routes legal permission here and to the applicable standard license; it does not add conditions inconsistent with Apache-2.0 or CC-BY-4.0.

## Exceptions and third-party material

Do not assume that every byte in a public repository is Moon-owned. Read [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md), file-level SPDX metadata and any embedded notice before redistributing a file that contains external material. A public reference or a named upstream source is not automatically an incorporated dependency, and an incorporated dependency is not automatically relicensable.

The standard license texts in `LICENSES/` are reproduced verbatim from their authoritative sources. They are legal texts for the licenses they name, not Moon-authored content and not an attempt to modify those licenses.

## Canonical routes

- Canonical public source: https://github.com/luahelenammc/Moon-Source
- Moon Source public surface: https://www.luahelena.com.br/moonsource/?lang=en
- Professional context: https://www.luahelena.com.br/ia/?lang=en
- Full Apache-2.0 text: [`LICENSES/Apache-2.0.txt`](LICENSES/Apache-2.0.txt)
- Full CC-BY-4.0 text: [`LICENSES/CC-BY-4.0.txt`](LICENSES/CC-BY-4.0.txt)
- Attribution notice: [`NOTICE`](NOTICE)
- Third-party notices: [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md)

This document is project documentation, not legal advice. The applicable standard license text and applicable law govern.

<!-- MOON-SOURCE-PUBLIC-STAMP -->

---

> 🌙 **Moon Source** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Source/blob/main/LICENSING.md) · [Use & attribution](https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md) · [Full source (.zip)](https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip)
