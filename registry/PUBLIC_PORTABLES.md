# Public Portables

These are the current public portables in the Moon Source family. Each has one canonical path in this repository. The active tree exposes only the latest generation of each portable family.

Want everything at once? [**Download the complete Moon Source repository (.zip)**](https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip) or open the [download hub](../DOWNLOADS.md).

| ID | Title | Version | Status | License | Function | Canonical file | Download |
|---|---|---:|---|---|---|---|---|
| moon-source-setup | Moon Source Setup | 3.0 | current | [CC BY 4.0](../LICENSES/CC-BY-4.0.txt) | Adaptive routing for proportionate personal and project AI context | [MOON_SOURCE_SETUP.md](../portables/setup/MOON_SOURCE_SETUP.md) | [⬇️ `.md`](https://github.com/luahelenammc/Moon-Source/raw/refs/heads/main/portables/setup/MOON_SOURCE_SETUP.md) |
| moon-source-language | Moon Source Language | 4.3 | current | [CC BY 4.0](../LICENSES/CC-BY-4.0.txt) | Adaptive structural grammar for context work | [MSL_4_3.md](../portables/msl/MSL_4_3.md) | [⬇️ `.md`](https://github.com/luahelenammc/Moon-Source/raw/refs/heads/main/portables/msl/MSL_4_3.md) |
| chat-work-routing | Chat–Work Routing Protocol V3 | 3.0-public | current | [CC BY 4.0](../LICENSES/CC-BY-4.0.txt) | Closed-loop surface/model/effort routing, Chat Postflight, acceptance and re-entry | [CHAT_WORK_ROUTING_PROTOCOL_V3.md](../portables/chat-work/CHAT_WORK_ROUTING_PROTOCOL_V3.md) | [⬇️ `.md`](https://github.com/luahelenammc/Moon-Source/raw/refs/heads/main/portables/chat-work/CHAT_WORK_ROUTING_PROTOCOL_V3.md) |

## Public components outside the portable registry

These are public components, not portable registry entries. Their chronology is derived from the first canonical public file and the latest material public method change in Git history. A public stamp, typo-only change or merge narration does not automatically count as a material update.

| Component | Public since | Last material update | Status | Purpose |
|---|---:|---:|---|---|
| [Preflight — Adaptive Task Shaping Before AI Execution](../docs/PREFLIGHT.md) | 2026-08-23 | 2026-08-23 | current | Shapes intent, authority, risk, destination and proportionate form before execution |
| [Credits & Attribution Ops](../docs/CREDITS_ATTRIBUTION_OPS.md) | 2026-08-17 | 2026-08-18 | current | Protects intellectual lineage, content custody and immaterial-asset boundaries |
| [Operational Devices](../docs/OPERATIONAL_DEVICES.md) | 2026-08-23 | 2026-08-23 | current | Embodies reusable procedures on concrete surfaces with bounded state and receipts |
| [Operational Reliability](../docs/OPERATIONAL_RELIABILITY.md) | 2026-08-23 | 2026-08-26 | current | Structures diagnosis, failure boundaries, reversibility, ordinary and Context Receipts, and freshness |
| [Failure to Capability — Failure Foundry](../docs/FAILURE_FOUNDRY.md) | 2026-08-23 | 2026-08-23 | current | Turns recurring failure into the smallest validated public mechanism |
| [Connected Sources](../docs/CONNECTED_SOURCES.md) | 2026-08-23 | 2026-08-26 | current | Governs connector-aware source/data and instruction authority, progressive retrieval, freshness, mutation and readback |
| [Source Operations — Retrieve, Process, Metabolize and Promote](../docs/SOURCE_OPERATIONS.md) | 2026-09-04 | 2026-09-04 | current | Defines source-operation grammar, promotion gates, lifecycle, legacy succession, readback and no-delta |
| [Source Hygiene](../docs/SOURCE_HYGIENE.md) | 2026-08-17 | 2026-08-17 | current | Diagnoses stale, duplicated, contradictory or orphaned corpus material |
| [Signal Calibration](../docs/SIGNAL_CALIBRATION.md) | 2026-08-21 | 2026-08-21 | current | Calibrates weak or convergent signals into bounded working inference |
| [Procedural Projection](../docs/PROCEDURAL_PROJECTION.md) | 2026-08-17 | 2026-08-17 | current | Projects stable methods into procedures without moving source authority |

The component inventory is machine-readable in [`registry/public-portables.json`](public-portables.json), currently at schema `1.1`. A component becoming public does not automatically make it a portable; a component update does not automatically require an MSL, Setup or Chat–Work version bump.

The [Browser Console Device reference](../examples/browser-console-device/) remains an experimental bounded implementation, not a current component registry entry or portable, and therefore has no portable fingerprint or mirror contract.

`MOON_SOURCE_USE_AND_ATTRIBUTION.md` is not a component. It remains repository/footer governance for Moon Source-specific use framing, project authorship and the compact watermark.

## Website mirrors

The current branded website keeps convenience copies of the current portables under:

- https://www.luahelena.com.br/moonsource/downloads/MOON_SOURCE_SETUP.md
- https://www.luahelena.com.br/moonsource/downloads/MOON_SOURCE_PUBLIC_PORTABLE_MSL_4_3.md
- https://www.luahelena.com.br/moonsource/downloads/CHAT_WORK_ROUTING_PROTOCOL_V3_MSL_4_3.md

These paths mirror only the current generation. Superseded mirror files are removed from the live surface and remain recoverable through Git history when needed.

## Freshness

Setup and MSL are general public documents, but their wording can evolve. Chat–Work contains a stable routing/postflight core plus product and model calibration that must be rechecked before volatile product facts are treated as current.

## Historical-version policy

The live repository and live mirror surface expose only current portable generations. A superseded portable is removed from `main` and from the website download tree when its successor is promoted.

Historical versions remain recoverable through Git history and, when useful, immutable tags or releases. History belongs to version control; it does not remain loaded into the current corpus merely to keep an old deep link alive.

## Mirror synchronization contract

The repository paths in the table are the only current semantic sources. The branded website paths are current convenience mirrors, not compatibility archives.

Each registry entry records the mirror path, mirror URL, portable version and canonical SHA-256 fingerprint. Run `python scripts/check_mirror_sync.py` after any portable or mirror change. Historical mirror synchronization and production promotion remain documented in Git history and [MIRROR_SYNCHRONIZATION.md](../docs/MIRROR_SYNCHRONIZATION.md).

The registry records portable identity, licensing class and fingerprints. Legal reuse permission comes from [LICENSING.md](../LICENSING.md) and the applicable standard license. The registry does not replace [Credits & Attribution Ops](../docs/CREDITS_ATTRIBUTION_OPS.md), which governs the broader intellectual chain of custody.

<!-- MOON-SOURCE-PUBLIC-STAMP -->

---

> 🌙 **Moon Source** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Source/blob/main/LICENSING.md) · [Use & attribution](https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md) · [Full source (.zip)](https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip)
