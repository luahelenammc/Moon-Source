# Versioning and Releases

## Layers

Moon Source has several versioned layers with different responsibilities:

- repository architecture version;
- public portable version;
- MSL version;
- website surface revision;
- internal source revision.

They should not be collapsed into one number.

## Current baseline

- Public architecture baseline: 2026-08-16; additive component and operational updates continued through 2026-08-23; public-legibility, registry and facade hardening is recorded on 2026-08-24; Context Receipt, loading-discipline and stack-legibility refinements are recorded on 2026-08-26.
- Current structural grammar: MSL 4.3.
- Public portables: Setup 3.0, MSL 4.3, Chat–Work Routing Protocol 2.0-public.
- The public component inventory is tracked separately from the portable inventory in `registry/public-portables.json` schema 1.1 and `registry/PUBLIC_PORTABLES.md`.
- Preflight, Credits & Attribution Ops, Operational Devices, Operational Reliability, Failure Foundry, Connected Sources, Source Hygiene, Signal Calibration and Procedural Projection are public components outside the portable registry.
- Browser Console Device is an experimental bounded reference implementation outside the current portable family.
- Website: production public convenience surface; canonical and mapped mirror bytes were verified after promotion on 2026-08-16.
- Repository: luahelenammc/Moon-Source, public reference and versioning body; software and automation are Apache-2.0, while documentation, methods and public portables are CC-BY-4.0.

## Release rules

1. Every current public portable has one canonical repository path.
2. Website copies are convenience mirrors, not competing semantic sources.
3. Superseded versions remain recoverable where feasible.
4. A version change must state whether it is additive, corrective, incompatible or archival.
5. A major MSL version requires a semantic grammar change and migration guidance, not a new label.
6. A public release must pass the public-boundary and claim checks.
7. A release that changes content identity, authorship, upstream lineage, transformation status, canonical path, permission scope, disclosure boundary, derivative relationship or mirror identity must run the relevant [Credits & Attribution Ops](CREDITS_ATTRIBUTION_OPS.md) custody checks.
8. Exact-identity claims should use version/fingerprint evidence when appropriate, without treating a fingerprint as proof of authorship, ownership or permission.
9. License rights come from the applicable standard license and file-level metadata; they are not broadened beyond those terms by implication.

## MSL decision

The 2026-08-16 promotion audit returns KEEP_MSL_4_3. Source jurisdiction, procedural skills, handoffs and bridges are important architectural layers, but the live MSL 4.3 source already provides the structural grammar needed to express them. They remain separate responsibilities rather than being absorbed into MSL 5.

The expanded Credits & Attribution Ops component does not by itself require an MSL major version. It adds a distinct operational responsibility for intellectual lineage and content custody rather than changing the MSL structural grammar.

The 2026-08-23 Operational Devices / Operational Reliability / Failure Foundry update is additive. It makes execution, receipts, failure boundaries and failure-to-capability projection explicit without changing the MSL grammar, bumping an existing portable or adding a repository-wide license. The Browser Console Device remains an experimental reference implementation and is not a current portable.

The 2026-08-24 public-legibility hardening is additive. It adds hypothetical application scenarios, Git-derived public component chronology, registry validation, a bounded README digest, contribution ergonomics, CI self-audit and a website facade pass without changing MSL 4.3, Setup 3.0, Chat–Work 2.0-public or portable bytes.

The 2026-08-26 Context Receipt and stack-legibility refinement is additive. It names progressive / just-in-time context loading, separates source/data authority from instruction authority, adds proportional context-path evidence to Operational Reliability and clarifies Moon Source's complementary position around model, harness/runtime and retrieval layers without changing MSL 4.3, Setup 3.0, Chat–Work 2.0-public or portable bytes.

## Future versions

A future MSL major version would need evidence that the grammar itself has changed: for example, a new invariant, a new form-selection law or a new structural responsibility that cannot remain a procedural projection or protocol. If that happens, publish migration guidance and preserve MSL 4.3 as a prior generation.

## Public routes

Inspect the current public family in the [portable registry](../registry/PUBLIC_PORTABLES.md), use the [download hub](../DOWNLOADS.md) for access, consult [Credits & Attribution Ops](CREDITS_ATTRIBUTION_OPS.md) for intellectual lineage and content-custody changes, or return to [Architecture](../ARCHITECTURE.md) for the governing model.

<!-- MOON-SOURCE-PUBLIC-STAMP -->

---

> 🌙 **Moon Source** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Source/blob/main/LICENSING.md) · [Use & attribution](https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md) · [Full source (.zip)](https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip)
