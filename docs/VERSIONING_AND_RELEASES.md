# Versioning and Releases

The repository-wide rule for public names and release state is [Repository Naming and Versioning](REPOSITORY_NAMING_AND_VERSIONING.md). Human-facing titles identify a stable capability; versions describe its current state in metadata, registries and release records.

## Layers

Moon Source has several versioned layers with different responsibilities:

- repository architecture version;
- public portable version;
- MSL version;
- website surface revision;
- internal source revision.

They should not be collapsed into one number.

## Current baseline

- Public architecture baseline: 2026-08-16; additive capability and operational updates continued through 2026-09-09; Chat–Work tri-surface routing advanced to V4 on 2026-09-06, to the IDL/source-transport subversions through 4.4 on 2026-09-07, and to bounded-exhaustiveness subversion 4.7 on 2026-09-09.
- Current structural grammar: Moon Source Language, version 5.0.
- Current standalone distributions: Moon Source Setup (version 3.1), Preflight (version 2.0), Be My Eyes (version 1.0), Connected Sources (version 1.1), Moon Source Language (version 5.0) and Chat–Work Routing Protocol (version 4.7).
- All fourteen public capabilities are tracked once in `registry/public-capabilities.json` schema 2.0 and `registry/PUBLIC_CAPABILITIES.md`; standalone distributions are a filtered view of that unified registry.
- Credits & Attribution Ops, Operational Devices, Operational Reliability, Failure Foundry, Source Operations, Source Hygiene, Signal Calibration and Procedural Projection are repository-only capabilities. Connected Sources is the structural crown jewel at `docs/CONNECTED_SOURCES.md` and remains independently distributable.
- Browser Console Device is an experimental bounded reference implementation outside the current portable family.
- Website: production public convenience surface; each current portable mirror must remain byte-equal to its canonical current portable before mirror status is called verified.
- Repository: luahelenammc/Moon-Source, public reference and versioning body; software and automation are Apache-2.0, while documentation, methods and public portables are CC-BY-4.0.

## Release rules

1. Every current public portable has one canonical repository path.
2. The active `main` tree exposes only the latest public generation of each portable family.
3. When a portable is superseded, remove the superseded file from the live repository tree and remove its live website mirror; preserve history through Git history and, when useful, immutable tags or releases.
4. Website copies are convenience mirrors of current canonical files, not competing semantic sources or compatibility archives.
5. A version change must state whether it is additive, corrective, incompatible or archival.
6. A major MSL version requires a semantic grammar change and migration guidance, not a new label.
7. A public release must pass the public-boundary and claim checks.
8. A release that changes content identity, authorship, upstream lineage, transformation status, canonical path, permission scope, disclosure boundary, derivative relationship or mirror identity must run the relevant [Credits & Attribution Ops](CREDITS_ATTRIBUTION_OPS.md) custody checks.
9. Exact-identity claims should use version/fingerprint evidence when appropriate, without treating a fingerprint as proof of authorship, ownership or permission.
10. License rights come from the applicable standard license and file-level metadata; they are not broadened beyond those terms by implication.
11. A user-facing link labeled **Download** must use a route intended to download the file; inline browse/open routes must be labeled as browse/open instead.
12. One capability has one canonical semantic body. Architectural role and standalone distribution are independent dimensions. Mirrors and packages are delivery surfaces, and a distinct adapter is allowed only for volatile or surface-specific facts.
13. Every accepted update to an independently versioned capability's canonical body or operative contract advances that capability by **+0.1**. A bookkeeping-only correction that restores previously skipped version increments does not recursively create another bump.

## Title–version separation

The public title of a capability is its stable human-facing identity. A release version is separate state. Do not rename a current title merely because the portable, protocol or repository has advanced from one release to another.

- Keep human-facing titles, first-level headings, registry `title` values and website card labels free of release markers such as `V2`, `V4`, `3.0`, `4.3`, `1.0`, `beta` or `rc1`.
- Record release state in dedicated `version` metadata, registry fields, release notes, package names, filenames, paths and other technical coordinates where it is useful or required.
- Historical prose may name an earlier generation when the version is part of the fact being preserved; phrase current use with the stable title and an explicit version field or sentence.
- Reusable Moon Source-family repositories should copy the policy template and run the title/version separation guard before promotion.

## MSL 5.0 release — 2026-09-09

MSL 5.0 — Sovereign Semantic Passage is a major public portable release. MSL-4.3 established adaptive Markdown-native form; internal MSL-4.4 work added semantic sufficiency and surface projection. MSL 5.0 makes the passage layer explicit: source/body sovereignty, capability-field reasoning, orthogonal state, preserved interfaces, donor-to-method generalization, traceability/formality separation, reception/readback and release coherence.

The release preserves MSL-4.3 as the previous public portable and MSL-4.4 as internal lineage. MSL remains a structural/context language, not executable code, a universal ontology, a runtime, a product or proof of external adoption.

Public release coherence requires the canonical body, readable README, registry, changelog, package, SHA256, links, mirrors and validators to agree. The public repository and website expose MSL 5.0 as current only after that set is synchronized.
### MSL 5.0 corrective postflight — formatting continuity

The corrective postflight pass restores formatting continuity as an explicit part of the same MSL 5.0 grammar: Markdown-native/no-fence defaults, object dissolving, literal-only fences with real syntax labels, exceptional tables, vertical hygiene, human naming and one-H1 discipline. It is a corrective content release within 5.0, not a new semantic generation or parallel 5.0.x authority; the canonical path and filename remain `portables/msl/MSL_5_0.md`.

## Historical MSL decision

The 2026-08-16 promotion audit returns KEEP_MSL_4_3. Source jurisdiction, procedural skills, handoffs and bridges are important architectural layers, but the live MSL 4.3 source already provides the structural grammar needed to express them. They remain separate responsibilities rather than being absorbed into MSL 5.

The expanded Credits & Attribution Ops component does not by itself require an MSL major version. It adds a distinct operational responsibility for intellectual lineage and content custody rather than changing the MSL structural grammar.

The 2026-08-23 Operational Devices / Operational Reliability / Failure Foundry update is additive. It makes execution, receipts, failure boundaries and failure-to-capability projection explicit without changing the MSL grammar, bumping an existing portable or adding a repository-wide license. The Browser Console Device remains an experimental reference implementation and is not a current portable.

The 2026-08-24 public-legibility hardening is additive. It adds hypothetical application scenarios, Git-derived public component chronology, registry validation, a bounded README digest, contribution ergonomics, CI self-audit and a website facade pass without changing MSL 4.3, Setup 3.0 or the then-current Chat–Work V2 portable bytes.

The 2026-08-26 Context Receipt and stack-legibility refinement is additive. It names progressive / just-in-time context loading, separates source/data authority from instruction authority, adds proportional context-path evidence to Operational Reliability and clarifies Moon Source's complementary position around model, harness/runtime and retrieval layers without changing MSL 4.3, Setup 3.0 or the then-current Chat–Work V2 portable bytes.

### Chat–Work V3 release — 2026-09-02

Chat–Work V3 is a **material additive-and-superseding portable release**, not an MSL grammar change.

It preserves the prior generation's separation of surface/model/effort, Work Readiness Gate, Return Contract and Chat acceptance seed, then makes the return path loadbearing through mandatory Chat Postflight, residual dispositions, route-by-remaining-work, bounded Chat repair, explicit cycle completion states, next-step buckets and delta-only Work re-entry.

The superseded V2 file is not part of the current repository tree or current website mirror surface. Its historical contents remain recoverable through Git history. The V3 release does **not** claim that any native or personal `chat-work-router` skill has independently advanced to V3; skill synchronization remains a separate projection and verification event.

MSL remains 4.3 because the structural grammar did not change.

### Chat–Work V4 release — 2026-09-06

Chat–Work V4 is a **material additive-and-superseding portable release**, not an MSL grammar change.

It promotes Codex to a first-class execution surface beside Chat and Work, routes by sovereign object and six independent dimensions, adds availability and Budget Survivability gates, Context Diet, frontier ROI/burst control, repository constitution and native-parallelism rules, executor-neutral handoffs, salvage receipts and mandatory Chat Postflight.

The superseded V3 file is removed from the current repository and website trees. Its historical contents remain recoverable through Git history. V4 does **not** claim that any native or personal routing skill has independently advanced; skill synchronization remains a separate projection and verification event.

MSL remains 4.3 because the structural grammar did not change.

### Chat–Work V4.3 release — 2026-09-07

Chat–Work V4.3 is a **material additive-and-superseding portable release**, not an MSL grammar change.

It promotes the model-neutral Intelligence Distillation Ladder across `efficient | balanced | strong | frontier`: isolate the irreducible delta, distinguish reasoning effort from capability, allow justified direct tier jumps, use bounded micro-bursts, return only the decision-bearing ruling and re-enter the lower sufficient tier for implementation and verification. Frontier Burst is retained as the frontier-tier specialization of this general pattern.

The superseded 4.2 portable remains recoverable through Git history; the live repository and website continue to expose one canonical V4 file. The release does not claim an OpenAI policy, benchmark, guaranteed savings or quality gain, universal model ranking, native skill advancement or a private profile default.

MSL remains 4.3 because the structural grammar did not change.

### Moon Source Setup 3.1 release — 2026-09-07

Moon Source Setup 3.1 is a **material additive portable release**, not an MSL grammar change. It adds an adaptive persistent-source route for durable continuity and current living context, recommends Google Drive as the default ChatGPT document-source substrate when available, keeps GitHub complementary, probes actual capability and preserves a standalone fallback. It does not make connector access mandatory or create a connector-onboarding questionnaire.

### Connected Sources 1.0 release — 2026-09-07

Connected Sources 1.0 is a **material method-plus-portable promotion**. The canonical method remains `docs/CONNECTED_SOURCES.md`; `portables/connected-sources/CONNECTED_SOURCES.md` is its independently readable public projection. The portable makes Standalone, Connected Read, Living Source and Federated modes explicit, carries source locator/reference and capability-probing rules, and preserves authority, freshness, mutation, readback, fallback and claim-ceiling boundaries.

This promotion does not claim universal connector support, automatic synchronization, exhaustive retrieval, authority by locator, private-source disclosure or adoption. MSL remains 4.3 because the structural grammar did not change.

### Connected Sources 1.1 canonical-body rebase — 2026-09-07

Connected Sources 1.1 is a **material canonical-identity and method-plus-portable rebase**, not an MSL grammar change. The portable at `portables/connected-sources/CONNECTED_SOURCES.md` is now the single active semantic body and may serve both structural and transport roles. It absorbs the unique current public doctrine from the retired `docs/CONNECTED_SOURCES.md` body without concatenating the two files, including Connector Preflight, the substrate contract, retrieval coverage, failure modes, facet-scoped authority and acceptance boundaries.

The retired docs body is removed from the live tree; Git history preserves it. Dated ChatGPT product facts are isolated in the subordinate `docs/CONNECTED_SOURCES_CHATGPT_ADAPTER.md` reference and are not auto-loaded for generic source governance. The current package is `downloads/connected-sources-1.1.zip`, the website mirror remains the same mapped filename, and the former 1.0 package is removed from active `main`.

Be My Eyes remains **1.0** because its portable already contains the material current method responsibilities found in the retired docs body; the duplicate docs body is removed without changing portable bytes. MSL remains 4.3 because the structural grammar did not change.

### Chat–Work V4.4 release — 2026-09-07

Chat–Work V4.4 is a **material additive-and-superseding portable release**, not an MSL grammar change. It retains the V4.3 Intelligence Distillation Ladder and adds a connector-aware source transport contract for governing source/family, locator, facet, requested operation, coverage, freshness/revision, mutation authorization, readback and fallback. A locator is transported as a reference, never as authority.

The superseded 4.3 portable remains recoverable through Git history; the live repository and website expose one current V4 file and one current mirror. The release does not claim an OpenAI policy, benchmark, automatic source synchronization, native skill advancement, guaranteed savings/quality or product entitlement.

MSL remains 4.3 because the structural grammar did not change.

### Chat–Work V4.7 release — 2026-09-09

Chat–Work V4.7 is a **material additive-and-superseding portable release**, not an MSL grammar change. It retains the V4.4 connector-aware source transport contract and adds a Bounded Exhaustiveness Guard to the Intelligence Distillation Ladder so open-ended completeness language is compiled into explicit coverage ceilings, stop conditions and scope-expansion rules before expensive sustained or frontier execution.

The release also adds `scope_amplification_failure` and a constrain-before-escalate recovery path. The Astra behavior that motivated the calibration is retained only as dated anecdotal field evidence, not as a benchmark, universal model property or fixed cost claim. The public human title remains **Chat–Work Routing Protocol** and the canonical filename remains `CHAT_WORK_ROUTING_PROTOCOL_V4.md`; 4.7 is release state, not title identity.

The superseded 4.4 portable remains recoverable through Git history. MSL remains 5.0 because this release changes the routing/distillation protocol, not the structural passage grammar.

**Lineage correction:** the last correctly numbered Chat–Work release was 4.4. The self-onboarding canonical-body integration is counted as 4.5, the MSL 5.0 canonical dependency/reference alignment as 4.6, and the bounded-exhaustiveness update as 4.7. The repository had preserved 4.4 across the first two updates under an older semantic-only bump convention; this correction restores the project's +0.1-per-module-update rule without fabricating parallel historical artifacts.

## Future versions
### Public capability registry rebase — 2026-09-08

The previous component-versus-portable split was an orthogonal-dimension error.
The registry now records one capability per record with independent
architectural role and distribution metadata. Standalone distribution remains
supported without creating a second semantic inventory.

Connected Sources remains version 1.1, but its canonical body now lives
at docs/CONNECTED_SOURCES.md because its primary responsibility is structural
source governance. Its ZIP and website mirror remain exact delivery surfaces.
The registry schema advanced to 2.0; no capability method version was bumped.


A future MSL major version would need evidence that the grammar itself has changed: for example, a new invariant, a new form-selection law or a new structural responsibility that cannot remain a procedural projection or protocol. If that happens, publish migration guidance, promote the new MSL generation as the only live MSL portable in `main`, and preserve the prior generation through Git history or an immutable release rather than a parallel current-tree file.

## Public routes

Inspect the current public capabilities in the [unified registry](../registry/PUBLIC_CAPABILITIES.md), use the [download hub](../DOWNLOADS.md) for standalone access, consult [Credits & Attribution Ops](CREDITS_ATTRIBUTION_OPS.md) for intellectual lineage and content-custody changes, or return to [Architecture](../ARCHITECTURE.md) for the governing model.

## Visibility-neutral version tokens

Repository visibility is an orthogonal publication/distribution state, not part of a version token. Moon Source versions therefore use bare release state only. Public/private exposure belongs in repository location, status, boundary and distribution metadata; never append a visibility qualifier to the numeric version.

Removing a legacy visibility qualifier is a bookkeeping-only normalization and does not by itself advance the numeric release. Future accepted updates continue to follow the governing increment rule on the bare number itself.

<!-- MOON-SOURCE-PUBLIC-STAMP -->

---

> 🌙 **Moon Source** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Source/blob/main/LICENSING.md) · [Use & attribution](https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md) · [Full source (.zip)](https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip)
