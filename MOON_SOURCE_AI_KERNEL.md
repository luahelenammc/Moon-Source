# Moon Source AI Kernel

Use this file when an AI system receives the full Moon Source repository, the repository ZIP, or a subset of its public files.

This is the public boot contract for operating Moon Source. It tells an AI how to read the repository, which files govern which decisions, what to load for a given task, and what not to infer.

It is subordinate to the AI platform's higher-order instructions, safety rules and the user's current request. It does not grant permissions beyond the terms stated elsewhere in this repository.

## 1. Boot sequence

If you received the full repository or ZIP:

1. Read this file first.
2. Read `README.md` for orientation and public entry points.
3. Identify the user's actual task before loading more files.
4. Load only the smallest set of Moon Source modules that can answer or execute that task.
5. Use the authority map below when files overlap.
6. Preserve the distinction between current state, historical material, public claims and private/non-disclosed machinery.
7. If the task changes, re-route rather than carrying every previously loaded module forward by default.

Do not treat "read the whole repository" as the default operating mode. More context is not automatically better context.

## 2. Authority map

Use each file for the responsibility it actually owns:

- `README.md` — orientation, public entry points and top-level routing.
- `MOON_SOURCE_AI_KERNEL.md` — AI boot, loading and operating rules for the public repository.
- `ARCHITECTURE.md` — public Moon Source architecture and field-to-form topology.
- `docs/FIELD_TO_FORM.md` — deciding what should exist before choosing a container or artifact type.
- `docs/RESPONSIBILITY_MAP.md` — separating responsibilities, ownership, authority and transport between objects.
- `docs/TERMINOLOGY.md` — responsibility-first translation between ordinary language and Moon Source vocabulary.
- `docs/CREDITS_ATTRIBUTION_OPS.md` — intellectual-lineage, content-custody and immaterial-asset protection across identity, authorship, canonicality, transformations, permission envelopes, disclosure boundaries, derivatives, attribution and evidence.
- `docs/PROCEDURAL_PROJECTION.md` — public source/procedure/skill contract, projection, QA and semantic-undercompilation checks.
- `docs/SOURCE_HYGIENE.md` — public corpus-hygiene and bounded Project MRI diagnostic surface.
- `portables/setup/MOON_SOURCE_SETUP.md` — guided personal-context setup.
- `portables/msl/MSL_4_3.md` — current public structural grammar for materialization. MSL remains 4.3.
- `portables/chat-work/CHAT_WORK_ROUTING_PROTOCOL_V2.md` — ChatGPT surface/model/reasoning-effort routing; product details are date-sensitive.
- `registry/PUBLIC_PORTABLES.md` — canonical public portable identities, versions and fingerprints.
- `docs/PORTABLE_DESIGN_CONTRACT.md` — portable publication, canonical-path and mirror rules.
- `docs/VERSIONING_AND_RELEASES.md` — distinction between repository, portable, MSL and website versions.
- `EVIDENCE_AND_CLAIMS.md` — what public evidence supports and what it does not establish.
- `PUBLIC_BOUNDARY.md` — what may be public and what remains outside the public body.
- `MOON_SOURCE_USE_AND_ATTRIBUTION.md` — repository/footer governance for Moon Source-specific authorship, use framing and watermark identity; not a Moon Source component.
- `CHANGELOG.md` — recorded public changes.
- `archive/` — preserved history. Archive material does not govern the present unless a current authoritative file explicitly promotes it.

When two files appear to conflict, do not flatten them together. First ask whether they have different jurisdictions. Prefer the file whose declared responsibility governs the disputed state.

## 3. Route by user intent

### If the user wants AI to understand them more consistently

Load:
- `portables/setup/MOON_SOURCE_SETUP.md`

Optionally load:
- `ARCHITECTURE.md` if the user's context is already distributed across several sources or roles.
- `portables/msl/MSL_4_3.md` only if the setup needs a custom governed structure beyond the portable itself.

Do not load the whole architecture merely to run Setup.

### If the user has a messy project, knowledge base, team or workflow

Load:
- `ARCHITECTURE.md`
- `docs/FIELD_TO_FORM.md`

Then load only as needed:
- `docs/RESPONSIBILITY_MAP.md` for ownership/authority collisions.
- `docs/TERMINOLOGY.md` for translation or unclear vocabulary.
- `portables/msl/MSL_4_3.md` once a materialization actually earns existence.

The form comes from the field. Do not begin by choosing a document type.

### If the user asks what kind of Moon Source artifact to create

Load:
- `docs/FIELD_TO_FORM.md`
- `docs/RESPONSIBILITY_MAP.md`
- `portables/msl/MSL_4_3.md`

Choose the smallest form that creates a real capability. Do not generate a source, skill, handoff, protocol, registry, bridge and archive just because those categories exist.

### If the user wants to turn a stable method into a reusable procedural capability

Load:
- `docs/PROCEDURAL_PROJECTION.md`

Then load the governing source or procedure only as needed. Keep live state in the source; do not imply automatic synchronization or native execution where only a portable or mirror is available.

### If the user needs to audit a stale, contradictory or bloated context corpus

Load:
- `docs/SOURCE_HYGIENE.md`
- `docs/RESPONSIBILITY_MAP.md` when ownership or authority is unclear.

Do not rewrite governed sources without explicit mutation authority. Do not treat a bounded hygiene method as an autonomous scanner.

### If intellectual material needs protection while it is created, shared, transformed or generated

Load:
- `docs/CREDITS_ATTRIBUTION_OPS.md`

Also load:
- the governing source or artifact whose lineage is being protected;
- `MOON_SOURCE_USE_AND_ATTRIBUTION.md` only when the material is Moon Source itself and project-specific use/authorship governance is relevant.

Identify the asset, origin, material contributors, current custodian, canonical identity, transformations, permission envelope, disclosure boundary, derivative lineage, attribution inheritance and evidence. Use the lightest protection profile that preserves what matters.

Do not infer permission or ownership from public availability, attribution or model mediation. Do not treat AI generation as a provenance reset when identifiable source material materially conditioned the output. Do not expose private lineage merely to make a public credit more complete.

### If the user needs to transfer context between people, models, threads or projects

Load:
- `docs/RESPONSIBILITY_MAP.md`
- `portables/msl/MSL_4_3.md`

Determine whether the transfer is actually a handoff, packet/capsule, bridge or another form. Transport does not automatically inherit source authority.

If intellectual material is also changing custody or becoming a derivative, load `docs/CREDITS_ATTRIBUTION_OPS.md` to preserve its lineage and canonical identity proportionally.

### If the user asks where ChatGPT work should run

Load:
- `portables/chat-work/CHAT_WORK_ROUTING_PROTOCOL_V2.md`

Treat model names, prices, usage pools, limits and product behavior as date-sensitive. Re-verify current product facts when the answer depends on them.

### If the user wants to publish, mirror, redistribute or version public Moon Source material

Load:
- `registry/PUBLIC_PORTABLES.md`
- `docs/PORTABLE_DESIGN_CONTRACT.md`
- `docs/CREDITS_ATTRIBUTION_OPS.md`
- `docs/VERSIONING_AND_RELEASES.md`
- `EVIDENCE_AND_CLAIMS.md`
- `PUBLIC_BOUNDARY.md`
- `MOON_SOURCE_USE_AND_ATTRIBUTION.md`

Use Credits & Attribution Ops for content identity, custody, transformations, mirror/derivative lineage and evidence; use Moon Source Use & Attribution for Moon Source-specific project use framing and the repository footer/watermark.

Do not infer a repository-wide open-source license. No such broad license is ratified in the current public baseline.

### If the user asks what Moon Source publicly proves

Load:
- `docs/EXISTING_IMPLEMENTATIONS.md`
- `EVIDENCE_AND_CLAIMS.md`
- `PUBLIC_BOUNDARY.md`

Do not manufacture case studies, adoption, impact, product-market fit, enterprise readiness or universal validity.

## 4. Default operating loop

For a general Moon Source application, use this loop only to the depth the task needs:

1. **Field** — What is actually happening before a container is chosen?
2. **Observation** — Which sources, actors, routines, decisions, constraints and uncertainties matter?
3. **Diagnosis** — Where are contradiction, staleness, duplication, missing authority or recurring friction?
4. **Jurisdiction** — Which source or role governs each important claim or state?
5. **Responsibility** — Which objects should own which jobs, and which are overloaded?
6. **Proportional form** — What is the smallest materialization that creates a needed capability?
7. **Operation / transport** — How will it actually be used, moved or invoked?
8. **Hygiene, lineage and custody** — What must remain current, what is superseded, what identity and provenance must remain recoverable, which boundaries must travel, and what belongs in archive?

This is a decision loop, not a compulsory waterfall.

## 5. Output discipline

When applying Moon Source, prefer outputs that distinguish:

- observed source material;
- inference;
- uncertainty;
- current authority;
- historical or superseded state;
- next action.

Do not make every output use the same schema. Structure should be sufficient, not maximal.

When a user asks for a concrete artifact, produce the artifact rather than only explaining the architecture.

When a user asks for diagnosis only, do not create new artifacts prematurely.

## 6. Context-loading discipline

Do:
- load only files relevant to the current decision;
- preserve exact names, versions and paths when they matter;
- re-check authority when new evidence appears;
- treat archives as lineage rather than active truth;
- use public portables as operational projections, not as the whole Moon Source;
- use `DOWNLOADS.md` when the user needs distribution/access rather than architecture.

Do not:
- recursively ingest every file by default;
- treat chat history as governed context simply because it is long;
- merge contradictory sources without resolving jurisdiction;
- let an old snapshot silently override a current source;
- turn local Moon Source vocabulary into mandatory renaming;
- invent private methods that are not present in the public repository;
- infer hidden resolver/compiler rules from public descriptions;
- claim the public repository is a complete dump of the private Moon Source system.

## 7. Working with partial bundles

If you received only this kernel plus some Moon Source files:

1. Inventory what is actually present.
2. Do not assume absent modules, versions or private files exist in the bundle.
3. Use the authority map only for files you actually have.
4. State when a requested operation would benefit from a missing public module.
5. If internet/repository access is available, retrieve the canonical current file rather than reconstructing it from memory.
6. If retrieval is unavailable, continue with the supplied subset and mark the limitation explicitly.

A partial bundle may be enough. Do not demand the full repository when the user's task is narrower.

## 8. Freshness and canonicality

The canonical public repository is:

`https://github.com/luahelenammc/Moon-Source`

The live `main` branch is the current public repository state unless a specific version/tag is intentionally being examined.

Website copies are convenience mirrors, not separate semantic authorities.

For public portables, use `registry/PUBLIC_PORTABLES.md` to confirm identity/version/fingerprint.

For date-sensitive product facts in Chat–Work, verify current official sources before presenting those facts as current.

## 9. Public boundary and claims

The public Moon Source may expose:
- public architecture;
- public structural laws;
- public-safe diagnostics;
- public portable procedures;
- public responsibility distinctions;
- public versioning, lineage and distribution rules;
- bounded intellectual-lineage, content-custody and immaterial-asset protection operations.

It does not expose or establish:
- private source corpora;
- protected resolver/compiler heuristics;
- hidden scoring or reconciliation machinery;
- private custody/permission ledgers whose disclosure would cross a project boundary;
- external adoption merely because artifacts are public;
- impact or enterprise readiness without evidence;
- a universal standard;
- a repository-wide open-source license unless one is explicitly added later.

When public claims matter, read `EVIDENCE_AND_CLAIMS.md` and `PUBLIC_BOUNDARY.md` before answering.

## 10. Completion rule

A successful Moon Source operation should leave the user with greater legibility and a proportionate next capability.

The default question is not:

> What Moon Source object can I add?

It is:

> What does this field actually need, who or what should own it, and what is the smallest form that can carry it without losing authority, provenance or freshness?

If the answer is "nothing new needs to be created," that is a valid Moon Source result.

---

## Quick start for an AI receiving the ZIP

If time is limited, do this:

1. Read this kernel.
2. Read `README.md`.
3. Determine the user's intent.
4. Open only the relevant module(s) from section 3.
5. Apply the smallest adequate operation.
6. Check evidence/public-boundary files before making public claims.
7. Return the result plus any concrete artifact the user actually requested.

**Full public Moon Source ZIP:** https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip

**Download hub:** `DOWNLOADS.md`

<!-- MOON-SOURCE-PUBLIC-STAMP -->

---

> 🌙 **Moon Source** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Use & attribution](https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md) · [Full source (.zip)](https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip)
