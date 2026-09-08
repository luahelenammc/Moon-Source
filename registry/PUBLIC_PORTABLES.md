# Public Portables

These are the current public portables in the Moon Source family. Each has one canonical path in this repository. The active tree exposes only the latest generation of each portable family. Individual download links use small ZIP packages containing the exact canonical file, `README.md` and `FIRST_USE.md` support material so browsers save the portable instead of opening Markdown inline.

Want everything at once? [**Download the complete Moon Source repository (.zip)**](https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip) or open the [download hub](../DOWNLOADS.md).

| ID | Title | Version | Status | License | Function | Canonical file | Download |
|---|---|---:|---|---|---|---|---|
| preflight | Preflight | 2.0 | current | [CC BY 4.0](../LICENSES/CC-BY-4.0.txt) | Human-intent reconstruction before execution, with consequence-triggered guardrails | [PREFLIGHT_V2.md](../portables/preflight/PREFLIGHT_V2.md) | [⬇️ package (`.zip`)](https://github.com/luahelenammc/Moon-Source/raw/refs/heads/main/downloads/preflight-v2.zip) |
| moon-source-setup | Moon Source Setup | 3.1 | current | [CC BY 4.0](../LICENSES/CC-BY-4.0.txt) | Adaptive routing for proportionate personal and project AI context, including a probed persistent-source route | [MOON_SOURCE_SETUP.md](../portables/setup/MOON_SOURCE_SETUP.md) | [⬇️ package (`.zip`)](https://github.com/luahelenammc/Moon-Source/raw/refs/heads/main/downloads/moon-source-setup-3.1.zip) |
| be-my-eyes | Be My Eyes | 1.0-public | current | [CC BY 4.0](../LICENSES/CC-BY-4.0.txt) | Reads human communication as a scene, separating observation from inference and checking subtext, overread, reception and response posture | [BE_MY_EYES.md](../portables/be-my-eyes/BE_MY_EYES.md) | [⬇️ package (`.zip`)](https://github.com/luahelenammc/Moon-Source/raw/refs/heads/main/downloads/be-my-eyes-1.0-public.zip) |
| connected-sources | Connected Sources | 1.1-public | current | [CC BY 4.0](../LICENSES/CC-BY-4.0.txt) | Living Source Protocol for standalone, connected-read, living-source and federated source operation with authority, freshness, mutation, readback and fallback boundaries | [CONNECTED_SOURCES.md](../portables/connected-sources/CONNECTED_SOURCES.md) | [⬇️ package (`.zip`)](https://github.com/luahelenammc/Moon-Source/raw/refs/heads/main/downloads/connected-sources-1.1-public.zip) |
| moon-source-language | Moon Source Language | 4.3 | current | [CC BY 4.0](../LICENSES/CC-BY-4.0.txt) | Adaptive structural grammar for context work | [MSL_4_3.md](../portables/msl/MSL_4_3.md) | [⬇️ package (`.zip`)](https://github.com/luahelenammc/Moon-Source/raw/refs/heads/main/downloads/moon-source-language-4.3.zip) |
| chat-work-routing | Chat–Work Routing Protocol | 4.4-public | current | [CC BY 4.0](../LICENSES/CC-BY-4.0.txt) | Object- and workload-routed execution across Chat, Work and optional Codex with capability floors, Budget Survivability, model-neutral Intelligence Distillation Ladder, connector-aware source transport, bounded micro-bursts, decision-bearing returns, Chat Postflight, acceptance and delta-only re-entry | [CHAT_WORK_ROUTING_PROTOCOL_V4.md](../portables/chat-work/CHAT_WORK_ROUTING_PROTOCOL_V4.md) | [⬇️ package (`.zip`)](https://github.com/luahelenammc/Moon-Source/raw/refs/heads/main/downloads/chat-work-routing-protocol-v4.zip) |

## Additional public components outside the portable registry

These are the eight additional public method components that are not current portables. Preflight moved into the portable registry on 2026-09-07; its earlier component-only lineage remains in Git history. Be My Eyes and Connected Sources are current portables that may also own structural responsibilities, so they appear in the portable table only and are not duplicated here. Chronology is derived from the first canonical public file and the latest material public method change in Git history. A public stamp, typo-only change or merge narration does not automatically count as a material update.

| Component | Public since | Last material update | Status | Purpose |
|---|---:|---:|---|---|
| [Credits & Attribution Ops](../docs/CREDITS_ATTRIBUTION_OPS.md) | 2026-08-17 | 2026-08-18 | current | Protects intellectual lineage, content custody and immaterial-asset boundaries |
| [Operational Devices](../docs/OPERATIONAL_DEVICES.md) | 2026-08-23 | 2026-08-23 | current | Embodies reusable procedures on concrete surfaces with bounded state and receipts |
| [Operational Reliability](../docs/OPERATIONAL_RELIABILITY.md) | 2026-08-23 | 2026-08-26 | current | Structures diagnosis, failure boundaries, reversibility, ordinary and Context Receipts, and freshness |
| [Failure to Capability — Failure Foundry](../docs/FAILURE_FOUNDRY.md) | 2026-08-23 | 2026-08-23 | current | Turns recurring failure into the smallest validated public mechanism |
| [Source Operations — Retrieve, Process, Metabolize and Promote](../docs/SOURCE_OPERATIONS.md) | 2026-09-04 | 2026-09-04 | current | Defines source-operation grammar, promotion gates, lifecycle, legacy succession, readback and no-delta |
| [Source Hygiene](../docs/SOURCE_HYGIENE.md) | 2026-08-17 | 2026-08-17 | current | Diagnoses stale, duplicated, contradictory or orphaned corpus material |
| [Signal Calibration](../docs/SIGNAL_CALIBRATION.md) | 2026-08-21 | 2026-08-21 | current | Calibrates weak or convergent signals into bounded working inference |
| [Procedural Projection](../docs/PROCEDURAL_PROJECTION.md) | 2026-08-17 | 2026-08-17 | current | Projects stable methods into procedures without moving source authority |

Preflight is now portable version **2.0**. Its earlier component-only lineage and V1 remain recoverable through Git history; current use routes to `portables/preflight/PREFLIGHT_V2.md`.

Be My Eyes is portable version **1.0-public**. `portables/be-my-eyes/BE_MY_EYES.md` is its one active canonical semantic body and may serve both structural and portable roles.

Connected Sources is portable version **1.1-public**. `portables/connected-sources/CONNECTED_SOURCES.md` is its one active canonical semantic body and may serve both structural and portable roles. The dated ChatGPT product facts live only in the subordinate adapter `docs/CONNECTED_SOURCES_CHATGPT_ADAPTER.md`.

The component inventory is machine-readable in [`registry/public-portables.json`](public-portables.json), currently at schema `1.1`. A component becoming public does not automatically make it a portable. A current portable may also be structural, but it is represented in the portable registry rather than duplicated in the non-portable component inventory. A component update does not automatically require an MSL, Setup or Chat–Work version bump.

The [Browser Console Device reference](../examples/browser-console-device/) remains an experimental bounded implementation, not a current component registry entry or portable, and therefore has no portable fingerprint or mirror contract.

`MOON_SOURCE_USE_AND_ATTRIBUTION.md` is not a component. It remains repository/footer governance for Moon Source-specific use framing, project authorship and the compact watermark.

## Website mirrors

The current branded website keeps convenience copies of the current portables under:

- https://www.luahelena.com.br/moonsource/downloads/PREFLIGHT_V2.md
- https://www.luahelena.com.br/moonsource/downloads/MOON_SOURCE_SETUP.md
- https://www.luahelena.com.br/moonsource/downloads/BE_MY_EYES.md
- https://www.luahelena.com.br/moonsource/downloads/CONNECTED_SOURCES.md
- https://www.luahelena.com.br/moonsource/downloads/MOON_SOURCE_PUBLIC_PORTABLE_MSL_4_3.md
- https://www.luahelena.com.br/moonsource/downloads/CHAT_WORK_ROUTING_PROTOCOL_V4_MSL_4_4.md

These paths mirror only the current generation. Superseded mirror files are removed from the live surface and remain recoverable through Git history when needed.

## Freshness

Preflight, Setup, Be My Eyes, Connected Sources and Moon Source Language are general public documents, but their wording can evolve. Be My Eyes is structurally stable as a contextual-reading method; Connected Sources is structurally stable around source authority, capability probing and bounded source operations, with dated ChatGPT product facts isolated in its subordinate adapter. Both portables should be rechecked when their canonical body changes. Chat–Work Routing Protocol contains a stable routing/postflight core plus product and model calibration that must be rechecked before volatile product facts are treated as current. Its version 4.4-public subversion retains the model-neutral Intelligence Distillation Ladder and adds connector-aware source transport with authority, freshness, mutation, readback and fallback fields.

## Historical-version policy

The live repository and live mirror surface expose only current portable generations. A superseded portable is removed from `main` and from the website download tree when its successor is promoted.

Historical versions remain recoverable through Git history and, when useful, immutable tags or releases. History belongs to version control; it does not remain loaded into the current corpus merely to keep an old deep link alive.

Public components follow the same active-state principle unless a current governing file explicitly creates a separate archive artifact. Preflight V1 and the component-only V2 body remain recoverable through repository history; `portables/preflight/PREFLIGHT_V2.md` governs current portable use.

## Mirror synchronization contract

The repository paths in the table are the only current semantic sources. The branded website paths are current convenience mirrors, not compatibility archives.

Each registry entry records the mirror path, mirror URL, portable version and canonical SHA-256 fingerprint. Run `python scripts/check_mirror_sync.py` after any portable or mirror change. Historical mirror synchronization and production promotion remain documented in Git history and [MIRROR_SYNCHRONIZATION.md](../docs/MIRROR_SYNCHRONIZATION.md).

The registry records portable identity, licensing class and fingerprints. Legal reuse permission comes from [LICENSING.md](../LICENSING.md) and the applicable standard license. The registry does not replace [Credits & Attribution Ops](../docs/CREDITS_ATTRIBUTION_OPS.md), which governs the broader intellectual chain of custody.

<!-- MOON-SOURCE-PUBLIC-STAMP -->

---

> 🌙 **Moon Source** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Source/blob/main/LICENSING.md) · [Use & attribution](https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md) · [Full source (.zip)](https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip)
