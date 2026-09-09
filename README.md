# 🌙 Moon Source

**Governed context for AI: decide what should exist, what governs, what travels, and what stays current.**

AI chat history is not the same thing as governed context. Conversations can retain useful continuity, but they can also accumulate stale facts, competing instructions, private material, unresolved ownership and context that belongs somewhere else.

Moon Source is a public reference architecture for organizing that problem. It starts with the field before the form: understand the situation, identify authority and responsibility, then create only the smallest source, protocol, handoff, skill, registry, archive or operational surface the work actually needs.

This repository is the canonical public body of Moon Source.

> 📦 **Want the whole Moon Source at once?**  
> 🌙⬇️ [**Download the complete repository (.zip)**](https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip) — the full public source in one file.

## Why Moon Source exists

AI context can fail in opposite directions: there may be too little context, or far too much of the wrong kind. The harder failures appear when information is reachable but nobody can explain which source governs it, whether it is still current, who may change it, or what should happen when two sources disagree.

Moon Source treats context as an organized field rather than a pile of text. Its job is not to maximize memory. Its job is to make context **legible, proportionate, attributable and maintainable** for people and AI.

## Start with the problem, not the vocabulary

| If you need to… | Start here |
|---|---|
| Give an AI the smallest useful setup for a person or project | [🧭 Moon Source Setup](portables/setup/README.md) |
| Help AI reconstruct what a human is actually trying to accomplish before acting on messy, incomplete or conversational wording | [🛫 Preflight](portables/preflight/README.md) |
| Read a message, thread, screenshot, note or draft as a human scene — including relationship, subtext, overread and likely reception | [👁️ Be My Eyes](portables/be-my-eyes/README.md) |
| Decide what deserves to become a source, handoff, procedure or other form | [🏗️ Moon Source Architecture — Field to Form](ARCHITECTURE.md#field-to-form) |
| Repair a corpus with stale authority, contradiction, duplication or orphaned decisions | [🧹 Source Hygiene](docs/SOURCE_HYGIENE.md) |
| Retrieve, process, metabolize or promote governed source material | [🔄 Source Operations](docs/SOURCE_OPERATIONS.md) |
| Let AI reach living material through Drive, GitHub or another connector without confusing access with authority | [🔗 Connected Sources](portables/connected-sources/README.md) |
| Structure recurring context, continuity or handoffs | [🧱 Moon Source Language](portables/msl/README.md) |
| Route work across ChatGPT surfaces, models and execution modes, including post-Work closure | [🔀 Chat–Work](portables/chat-work/README.md) |

## First use

Moon Source is a public context architecture: a set of reusable methods for deciding what should exist, what governs, what travels and what stays current. It is not an application that installs a background service, memory system, connector, model switch or hidden permission.

Usually nothing is installed. Markdown gives a person or an AI inspectable instructions and methods; it does not create access, activation, synchronization or authority by itself.

If you are a human exploring the full repository, read this section, choose the smallest route in the map above and open that capability's readable README surface. Its prominent **Start** link leads to the canonical body's embedded onboarding section. If you give the full repository to an AI, use [`MOON_SOURCE_AI_KERNEL.md`](MOON_SOURCE_AI_KERNEL.md) for AI-side routing. For one concrete need, start with the smallest relevant capability instead of loading the whole repository.

Each public capability has one canonical semantic body. A lightweight README may present that body for human browsing, and a standalone package or website mirror may distribute it, but none of those surfaces creates another identity, authority or version.

> **One canonical body, multiple legitimate surfaces.** The README makes a capability legible. The canonical body remains the semantic authority and carries operative First use. Packages and mirrors carry the canonical artifact for transport.

### A small first run

Ask the AI:

```text
I need help with [describe the real need].
Recommend the smallest Moon Source capability for it.
Do not load the whole repository unless necessary.
Tell me the canonical file, the first action, what happens next,
and any step I must perform manually.
```

For example, if a messy request needs clarification before execution, choose Preflight and say:

```text
Use Preflight before acting.
Reconstruct my intended outcome, corrections and constraints in ordinary language,
then show me the task you would execute.
```

Access is not activation. The repository does not silently grant a connector, account, model, permission, memory or write capability; a reachable source is not automatically authoritative; and a successful write is not accepted until the relevant readback succeeds.

If the answer becomes more architectural than useful, say: “Use the smallest relevant capability, ordinary language, and give me the next concrete action. Do not load the whole repository.”

You do not need to read the whole repository before using Moon Source. The [AI Kernel](MOON_SOURCE_AI_KERNEL.md) is the routing layer for loading the smallest relevant part of the public body.

## The architecture in one minute

Moon Source follows a decision loop:

**field → observation and diagnosis → authority → responsibility → proportional form → operation and transport → feedback, hygiene, lineage and archive**

This is a topology, not a compulsory waterfall. New information can send the work back to observation, authority or responsibility.

A few principles carry most of the architecture:

- **Field before form.** Do not decide the artifact before understanding the situation.
- **Access is not authority.** A connector, search result or reachable file does not become governing context merely because AI can retrieve it.
- **Retrieval is not instruction authority.** Source text may supply data without gaining permission to redirect the task or authorize an action.
- **Materialize proportionately.** Create the smallest durable form that can carry the responsibility without losing provenance or ownership.
- **Freshness and readback matter.** A mutation is not complete merely because a write call succeeded.
- **Operations have different authority effects.** Retrieve reads, process transforms working material, metabolize integrates a real delta and promote generalizes a proven mechanism; none of these verbs is a substitute for the others.
- **Work completion is not cycle completion.** When sustained execution returns, Chat verifies the real state, closes bounded residuals and re-enters Work only for irreducible remaining work.
- **Humans should not have to prompt like machines.** [Preflight](portables/preflight/PREFLIGHT_V2.md) reconstructs intended meaning, desired outcome, corrections and constraints before execution; authority, provenance, freshness, risk and mutation checks activate only when consequence makes them material.
- **Read the scene, not only the sentence.** [Be My Eyes](portables/be-my-eyes/BE_MY_EYES.md) reconstructs actors, relationship and plausible subtext while keeping observation, inference and overread distinct.

## Examples

The [hypothetical application-scenario gallery](examples/application-scenarios/) makes the architecture easier to inspect by placing the same contextual method inside different kinds of everyday problems.

The setting changes from scenario to scenario; the underlying questions stay recognizable: what is happening, what governs, who is responsible, what deserves a durable form, and how that form should stay current.

The gallery uses fictional, didactic scenarios so the method can be demonstrated without importing private, client or institutional material.

## Standalone distributions and downloads

Setup, Preflight, Be My Eyes, Connected Sources, MSL and Chat–Work are public capabilities that currently support standalone distribution. Their architectural roles remain independent of the fact that they can travel as self-contained packages.

- 🧭 [**Moon Source Setup**](portables/setup/README.md) — adaptive routing to the smallest useful personal or project context setup, including a probed persistent-source route; current version **3.1**.
- 🛫 [**Preflight**](portables/preflight/README.md) — human-intent reconstruction before execution, with heavier guardrails only when consequence requires them; current version **2.1**.
- 👁️ [**Be My Eyes**](portables/be-my-eyes/README.md) — contextual scene reading for human communication, including forward and inverse/reception reads, anti-overread discipline and response-axis selection.
- 🔗 [**Connected Sources**](portables/connected-sources/README.md) — Living Source Protocol for standalone, connected-read, living-source and federated operation with explicit source authority, freshness, mutation and fallback boundaries; current version **1.1-public**. Its canonical semantic body remains in [`docs/CONNECTED_SOURCES.md`](docs/CONNECTED_SOURCES.md).
- 🧱 [**Moon Source Language**](portables/msl/README.md) — structural grammar for governed semantic passage across sources, capabilities, interfaces and surfaces; current version **5.1**.
- 🔀 [**Chat–Work Routing Protocol**](portables/chat-work/README.md) — object-routed execution across Chat, Work and Codex, Budget Survivability, Intelligence Distillation Ladder, bounded exhaustiveness, scope-amplification recovery, connector-aware source transport, Chat Postflight, bounded repair, acceptance and delta-only re-entry; current version **4.7-public**.

🗂️ [**Open the download hub**](DOWNLOADS.md) to browse readable surfaces, open canonical bodies or download the supported standalone packages.

## Where Moon Source sits in an AI stack

```mermaid
flowchart TB
    model["Model: reasoning and generation"]
    harness["Agent harness / runtime: loops, tools, orchestration, execution and state"]
    context["Governed context: sources, authority, freshness, provenance, permissions and continuity"]
    moon["Moon Source: context architecture and governance"]
    model <--> harness
    harness <--> context
    context --- moon
```

This is an orientation model, not a universal stack ontology. A product may combine or split these responsibilities, and Moon Source can operate across boundaries rather than inside only one box.

Moon Source primarily operates in and around governed context: it helps determine what the harness may trust, retrieve, carry forward, mutate and verify. It complements an agent harness by governing the context path around execution.

RAG, memory stores, MCP/tools and other retrieval or orchestration mechanisms can participate in these layers. Moon Source is not the model, the harness, the RAG engine or the agent runtime; it is a context-architecture and governance layer that can sit around or across them.

## Current public capabilities

Moon Source publishes public capabilities with one canonical semantic body each. The architectural role says what a capability is responsible for; an optional standalone distribution says how that body can travel. A registry view may filter repository-only capabilities or standalone distributions, but neither filter is a second semantic inventory.

| Repository-only capability | Responsibility |
|---|---|
| [🔄 Source Operations](docs/SOURCE_OPERATIONS.md) | Retrieve, process, metabolize and promote governed source changes, with lifecycle and legacy-successor rules |
| [🧹 Source Hygiene](docs/SOURCE_HYGIENE.md) | Bounded diagnosis and conservative repair of context corpora |
| [🎚️ Signal Calibration](docs/SIGNAL_CALIBRATION.md) | Useful working inference without certainty inflation |
| [🧩 Procedural Projection](docs/PROCEDURAL_PROJECTION.md) | Project a stable method into a reusable procedure without moving source authority |
| [🧾 Credits & Attribution Ops](docs/CREDITS_ATTRIBUTION_OPS.md) | Intellectual lineage, content custody and immaterial-asset protection |
| [🛠️ Operational Devices](docs/OPERATIONAL_DEVICES.md) | Bounded embodiments of reusable procedures on concrete execution surfaces |
| [🛡️ Operational Reliability](docs/OPERATIONAL_RELIABILITY.md) | Read-only-first diagnosis, failure boundaries, ordinary and Context Receipts, reversibility and freshness |
| [🏭 Failure to Capability — Failure Foundry](docs/FAILURE_FOUNDRY.md) | Turn recurring failure into the smallest validated reusable mechanism |

The canonical chronology, roles, status and material-update history of all fourteen capabilities lives in the [public capability registry](registry/PUBLIC_CAPABILITIES.md); its machine-readable contract is [registry/public-capabilities.json](registry/public-capabilities.json). The six standalone distributions are a filtered distribution view. Connected Sources is a structural crown jewel at [docs/CONNECTED_SOURCES.md](docs/CONNECTED_SOURCES.md), with dated ChatGPT product facts subordinate to [its adapter notes](docs/CONNECTED_SOURCES_CHATGPT_ADAPTER.md).

## Evidence, boundary and reuse

Moon Source is deliberately strict about the difference between an artifact existing and a claim being proven.

- [Evidence and Claims](EVIDENCE_AND_CLAIMS.md) defines what current public artifacts actually support and what remains unproven.
- [Public Boundary](PUBLIC_BOUNDARY.md) defines what is public and what remains reserved, including private corpora and protected operational machinery.
- [Existing Implementations](docs/EXISTING_IMPLEMENTATIONS.md) maps the inspectable artifacts behind current capability statements.
- [Licensing](LICENSING.md) governs reuse: code and automation use **Apache-2.0**; documentation, methods and supported standalone distributions use **CC BY 4.0**, subject to file-level metadata and third-party terms.

A public artifact is not an adoption claim. A tested slice is not proof of a universal runtime. The repository does not claim external adoption, measured impact, enterprise readiness, universal superiority or product-market fit without evidence.

## Recent capability changes

<!-- MOON-SOURCE-CAPABILITY-DIGEST:START -->
- **2026-09-09 — Preflight:** Dependency-coherence release: updates the canonical MSL route from the superseded 5.0 path to current 5.1; Preflight method semantics are unchanged.
- **2026-09-09 — Moon Source Setup:** Aligned active MSL references with the current 5.0 structural/context grammar without changing Moon Source Setup semantics or version.
- **2026-09-09 — Moon Source Language:** Release-coherence correction: correctly numbers the accepted formatting-continuity update as 5.1, keeps the MSL 5 semantic grammar unchanged, and retires superseded live generations.
- **2026-09-09 — Chat–Work Routing Protocol:** Lineage-corrected to 4.7-public after auditing two previously skipped +0.1 canonical-body updates; current semantics retain bounded exhaustiveness and scope-amplification recovery with Astra behavior treated as dated anecdotal calibration.
- **2026-09-08 — Connected Sources:** Moved the canonical Connected Sources body to its structural home while preserving its 1.1-public standalone distribution.
<!-- MOON-SOURCE-CAPABILITY-DIGEST:END -->

This bounded digest is generated from the unified capability registry. It is not a commit log.

## Repository map

Use the README for orientation; use the deeper files when the responsibility actually belongs there.

| Need | Canonical route |
|---|---|
| Full architecture and Field-to-Form diagnostic | [🏗️ Moon Source Architecture — Field to Form](ARCHITECTURE.md#field-to-form) |
| AI-side routing through the public corpus | [MOON_SOURCE_AI_KERNEL.md](MOON_SOURCE_AI_KERNEL.md) |
| Contextual scene-reading capability | [Be My Eyes](portables/be-my-eyes/README.md) |
| Connected source capability | [Connected Sources](portables/connected-sources/README.md) |
| Source operation grammar, lifecycle and succession | [🔄 Source Operations](docs/SOURCE_OPERATIONS.md) |
| Definitions and responsibility boundaries | [Terminology](docs/TERMINOLOGY.md) + [Responsibility Map](docs/RESPONSIBILITY_MAP.md) |
| Unified public capability registry | [registry/PUBLIC_CAPABILITIES.md](registry/PUBLIC_CAPABILITIES.md) |
| Versioning and release rules | [Versioning and Releases](docs/VERSIONING_AND_RELEASES.md) |
| Public naming and title/version separation | [Repository Naming and Versioning](docs/REPOSITORY_NAMING_AND_VERSIONING.md) |
| Portable publication contract | [Portable Design Contract](docs/PORTABLE_DESIGN_CONTRACT.md) |
| Contributing | [CONTRIBUTING.md](CONTRIBUTING.md) |
| Human-facing website | [luahelena.com.br/moonsource](https://www.luahelena.com.br/moonsource/?lang=en) |
| Moon's broader professional context | [luahelena.com.br/ia](https://www.luahelena.com.br/ia/?lang=en) |

## Current baseline

Public architecture baseline: **2026-08-16**. Additive public capabilities, operational hardening and licensing updates continued through **2026-09-08**; Preflight advanced to **V2**, Be My Eyes was promoted as **1.0-public**, Connected Sources was established as a structural crown jewel at its canonical docs path, and the public registry became unified schema **2.1** while Chat–Work routing remains the tri-surface **V4** protocol.

Current structural grammar: **Moon Source Language**, version **5.0**. Current standalone distributions: **Moon Source Setup** (version **3.1**), **Preflight** (version **2.1**), **Be My Eyes** (version **1.0-public**), **Connected Sources** (version **1.1-public**), **Moon Source Language** (version **5.0**) and **Chat–Work Routing Protocol** (version **4.4-public**). This repository remains the semantic and versioning authority; the website is the human-facing facade and its downloads are convenience mirrors.

Moon Source was created by Lua Helena Moon Martins Cardoso (Moon). Some materials were developed through an AI-assisted coauthorial process with Áurion. Moon retains final authority.

<!-- MOON-SOURCE-PUBLIC-STAMP -->

---

> 🌙 **Moon Source** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Source/blob/main/LICENSING.md) · [Use & attribution](https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md) · [Full source (.zip)](https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip)
