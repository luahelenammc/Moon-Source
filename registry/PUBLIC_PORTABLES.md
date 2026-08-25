# Public Portables

These are the current public portables in the Moon Source family. Each has one canonical path in this repository.

Want everything at once? [**Download the complete Moon Source repository (.zip)**](https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip) or open the [download hub](../DOWNLOADS.md).

| ID | Title | Version | Status | License | Function | Canonical file | Download |
|---|---|---:|---|---|---|---|---|
| moon-source-setup | Moon Source Setup | 3.0 | current | [CC BY 4.0](../LICENSES/CC-BY-4.0.txt) | Adaptive routing for proportionate personal and project AI context | [MOON_SOURCE_SETUP.md](../portables/setup/MOON_SOURCE_SETUP.md) | [`.md`](https://raw.githubusercontent.com/luahelenammc/Moon-Source/main/portables/setup/MOON_SOURCE_SETUP.md) |
| moon-source-language | Moon Source Language | 4.3 | current | [CC BY 4.0](../LICENSES/CC-BY-4.0.txt) | Adaptive structural grammar for context work | [MSL_4_3.md](../portables/msl/MSL_4_3.md) | [`.md`](https://raw.githubusercontent.com/luahelenammc/Moon-Source/main/portables/msl/MSL_4_3.md) |
| chat-work-routing | Chat–Work Routing Protocol V2 | 2.0-public | current | [CC BY 4.0](../LICENSES/CC-BY-4.0.txt) | Surface, model and reasoning-effort routing | [CHAT_WORK_ROUTING_PROTOCOL_V2.md](../portables/chat-work/CHAT_WORK_ROUTING_PROTOCOL_V2.md) | [`.md`](https://raw.githubusercontent.com/luahelenammc/Moon-Source/main/portables/chat-work/CHAT_WORK_ROUTING_PROTOCOL_V2.md) |

## Public components outside the portable registry

These are public components, not portable registry entries. Their chronology is derived from the first canonical public file and the latest material public method change in Git history. A public stamp, typo-only change or merge narration does not automatically count as a material update.

| Component | Public since | Last material update | Status | Purpose |
|---|---:|---:|---|---|
| [Preflight — Adaptive Task Shaping Before AI Execution](../docs/PREFLIGHT.md) | 2026-08-23 | 2026-08-23 | current | Shapes intent, authority, risk, destination and proportionate form before execution |
| [Credits & Attribution Ops](../docs/CREDITS_ATTRIBUTION_OPS.md) | 2026-08-17 | 2026-08-18 | current | Protects intellectual lineage, content custody and immaterial-asset boundaries |
| [Operational Devices](../docs/OPERATIONAL_DEVICES.md) | 2026-08-23 | 2026-08-23 | current | Embodies reusable procedures on concrete surfaces with bounded state and receipts |
| [Operational Reliability](../docs/OPERATIONAL_RELIABILITY.md) | 2026-08-23 | 2026-08-23 | current | Structures diagnosis, failure boundaries, reversibility, receipts and freshness |
| [Failure to Capability — Failure Foundry](../docs/FAILURE_FOUNDRY.md) | 2026-08-23 | 2026-08-23 | current | Turns recurring failure into the smallest validated public mechanism |
| [Connected Sources](../docs/CONNECTED_SOURCES.md) | 2026-08-23 | 2026-08-23 | current | Governs connector-aware authority, retrieval, freshness, mutation and readback |
| [Source Hygiene](../docs/SOURCE_HYGIENE.md) | 2026-08-17 | 2026-08-17 | current | Diagnoses stale, duplicated, contradictory or orphaned corpus material |
| [Signal Calibration](../docs/SIGNAL_CALIBRATION.md) | 2026-08-21 | 2026-08-21 | current | Calibrates weak or convergent signals into bounded working inference |
| [Procedural Projection](../docs/PROCEDURAL_PROJECTION.md) | 2026-08-17 | 2026-08-17 | current | Projects stable methods into procedures without moving source authority |

The component inventory is machine-readable in [`registry/public-portables.json`](public-portables.json), currently at schema `1.1`. A component becoming public does not automatically make it a portable; a component update does not automatically require an MSL, Setup or Chat–Work version bump.

The [Browser Console Device reference](../examples/browser-console-device/) remains an experimental bounded implementation, not a current component registry entry or portable, and therefore has no portable fingerprint or mirror contract.

`MOON_SOURCE_USE_AND_ATTRIBUTION.md` is not a component. It remains repository/footer governance for Moon Source-specific use framing, project authorship and the compact watermark.

## Website mirrors

The current branded website keeps convenience copies under:

- https://www.luahelena.com.br/moonsource/downloads/MOON_SOURCE_SETUP.md
- https://www.luahelena.com.br/moonsource/downloads/MOON_SOURCE_PUBLIC_PORTABLE_MSL_4_3.md
- https://www.luahelena.com.br/moonsource/downloads/CHAT_WORK_ROUTING_PROTOCOL_V2_MSL_4_3.md

These paths are mirrors for access. The repository paths above are the canonical semantic sources for the current public family.

## Freshness

Setup and MSL are general public documents, but their wording can evolve. Chat–Work contains product and model calibration that must be rechecked before being treated as current fact.

## Legacy policy

A superseded version should remain recoverable through Git history, an archive path or a preserved website URL where feasible. It should be marked superseded rather than silently deleted.

## Mirror synchronization contract

The repository paths in the table are the only current semantic sources. The branded website paths are convenience mirrors preserved for compatibility.

Each registry entry records the mirror path, mirror URL, portable version and canonical SHA-256 fingerprint. Run `python scripts/check_mirror_sync.py` after any portable or mirror change. The 2026-08-16 rebase prepared exact mirror updates in [LUAHELENA PR #11](https://github.com/luahelenammc/LUAHELENA/pull/11), which merged into `main` as `31e1473ead26ba6f23900ad4f7259cbe2bdec7e4`. Canonical and mirror bytes were verified equal on 2026-08-16 after production promotion PR #12 and title cleanup PR #13; GitHub Pages run `31985711151` completed successfully.

The registry records portable identity, licensing class and fingerprints. Legal reuse permission comes from [LICENSING.md](../LICENSING.md) and the applicable standard license. The registry does not replace [Credits & Attribution Ops](../docs/CREDITS_ATTRIBUTION_OPS.md), which governs the broader intellectual chain of custody.

<!-- MOON-SOURCE-PUBLIC-STAMP -->

---

> 🌙 **Moon Source** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Source/blob/main/LICENSING.md) · [Use & attribution](https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md) · [Full source (.zip)](https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip)
