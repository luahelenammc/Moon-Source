# 🛠️ Operational Devices — Moon Source component

An **operational device** is a bounded operational embodiment of a reusable procedure on a concrete execution surface.

> A procedure describes how work should be done. An operational device embodies a bounded procedure on a concrete execution surface.

The device is useful when a recurring method needs an explicit trigger, state, guardrail, failure behavior and observable output. It does not become a source of authority merely because it is executable or documented.

**MSL profile:** 5.1-compatible Markdown-native method surface; preserve the procedure/device distinction and execution-surface boundary.

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

## Conversation-native interactive response tools

Some AI conversations can present a working, task-specific interface directly in an answer: editable inputs, checklists, comparisons, simulations, charts or step-by-step controls. This is a **response instrument**, not automatically an installed application or an operational device. It earns a device contract only if there is an actual recurring procedure with a named executable surface, invocation, bounded state, guardrails and observable results. This distinction prevents a convenient chat control from impersonating source authority or persistent infrastructure.

### Choose the operation before the widget

First ask what the person needs to *do with* the answer. A useful set of reusable operations is:

| Operation | User capability | Possible response instrument |
|---|---|---|
| **Change** | Adjust assumptions and inspect consequences | Savings projection or budget allocator with editable inputs |
| **Select** | Assign, tick, include or exclude items | Shared-expense allocation or grouped checklist |
| **Compare** | Apply common criteria to alternatives | Plan selector with actual usage and transparent pricing rules |
| **Sequence** | Work through dependent steps | Scalable recipe, study sequence or staged review |
| **Evaluate** | Attempt, receive feedback and identify gaps | Quiz with explanations and a revision queue |
| **Replan** | Recalculate the unfinished work after real progress | Study or project plan that preserves completed work and redistributes remaining tasks |

These operations are composable, not six mandatory interfaces or six new Moon Source capabilities. The best answer may still be a sentence, table or ordinary document. A user should not have to learn a special prompt formula to receive a useful presentation when their intent is already clear.

### Response-instrument contract

1. **Purpose and eligibility.** Identify the actual human decision or task and test whether interaction offers more value than text. Do not turn routine answers into dashboards by default.
2. **Inputs and provenance.** Use real supplied or retrieved data; identify assumptions, missing fields, units and freshness. Do not populate plausible but invented prices, scores, baselines or availability.
3. **Controls and transformation.** Make each exposed control functional and bind it to explicit calculations, criteria, constraints or dependencies. Label the controls clearly; show units, precision and any important rounding.
4. **Result and delta.** Show the answer after a change and explain consequential differences, remaining amounts, trade-offs or unmet conditions. Essential information must stay readable without interaction.
5. **Replanning semantics.** When progress changes, preserve the baseline and genuinely completed items. Reallocate only the remaining work, taking available time, priority, blockers and dependencies into account. Report the new plan and the cost of changed assumptions; never silently mark work done.
6. **State and authority.** Distinguish ephemeral view state, supported same-conversation state, exported data, governed persistent records and third-party actions. A checkbox does not write to a source-of-record; a button is not permission to send, purchase, publish, schedule or modify an external system. Use an authorized connector or runtime and verify the resulting action separately.
7. **Accessibility and postflight.** Prefer short labels, usable mobile layouts, numerical sanity checks, reset/revision paths where meaningful and meaningful text fallback. Verify dependent outputs update together and that empty, extreme and conflicting inputs fail visibly rather than returning misleading certainty.

A timer, drag handle, export button or persistent checkbox should only be offered as *working* when the current client actually supports that interaction. Otherwise use a supported alternative and state the boundary. A working interactive answer is not, by itself, a reusable web application, standalone HTML, a packaged module or a live integration.

### Try the pattern without over-specifying the layout

> Using these actual [items, amounts, rules], help me [make a decision or complete a task]. Let me change [inputs], select [items] and compare [results]. Recalculate [output and remaining work] when I change a value or mark a step finished. Show assumptions and limitations; do not execute any external changes. If interactive controls are unavailable, give me a usable non-interactive alternative.

This is an optional formulation, not an activation spell. For higher-risk cases, decide authorization, privacy, jurisdiction and correctness before optimizing the presentation. When reliable persistence, long-running execution, external integrations or independent distribution are necessary, route to the appropriate application, workflow or [Adaptive Orchestration Protocol](../portables/adaptive-orchestration/ADAPTIVE_ORCHESTRATION_PROTOCOL.md). An interactive response remains subordinate to the source-of-record and the execution surface's controls.

### Capability boundary and provenance

OpenAI documented **Intelligent UI in GPT-6 ChatGPT** on 2026-10-07, including composable text, visualizations, buttons, forms and interactive tools inside a conversation; availability depends on the supported Chat client and model setting. This public method is vendor-neutral: it describes how to *design and check* a bounded interactive answer, not how to call undocumented platform APIs or guarantee equivalent UI in every AI product. See the [OpenAI launch](https://openai.com/index/gpt-6-for-everyone/) and [Intelligent UI help](https://help.openai.com/en/articles/20001598-intelligent-ui-in-chatgpt) for volatile product-specific behavior.

**Community provenance:** the operational examples and change/select framing were informed by u/Professional-Rest138, “10 things to ask GPT-6 to build you now that ChatGPT answers with working tools instead of text,” r/PromptEngineering (excerpt supplied 2026-10-18); a comment by u/Educational-View8524 specifically suggested redistributing unfinished study topics after actual progress. The source was a practical inspiration, not a validated performance study, an implementation dependency or evidence of external adoption. The reusable six-operation contract and governance constraints above are a Moon Source adaptation.

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

> 🌙 **Moon Source** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Source/blob/main/LICENSING.md) · [Use & attribution](https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md) · [Full source (.zip)](https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip) · Questions, suggestions, or proposals? Feel free to contact me at [LuaHelenaMMC@gmail.com](mailto:LuaHelenaMMC@gmail.com).
