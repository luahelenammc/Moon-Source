# Moon Source

Moon Source is a public reference architecture for turning a situated field into context that people and AI can understand, govern, move and update.

It starts with the field: a person, project, team, institution, workflow, knowledge base or changing situation. It helps you observe what is happening, locate authority, map responsibility, choose a proportionate form and keep the result current.

Moon Source becomes useful when context is scattered, authority is unclear, work has to travel between people or AI systems, or one document is being asked to perform several incompatible jobs.

This repository is the canonical public body of the architecture. Its public projections include a guided personal setup, an adaptive structural grammar and a Chat–Work routing protocol. These are working entry points into the same architecture, each exposing a different responsibility.

## What can I use Moon Source for?

| If your situation looks like this | Start here | What the material helps you do |
|---|---|---|
| You want an AI to understand your personal context more consistently | [Moon Source Setup 2.0](portables/setup/MOON_SOURCE_SETUP.md) | Create a guided, reusable personal context source and use it inside the AI tool you already use |
| A project or knowledge base has scattered sources, unclear ownership or recurring friction | [Architecture](ARCHITECTURE.md) and [Field to form](docs/FIELD_TO_FORM.md) | Inspect the field, identify authority and responsibility, and choose what deserves to become a source, procedure or other form |
| You need a structure for recurring context work, updates or handoffs | [Moon Source Language 4.3](portables/msl/MSL_4_3.md) | Choose a proportionate Markdown-native form for sources, skills, handoffs, packets, protocols, registries and archives |
| Work needs to move between a person, model, thread or project without losing state | [MSL 4.3](portables/msl/MSL_4_3.md) and the [responsibility map](docs/RESPONSIBILITY_MAP.md) | Separate objective, current state, constraints, authority, provenance and next actions |
| You work across ChatGPT surfaces and need to decide where a task belongs | [Chat–Work Routing Protocol V2](portables/chat-work/CHAT_WORK_ROUTING_PROTOCOL_V2.md) | Route a task by surface, model and reasoning effort, with date-sensitive product details clearly bounded |
| You want to publish, mirror or adapt one of the public materials | [Portable Design Contract](docs/PORTABLE_DESIGN_CONTRACT.md), [registry](registry/PUBLIC_PORTABLES.md) and [versioning rules](docs/VERSIONING_AND_RELEASES.md) | Find canonical paths, freshness rules, attribution requirements, mirror rules and release boundaries |

## How the architecture fits together

Moon Source follows a decision topology:

**field → observation and diagnosis → authority → topology and responsibility → proportional materialization → operation and transport → feedback, hygiene and archive**

This is a loop of decisions, not a compulsory workflow. A materialization can reveal new facts and send the work back to observation, authority or topology.

## Architecture map

The table below names the public components by the responsibility they carry. The links lead to the explanation or usable projection for each one.

| Component or layer | Public responsibility | Public entrypoint |
|---|---|---|
| Field | Describe the situation before reducing it to a document type | [Field to form](docs/FIELD_TO_FORM.md) and [Field](ARCHITECTURE.md#1-field) |
| Observation and diagnosis | Gather signal, friction, freshness, contradiction, risk and missing context | [Observation and diagnosis](ARCHITECTURE.md#2-observation-and-diagnosis) |
| Source and living source | Hold governed, updateable context with scope, authority, ownership and freshness | [Jurisdiction and authority](ARCHITECTURE.md#3-jurisdiction-and-authority) and [Responsibility map](docs/RESPONSIBILITY_MAP.md) |
| Project, procedure, skill and task | Give work a boundary, a reusable operation and a concrete next step | [Responsibility map](docs/RESPONSIBILITY_MAP.md) |
| Handoff, packet, capsule and bridge | Move objective, state, limits and provenance across people, models, threads or systems | [Operation and transport](ARCHITECTURE.md#6-operation-and-transport) and [MSL 4.3](portables/msl/MSL_4_3.md) |
| Protocol | Define repeatable operating rules, boundaries and acceptance conditions | [Chat–Work Routing Protocol V2](portables/chat-work/CHAT_WORK_ROUTING_PROTOCOL_V2.md) |
| Ledger, registry and archive | Track decisions, identities, versions, checkpoints and lineage while preserving the boundary between active state and history | [Public registry](registry/PUBLIC_PORTABLES.md), [Versioning and releases](docs/VERSIONING_AND_RELEASES.md) and [Feedback, hygiene and archive](ARCHITECTURE.md#7-feedback-hygiene-and-archive) |
| Runtime | Execute a bounded operation when real callable capacity and observable state exist | [Responsibility map](docs/RESPONSIBILITY_MAP.md) and [Evidence and claims](EVIDENCE_AND_CLAIMS.md) |
| MSL | Provide the adaptive Markdown-native grammar that selects proportionate form and preserves structural hygiene | [MSL 4.3 portable](portables/msl/MSL_4_3.md) and [MSL portable guide](portables/msl/README.md) |
| Public surface | Explain, route or distribute public material for human readers | [Public implementation map](docs/EXISTING_IMPLEMENTATIONS.md), [Moon Source website](https://www.luahelena.com.br/moonsource/?lang=en) and [professional context](https://www.luahelena.com.br/ia/?lang=en) |

## Public projections and entry points

The public family is organized by responsibility. You can use one projection on its own or combine several when the field requires it.

| Public projection | Useful when | What it gives you | Read |
|---|---|---|---|
| Moon Source Setup 2.0 | You need a practical personal starting point | A guided way to create reusable personal AI context | [Setup portable](portables/setup/MOON_SOURCE_SETUP.md) · [guide](portables/setup/README.md) |
| Moon Source Language 4.3 | You maintain recurring projects, governed sources or context systems | An adaptive grammar for choosing structure, continuity and transport | [MSL portable](portables/msl/MSL_4_3.md) · [guide](portables/msl/README.md) |
| Chat–Work Routing Protocol V2 | You use ChatGPT across conversational and sustained execution surfaces | A protocol for separating surface, model and reasoning-effort decisions | [Routing portable](portables/chat-work/CHAT_WORK_ROUTING_PROTOCOL_V2.md) · [guide](portables/chat-work/README.md) |
| Moon Source repository | You want to inspect the architecture, evidence, boundaries and canonical files | The public reference and versioning body | [Repository map](docs/EXISTING_IMPLEMENTATIONS.md) · [registry](registry/PUBLIC_PORTABLES.md) |
| Moon Source public surface | You want a human-facing explanation and convenient paths into the family | A public portal for orientation and access | [luahelena.com.br/moonsource](https://www.luahelena.com.br/moonsource/?lang=en) |
| Moon's professional context | You want to understand the professional work around context architecture and AI adoption | A separate professional surface with its own scope and claims | [luahelena.com.br/ia](https://www.luahelena.com.br/ia/?lang=en) |

## Read next

- [Architecture](ARCHITECTURE.md) explains the field-to-form topology in full.
- [Responsibility map](docs/RESPONSIBILITY_MAP.md) explains what each object is responsible for.
- [Terminology](docs/TERMINOLOGY.md) translates internal language into public language.
- [Existing implementations](docs/EXISTING_IMPLEMENTATIONS.md) maps the public artifacts and their evidence class.
- [Portable Design Contract](docs/PORTABLE_DESIGN_CONTRACT.md) explains how a public portable remains independently readable and canonical.
- [Public boundary](PUBLIC_BOUNDARY.md) and [Evidence and claims](EVIDENCE_AND_CLAIMS.md) define the disclosure and claim ceiling.
- [Attribution and lineage](ATTRIBUTION_AND_LINEAGE.md) records authorship and historical relation.

## Current baseline

- Public architecture baseline: 2026-08-16.
- Current structural grammar: MSL 4.3.
- MSL verdict: KEEP_MSL_4_3.
- Public portables: Setup 2.0, MSL 4.3 and Chat–Work Routing Protocol V2 2.0-public.
- Canonical repository: [luahelenammc/Moon-Source](https://github.com/luahelenammc/Moon-Source).
- Human-facing public surface: [luahelena.com.br/moonsource](https://www.luahelena.com.br/moonsource/?lang=en).
- Professional context: [luahelena.com.br/ia](https://www.luahelena.com.br/ia/?lang=en).
- Website downloads are convenience mirrors. The repository remains the semantic and versioning source.

## Evidence and public boundary

The public body documents architecture, terminology, interfaces, versioning, evidence classes and published portables. It is built from existing evidence and deliberately does not manufacture a case study or before-and-after story.

Private source corpora, third-party material, deployment state, full resolver and compiler heuristics, detailed reconciliation machinery and enough cross-file detail to reconstruct protected methods remain outside this repository.

The public body supports claims about the published artifacts and the public reference architecture. It does not establish external adoption, impact, universal validity, product-market fit, enterprise readiness or MSL 5. See [Evidence and claims](EVIDENCE_AND_CLAIMS.md) for the full claim map.

## Authorship, attribution and license

Moon Source was created by Lua Helena Moon Martins Cardoso (Moon). Some materials were developed through an AI-assisted coauthorial process with Áurion. Moon retains final authority. See [Attribution and lineage](ATTRIBUTION_AND_LINEAGE.md).

Public portables retain their own attribution and usage language. No repository-wide open-source license is ratified in this baseline, so reuse, adaptation and commercial rights should not be inferred beyond the terms stated in each artifact.
