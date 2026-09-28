# 🌙 Moon Source

**Governed context for AI: decide what should exist, what governs, what travels, and what stays current.**

AI chat history is not the same thing as governed context. Conversations can retain useful continuity, but they can also accumulate stale facts, competing instructions, private material, unresolved ownership and context that belongs somewhere else.

Moon Source is a public reference architecture for organizing that problem. It starts with the field before the form: understand the situation, identify authority and responsibility, then create only the smallest source, protocol, handoff, skill, registry, archive or operational surface the work actually needs.

This repository is the canonical public body of Moon Source.

> 📦 **Want the whole Moon Source at once?**  
> 🌙⬇️ [**Download the complete repository (.zip)**](https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip)

## Why Moon Source exists

AI context can fail in opposite directions: there may be too little context, or far too much of the wrong kind. The harder failures appear when information is reachable but nobody can explain which source governs it, whether it is still current, who may change it, or what should happen when sources disagree.

Moon Source treats context as an organized field rather than a pile of text. Its job is not to maximize memory. Its job is to make context **legible, proportionate, attributable and maintainable** for people and AI.

The short version:

**field → observation and diagnosis → authority → responsibility → proportional form → operation and transport → feedback, hygiene, lineage and archive**

This is a topology, not a compulsory waterfall. New information can send the work back to observation, authority or responsibility.

Execution choices need proportionate governance too. [Adaptive Orchestration Protocol (AOP)](portables/adaptive-orchestration/README.md) starts from a practical rule: **use each model, surface and unit of reasoning where it actually pays for itself**. It separates the control root, execution surface, model capability, reasoning effort and delegation instead of collapsing them into one prestige choice. Its target is **minimum total work to an accepted state**: cheaper sufficient execution absorbs reducible bulk, stronger cognition is concentrated at real bottlenecks, and repeated context ingestion, retries, tool churn, unnecessary fan-out and surface switching are treated as costs to reduce rather than invisible overhead.

## Start with the problem, not the vocabulary

The split below is architectural rather than merely a download taxonomy. **Portables** are capabilities whose semantic identity is itself portable. **Standalone distribution** is a separate delivery property: a structural component can also be distributed independently without becoming a portable. Connected Sources is the important example below.

### Portable entry points

| If you need to… | Start here |
|---|---|
| Spend AI capability efficiently across roots, surfaces, models, reasoning effort and delegation while minimizing total work to an accepted result | [🧬 Adaptive Orchestration Protocol](portables/adaptive-orchestration/README.md) |
| Carry context across sources and surfaces without losing meaning, provenance or authority | [🧱 Moon Source Language](portables/msl/README.md) |
| Build the smallest useful context for a person or project | [🧭 Setup](portables/setup/README.md) |
| Reconstruct the human task before execution when expression is messy, incomplete or self-correcting | [🛫 Preflight](portables/preflight/README.md) |
| Read communications and artifacts as human scenes while distinguishing observation from inference | [👁️ Be My Eyes](portables/be-my-eyes/README.md) |

### Structural architecture & components

| If you need to… | Start here |
|---|---|
| Decide what a field needs before choosing its durable form | [🏗️ Architecture — Field to Form](ARCHITECTURE.md#field-to-form) |
| Reach living sources while keeping access, authority, freshness, mutation and readback governed | [🔗 Connected Sources](docs/CONNECTED_SOURCES.md#first-use) |
| Retrieve, process, metabolize or promote governed source material | [🔄 Source Operations](docs/SOURCE_OPERATIONS.md) |
| Diagnose stale authority, freshness problems, duplication or contradiction and find the smallest safe corpus repair | [🧹 Source Hygiene](docs/SOURCE_HYGIENE.md) |
| Recover a corpus's semantic topology and repair inherited organization without rebuilding it from scratch | [🧵 Semantic Reweave](docs/SEMANTIC_REWEAVE.md) |
| Project lifecycle, action and provenance onto durable workspace surfaces | [🗂️ Lifecycle Workspace Router](docs/LIFECYCLE_WORKSPACE_ROUTER.md) |
| Preserve authorship, permissions, lineage and evidence as material moves or changes | [🧾 Credits & Attribution Ops](docs/CREDITS_ATTRIBUTION_OPS.md) |
| Turn a stable method into a bounded reusable procedure | [🧩 Procedural Projection](docs/PROCEDURAL_PROJECTION.md) |
| Keep execution bounded, diagnosable and recoverable where possible | [🛡️ Operational Reliability](docs/OPERATIONAL_RELIABILITY.md) |
| Embody a recurring procedure on a concrete execution surface with state, guards and receipts | [🛠️ Operational Devices](docs/OPERATIONAL_DEVICES.md) |
| Use ambiguous or convergent evidence without inflating certainty | [🎚️ Signal Calibration](docs/SIGNAL_CALIBRATION.md) |
| Turn recurring failure into the smallest validated reusable mechanism | [🏭 Failure to Capability — Failure Foundry](docs/FAILURE_FOUNDRY.md) |

## First use

Moon Source is a context architecture, not an application that installs a background service, memory system, connector, model switch or hidden permission. Usually nothing is installed.

If you are a human exploring the repository, choose the smallest route in the map above and open that capability's README. If you give the full repository to an AI, use [`MOON_SOURCE_AI_KERNEL.md`](MOON_SOURCE_AI_KERNEL.md) for AI-side routing. For one concrete need, start with the smallest relevant capability instead of loading the whole repository.

Each public capability has one canonical semantic body. A README may make it easier to browse and a package or website mirror may make it easier to transport, but those surfaces do not create another identity, authority or version.

> **One canonical body, multiple legitimate surfaces.**

A useful first prompt is:

```text
I need help with [describe the real need].
Recommend the smallest Moon Source capability for it.
Do not load the whole repository unless necessary.
Tell me the canonical file, the first action, what happens next,
and any step I must perform manually.
```

Access is not activation. A reachable source is not automatically authoritative, and a successful write is not accepted until the relevant readback succeeds.

## Core principles

- **Field before form.** Do not decide the artifact before understanding the situation.
- **Access is not authority.** Retrieval, connectors and search results do not become governing context merely because AI can reach them.
- **Retrieval is not instruction authority.** Source text may supply data without gaining permission to redirect the task or authorize an action.
- **Materialize proportionately.** Create the smallest durable form that can carry the responsibility without losing provenance or ownership.
- **Freshness and readback matter.** Mutation is incomplete until the relevant state is verified.
- **Different operations have different authority effects.** Retrieve reads; process transforms working material; metabolize integrates a real delta; promote generalizes a proven mechanism.
- **Humans should not have to prompt like machines.** [Preflight](portables/preflight/PREFLIGHT.md) reconstructs intended meaning before execution and escalates guardrails only when consequence requires them.
- **Read the scene, not only the sentence.** [Be My Eyes](portables/be-my-eyes/BE_MY_EYES.md) reconstructs actors, relationship and plausible subtext while keeping observation, inference and overread distinct.
- **Workspace state must not invent authority.** [Lifecycle Workspace Router](docs/LIFECYCLE_WORKSPACE_ROUTER.md) projects lifecycle, action and provenance onto durable surfaces without replacing the source of record.
- **Optimize total work to an accepted state.** [Adaptive Orchestration](portables/adaptive-orchestration/README.md) uses cheaper sufficient execution for reducible bulk, concentrates stronger cognition at real bottlenecks, and treats context churn, retries and unnecessary fan-out as costs rather than free plumbing.

## Public capabilities

Moon Source publishes reusable public capabilities with one canonical semantic body each. Some also support standalone distribution; others live only in the repository because their value depends on the wider architecture.

The authoritative inventory, chronology, status and material-update history lives in the [public capability registry](registry/PUBLIC_CAPABILITIES.md), with a machine-readable contract at [registry/public-capabilities.json](registry/public-capabilities.json).

For standalone packages and human-readable entry points, use the [download hub](DOWNLOADS.md). Connected Sources remains a structural component even though Moon Source also publishes it as a supported standalone distribution. For examples of the architecture applied to fictional everyday situations, see the [application-scenario gallery](examples/application-scenarios/).

## Where Moon Source sits in an AI stack

```mermaid
flowchart TB
    model["Model: reasoning and generation"]
    harness["Agent harness / runtime: actual loops, tool use, execution and state"]
    context["Governed context: sources, authority, freshness, provenance, permissions and continuity"]
    moon["Moon Source: context architecture and governance"]
    model <--> harness
    harness <--> context
    context --- moon
```

This is an orientation model, not a universal stack ontology. Products may combine or split these responsibilities.

Moon Source primarily operates in and around governed context: it helps determine what a harness may trust, retrieve, carry forward, mutate and verify. The [Adaptive Orchestration Protocol (AOP)](portables/adaptive-orchestration/README.md) governs how choices are made across available control roots, execution surfaces, models, reasoning effort and delegated workers; the harness/runtime still performs the actual loops, tool use and execution. RAG, memory stores, MCP/tools and other retrieval or orchestration mechanisms can participate in these layers, but Moon Source is not the model, the harness, the RAG engine or the agent runtime.

## Evidence, boundaries and reuse

Moon Source is deliberately strict about the difference between an artifact existing and a claim being proven.

- [Evidence and Claims](EVIDENCE_AND_CLAIMS.md) defines what current public artifacts support and what remains unproven.
- [Public Boundary](PUBLIC_BOUNDARY.md) defines what is public and what remains reserved.
- [Existing Implementations](docs/EXISTING_IMPLEMENTATIONS.md) maps inspectable artifacts behind current capability statements.
- [Licensing](LICENSING.md) governs reuse: code and automation use **Apache-2.0**; documentation, methods and supported standalone distributions use **CC BY 4.0**, subject to file-level metadata and third-party terms.

A public artifact is not an adoption claim. A tested slice is not proof of a universal runtime. The repository does not claim external adoption, measured impact, enterprise readiness, universal superiority or product-market fit without evidence.

## Repository maintenance

The public repository includes a bounded executable maintenance layer over its validators:

```bash
python scripts/moon_source.py validate
```

Current canonical-to-website mirror state is a separate read-only check:

```bash
python scripts/moon_source.py mirror --check
```

The CLI is repository maintenance tooling. It does not add a public capability, change semantic versioning or replace canonical source contracts.

## Applying Moon Source to an organization

Moon Source itself remains public. Organizations that want the architecture applied to a real context — across existing sources, tools, workflows, authority boundaries, handoffs and maintenance — can work directly with Moon through the professional application surface:

**[Work with Moon →](https://www.luahelena.com.br/moonsource/work-with-moon/?lang=en)**

This is a professional-service bridge, not a claim that Moon Source is a mature enterprise platform. Engagements are scoped to the actual context and retain the evidence, privacy, authority and claim ceilings documented in this repository.

## Recent capability changes

<!-- MOON-SOURCE-CAPABILITY-DIGEST:START -->
- **2026-09-27 — Connected Sources:** Added consumer-scoped context delivery and rehydratable offload of decision-bearing material while preserving source authority boundaries; credited bounded mechanism-level study without copying code or runtime.
- **2026-09-27 — Adaptive Orchestration Protocol:** Canonical identity and paths migrated from Chat–Work Routing Protocol to Adaptive Orchestration Protocol. Version 6.1 and execution semantics remain unchanged under the naming-only rule; old GitHub paths, package and website mirror remain explicit aliases. Astra 1.6 and GPT-6 Sol/Luna 1.3 remain unchanged.
- **2026-09-24 — Preflight:** Normalized the current canonical, package and mirror routes to stable artifact identity; semantic content and capability version remain unchanged.
- **2026-09-24 — Moon Source Setup:** Normalized the current canonical, package and mirror routes to stable artifact identity; semantic content and capability version remain unchanged.
- **2026-09-24 — Moon Source Language:** Normalized the current canonical, package and mirror routes to stable artifact identity; semantic content and capability version remain unchanged.
<!-- MOON-SOURCE-CAPABILITY-DIGEST:END -->

This bounded digest is generated from the unified capability registry. It is not a commit log.

## Repository navigation

| Need | Canonical route |
|---|---|
| Full architecture and Field-to-Form diagnostic | [🏗️ Architecture](ARCHITECTURE.md#field-to-form) |
| AI-side routing through the public corpus | [MOON_SOURCE_AI_KERNEL.md](MOON_SOURCE_AI_KERNEL.md) |
| Definitions and responsibility boundaries | [Terminology](docs/TERMINOLOGY.md) + [Responsibility Map](docs/RESPONSIBILITY_MAP.md) |
| Unified public capability registry | [registry/PUBLIC_CAPABILITIES.md](registry/PUBLIC_CAPABILITIES.md) |
| Versioning, naming and release rules | [Versioning and Releases](docs/VERSIONING_AND_RELEASES.md) + [Repository Naming and Versioning](docs/REPOSITORY_NAMING_AND_VERSIONING.md) |
| Portable publication contract | [Portable Design Contract](docs/PORTABLE_DESIGN_CONTRACT.md) |
| Contributing | [CONTRIBUTING.md](CONTRIBUTING.md) |
| Human-facing website | [luahelena.com.br/moonsource](https://www.luahelena.com.br/moonsource/?lang=en) |
| Moon's broader professional context | [luahelena.com.br/ia](https://www.luahelena.com.br/ia/?lang=en) |

## Related public project

[Moon Cortex](https://github.com/luahelenammc/Moon-Cortex) is a separate, optional applied/system body for domain-shaped modules. It can use Moon Source governance where useful, but it is not part of Moon Source and is not a permanent runtime dependency.

Moon Source was created by Lua Helena Moon Martins Cardoso (Moon). Some materials were developed through an AI-assisted coauthorial process with Áurion. Moon retains final authority.

<!-- MOON-SOURCE-PUBLIC-STAMP -->

---

> 🌙 **Moon Source** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Source/blob/main/LICENSING.md) · [Use & attribution](https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md) · [Full source (.zip)](https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip) · Questions, suggestions, or proposals? Feel free to contact me at [LuaHelenaMMC@gmail.com](mailto:LuaHelenaMMC@gmail.com).
