# Public Capabilities

This is Moon Source's unified public capability registry. Each capability has
one canonical semantic body and one architectural responsibility. Some
capabilities also have a supported standalone distribution.

Standalone distribution is a delivery profile, not a competing semantic
class. Most independently distributed capabilities are also portables, but
that is not required: Connected Sources is a structural component with a
supported standalone distribution. The machine-readable contract is
[registry/public-capabilities.json](public-capabilities.json), schema 2.0.
The table below is a human-readable view of the same sixteen records.

The table's **Summary title** is the concise browsing label. The registry's semantic `title` remains stable in machine-readable metadata; individual README and canonical-body headings use `surface_title` to make the Moon Source role explicit without folding version into identity.

| ID | Summary title | Architectural role | Version | Status | Canonical body | Standalone distribution |
|---|---|---|---:|---|---|---|
| be-my-eyes | [Be My Eyes](../portables/be-my-eyes/README.md) | contextual scene-reading method | 1.0-public | current | [BE_MY_EYES.md](../portables/be-my-eyes/BE_MY_EYES.md#first-use) | [ZIP](../downloads/be-my-eyes.zip) |
| adaptive-orchestration | [Adaptive Orchestration Protocol](../portables/adaptive-orchestration/README.md) | adaptive execution orchestration protocol | 6.3 | current | [ADAPTIVE_ORCHESTRATION_PROTOCOL.md](../portables/adaptive-orchestration/ADAPTIVE_ORCHESTRATION_PROTOCOL.md#first-use) | [ZIP](../downloads/adaptive-orchestration-protocol.zip) |
| connected-sources | [Connected Sources](../portables/connected-sources/README.md) | structural crown jewel | 1.2 | current | [CONNECTED_SOURCES.md](../docs/CONNECTED_SOURCES.md#first-use) | [ZIP](../downloads/connected-sources.zip) |
| credits-attribution-ops | 🧾 Credits & Attribution Ops | immaterial-asset protection | — | current | [CREDITS_ATTRIBUTION_OPS.md](../docs/CREDITS_ATTRIBUTION_OPS.md) | — |
| failure-foundry | 🏭 Failure to Capability — Failure Foundry | failure-to-capability method | — | current | [FAILURE_FOUNDRY.md](../docs/FAILURE_FOUNDRY.md) | — |
| lifecycle-workspace-router | 🗂️ Lifecycle Workspace Router | lifecycle workspace routing method | 1.2 | current | [LIFECYCLE_WORKSPACE_ROUTER.md](../docs/LIFECYCLE_WORKSPACE_ROUTER.md) | — |
| moon-source-language | [Moon Source Language](../portables/msl/README.md) | sovereign semantic passage grammar | 5.1 | current | [MOON_SOURCE_LANGUAGE.md](../portables/msl/MOON_SOURCE_LANGUAGE.md#first-use) | [ZIP](../downloads/moon-source-language.zip) |
| moon-source-setup | [Setup](../portables/setup/README.md) | adaptive context router | 3.1 | current | [MOON_SOURCE_SETUP.md](../portables/setup/MOON_SOURCE_SETUP.md#first-use) | [ZIP](../downloads/moon-source-setup.zip) |
| operational-devices | 🛠️ Operational Devices | operational-device pattern | — | current | [OPERATIONAL_DEVICES.md](../docs/OPERATIONAL_DEVICES.md) | — |
| operational-reliability | 🛡️ Operational Reliability | operational-reliability method | — | current | [OPERATIONAL_RELIABILITY.md](../docs/OPERATIONAL_RELIABILITY.md) | — |
| preflight | [Preflight](../portables/preflight/README.md) | transversal interface method | 2.3 | current | [PREFLIGHT.md](../portables/preflight/PREFLIGHT.md#first-use) | [ZIP](../downloads/preflight.zip) |
| procedural-projection | 🧩 Procedural Projection | procedural-projection method | — | current | [PROCEDURAL_PROJECTION.md](../docs/PROCEDURAL_PROJECTION.md) | — |
| semantic-reweave | 🧵 Semantic Reweave | semantic-topology repair method | — | current | [SEMANTIC_REWEAVE.md](../docs/SEMANTIC_REWEAVE.md) | — |
| signal-calibration | 🎚️ Signal Calibration | qualitative signal calibration | — | current | [SIGNAL_CALIBRATION.md](../docs/SIGNAL_CALIBRATION.md) | — |
| source-hygiene | 🧹 Source Hygiene | source-hygiene method | — | current | [SOURCE_HYGIENE.md](../docs/SOURCE_HYGIENE.md) | — |
| source-operations | 🔄 Source Operations | source-operations method | — | current | [SOURCE_OPERATIONS.md](../docs/SOURCE_OPERATIONS.md) | — |

## Related public body

[Moon Cortex](https://github.com/luahelenammc/Moon-Cortex) is a separate related public body for domain-shaped systems. It is intentionally not a record in this Moon Source capability registry.

## How to read the registry

The canonical body is the semantic authority. The architectural role says what
the capability is responsible for. The optional distribution object says
whether Moon Source supports an independently usable package and where that
package and its exact-byte website mirror live. Readable capability names may
point to lightweight README facades for human browsing; those links do not
change the canonical-body column or machine registry.

A capability may receive a supported standalone distribution when its
canonical body can be used independently within a declared scope. Distribution
does not change architectural identity and does not create a second authority.
Connected Sources therefore remains structural even though it can travel as a
standalone package.

The six standalone distributions are a filtered view of the unified registry:
👁️ Be My Eyes, 🧬 Adaptive Orchestration Protocol, 🔗 Connected Sources, 🧱 Moon Source Language,
🧭 Setup and 🛫 Preflight. This filter is not a second semantic
inventory.

## Connected Sources

[Connected Sources](../docs/CONNECTED_SOURCES.md#first-use) is a structural
crown jewel governing source reach, source/data authority, instruction
authority, jurisdiction, freshness, targeted versus exhaustive retrieval,
consumer-scoped delivery, rehydratable offload, connector capability probing,
mutation authorization, readback, fallback and federated source responsibility.
Its canonical home follows that responsibility. It remains independently
distributable as version 1.2.
The readable [distribution facade](../portables/connected-sources/README.md)
exists only for human presentation and routing.

The dated [ChatGPT adapter notes](../docs/CONNECTED_SOURCES_CHATGPT_ADAPTER.md)
remain subordinate and product-sensitive. They are not a second method body,
registry identity or authority map.

## Website mirrors

The branded website keeps convenience copies of the six current standalone
capabilities under:

- https://www.luahelena.com.br/moonsource/downloads/PREFLIGHT.md
- https://www.luahelena.com.br/moonsource/downloads/MOON_SOURCE_SETUP.md
- https://www.luahelena.com.br/moonsource/downloads/BE_MY_EYES.md
- https://www.luahelena.com.br/moonsource/downloads/CONNECTED_SOURCES.md
- https://www.luahelena.com.br/moonsource/downloads/MOON_SOURCE_PUBLIC_PORTABLE_MSL.md
- https://www.luahelena.com.br/moonsource/downloads/ADAPTIVE_ORCHESTRATION_PROTOCOL.md

The former CHAT_WORK_ROUTING_PROTOCOL.md mirror remains a minimal migration pointer to this current mirror.

These are delivery surfaces, not semantic authorities. Each mirror must remain
byte-identical to its mapped canonical body.

## Freshness and versioning

Capabilities may remain unversioned when their release state is governed only
by canonical material updates. Repository-only capabilities may still carry an
independent version when their method earns a distinct release state;
standalone distribution and semantic versioning are separate dimensions.
Version identifiers describe release state, not visibility or distribution.
New version identifiers must not add audience labels such as `public`, `private`
or `local`. Be My Eyes `1.0-public` remains a narrow legacy exception tied to
already-published standalone package coordinates until its next accepted
material release. Connected Sources advanced to `1.2` on 2026-09-27 and is
no longer covered by this exception; the legacy value does not establish a
naming precedent.

The current independently versioned capabilities are Lifecycle Workspace Router at
1.2, Connected Sources at 1.2, MSL at 5.1, Adaptive Orchestration at 6.3,
Setup at 3.1, Preflight at 2.3 and Be My Eyes at 1.0-public. Adaptive Orchestration 6.3
preserves Delegation-First, the surface-neutral control-root model and Behavioral Fit while adding Commitment Geometry as a separate decision-closure route: high-leverage solution choices can be probed or explored before dependent work scales, only the commitment-bearing delta may be side-routed or up-routed, and objective-linked evidence can reopen the smallest affected boundary. The historical Chat → Work/Codex → Chat loop remains a named first-class profile rather than the mandatory topology. The Astra Strategy Adapter is 1.9 and the GPT-6 Sol/Luna Adapter is 1.6. Model, token-economy, behavior and subagent calibration remains dated and subordinate; Maximum Token Economy is public opt-in only and does not globally demote Astra. MSL's formatting contract remains part of the current 5.1 body and release identity.

Product-specific connector behavior, model names, plans, prices, availability
and other volatile facts must be rechecked before being treated as current.
Historical generations belong to Git history or explicit releases, not the
active semantic tree.

## Mirror synchronization contract

Moon Source is the semantic and versioning authority. After a canonical body
changes, update its supported distribution and mirror only after the canonical
registry and validators pass. Use
python scripts/check_mirror_sync.py for exact SHA-256 equality.

The legacy id chat-work-routing, legacy names Chat–Work Routing Protocol / Chat–Work Router / Chat–Work, old artifact paths, package and mirror are compatibility pointers to adaptive-orchestration; they do not add a second capability record.

The registry does not replace [Credits & Attribution
Ops](../docs/CREDITS_ATTRIBUTION_OPS.md), which governs intellectual lineage,
content custody and immaterial-asset boundaries.

<!-- MOON-SOURCE-PUBLIC-STAMP -->

---

> 🌙 **Moon Source** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Source/blob/main/LICENSING.md) · [Use & attribution](https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md) · [Full source (.zip)](https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip) · Questions, suggestions, or proposals? Feel free to contact me at [LuaHelenaMMC@gmail.com](mailto:LuaHelenaMMC@gmail.com).