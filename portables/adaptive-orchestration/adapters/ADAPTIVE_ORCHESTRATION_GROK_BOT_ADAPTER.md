# Adaptive Orchestration Protocol — Grok Bot & Persistent Agent Economy Adapter

*Provider-specific operational adapter. It does not modify the model-neutral AOP control-root, commitment, authority or acceptance laws.*

## Identity

- **adapter version:** 1.0
- **as of:** 2026-11-17
- **parent:** [Adaptive Orchestration Protocol 6.4](../ADAPTIVE_ORCHESTRATION_PROTOCOL.md)
- **primary host:** xAI Grok Bot, a persistent computer-using agent with named Bots, shared tools, skills and routines
- **secondary scope:** other persistent agents **only where equivalent capabilities have been observed**
- **status:** public field-derived procedure, not a token-use benchmark
- **authorship:** Lua Helena Moon Martins Cardoso (Moon), with AI-assisted coauthorial development by Áurion
- **origin:** a sanitized, single-day field note on Grok Bot token economy, 2026-11-17. No private project identifiers, account details, interests or personal exports are reproduced.

## Why this adapter exists

For recurring agent work, the relevant optimization unit is **total work and allowance consumed per accepted, evidence-bearing delta**, not the shortest prompt or the fewest tool calls in isolation. Expense may be driven by repeated source ingestion, avoidable agent turns, browser/computer actions, fan-out and context transported to helpers. Which channel is cheaper is a **working hypothesis**, dependent on the runtime's billing, token accounting, cache, tool execution and data size. It is not a measured universal ranking.

Grok Bot's documented environment includes a cloud computer, connected apps, Bots that collaborate, reusable skills and routines scheduled or triggered by events. Its private skills are shareable among Bots; permissions and app availability still require runtime checks. See the [official overview](https://docs.x.ai/grok-bot/overview), [skills and routines](https://docs.x.ai/grok-bot/skills-routines-and-automations) and [approvals and privacy](https://docs.x.ai/grok-bot/approvals-security-and-privacy). Do not conflate Grok Bot with the ordinary Grok chat model.

## 1. Capability and custody preflight

Before choosing a path, verify: which Bot owns the task, which durable state it can really read, whether a terminal or file system is available, which connected apps/APIs are authorized, whether browser interaction is necessary, what helper continuation preserves, what actions require approval, and what allowance or usage evidence is actually visible.

Treat the computer, browser session and authenticated accounts as a **shared trust surface**, not as a per-Bot security boundary. Give each workflow the smallest data scope needed; do not infer that a separate named Bot has isolated credentials. A login in an available browser is not unlimited authorization to inspect unrelated data.

When feature, budget or permission is unverified, mark it `UNKNOWN` and route conservatively. Do not fabricate a token-cost ratio, quota reset, fixed agent memory behavior or permissions.

## 2. Least-expensive sufficient information route

Evaluate candidates in this order, **subject to adequacy and observed cost**, not as a guaranteed numeric price ladder:

1. **Verified state / ledger / cursor:** answer or close from existing evidence when the question has not changed. A cursor alone never proves there is no new upstream data.
2. **Structured export + local processing:** when an official export and authorized local runtime exist, filter and deduplicate CSV/JSON/other structured data before bringing a small summary into model context. Local processing has compute, storage and possibly tool cost; it is not automatically free or constant-cost.
3. **Connector or API:** request bounded fields, pages, dates or identifiers instead of whole documents when the interface supports it. Respect pagination and rate limits.
4. **Targeted search or fetch:** small, scoped queries after checking cached/indexed evidence; preserve source URLs and retrieval dates.
5. **Computer use / browser:** prefer when necessary for visual meaning, login-only surfaces or unsupported actions. Browser cost depends on action count, screenshots, interface stability and model/tool accounting; it is not always the most expensive path.

**Routing gate:** choose the cheapest *verified sufficient* channel that can meet freshness, privacy, correctness and acceptance. A failed cheaper route should not trigger blind repetition or an unnecessary low-tier detour.

## 3. Stateful delta cycle

`PRE_EXECUTION → FRESHNESS_CHECK → CONTEXT_DIET → FOCAL_DELTA → STOP_GATES → QA → SCOPED_WRITE → READBACK → PRE_EMISSION`

- **PRE_EXECUTION:** identify the sovereign task, target outcome, owning Bot, source permissions and smallest acceptable evidence.
- **FRESHNESS_CHECK:** compare reliable version, modification timestamp, cursor, ETag, digest or bounded source probe. Use `NO_DELTA` only when the checked scope and freshness evidence justify it; otherwise use `UNVERIFIED` or `BLOCKED`.
- **CONTEXT_DIET:** load index or metadata first. Expand only pertinent sections, records and time windows. Never rely on an old snapshot when a more authoritative changed source exists.
- **FOCAL_DELTA:** work a bounded partition from a queue or defined priority, then persist a cursor and evidence for completed partitions.
- **STOP_GATES:** set limits for reads, requests, helper calls, browser actions, elapsed work and retries where observable. Stop on acceptance, diminishing marginal new evidence, a hard block, authorization boundary or exhausted budget. “Two unproductive batches” is an optional heuristic, never a universal stopping proof.
- **QA:** distinguish source fact, reported claim, inference, hypothesis and verification; preserve failures and unsupported scope.
- **SCOPED_WRITE:** write the smallest authorized change to its actual source of truth. Prefer in-place, revision-safe edits or compact append-only events **only when the target is a ledger**. Do not accumulate endless patches inside a living source.
- **READBACK:** inspect the changed section and its metadata/version after writing. A write call alone is not evidence of completion.
- **PRE_EMISSION:** communicate concise verified outcomes; link to the durable artifact only when a real link exists. Record claim ceilings.

## 4. Grok Bot-specific operating rules

### Helpers and delegation

Retain the current competent Bot as the control root where possible. Reuse a previously established helper **only if its usable state/continuity is observed**, and pass a task capsule of identifiers, bounded scope, proof requirements and return shape instead of a pasted corpus. Physical fan-out needs a demonstrable net benefit; logical roles do not require separate Bots. One linear task generally merits one worker.

### Routines, skills and triggers

Start with one reliable manual run, convert the repeatable method into a **skill**, and only then attach a **routine**. Grok Bot documents both scheduled and event-triggered routines; use a relevant event trigger or the coarsest cadence that meets required freshness. Two runs per day, twelve-hour spacing and avoiding hourly polling are useful *examples*, not global mandates. Time-critical workflows may need shorter cadence with explicit rationale and bounded cost. Keep routine prompts short and refer to the skill, source map and ledger rather than duplicating full instructions.

### Large personal collections

Where permitted, use official exports and local structured filtering for large collections before model analysis. Deduplicate by platform ID, canonical URL and event/version; retain provenance and deletion behavior. Visual interfaces remain useful for thumbnails, visual semantics and stratified samples; a small set such as 8–12 samples is a starting hypothesis, not representative by default. Do not silently ingest personal categories unrelated to the authorized task. Sensitive content requires explicit applicable permission and purpose limits.

### Browser

Open the exact authorized URL where known; define a maximum sequence, fields to capture and stop condition. Never scroll indefinitely “to be thorough.” Collect identifiers/counts/URLs before opening full records. If no bounded mechanism gives acceptable coverage, disclose the gap rather than fabricate completeness.

### Errors and mutation safety

Classify errors before retry: transient transport failure may merit one bounded retry; permission denial, absent feature, invalid source or uncertain destructive action does not. Preserve a `BLOCKED` receipt with attempted route, observed error, last valid evidence and smallest re-entry condition. User approval remains required where the host and task demand it.

## 5. Minimal ledger contract

A persistent workflow should have a compact record, whether stored in a file or a governed database:

```yaml
workflow_id: example
owner_bot: observed_bot_id_or_name
scope: bounded_source_partition
source_locator: validated_locator
source_version_or_etag: value_or_unknown
last_processed_id: value_or_null
last_verified_at: ISO_8601_or_unknown
evidence_ref: durable_link_or_log_ref
next_partition: cursor_or_null
status: ACCEPTED | NO_DELTA | PARTIAL | BLOCKED | UNVERIFIED
invalidation_triggers: [version_change, permission_change, schema_change, user_request]
```

The ledger is continuity metadata, not a data dump. Store decisions, scopes and cursors rather than copies of sensitive documents. A hash or timestamp can signal change but may not detect deletion, backfill or changed meaning; plan occasional bounded reconciliation according to source risk.

## 6. Execution profiles and portability

| Property | Grok Bot | Other persistent computer-using agents | Stateless chat / generic task scheduler |
|---|---|---|---|
| Persistent owner Bot | Documented, verify actual setup | Capability-gated | Do not assume |
| Scheduled or event routines | Documented, verify trigger | Capability-gated | Use only available scheduling |
| Shared cloud computer / browser | Check account-level custody | Host-specific | Do not assume |
| Connected API vs browser choice | Per installed/authorized tool | Capability-gated | Often limited |
| Durable cursor / ledger | Write to a verified source | Must implement or verify | External state required |
| Helper reuse | Verify actual retained context | Verify actual retained context | Assume none until proven |

The invariant exported to other hosts is **state-aware, delta-first, source-scoped, evidence-backed orchestration**. Grok Bot's product mechanics remain adapter-specific. Do not apply shared-browser, scheduling, agent-identity or cost assumptions to other platforms by analogy alone.

## 7. Measurement plan, not fabricated savings

For each repeated workflow, compare a small set of like-for-like runs against a baseline on: accepted useful deltas, source records checked, prompts/model context injected, helper count, browser steps, retries, wall-clock latency, provider-reported usage if available and QA failures. Preserve the measurement method, not inferred pricing. A shorter run that misses material changes is not a saving.

No calibrated token ratios, channel multipliers, globally optimal cadence, representative sample size or default budget are asserted in this version. Calibrate from observed provider usage and validated acceptance before promoting defaults.

## 8. Minimal routine instruction

> On each run, check the authorized ledger and source freshness in the smallest available way. If the scoped source is demonstrably unchanged, return NO_DELTA with evidence and stop. Otherwise process only the next due partition using the cheapest sufficient authorized channel. Bound browsing, helper calls and retries; deduplicate before analysis; write only the accepted delta to the source of truth, read it back, and send a compact status with the artifact link. Report uncertainty or BLOCKED rather than claiming unverified completion.

## Claim ceiling and attribution

This adapter derives a provider-specific procedure from a sanitized field note and publicly documented Grok Bot affordances. It is not xAI-endorsed, a benchmark, an official rate card, a guarantee of token savings or proof of currently available features on any particular account. The model-neutral AOP 6.4 remains sovereign; this adapter governs only valid host-specific execution options.

<!-- MOON-SOURCE-PUBLIC-STAMP -->

---

> 🌙 **Moon Source** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Source/blob/main/LICENSING.md) · [Use & attribution](https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md) · [Full source (.zip)](https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip) · Questions, suggestions, or proposals? Feel free to contact me at [LuaHelenaMMC@gmail.com](mailto:LuaHelenaMMC@gmail.com).
