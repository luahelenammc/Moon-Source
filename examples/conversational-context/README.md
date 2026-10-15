# Conversational Context — Synthetic Reference

**Status:** experimental, read-only, deterministic reference example. **Not** a chatbot, SDK, legal-compliance engine, medical system, production API adapter, standalone Moon Source capability or external adoption.

This example demonstrates one narrow problem: how a product might decide which **consented and permitted context** from an API, query or spreadsheet *may* enter a conversational interaction. It does not retrieve data from those systems. Input records are fabricated and supplied directly by a caller.

**Concept versus implementation:** the conversational-context contract describes what context may enter an interaction. This Node.js selector implements only deterministic checks over fabricated input; it does not invoke an LLM, connect real APIs or enforce production privacy requirements.

## Run the tests

Requires Node.js 20+; no packages or network access:

```bash
node --test examples/conversational-context/test-router.js
```

The reference uses CommonJS to make local invocation straightforward. It supplies one pure function:

```js
const {buildContext} = require("./router.js");
// Supply a controlled SYNTHETIC input containing:
// today, request, consent, policy, jurisdictionProfile and records.
// buildContext returns a structured decision, NOT a message to send.
```

The test file contains a complete ready-to-run fabricated input.

## Journey re-entry, boundary and handoff composition

The original `buildContext(input)` remains available with its prior shape. A
second pure entry point adds a **decision over its approved output**, never a
parallel permission system:

```js
const {evaluateContinuity} = require("./continuity.js");
const decision = evaluateContinuity(syntheticInput);
```

`evaluateContinuity` calls `buildContext` first. The same policy, consent,
jurisdiction profile, subject, region, provenance, freshness and field
allowlists govern every value. Optional narrower restrictions are
`policy.allowedActorScopes`, `consent.allowedActorScopes`,
`consent.subjectKey` / `consent.region`, `consent.revokedAt` /
`validFrom`, `policy.maxAgeDaysByKind`,
`request.fieldSelection`, `record.fieldsByPurpose`,
`record.effectiveFrom` / `validUntil`, and operator-configured
`policy.substratePriorityByKind`. Omitting these preserves the older
fixture contract; providing them cannot expand the existing field allowlists.

**Synthetic end-to-end input:** the `journey()` fixture inside
[`test-router.js`](test-router.js) supplies a fictional subject in a fictional
region, purpose `continuity`, actor scope `continuity_operator`, an approved
current `program_state` (`module: 3`, `next_activity: "Exercise 4"`),
authorized `dialogue_state` (`last_known_module: 2`,
`last_seen_on: "2026-09-25"`) and a still-current `preference`
(`interaction_style: "concise"`), evaluated on `2026-10-14`.

**Expected structured decision:** `status: "ready"`,
`reason: "continuity_assessed"`,
`reentry.continuity: "operational_state_changed"`,
`reentry.operationalUpdatedDuringGap: true`,
`reentry.daysSinceLastInteraction: 19`,
`reentry.nextStep.kind: "candidate_for_application_review"`,
`handoff: null`. The authorized fields remain in `context`; forbidden
`medical_note`, `raw_transcript` and `private_note` do not appear.
The 19-day interval is calculated, not interpreted as a motive. A next
activity is **a candidate**, not an executed action.

For the controlled single-case demonstration:

```bash
node --test --test-name-pattern="re-entry composes" examples/conversational-context/test-router.js
```

If valid current operational state is missing, or equally authoritative
current records conflict, the decision contains `handoff_recommended`
with a minimal field-free review packet. An explicit request produces
`handoff_requested`. Neither means delivered, accepted or resolved:
`delivery` is always `not_attempted`. Unauthorized external actions
stop, without fabricated notification. Any actual referral requires a
separate authorized integration, operator decision and delivery readback.

No production identity, consent, security, retention or action capability
is added here. The detailed responsibility contract stays in
[Conversational Context](../../docs/CONVERSATIONAL_CONTEXT.md).

## Contract and observed behavior

**Input responsibilities:**

- `request` declares a known action, purpose, fictional region and pseudonymous subject key resolved by a trusted application. Every input record must match that scope; the key is not returned.
- `consent` and `policy` are **application-side**, not arbitrary user prompts.
- `jurisdictionProfile` represents an externally reviewed requirement envelope supplied by the operator. The demo cannot verify that any actual reviewer, consent system or statute exists.
- `records` are synthetically shaped `program_state`, `dialogue_state` or `preference` objects, with dates, purpose, provenance and candidate fields.
- `today` is a fixed fictional evaluation date.

**Output:**

- `ready`: a minimal structured context that has passed the fixture's declared allowlists. This is *not* permission to send it to a model or user.
- `blocked`: do not assemble context; application review is needed.
- `escalate`: a human should resolve conflicting or missing authorized state before proceeding.
- `trace`: stage names, counts and reasons, without raw dialogue, participant identifiers, medical details or full source content.

Tests cover consent revocation/expiry, mismatched purpose and region, subject/record isolation, unreviewed/expired requirement profile, unknown actions, stale and future-dated records, source authority, cross-source conflict, allowed API/query/spreadsheet substrate labels, field-level minimization and safe handling of unsupported values.

## What the code purposely does not do

There is **no network request**, LLM inference, backend, participant identity, clinical decision, country-specific law, deletion mechanism, localization policy, cryptographic proof, session database, safety classifier, authentication, access enforcement or real retention service.

The caller must authenticate users, prevent profile tampering, check data rights, implement validated consent and privacy controls, classify high-risk user requests, isolate retrieved text from instructions, audit actions, handle sensitive fields and perform actual redaction/deletion. A boolean or string flag alone is insufficient security.

The code's deterministic decisions are **illustrative**, and its timestamps, accepted purposes, mock source authority and profile are fabricated. Do not mistake passing synthetic tests for operational, regulatory or security readiness.

## Architecture and legal seams

Read [Conversational Context](../../docs/CONVERSATIONAL_CONTEXT.md) for the interaction contract and implementation path. Read [Jurisdictional Requirements](../../docs/JURISDICTIONAL_REQUIREMENTS.md) for the boundary between operator-approved legal/privacy profiles and software enforcement. Existing [Connected Sources](../../docs/CONNECTED_SOURCES.md), [Procedural Projection](../../docs/PROCEDURAL_PROJECTION.md), [Operational Devices](../../docs/OPERATIONAL_DEVICES.md) and [Operational Reliability](../../docs/OPERATIONAL_RELIABILITY.md) retain semantic authority.

The expected handoff is: **work with a real product team to define the genuine use case, data owner, actual processing rules and integration contract before writing a production adapter**.

<!-- MOON-SOURCE-PUBLIC-STAMP -->

---

> 🌙 **Moon Source** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Source/blob/main/LICENSING.md) · [Use & attribution](https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md) · [Full source (.zip)](https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip) · Questions, suggestions, or proposals? Feel free to contact me at [LuaHelenaMMC@gmail.com](mailto:LuaHelenaMMC@gmail.com).
