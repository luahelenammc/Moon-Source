# 🌙 Moon Source

AI chat history is not the same thing as governed context.

A conversation can preserve useful memory, but it can also accumulate stale facts, competing instructions, old decisions, private material, unresolved ownership and context that belongs somewhere else. More text does not automatically create continuity.

Moon Source is a public reference architecture for deciding what context should exist, where authority lives, how it travels, and how it stays current. It starts with the field before the form: understand the situation first, then choose a proportionate source, protocol, handoff, skill, registry, archive or other materialization.

This repository is the canonical public body of Moon Source. Setup, MSL and Chat–Work are public projections of that same architecture. Each is an entry point into a different responsibility, not a separate system.

**Preflight is one of Moon Source's crown-jewel mechanisms:** the adaptive pass where the AI reshapes the task before the task shapes the output. It checks intent, authority, missing facts, risk, destination and proportionate form before deciding whether to ask, route, create or act.

## Start here

Choose the smallest door that matches the problem:

- **I want an AI to understand my context better.** Start with [Moon Source Setup 3.0](portables/setup/MOON_SOURCE_SETUP.md).
- **The request is vague, risky or keeps producing the wrong answer.** Start with [Preflight](docs/PREFLIGHT.md).
- **My sources, memory or handoffs are messy.** Start with [Architecture](ARCHITECTURE.md), [Field to Form](docs/FIELD_TO_FORM.md) and [Source Hygiene](docs/SOURCE_HYGIENE.md).
- **I need AI to reach living material across tools.** Start with [Connected Sources](docs/CONNECTED_SOURCES.md) and the [Responsibility Map](docs/RESPONSIBILITY_MAP.md).

For recurring work, use [MSL 4.3](portables/msl/MSL_4_3.md). For ChatGPT surface and execution routing, use [Chat–Work Routing Protocol V2](portables/chat-work/CHAT_WORK_ROUTING_PROTOCOL_V2.md).

## What problem does it solve?

Moon Source treats context as an organized field rather than a pile of text. A useful context system must identify what is happening, which source or role governs each facet, what deserves materialization, what may be retrieved or changed, and how freshness and readback are handled.

The public architecture loop is:

**field → observation and diagnosis → authority → responsibility → proportional form → operation and transport → feedback, hygiene, lineage and archive**

It is a decision loop, not a compulsory waterfall. A materialization can reveal new facts and send the work back to observation, authority or responsibility.

## Where could it apply?

Moon Source can help organize these kinds of context problems. The wording is intentionally hypothetical: the public repository does not claim sector-specific adoption or measured impact.

| Domain | Possible context problem |
|---|---|
| **Customer service & journeys** | Channels, routing and continuity without making raw conversation history the authority |
| **Health & care** | Sensitive information, team handoffs, current status and proportionate disclosure |
| **Management & operations** | Real workflow, roles, ownership, exceptions and update responsibility |
| **Transparency & audit** | Sources, traceability, evidence classes, versions and claim ceilings |
| **People & learning** | Role-aware onboarding, local language, autonomy and material maintenance |
| **Knowledge & data** | Living documentation, indicators, source freshness and federated memory |
| **Companies** | Process clarity, institutional memory and bounded AI adoption work |
| **Public services** | Citizen guidance, cross-department coordination and transparent handoffs |
| **Third sector** | Network continuity, partner memory and sustainable coordination under turnover |

The [hypothetical application-scenario gallery](examples/application-scenarios/) works through one fictional example in each family. It is explanation, not evidence.

## Public components

Public components are responsibility-bearing methods with canonical files. They are distinct from the three current public portables and do not automatically create a new version.

- [Preflight](docs/PREFLIGHT.md) — adaptive task shaping before execution.
- [Connected Sources](docs/CONNECTED_SOURCES.md) — authority, jurisdiction, retrieval, freshness, mutation and readback for connected sources.
- [Source Hygiene](docs/SOURCE_HYGIENE.md) — bounded diagnosis of stale, duplicated, contradictory or orphaned corpus material.
- [Signal Calibration](docs/SIGNAL_CALIBRATION.md) — bounded working inference from weak, convergent or ambiguous signals.
- [Procedural Projection](docs/PROCEDURAL_PROJECTION.md) — projecting a stable method into a procedure without moving source authority.
- [Credits & Attribution Ops](docs/CREDITS_ATTRIBUTION_OPS.md) — intellectual lineage, content custody and immaterial-asset protection.
- [Operational Devices](docs/OPERATIONAL_DEVICES.md) — bounded embodiments of reusable procedures on concrete surfaces.
- [Operational Reliability](docs/OPERATIONAL_RELIABILITY.md) — diagnosis, failure boundaries, receipts, reversibility and freshness.
- [Failure to Capability — Failure Foundry](docs/FAILURE_FOUNDRY.md) — turning recurring failure into the smallest validated public mechanism.

The complete chronology, public dates, material-update summaries and controlled status values live in the [public registry](registry/PUBLIC_PORTABLES.md). The machine-readable contract is [`registry/public-portables.json`](registry/public-portables.json).

## Recent component changes

<!-- MOON-SOURCE-COMPONENT-DIGEST:START -->
- **2026-08-23 — Preflight:** Promoted adaptive task shaping as a transversal public mechanism for intent, authority, risk, destination and form.
- **2026-08-23 — Operational Reliability:** Added read-only-first diagnosis, failure domains, receipts, reversibility and freshness gates.
- **2026-08-23 — Operational Devices:** Added bounded operational-device contracts for state, guards, failure behavior and receipts.
- **2026-08-23 — Failure to Capability:** Added a bounded failure-to-capability loop for recurring failure without exposing promotion machinery.
- **2026-08-23 — Connected Sources:** Added connector-aware authority, retrieval scope, mutation and readback contracts.
<!-- MOON-SOURCE-COMPONENT-DIGEST:END -->

This is a bounded registry-backed digest, not a commit log. It contains no merge procedure, CI narration or repository hash.

## Public portables and downloads

**Want the whole public architecture offline?**  
[📦 **Download the complete Moon Source repository (.zip)**](https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip)

Or download only the portable you need:

- [🧭 **Moon Source Setup 3.0 (.md)**](https://raw.githubusercontent.com/luahelenammc/Moon-Source/main/portables/setup/MOON_SOURCE_SETUP.md) — adaptive routing for proportionate personal and project AI context.
- [🧱 **Moon Source Language 4.3 (.md)**](https://raw.githubusercontent.com/luahelenammc/Moon-Source/main/portables/msl/MSL_4_3.md) — adaptive structural grammar for context work.
- [🔀 **Chat–Work Routing Protocol V2 (.md)**](https://raw.githubusercontent.com/luahelenammc/Moon-Source/main/portables/chat-work/CHAT_WORK_ROUTING_PROTOCOL_V2.md) — routing across ChatGPT surfaces, models and reasoning effort.

[🗂️ **Open the download hub →**](DOWNLOADS.md) for the standalone AI Kernel, individual files and guidance on which download to choose.

## 🔓 Open licensing

Moon Source is openly reusable under a mixed standard-license model:

- **Code and automation:** [Apache License 2.0](LICENSES/Apache-2.0.txt).
- **Documentation, methods and public portables:** [CC BY 4.0](LICENSES/CC-BY-4.0.txt).
- **Attribution:** preserve Moon Source authorship, applicable notices and material lineage; adaptations should identify changes.
- **Third-party material:** remains subject to its own terms.

See the full [licensing guide](LICENSING.md), [`NOTICE`](NOTICE), [Moon Source Use & Attribution](MOON_SOURCE_USE_AND_ATTRIBUTION.md) and [Credits & Attribution Ops](docs/CREDITS_ATTRIBUTION_OPS.md).

## More entry points

| Situation | Start here | What it helps you do |
|---|---|---|
| You want an AI to understand your context more consistently | [Moon Source Setup 3.0](portables/setup/MOON_SOURCE_SETUP.md) | Infer the smallest useful setup for your need, maturity, destination and privacy boundary |
| A request is vague, high-stakes, destination-sensitive or keeps producing answers to the wrong problem | [Preflight](docs/PREFLIGHT.md) | Shape the task before execution: clarify intent, authority, missing facts, risk, destination and the smallest adequate form |
| An AI needs durable external memory or must reach a governed source through Drive, GitHub or another connector | [Connected Sources](docs/CONNECTED_SOURCES.md) | Resolve source substrate, authority, jurisdiction, freshness, retrieval scope, mutation authority and readback before treating connected material as context |
| A project or knowledge base has scattered sources, unclear ownership or recurring friction | [Architecture](ARCHITECTURE.md) and [Field to form](docs/FIELD_TO_FORM.md) | Inspect the field, identify authority and responsibility, and choose what deserves to become a source, procedure or other form |
| You need a structure for recurring context work, updates or handoffs | [Moon Source Language 4.3](portables/msl/MSL_4_3.md) | Choose a proportionate Markdown-native form for sources, skills, handoffs, packets, protocols, registries and archives |
| Work needs to move between a person, model, thread or project without losing state | [MSL 4.3](portables/msl/MSL_4_3.md) and the [responsibility map](docs/RESPONSIBILITY_MAP.md) | Separate objective, current state, constraints, authority, provenance and next actions |
| You work across ChatGPT surfaces and need to decide where a task belongs | [Chat–Work Routing Protocol V2](portables/chat-work/CHAT_WORK_ROUTING_PROTOCOL_V2.md) | Route a task by surface, model and reasoning effort, with product details bounded by freshness and official references |
| You want to publish, mirror or adapt one of the public materials | [📐 Portable Design Contract](docs/PORTABLE_DESIGN_CONTRACT.md), [🗂️ registry](registry/PUBLIC_PORTABLES.md) and [📚 versioning rules](docs/VERSIONING_AND_RELEASES.md) | Find canonical paths, freshness rules, attribution guidance, mirror rules and release boundaries |
| Intellectual material needs to retain its identity, authorship and lineage as it moves or changes | [🧬 Credits & Attribution Ops](docs/CREDITS_ATTRIBUTION_OPS.md) | Protect content identity and chain of custody across origin, authorship, transformations, permission scope, disclosure boundaries, canonical versions, derivatives, attribution and evidence |
| A stable method needs to become a reusable procedural capability | [🧭 Procedural Projection](docs/PROCEDURAL_PROJECTION.md) | Separate governing source, reusable procedure, triggers, guards, QA and native/fallback surfaces |
| A recurring procedure needs a bounded concrete execution surface | [Operational Devices](docs/OPERATIONAL_DEVICES.md) and [Operational Reliability](docs/OPERATIONAL_RELIABILITY.md) | Embody a procedure with explicit state, guardrails, failure behavior, receipts and recovery |
| Repeated failure keeps generating the same loop | [Failure to Capability — Failure Foundry](docs/FAILURE_FOUNDRY.md) | Preserve the evidence, separate failure domains and forge the smallest validated reusable mechanism |
| A context corpus feels stale, contradictory or bloated | [🧹 Source Hygiene](docs/SOURCE_HYGIENE.md) | Audit authority, freshness, duplication, contradiction, orphaned decisions, provenance and the smallest safe repair |
| You have several weak or ambiguous signals and need a useful interpretation without pretending certainty | [🔭 Signal Calibration](docs/SIGNAL_CALIBRATION.md) | Separate observation, convergence, working inference, meaningful alternatives and the evidence needed to update the read |

## Examples and hypothetical applications

The [examples directory](examples/README.md) contains an experimental synthetic Browser Console Device reference and the [hypothetical application-scenario gallery](examples/application-scenarios/).

Every application scenario is explicitly fictional and didactic. It illustrates how Moon Source could be applied to a common context problem; it is not evidence of external adoption, implementation, measured impact or independent validation. No real patient, client, institution, organization, outcome metric or private corpus is used in the gallery.

## ⚙️ How Moon Source works

Moon Source follows a decision loop:

**field → observation and diagnosis → authority → responsibility → proportional form → operation and transport → feedback, hygiene, lineage and archive**

When the immediate problem is not yet the field's structure but the request itself, begin with [Preflight](docs/PREFLIGHT.md). It is a transversal before-execution gate that may resolve quickly, route into Field to Form or another component, or reroute when the task changes. It is not a mandatory extra stage for every operation.

It is not a compulsory workflow. A materialization can reveal new facts and send the work back to observation, authority or responsibility. The point is to let the situation determine the smallest form that can carry the work without losing provenance, scope or ownership.

Apply the architecture directly through [Architecture](ARCHITECTURE.md), [Field to Form](docs/FIELD_TO_FORM.md), the [Responsibility Map](docs/RESPONSIBILITY_MAP.md) and [Terminology](docs/TERMINOLOGY.md); each includes a practical way to use that layer and routes to the relevant public portable.

## 🔗 Read deeper

- [Existing implementations](docs/EXISTING_IMPLEMENTATIONS.md) maps the public artifacts that actually exist and the evidence class behind them.
- [Evidence and Claims](EVIDENCE_AND_CLAIMS.md) and [Public Boundary](PUBLIC_BOUNDARY.md) define what the public body supports, what it does not establish and what remains private.
- 🛫 [Preflight](docs/PREFLIGHT.md) explains the crown-jewel method for shaping a task before AI execution, including its self-prompt and self-adjusting-prompt metaphors.
- 🔗 [Connected Sources](docs/CONNECTED_SOURCES.md) explains how an AI reaches living external sources, why Google Drive is the ChatGPT document-source reference, when GitHub governs executable facets and how retrieval returns to authority and readback.
- [Portable Design Contract](docs/PORTABLE_DESIGN_CONTRACT.md), the [portable registry](registry/PUBLIC_PORTABLES.md) and [Versioning and Releases](docs/VERSIONING_AND_RELEASES.md) govern canonical paths, mirrors, freshness and releases.
- 🧬 [Credits & Attribution Ops](docs/CREDITS_ATTRIBUTION_OPS.md) is the reusable immaterial-asset protection component for intellectual lineage, content custody, transformations, permission envelopes, disclosure boundaries, derivatives, attribution and evidence.
- 🧭 [Procedural Projection](docs/PROCEDURAL_PROJECTION.md) explains reusable methods without turning them into sources of truth.
- ⚙️ [Operational Devices](docs/OPERATIONAL_DEVICES.md) explains when a procedure deserves a bounded concrete execution surface.
- 🛡️ [Operational Reliability](docs/OPERATIONAL_RELIABILITY.md) keeps execution diagnosable, reversible where possible and honest about partial results.
- 🔧 [Failure to Capability — Failure Foundry](docs/FAILURE_FOUNDRY.md) turns recurring failure into the smallest validated capability without exposing protected machinery.
- 🧪 [Browser Console Device reference](examples/browser-console-device/) demonstrates that layer on a synthetic `localhost` surface; it is experimental and not a current portable.
- 🧹 [Source Hygiene](docs/SOURCE_HYGIENE.md) explains bounded corpus diagnosis and conservative repair.
- 🔭 [Signal Calibration](docs/SIGNAL_CALIBRATION.md) explains how to preserve useful inference without promoting weak signals to fact or flattening them into “we cannot know”.

## 📌 Current baseline

- Public architecture baseline: 2026-08-16; additive public components, operational hardening and licensing updates continued through 2026-08-23; public-legibility, registry and facade hardening continued on 2026-08-24.
- Current structural grammar: MSL 4.3 (`KEEP_MSL_4_3`). Public portables remain Setup 3.0 and Chat–Work 2.0-public.
- Public component chronology and status are tracked separately from portable versions in the [component registry](registry/PUBLIC_PORTABLES.md).
- The current public portable family is tracked in the [portable registry](registry/PUBLIC_PORTABLES.md).
- Human-facing public surface: [luahelena.com.br/moonsource](https://www.luahelena.com.br/moonsource/?lang=en). Professional context: [luahelena.com.br/ia](https://www.luahelena.com.br/ia/?lang=en).
- This repository remains the semantic and versioning authority; the website is a human-facing facade and its downloads are convenience mirrors.

## 🛡️ Evidence, boundary and terms

The public body is built from existing inspectable evidence. It does not manufacture a case study or before-and-after story, and it does not establish external adoption, impact, universal validity, product-market fit, enterprise readiness or a universal standard.

The application-scenario gallery is explicitly hypothetical / fictional / didactic. Its files establish only that explanatory examples exist; they do not establish real implementation, adoption, measured impact, sector validation or independent validation.

Private source corpora, third-party material, deployment state, private resolver and compiler heuristics, detailed reconciliation machinery and enough cross-file detail to reconstruct protected methods remain outside this repository.

Moon Source was created by Lua Helena Moon Martins Cardoso (Moon). Some materials were developed through an AI-assisted coauthorial process with Áurion. Moon retains final authority.

Moon Source is openly reusable under the applicable standard license: software and automation use Apache-2.0; documentation, methods and public portables use CC-BY-4.0. Attribution and provenance remain important, but the repository does not invent a custom license or silently relicense third-party material. See [LICENSING.md](LICENSING.md) for scope, exceptions and the legal ceiling.

<!-- MOON-SOURCE-PUBLIC-STAMP -->

---

> 🌙 **Moon Source** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Source/blob/main/LICENSING.md) · [Use & attribution](https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md) · [Full source (.zip)](https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip)
