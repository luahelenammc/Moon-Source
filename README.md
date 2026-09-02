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
| Give an AI the smallest useful setup for a person or project | [Moon Source Setup 3.0](portables/setup/MOON_SOURCE_SETUP.md) |
| Shape an ambiguous, risky or destination-sensitive request before execution | [Preflight](docs/PREFLIGHT.md) |
| Decide what deserves to become a source, handoff, procedure or other form | [Architecture](ARCHITECTURE.md) + [Field to Form](docs/FIELD_TO_FORM.md) |
| Repair a corpus with stale authority, contradiction, duplication or orphaned decisions | [Source Hygiene](docs/SOURCE_HYGIENE.md) |
| Let AI reach living material through Drive, GitHub or another connector without confusing access with authority | [Connected Sources](docs/CONNECTED_SOURCES.md) |
| Structure recurring context, continuity or handoffs | [MSL 4.3](portables/msl/MSL_4_3.md) + [Responsibility Map](docs/RESPONSIBILITY_MAP.md) |
| Route work across ChatGPT surfaces, models and execution modes, including post-Work closure | [Chat–Work Routing Protocol V3](portables/chat-work/CHAT_WORK_ROUTING_PROTOCOL_V3.md) |

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
- **Work completion is not cycle completion.** When sustained execution returns, Chat verifies the real state, closes bounded residuals and re-enters Work only for irreducible remaining work.
- **Preflight can happen before any of this.** One of Moon Source's crown-jewel mechanisms reshapes the task itself by checking intent, authority, missing facts, risk, destination and proportionate form before execution.

## Examples

The [hypothetical application-scenario gallery](examples/application-scenarios/) makes the architecture easier to inspect by placing the same contextual method inside different kinds of everyday problems.

The setting changes from scenario to scenario; the underlying questions stay recognizable: what is happening, what governs, who is responsible, what deserves a durable form, and how that form should stay current.

The gallery uses fictional, didactic scenarios so the method can be demonstrated without importing private, client or institutional material.

## Public portables and downloads

Setup, MSL and Chat–Work are separately versioned public projections of the architecture, not separate systems.

- 🧭 [**Moon Source Setup 3.0**](portables/setup/MOON_SOURCE_SETUP.md) — adaptive routing to the smallest useful personal or project context setup.
- 🧱 [**Moon Source Language 4.3**](portables/msl/MSL_4_3.md) — structural grammar for proportionate sources, handoffs, packets, protocols, registries and archives.
- 🔀 [**Chat–Work Routing Protocol V3**](portables/chat-work/CHAT_WORK_ROUTING_PROTOCOL_V3.md) — closed-loop routing across conversational reasoning, sustained execution, Chat Postflight, bounded repair, acceptance and re-entry.

🗂️ [**Open the download hub**](DOWNLOADS.md) for the individual public portables.

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

## Current public components

Public components are responsibility-bearing methods with canonical files. They are not automatically portables and do not create a version bump merely by being updated.

| Component | Responsibility |
|---|---|
| [Preflight](docs/PREFLIGHT.md) | Adaptive task shaping before execution |
| [Connected Sources](docs/CONNECTED_SOURCES.md) | Source/data and instruction authority, jurisdiction, freshness, retrieval, mutation boundaries and readback for connected sources |
| [Source Hygiene](docs/SOURCE_HYGIENE.md) | Bounded diagnosis and conservative repair of context corpora |
| [Signal Calibration](docs/SIGNAL_CALIBRATION.md) | Useful working inference without certainty inflation |
| [Procedural Projection](docs/PROCEDURAL_PROJECTION.md) | Project a stable method into a reusable procedure without moving source authority |
| [Credits & Attribution Ops](docs/CREDITS_ATTRIBUTION_OPS.md) | Intellectual lineage, content custody and immaterial-asset protection |
| [Operational Devices](docs/OPERATIONAL_DEVICES.md) | Bounded embodiments of reusable procedures on concrete execution surfaces |
| [Operational Reliability](docs/OPERATIONAL_RELIABILITY.md) | Read-only-first diagnosis, failure boundaries, ordinary and Context Receipts, reversibility and freshness |
| [Failure to Capability — Failure Foundry](docs/FAILURE_FOUNDRY.md) | Turn recurring failure into the smallest validated reusable mechanism |

The canonical chronology, status and material-update history of these components lives in the [public registry](registry/PUBLIC_PORTABLES.md); its machine-readable contract is [`registry/public-portables.json`](registry/public-portables.json).

## Evidence, boundary and reuse

Moon Source is deliberately strict about the difference between an artifact existing and a claim being proven.

- [Evidence and Claims](EVIDENCE_AND_CLAIMS.md) defines what current public artifacts actually support and what remains unproven.
- [Public Boundary](PUBLIC_BOUNDARY.md) defines what is public and what remains reserved, including private corpora and protected operational machinery.
- [Existing Implementations](docs/EXISTING_IMPLEMENTATIONS.md) maps the inspectable artifacts behind current capability statements.
- [Licensing](LICENSING.md) governs reuse: code and automation use **Apache-2.0**; documentation, methods and public portables use **CC BY 4.0**, subject to file-level metadata and third-party terms.

A public artifact is not an adoption claim. A tested slice is not proof of a universal runtime. The repository does not claim external adoption, measured impact, enterprise readiness, universal superiority or product-market fit without evidence.

## Recent component changes

<!-- MOON-SOURCE-COMPONENT-DIGEST:START -->
- **2026-08-26 — Operational Reliability:** Added lightweight, materiality-triggered Context Receipts for context-path evidence alongside ordinary operational receipts.
- **2026-08-26 — Connected Sources:** Separated source/data authority from instruction authority, added indirect-instruction failure handling and named proportional progressive loading.
- **2026-08-23 — Preflight:** Promoted adaptive task shaping as a transversal public mechanism for intent, authority, risk, destination and form.
- **2026-08-23 — Operational Devices:** Added bounded operational-device contracts for state, guards, failure behavior and receipts.
- **2026-08-23 — Failure to Capability:** Added a bounded failure-to-capability loop for recurring failure without exposing promotion machinery.
<!-- MOON-SOURCE-COMPONENT-DIGEST:END -->

This bounded digest is generated from the component registry. It is not a commit log.

## Repository map

Use the README for orientation; use the deeper files when the responsibility actually belongs there.

| Need | Canonical route |
|---|---|
| Full architecture | [ARCHITECTURE.md](ARCHITECTURE.md) |
| AI-side routing through the public corpus | [MOON_SOURCE_AI_KERNEL.md](MOON_SOURCE_AI_KERNEL.md) |
| Definitions and responsibility boundaries | [Terminology](docs/TERMINOLOGY.md) + [Responsibility Map](docs/RESPONSIBILITY_MAP.md) |
| Public components and portable registry | [registry/PUBLIC_PORTABLES.md](registry/PUBLIC_PORTABLES.md) |
| Versioning and release rules | [Versioning and Releases](docs/VERSIONING_AND_RELEASES.md) |
| Portable publication contract | [Portable Design Contract](docs/PORTABLE_DESIGN_CONTRACT.md) |
| Contributing | [CONTRIBUTING.md](CONTRIBUTING.md) |
| Human-facing website | [luahelena.com.br/moonsource](https://www.luahelena.com.br/moonsource/?lang=en) |
| Moon's broader professional context | [luahelena.com.br/ia](https://www.luahelena.com.br/ia/?lang=en) |

## Current baseline

Public architecture baseline: **2026-08-16**. Additive public components, operational hardening and licensing updates continued through **2026-08-26**; Chat–Work routing advanced to the closed-loop **V3** protocol on **2026-09-02**.

Current structural grammar: **MSL 4.3**. Current public portables: **Setup 3.0**, **MSL 4.3** and **Chat–Work 3.0-public**. This repository remains the semantic and versioning authority; the website is the human-facing facade and its downloads are convenience mirrors.

Moon Source was created by Lua Helena Moon Martins Cardoso (Moon). Some materials were developed through an AI-assisted coauthorial process with Áurion. Moon retains final authority.

<!-- MOON-SOURCE-PUBLIC-STAMP -->

---

> 🌙 **Moon Source** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Source/blob/main/LICENSING.md) · [Use & attribution](https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md) · [Full source (.zip)](https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip)
