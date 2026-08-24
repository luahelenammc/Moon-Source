# Operational Devices

An **operational device** is a bounded operational embodiment of a reusable procedure on a concrete execution surface.

> A procedure describes how work should be done. An operational device embodies a bounded procedure on a concrete execution surface.

The device is useful when a recurring method needs an explicit trigger, state, guardrail, failure behavior and observable output. It does not become a source of authority merely because it is executable or documented.

## Responsibility contract

| Object | Owns | Does not replace |
|---|---|---|
| Source | Facts, decisions, rules, current state and authority | A procedure or runtime |
| Procedure | A reusable way of working, including sequence and quality checks | A source of truth for every claim |
| Operational device | A bounded embodiment of that procedure on a named surface | Source authority, unrestricted automation or new privilege |
| Adapter | The binding between a generic device and one concrete surface | The generic device contract or the surface's authority |
| Runtime / surface | The environment in which the device can actually operate | Proof that documentation alone can execute |
| Receipt / checkpoint | Observable action, state, findings and recovery information | A claim of correctness by itself |

The core relation is:

```text
procedure
  → operational device
  → concrete execution surface / runtime
  → action + observable state + receipt
```

An adapter may bind the device to a browser page, console, launcher, local workflow or another bounded surface. The generic device and the adapter should remain distinguishable so that a surface-specific assumption does not masquerade as a universal capability.

## When a device earns existence

Choose an operational device when all of the following are true:

- a procedure recurs often enough that invocation cost or inconsistency matters;
- the execution surface can be named and its authority is legitimate;
- the operation has a bounded input and output;
- state, stop conditions and failure behavior can be made visible;
- a read-only or dry-run path is possible where mutation would be risky;
- a human or responsible system can inspect the resulting receipt;
- a simpler source, checklist, protocol or handoff would not already carry the work adequately.

Do not create a device merely because a procedure has a memorable name, because a script is convenient, or because a repository would look more complete with another folder. A documented procedure is still the right form when there is no concrete execution surface or when the operation cannot be bounded honestly.

## Public device contract

An operational device should make these fields legible before it runs:

| Field | Public responsibility |
|---|---|
| Identity and version | Identify the device and the public revision being invoked |
| Execution surface | Name the browser, console, workflow, local tool or other surface without implying broader reach |
| Trigger | State when the device should be invoked |
| Inputs | Define the minimum data or context required |
| State | Expose checkpoints, progress, limits and current run state |
| Guardrails | State read-only defaults, authorization assumptions, stop lines and prohibited bypasses |
| Action | Describe the bounded operation the device performs |
| Failure behavior | Separate target, instrument, environment, dependency, instruction, interaction and upstream failures where relevant |
| Output / receipt | Return inspectable results, warnings, errors, counts or recovery information |
| Freshness | Identify assumptions that can change when the surface or upstream service changes |
| Recovery | Describe retry, resume, rollback, quarantine or safe escalation when applicable |
| Claim ceiling | State what the device demonstrates and what it does not establish |

The execution authority of a device must not exceed the legitimate authority already available on its surface. A device may make an operation easier to invoke; it does not authorize access, defeat a control or transfer ownership.

## Generic device and surface adapter

Keep the following boundary explicit:

```text
generic device contract ≠ surface-specific adapter
```

A generic device can define discovery, bounded loading, deduplication, checkpointing, receipts and export. An adapter supplies the surface-specific details: selectors, API shapes, stable identifiers, schema mapping, enrichment and freshness notes.

An adapter should declare at least:

- adapter name and version;
- intended origin or execution surface;
- discovery strategy;
- stable-key extraction;
- semantic extraction and optional enrichment;
- schema mapping;
- stop and limit assumptions;
- known fragility and freshness notes;
- whether same-session, same-origin access is needed;
- the read-only and no-bypass boundary.

The device must not guess an adapter for a real site, infer a private endpoint, or silently turn a site-specific assumption into a public guarantee.

## Invocation lifecycle

1. **Reconstruct the need.** Identify the literal request, operational pain, likely failure layer, risk, missing evidence and smallest safe movement.
2. **Preflight the surface.** Prove that the intended surface and its legitimate session are present before relying on a dependent operation.
3. **Bind the adapter.** Record the surface-specific assumptions and the freshness boundary.
4. **Run bounded execution.** Apply caps, pacing, concurrency limits, read-only defaults and per-item fault isolation.
5. **Write observable state.** Preserve live checkpoint information without secrets and produce a receipt with findings separated from errors.
6. **Read back.** Count and inspect the result before declaring success; a partial, safe result is preferable to an inflated completeness claim.
7. **Recover or update.** Resume, retry, rollback, quarantine or escalate according to the classified failure. Update the smallest authoritative source when a reusable learning has actually been validated.

## Authenticated Session Runtime

Some devices operate inside a session the user has already legitimately opened. This does not grant the device a new credential boundary.

Same-session access is acceptable only when:

- the call is initiated by the current page or session;
- normal browser Same-Origin / CORS rules are respected;
- credentials remain in the browser and are never read, exported or logged;
- the operation is within the user's legitimate authorization;
- a challenge, repeated `403`, `429` or access-control response stops or reclassifies the run;
- account-state mutation is explicitly outside the reference device unless a separate, authorized contract says otherwise.

The browser reference in [`examples/browser-console-device/`](../examples/browser-console-device/) is intentionally synthetic and experimental. It demonstrates same-origin enrichment on `localhost`; it is not a production crawler, extension, bookmarklet, userscript or cross-origin access layer.

## Operational record template

Use this compact record when designing or reviewing a device:

```text
Device:
Version:
Procedure embodied:
Execution surface:
Trigger:
Inputs:
Read-only / mutation mode:
State and checkpoint:
Guardrails and stop conditions:
Failure domains:
Output / receipt:
Recovery path:
Freshness assumptions:
Known adapter-specific fragility:
Claim ceiling:
```

## Public boundaries

The public component may expose a device contract, responsibility distinctions, bounded interfaces, synthetic examples, qualitative reliability rules and inspectable receipts.

It does not expose or imply:

- private adapters, selectors, endpoints, corpora or account state;
- credentials, cookies, tokens, passwords or authentication headers;
- CAPTCHA, paywall, access-control or rate-limit bypass;
- stealth persistence, fingerprint spoofing or CORS/Same-Origin disablement;
- automatic adapter generation or universal cross-site stability;
- a runtime, service or product where only a document or bounded example exists;
- private promotion thresholds, compiler ordering or evaluation machinery.

## Claim ceiling

This is a public responsibility pattern for bounded operational embodiments. It does not establish universal runtime support, automatic adapter generation, cross-surface stability, autonomous operation, safety in every environment or external adoption. The synthetic Browser Console Device is an experimental reference implementation with a deliberately narrow claim ceiling.

Use [Operational Reliability](OPERATIONAL_RELIABILITY.md) for execution discipline, [Failure to Capability — Failure Foundry](FAILURE_FOUNDRY.md) when repeated failure may deserve a reusable artifact, and [Procedural Projection](PROCEDURAL_PROJECTION.md) for the relationship between governing source, procedure and portable projection.

See [Public Boundary](../PUBLIC_BOUNDARY.md), [Evidence and Claims](../EVIDENCE_AND_CLAIMS.md) and [Existing Implementations](EXISTING_IMPLEMENTATIONS.md) for the public evidence and disclosure limits.

<!-- MOON-SOURCE-PUBLIC-STAMP -->

---

> 🌙 **Moon Source** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Source/blob/main/LICENSING.md) · [Use & attribution](https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md) · [Full source (.zip)](https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip)
