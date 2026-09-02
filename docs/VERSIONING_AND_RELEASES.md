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

- Public architecture baseline: 2026-08-16; additive component and operational updates continued through 2026-08-26; Chat–Work closed-loop routing advanced to V3 on 2026-09-02.
- Current structural grammar: MSL 4.3.
- Public portables: Setup 3.0, MSL 4.3, Chat–Work Routing Protocol 3.0-public.
- The public component inventory is tracked separately from the portable inventory in `registry/public-portables.json` schema 1.1 and `registry/PUBLIC_PORTABLES.md`.
- Preflight, Credits & Attribution Ops, Operational Devices, Operational Reliability, Failure Foundry, Connected Sources, Source Hygiene, Signal Calibration and Procedural Projection are public components outside the portable registry.
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

## MSL decision

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

## Future versions

A future MSL major version would need evidence that the grammar itself has changed: for example, a new invariant, a new form-selection law or a new structural responsibility that cannot remain a procedural projection or protocol. If that happens, publish migration guidance, promote the new MSL generation as the only live MSL portable in `main`, and preserve the prior generation through Git history or an immutable release rather than a parallel current-tree file.

## Public routes

Inspect the current public family in the [portable registry](../registry/PUBLIC_PORTABLES.md), use the [download hub](../DOWNLOADS.md) for access, consult [Credits & Attribution Ops](CREDITS_ATTRIBUTION_OPS.md) for intellectual lineage and content-custody changes, or return to [Architecture](../ARCHITECTURE.md) for the governing model.

<!-- MOON-SOURCE-PUBLIC-STAMP -->

---

> 🌙 **Moon Source** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Source/blob/main/LICENSING.md) · [Use & attribution](https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md) · [Full source (.zip)](https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip)
