# Public Capabilities

This is Moon Source's unified public capability registry. Each capability has
one canonical semantic body and one architectural responsibility. Some
capabilities also have a supported standalone distribution.

“Portable” is therefore a distribution profile, not a competing semantic
class. The machine-readable contract is
[registry/public-capabilities.json](public-capabilities.json), schema 2.0.
The table below is a human-readable view of the same fourteen records.

| ID | Capability | Architectural role | Version | Status | Canonical body | Standalone distribution |
|---|---|---|---:|---|---|---|
| be-my-eyes | [Be My Eyes](../portables/be-my-eyes/README.md) | contextual scene-reading method | 1.0-public | current | [BE_MY_EYES.md](../portables/be-my-eyes/BE_MY_EYES.md#first-use) | [ZIP](../downloads/be-my-eyes-1.0-public.zip) |
| chat-work-routing | [Chat–Work Routing Protocol](../portables/chat-work/README.md) | operational routing protocol | 4.5-public | current | [CHAT_WORK_ROUTING_PROTOCOL_V4.md](../portables/chat-work/CHAT_WORK_ROUTING_PROTOCOL_V4.md#first-use) | [ZIP](../downloads/chat-work-routing-protocol-v4.zip) |
| connected-sources | [Connected Sources](../portables/connected-sources/README.md) | structural crown jewel | 1.1-public | current | [CONNECTED_SOURCES.md](../docs/CONNECTED_SOURCES.md#first-use) | [ZIP](../downloads/connected-sources-1.1-public.zip) |
| credits-attribution-ops | 🧾 Credits & Attribution Ops | immaterial-asset protection | — | current | [CREDITS_ATTRIBUTION_OPS.md](../docs/CREDITS_ATTRIBUTION_OPS.md) | — |
| failure-foundry | 🏭 Failure to Capability — Failure Foundry | failure-to-capability method | — | current | [FAILURE_FOUNDRY.md](../docs/FAILURE_FOUNDRY.md) | — |
| moon-source-language | [Moon Source Language](../portables/msl/README.md) | sovereign semantic passage grammar | 5.0 | current | [MSL_5_0.md](../portables/msl/MSL_5_0.md#first-use) | [ZIP](../downloads/moon-source-language-5.0.zip) |
| moon-source-setup | [Moon Source Setup](../portables/setup/README.md) | adaptive context router | 3.1 | current | [MOON_SOURCE_SETUP.md](../portables/setup/MOON_SOURCE_SETUP.md#first-use) | [ZIP](../downloads/moon-source-setup-3.1.zip) |
| operational-devices | 🛠️ Operational Devices | operational-device pattern | — | current | [OPERATIONAL_DEVICES.md](../docs/OPERATIONAL_DEVICES.md) | — |
| operational-reliability | 🛡️ Operational Reliability | operational-reliability method | — | current | [OPERATIONAL_RELIABILITY.md](../docs/OPERATIONAL_RELIABILITY.md) | — |
| preflight | [Preflight](../portables/preflight/README.md) | transversal interface method | 2.0 | current | [PREFLIGHT_V2.md](../portables/preflight/PREFLIGHT_V2.md#first-use) | [ZIP](../downloads/preflight-v2.zip) |
| procedural-projection | 🧩 Procedural Projection | procedural-projection method | — | current | [PROCEDURAL_PROJECTION.md](../docs/PROCEDURAL_PROJECTION.md) | — |
| signal-calibration | 🎚️ Signal Calibration | qualitative signal calibration | — | current | [SIGNAL_CALIBRATION.md](../docs/SIGNAL_CALIBRATION.md) | — |
| source-hygiene | 🧹 Source Hygiene | source-hygiene method | — | current | [SOURCE_HYGIENE.md](../docs/SOURCE_HYGIENE.md) | — |
| source-operations | 🔄 Source Operations — Retrieve, Process, Metabolize and Promote | source-operations method | — | current | [SOURCE_OPERATIONS.md](../docs/SOURCE_OPERATIONS.md) | — |

## How to read the registry

The canonical body is the semantic authority. The architectural role says what
the capability is responsible for. The optional distribution object says
whether Moon Source supports an independently usable package and where that
package and its exact-byte website mirror live. Readable capability names may
point to lightweight README facades for human browsing; those links do not
change the canonical-body column or machine registry.

A capability is portable when its canonical body can be used independently
within a declared scope and Moon Source publishes a supported standalone route
for it. A standalone distribution does not create a second authority.

The six standalone distributions are a filtered view of the unified registry:
👁️ Be My Eyes, 🔀 Chat–Work Routing Protocol, 🔗 Connected Sources, 🧱 Moon Source Language,
🧭 Moon Source Setup and 🛫 Preflight. This filter is not a second semantic
inventory.

## Connected Sources

[Connected Sources](../docs/CONNECTED_SOURCES.md#first-use) is a structural
crown jewel governing source reach, source/data authority, instruction
authority, jurisdiction, freshness, targeted versus exhaustive retrieval,
connector capability probing, mutation authorization, readback, fallback and
federated source responsibility. Its canonical home follows that
responsibility. It remains independently distributable as version 1.1-public.
The readable [distribution facade](../portables/connected-sources/README.md)
exists only for human presentation and routing.

The dated [ChatGPT adapter notes](../docs/CONNECTED_SOURCES_CHATGPT_ADAPTER.md)
remain subordinate and product-sensitive. They are not a second method body,
registry identity or authority map.

## Website mirrors

The branded website keeps convenience copies of the six current standalone
capabilities under:

- https://www.luahelena.com.br/moonsource/downloads/PREFLIGHT_V2.md
- https://www.luahelena.com.br/moonsource/downloads/MOON_SOURCE_SETUP.md
- https://www.luahelena.com.br/moonsource/downloads/BE_MY_EYES.md
- https://www.luahelena.com.br/moonsource/downloads/CONNECTED_SOURCES.md
- https://www.luahelena.com.br/moonsource/downloads/MOON_SOURCE_PUBLIC_PORTABLE_MSL_5_0.md
- https://www.luahelena.com.br/moonsource/downloads/CHAT_WORK_ROUTING_PROTOCOL_V4_MSL_4_5.md

These are delivery surfaces, not semantic authorities. Each mirror must remain
byte-identical to its mapped canonical body.

## Freshness and versioning

Unversioned capabilities are governed by their canonical material updates.
Standalone capabilities carry independent public versions when a method or
distribution contract earns one. Registry schema changes do not automatically
change a capability version. This presentation-surface restoration keeps
Connected Sources at 1.1-public, MSL at 5.0, Chat–Work at 4.5-public, Setup at
3.1, Preflight at 2.0 and Be My Eyes at 1.0-public.

Product-specific connector behavior, model names, plans, prices, availability
and other volatile facts must be rechecked before being treated as current.
Historical generations belong to Git history or explicit releases, not the
active semantic tree.

## Mirror synchronization contract

Moon Source is the semantic and versioning authority. After a canonical body
changes, update its supported distribution and mirror only after the canonical
registry and validators pass. Use
python scripts/check_mirror_sync.py for exact SHA-256 equality.

The registry does not replace [Credits & Attribution
Ops](../docs/CREDITS_ATTRIBUTION_OPS.md), which governs intellectual lineage,
content custody and immaterial-asset boundaries.

<!-- MOON-SOURCE-PUBLIC-STAMP -->

---

> 🌙 **Moon Source** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Source/blob/main/LICENSING.md) · [Use & attribution](https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md) · [Full source (.zip)](https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip)