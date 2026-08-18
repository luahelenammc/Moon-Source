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

- Public architecture baseline: 2026-08-16.
- Current structural grammar: MSL 4.3.
- Public portables: Setup 2.0, MSL 4.3, Chat–Work Routing Protocol 2.0-public.
- Website: production public convenience surface; canonical and mapped mirror bytes were verified after promotion on 2026-08-16.
- Repository: luahelenammc/Moon-Source, public reference and versioning body.

## Release rules

1. Every current public portable has one canonical repository path.
2. Website copies are convenience mirrors, not competing semantic sources.
3. Superseded versions remain recoverable where feasible.
4. A version change must state whether it is additive, corrective, incompatible or archival.
5. A major MSL version requires a semantic grammar change and migration guidance, not a new label.
6. A public release must pass the public-boundary and claim checks.
7. A release that changes authorship, lineage, adaptation status, canonical path or mirror identity must run the [Credits & Attribution Ops](CREDITS_ATTRIBUTION_OPS.md) checks.
8. No license rights are broadened by implication.

## MSL decision

The 2026-08-16 promotion audit returns KEEP_MSL_4_3. Source jurisdiction, procedural skills, handoffs and bridges are important architectural layers, but the live MSL 4.3 source already provides the structural grammar needed to express them. They remain separate responsibilities rather than being absorbed into MSL 5.

## Future versions

A future MSL major version would need evidence that the grammar itself has changed: for example, a new invariant, a new form-selection law or a new structural responsibility that cannot remain a procedural projection or protocol. If that happens, publish migration guidance and preserve MSL 4.3 as a prior generation.

## Public routes

Inspect the current public family in the [portable registry](../registry/PUBLIC_PORTABLES.md), use the [download hub](../DOWNLOADS.md) for access, consult [Credits & Attribution Ops](CREDITS_ATTRIBUTION_OPS.md) for provenance changes, or return to [Architecture](../ARCHITECTURE.md) for the governing model.
