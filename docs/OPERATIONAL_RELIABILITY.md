# Operational Reliability

Operational reliability is the discipline of making execution diagnosable, bounded, reversible where possible and honest about what the evidence shows.

It applies to a procedure, device, workflow or bounded runtime. It does not promise that a target is healthy, that a repair is safe in every environment or that a log is automatically authoritative.

## 1. Reconstruct the problem before touching the target

Translate the request into an operational reconstruction:

| Question | Purpose |
|---|---|
| What is the literal request? | Preserve the user's stated task |
| What is the actual operational pain? | Avoid fixing the wording while leaving the blockage intact |
| Which failure layer is probable? | Choose the smallest useful diagnostic movement |
| What is the risk of action? | Decide whether read-only, dry-run, quarantine, rollback or escalation is required |
| What evidence is missing? | Prevent confident repair of an unclassified state |
| What is the smallest safe next movement? | Keep the intervention bounded and reversible where possible |

Do not collapse a working inference into a fact. Record the observation, the current interpretation, meaningful alternatives and what evidence would update the interpretation when that distinction changes the action.

## 2. Read-only first

The default operating order is:

```text
diagnose → inventory → classify → simulate / dry-run → bounded apply → validate → receipt
```

Read-only work should come first whenever mutation could delete, overwrite, expose, duplicate, compound or irreversibly alter state. A read-only diagnostic may still fail; its failure must be recorded as an instrument or environment finding rather than silently assigned to the target.

Before deletion or move, inventory the candidates. Before repair, identify the object and its dependency. Before rewriting configuration, capture the relevant current state. Before claiming a current external service is broken, verify the version or status that the conclusion depends on.

## 3. Dependency Staircase

Validate lower layers before blaming higher layers:

1. **Target:** Is the intended object, page, file, process, route or state present?
2. **Instrument:** Did the diagnostic or operating tool itself start and produce trustworthy output?
3. **Environment:** Is the execution surface, session, runtime or host available?
4. **Dependency:** Does the required package, file, service, permission or upstream object exist?
5. **Configuration:** Do names, paths, parameters and versions refer to the proven dependency?
6. **Interaction:** Is the actual invocation compatible with the surface's contract?
7. **Upstream state:** Is an external service, policy or rate limit changing the result?

Do not repair a reference to an object that has not been proven to exist. Do not configure a dependent layer before establishing its prerequisite. A changed error can be evidence that the staircase moved; it is not, by itself, proof that the work succeeded.

## 4. Layered troubleshooting funnel

Use only the layers relevant to the field:

| Layer | Diagnostic question |
|---|---|
| Target | Is the target present, identifiable and in the expected state? |
| Instrument | Did the tool start, parse, self-test and emit a trustworthy receipt? |
| Environment | Is the surface, runtime, session or host available? |
| Dependency | Are the required objects available and compatible? |
| Configuration | Do references, parameters and limits match the proven state? |
| Permissions / storage / network | Is a boundary external to the operation blocking it? |
| Upstream service | Did an external service, policy, challenge or freshness change alter the result? |
| Reversible repair | Is there a bounded change with validation and a recovery path? |

The funnel is not a command to mutate every layer. It is a way to keep hypotheses separate until evidence justifies moving upward or applying a repair.

## 5. Change-of-error as evidence

After an intervention, compare the failure before and after:

- **same failure:** the intervention may not have reached the relevant layer;
- **different failure:** the dependency staircase or execution path may have changed;
- **partial progress:** some layers may now work while another remains blocked;
- **no failure observed:** validate the intended output rather than treating silence as success.

The change is evidence about state transition, not a verdict. A new error can be a useful diagnostic milestone or a regression. The receipt should preserve the before/after distinction when it matters.

## 6. Safe Mutation Gate

Mutation earns authorization only after a bounded gate:

1. inventory the affected state;
2. classify the risk and the failure domain;
3. define the smallest intended change;
4. run a dry-run or simulation when feasible;
5. confirm the operation is within legitimate authority;
6. apply within an explicit scope and cap;
7. validate the intended result and the untouched boundary;
8. preserve a rollback, quarantine, backup or recovery path when practical;
9. write a receipt with before/after, findings, errors and next action.

If a safe gate cannot be satisfied, stop, preserve evidence and escalate or ask for a narrower authorization. A device should prefer a valid partial result or an explicit `ABORTED_BY_GUARDRAIL` state to an unbounded repair.

## 7. Instrument Reliability

The diagnostic tool can fail independently of the target. A reliability-aware operation checks:

- whether the instrument started;
- whether syntax, parsing and configuration were valid;
- whether a self-test or boot marker was emitted;
- whether minimum output remains available when one field fails;
- whether a manual or critical read overrides a broken automated field;
- whether instrument failure is being misreported as target failure.

An empty report is not automatically a clean target. A script that never started did not diagnose anything. A tool that produced a partial receipt should preserve the partial evidence and identify the missing field.

## 8. Failure domains

Use the smallest public classification that clarifies responsibility:

| Domain | Meaning |
|---|---|
| `TARGET` | The intended object or state is absent, invalid or behaving unexpectedly |
| `INSTRUMENT` | The diagnostic or operating tool failed to start, parse or report reliably |
| `ENVIRONMENT` | The execution surface, runtime, host or session is unavailable or incompatible |
| `DEPENDENCY` | A required package, object, route, service or prerequisite is missing or incompatible |
| `INSTRUCTION` | The supplied procedure, parameter or assumption is incomplete or wrong |
| `INTERACTION` | The invocation, handoff or user/system interaction broke the expected contract |
| `OPTIONAL_PROBE` | An enrichment or non-essential check failed without invalidating the core result |
| `UPSTREAM_SERVICE` | An external service, policy, challenge, rate limit or freshness condition changed the result |

These labels describe failure responsibility; they do not diagnose a person, product or organization. Site- or tool-specific taxonomies may be useful locally, but they should not be exported as universal Moon Source doctrine without a separate reason.

## 9. Status contract

Bounded devices and procedures may use this public status contract:

| Status | Meaning |
|---|---|
| `OK` | The intended bounded operation completed without material item-level failure |
| `PARTIAL` | Useful output exists, but one or more items, fields or optional probes are incomplete |
| `ERROR` | The operation could not produce a usable bounded result, or a fatal failure prevented the contract from being met |
| `ABORTED_BY_GUARDRAIL` | The operation stopped because a safety, authorization, challenge, limit or boundary condition required it to stop |

`PARTIAL` is a valid result when the preserved corpus and its gaps are legible. It should not be silently upgraded to completeness.

## 10. Receipts and logs

A receipt should make the following inspectable when relevant:

- the observable action and invocation context;
- the device, adapter or procedure version;
- before/after state for a change;
- findings separated from errors and warnings;
- path, origin, dependency or version context that is safe to disclose;
- item counts, caps, stop reason and partial state;
- the recovery or next action;
- provenance sufficient to inspect what happened without exposing secrets.

Logs are evidence, not authority by themselves. A receipt can show what a tool observed or attempted; it does not prove that the observation was complete, truthful or legally sufficient without the appropriate source and validation.

## 11. Idempotency and bounded repetition

Where useful, repeated invocation should not duplicate, compound or corrupt an operation. Prefer:

- stable keys and deduplication;
- explicit run identifiers and checkpoints;
- bounded rounds, item caps and concurrency;
- dry-run output before apply;
- resume semantics that do not replay completed work blindly;
- clear handling for a changed upstream state.

Idempotency is a design goal, not a claim to make when the surface cannot support it. If repetition can compound a mutation, the device must say so and require a stronger gate.

## 12. Freshness gates

When a conclusion depends on current behavior, verify the relevant freshness boundary:

- version or release;
- endpoint or schema shape;
- service availability or policy response;
- browser/session state;
- dependency compatibility;
- the date of the receipt.

Do not call an external tool, service or surface “broken” from a historical observation alone. Mark the conclusion as stale, unverified or provisional when the needed current evidence is unavailable.

## 13. Recovery and escalation

After classification, choose the smallest safe response:

- retry only when the failure is transient and retry is bounded;
- resume from a checkpoint when completed work is trustworthy;
- quarantine or skip an item when per-item isolation is safe;
- roll back or restore when a mutation changed the wrong state;
- reconfigure only after the dependency is proven;
- stop on access challenges, repeated `403` / `429`, missing authorization or unsafe ambiguity;
- escalate with the evidence needed by the next responsible actor.

The operation is complete when the current state, remaining uncertainty and next responsibility are legible, not merely when a command exits with code zero.

## Minimal review checklist

```text
[ ] Problem reconstructed before mutation
[ ] Read-only inventory completed where relevant
[ ] Dependency staircase checked from lower layers upward
[ ] Instrument self-test / boot evidence available
[ ] Failure domain separated from target blame
[ ] Status and stop reason are explicit
[ ] Limits, pacing and idempotency considered
[ ] Same-session / upstream boundaries respected
[ ] Receipt preserves findings, errors, partial state and recovery
[ ] Freshness checked where the conclusion depends on it
[ ] Public claim does not exceed the observed bounded evidence
```

## Claim ceiling

This is a public execution-discipline component informed by repeated operational cases. It does not guarantee safe diagnosis, universal troubleshooting correctness, autonomous repair, complete logs, cross-platform behavior or successful recovery in every environment. It provides a responsibility and evidence contract for bounded work.

Use [Operational Devices](OPERATIONAL_DEVICES.md) when a procedure needs concrete embodiment, [Failure to Capability — Failure Foundry](FAILURE_FOUNDRY.md) when repeated failure may deserve a reusable artifact, and [Source Hygiene](SOURCE_HYGIENE.md) when the unresolved problem is stale, contradictory or bloated context rather than execution itself.

See [Evidence and Claims](../EVIDENCE_AND_CLAIMS.md) and [Public Boundary](../PUBLIC_BOUNDARY.md) for the public claim and disclosure limits.

<!-- MOON-SOURCE-PUBLIC-STAMP -->

---

> 🌙 **Moon Source** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Source/blob/main/LICENSING.md) · [Use & attribution](https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md) · [Full source (.zip)](https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip)
