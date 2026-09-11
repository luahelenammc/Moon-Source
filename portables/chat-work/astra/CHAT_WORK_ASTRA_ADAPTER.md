# Chat–Work Astra Strategy Adapter

*Optional subordinate adapter for model-specific frontier strategy without changing Chat–Work's model-neutral core*

## Public status

- **status:** current subordinate adapter; optional public guidance
- **version:** 1.2
- **versioning mode:** independently versioned subordinate submodule; the human title remains unversioned
- **first public release:** 2026-09-09
- **last material update:** 2026-09-10
- **lineage:** 1.0 initial public strategy adapter → 1.1 total-work efficiency calibration → 1.2 mandatory setup/customization contract and tighter Chat–Work integration
- **applies to:** Chat–Work Routing Protocol 5.1
- **effective date:** 2026-09-09
- **governing canonical body:** `portables/chat-work/CHAT_WORK_ROUTING_PROTOCOL_V4.md`
- **canonical release:** Chat–Work 5.1; the stable human title and V4 filename remain unchanged
- **MSL dependency:** Moon Source Language 5.1
- **authority:** subordinate adapter only; the Chat–Work canonical body governs on conflict
- **scope:** Astra-specific strategy geometry, reusable presets and volatile model/surface calibration
- **non-scope:** general routing law, universal model ranking, entitlement inference, benchmarks, pricing guarantees, hidden reasoning access or automatic autonomy

## Why this adapter exists

Chat–Work accumulated several mechanisms that were discovered or refined while working with frontier models such as Astra: the Intelligence Distillation Ladder, Decision Capsules, Return Capsules, Frontier Burst, Bounded Exhaustiveness, Decision Trace, Decision Sprint and Sprint Mode.

Those mechanisms are useful beyond Astra and therefore belong to the model-neutral core. What does **not** belong in the core is the assumption that Astra itself should always be used through one particular geometry.

Astra can be used as a bounded reasoning brain with almost no execution autonomy, but that is only one valid strategy. Another user may need a broad read-only review, iterative co-architecture, bounded mutation, sustained execution or a coherent frontier full run. The router should not confuse a model's capability with one author's preferred way of spending that capability.

> **Astra is a capability target, not a prescribed work style.**

This adapter makes Astra configurable without allowing Astra-specific habits or volatile product facts to colonize the general router.

## Core / adapter boundary

### Chat–Work core owns

The canonical Chat–Work protocol continues to own stable, model-neutral laws:

- sovereign object and observable delta;
- surface and harness routing;
- capability floor;
- reasoning effort as a separate dimension;
- Execution Profile and Run State;
- Budget Survivability;
- Context Diet;
- Intelligence Distillation Ladder;
- Bounded Exhaustiveness;
- source transport and authority;
- mutation authorization;
- Decision Trace semantics;
- Sprint as an optional run-level overlay;
- Native Parallelism Gate;
- verification, receipts and Chat Postflight;
- acceptance states and claim ceiling.

### Astra adapter owns

This subordinate adapter may organize:

- Astra role and autonomy strategies;
- Astra-specific context/corpus geometry;
- recurring Astra reference presets;
- strategy selection when Astra is actually available;
- date-sensitive observations about Astra behavior or product exposure;
- Astra-specific ergonomics and failure patterns;
- migration guidance when model economics or product surfaces change.

The adapter never creates a second semantic authority. It cannot waive safety, user authority, evidence, capability floor, source authority, scope ceilings, mutation permission, verification, claim ceilings or Chat Postflight.

## Orthogonal laws

The adapter begins with separation, not presets:

> **Model capability does not determine autonomy geometry.**

> **Reasoning depth is not execution autonomy.**

> **Context breadth is not mutation authority.**

> **Frontier capability is not a frontier full run.**

> **High autonomy is not unbounded scope.**

> **Sprint is not an Astra mode.**

> **Decision Trace is not Astra-only.**

> **An IDL brain burst is one Astra strategy, not Astra's identity.**

These distinctions prevent the router from turning a successful local workflow into a universal prescription.

## Astra Setup Contract

Astra must not begin from an author-imposed operating style. **Before this adapter compiles or executes an Astra strategy, an Astra Setup must be resolved.** This gate is mandatory on first activation in a run unless a verified persistent Astra profile already exists and the user explicitly chooses to reuse it.

Setup is not questionnaire debt. Resolve only the preferences that materially change the route. Unknown fields may remain `auto` or inherit Chat–Work only when the user has explicitly accepted that adaptive behavior. A reference preset may be recommended after setup, but it must never be silently treated as the user's default.

The setup may complete in one turn when the user supplies enough configuration. Otherwise, the router presents the smallest decision-bearing proposal and obtains the user's acceptance before Astra execution begins.

Supported setup modes:

- **AUTO** — compile a proposed Astra configuration from the task plus the active Chat–Work profile, disclose the material fields and let the user accept or override it;
- **PROFILE** — reuse a verified persistent Astra profile, while disclosing material run-specific deviations before execution;
- **RUN_OVERRIDE** — apply explicit one-run changes without mutating a reusable profile.

A portable setup shape is:

```yaml
astra_setup:
  mode: AUTO | PROFILE | RUN_OVERRIDE
  persistence: ephemeral | persistent | unknown
  objective: null
  role_preference: auto | judgment | reviewer | co_architect | executor | mixed
  autonomy_preference: auto | read_only | recommend | bounded_mutation | sustained_execution
  context_breadth_preference: auto | micro_capsule | bounded_corpus | broad_corpus | workspace_scale
  coverage_preference: auto | single_delta | sibling_docket | multi_domain | exhaustive_bounded
  reasoning_preference: adaptive | conserve | balanced | deep
  optimization_priority: inherit_chat_work | throughput_per_allowance | quality | latency | balanced
  parallelism_preference: inherit_chat_work | logical_only | bounded | permissive
  mutation_authority: inherit_chat_work | none | bounded_explicit | sustained_explicit
  return_preference: auto | return_capsule | decision_trace | structured_report | artifact | patch | evidence_receipt | mixed
  checkpoints: proportional | aggressive
  stop_condition: null
```

These are preferences and routing inputs, not capability claims. Setup cannot manufacture model availability, surface access, source authority, mutation permission, budget, persistence or safety clearance.

### Setup precedence

When Astra-specific preferences conflict, use this order:

1. safety, authority, evidence and capability-floor constraints;
2. explicit current-run Astra override;
3. explicitly selected persistent Astra profile;
4. active Chat–Work Execution Profile fields that are semantically compatible with Astra;
5. an accepted Astra AUTO proposal;
6. adapter reference presets only as recommendations.

Absence of a preference is not permission to infer one from Moon's habits, a model's prestige, a previous user's workflow or a preset name.

> **No Astra preset is the default. Setup chooses the strategy space; the compiler chooses within it.**

### Persistence boundary

A named Astra profile is reusable only when it is actually stored in a persistent source available to the current environment. Otherwise it is ephemeral. This inherits Chat–Work's Profile Persistence Law: never claim that Astra preferences were saved, remembered or made default without evidence.

Material changes in objective, authority, available surfaces, resource posture or desired autonomy reopen only the affected setup fields. Do not rerun the entire questionnaire ritualistically.

## Astra Strategy Profile

After Astra Setup is resolved, the strategy is compiled from independent dimensions. The exact syntax is illustrative; the semantic separation is load-bearing.

```yaml
astra_strategy:
  setup_ref: required
  role: judgment | reviewer | co_architect | executor | mixed
  autonomy: read_only | recommend | bounded_mutation | sustained_execution
  context_breadth: micro_capsule | bounded_corpus | broad_corpus | workspace_scale
  coverage_topology: single_delta | sibling_docket | multi_domain | exhaustive_bounded
  direction_constraint_density: tight | moderate | permissive
  mutation_authority: none | bounded_explicit | sustained_explicit
  reasoning_effort: adaptive
  return_geometry: return_capsule | decision_trace | structured_report | artifact | patch | evidence_receipt | mixed
  resource_overlay: inherit_chat_work
  parallelism: inherit_native_parallelism_gate
  checkpoints: proportional
  stop_condition: null
  fallback: null
```

`direction_constraint_density` describes how much freedom Astra has to explore and choose methods **inside the authorized task**. It never relaxes safety, source authority, mutation authority, privacy, scope authorization or the claim ceiling.

## Context Breadth Law

Raw document count is only one burden signal.

When selecting an Astra strategy, consider the geometry of the corpus:

- number of source families and authority domains;
- coupling among documents, topics and decisions;
- freshness and version conflicts;
- amount of context that must remain simultaneously coherent;
- reconstruction cost if the work is split into many calls;
- breadth and reversibility of possible mutation;
- verification and reconciliation burden;
- likely duration and interruption sensitivity.

Do not create universal thresholds such as `N documents = full run` or `N topics = frontier`. Ten independent files may be easier than three tightly coupled governing sources. Corpus geometry changes strategy; document count alone does not determine it.

## Role and autonomy are separate

A role describes what Astra contributes. Autonomy describes how far Astra may carry work without handing control back.

Examples:

- `judgment + read_only` can return one ruling without touching the object;
- `reviewer + recommend` can traverse a broad corpus and propose changes without mutation;
- `co_architect + bounded_mutation` can iterate on architecture and apply explicitly bounded edits;
- `executor + sustained_execution` can own a coherent implementation run when tools, permissions, budget, checkpoints and verification support it.

A user may deliberately choose low autonomy with very high reasoning capability. That is a resource strategy, not a deficiency. A different user may rationally choose high autonomy when repeated handoffs would destroy coherence or cost more than sustained frontier execution.

## Mutation Authority Law

Autonomy never manufactures permission.

`autonomy: sustained_execution` means the selected strategy permits a sustained execution shape **if** the underlying task already supplies legitimate mutation authority. If authority is absent, the same strategy must downshift to read, recommend, report or return a blocked authority condition.

> **Capability can propose a mutation geometry; only authority can permit mutation.**

## Reference presets

These are ergonomic starting points, not closed modes or defaults. They may be suggested only after Astra Setup has established the user's preferences and task envelope. A compiled strategy may mix fields differently when the task requires it.

### Astra Brain Burst / Judgment Burst

Use when frontier cognition is load-bearing but expensive execution is not.

Typical geometry:

```yaml
role: judgment
autonomy: read_only
context_breadth: micro_capsule | bounded_corpus
coverage_topology: single_delta | sibling_docket
return_geometry: return_capsule | decision_trace
```

This is the geometry behind strongly distilled Decision Capsules: prepare cheaply, buy the difficult ruling, return cheaply, implement and verify elsewhere.

It is especially useful when the user wants to spend Astra on cognition rather than tool loops or routine mutation. It must not become Astra's default identity.

### Astra Deep Review

Use when the value comes from seeing a broad body of material together without granting execution authority.

Typical geometry:

```yaml
role: reviewer
autonomy: read_only | recommend
context_breadth: broad_corpus
coverage_topology: multi_domain | exhaustive_bounded
return_geometry: structured_report | decision_trace | mixed
```

The review may be extensive. Decision Trace remains proportional: only materially consequential rulings need its full audit structure.

### Astra Co-Architect

Use when the task benefits from iterative architecture rather than a single ruling.

Typical geometry:

```yaml
role: co_architect
autonomy: recommend | bounded_mutation
context_breadth: bounded_corpus | broad_corpus
coverage_topology: multi_domain
return_geometry: structured_report | patch | artifact | mixed
checkpoints: proportional
```

This preset should preserve room for Astra to discover and compare architectural options while keeping scope, authority and acceptance explicit.

### Astra Executor

Use when frontier capability is materially useful during the execution itself rather than only before it.

Typical geometry:

```yaml
role: executor
autonomy: bounded_mutation | sustained_execution
context_breadth: bounded_corpus | broad_corpus | workspace_scale
return_geometry: artifact | patch | evidence_receipt | mixed
```

Requirements rise with autonomy:

- explicit mutation authority;
- real tools/surfaces observed as available;
- checkpoint and salvage strategy;
- tests/readback appropriate to the sovereign object;
- bounded scope and stop condition;
- evidence-bearing receipt;
- mandatory Chat Postflight.

Do not force extreme capsule distillation when sustained execution needs broader context to remain correct.

### Astra Full Run

Use only when decomposition would materially damage coherence or create greater cost/risk than one sustained frontier execution.

A Full Run may use broad corpus or workspace-scale context and substantial autonomy. It is still bounded by:

- Budget Survivability;
- source and mutation authority;
- explicit scope and stop conditions;
- Bounded Exhaustiveness where relevant;
- checkpoints and salvageability;
- tool/environment availability;
- verification and evidence;
- Chat Postflight.

`Full Run` means sustained responsibility, not unlimited responsibility.

### Astra Decision Sprint

Decision Sprint is the intersection of the generic Sprint overlay and the generic IDL sibling-delta exception. It is not the default for Astra and not the default for Sprint.

Typical geometry:

```yaml
role: judgment | mixed
autonomy: read_only | recommend
context_breadth: bounded_corpus | broad_corpus
coverage_topology: sibling_docket
resource_overlay: sprint
return_geometry: return_capsule | decision_trace | mixed
```

It is appropriate when a finite family of related decisions shares enough context that repeatedly reconstructing the same expensive frame would be wasteful or coherence-destroying.

## Astra Strategy Compiler

Resolve the strategy in this order:

1. **Astra Setup Gate** — which setup mode is active, which user preferences are explicit, which fields may adapt, and has the setup been accepted for this run?
2. **Sovereign objective and sovereign object** — what must actually change or be decided?
3. **Astra value test** — would Astra materially improve this task or irreducible slice, and is it actually available?
4. **Role** — judgment, review, co-architecture, execution or mixed within the accepted setup?
5. **Autonomy** — how far should Astra carry the work before returning control?
6. **Corpus geometry** — how much context and how many authority domains must remain coherent?
7. **Mutation authority** — what may Astra actually change?
8. **Coverage topology** — one delta, finite docket, multiple domains or explicit bounded exhaustiveness?
9. **Reasoning effort** — what depth is required independently of role/autonomy and consistent with the user's resource preference?
10. **Resource overlay** — normal Budget Survivability or an explicitly activated Sprint/perishable-capacity envelope?
11. **Return geometry** — ruling, trace, report, artifact, patch, receipt or a mixed return?
12. **Checkpoints and stop condition** — where can the run safely stop, salvage or re-enter?
13. **Verification and Chat Postflight** — what observable evidence closes the loop?

The compiler should choose the smallest structure that preserves the task's required autonomy and coherence **inside the accepted setup envelope**. It must not silently override user preferences merely because another preset looks more efficient. When a preference conflicts with safety, authority, capability floor or observed availability, disclose the conflict and downroute, request a bounded override or return a blocked condition rather than inventing consent.

## Chat–Work integration contract

The Astra adapter is not a parallel router. It is a subordinate strategy layer inside Chat–Work.

Chat–Work resolves the general Execution Profile, Run State, task requirements, authority and capability floor first. When Astra is selected as a possible capability target, the adapter then resolves the **Astra Setup Contract** before compiling model-specific strategy.

This creates a nested setup relationship:

```text
Chat–Work Setup
  → general surface / capability / resource / authority envelope
  → Astra selected as a possible target
    → Astra Setup
      → user-specific role / autonomy / context / effort / fanout / return preferences
      → Astra Strategy Compiler
        → bounded execution or return
  → Chat Postflight
```

Chat–Work may recommend Astra and may prefill an AUTO proposal from explicit profile data, but it must not silently choose Brain Burst, Deep Review, Co-Architect, Executor, Full Run, Decision Sprint, maximum reasoning, maximum autonomy or physical fanout on the user's behalf.

The same user may rationally configure Astra differently for different tasks. A persistent Astra profile is a convenience, not an identity claim or an immutable default.

## Relationship to IDL and capsules

The Intelligence Distillation Ladder remains model-neutral.

Decision Capsules and Return Capsules are tools for a particular geometry: bounded higher-tier judgment with lower-tier preparation and re-entry. They are excellent when the user wants Astra primarily as a brain. They are not mandatory wrappers for every Astra invocation.

When Astra is selected as executor, co-architect or full-run owner, the router may intentionally retain broader context and more operational autonomy when those are load-bearing and authorized.

The correct question is not:

> How do we force this task through an Astra capsule?

It is:

> What Astra strategy buys the most verified useful delta for this task, given the desired autonomy, corpus geometry, authority, resources and return contract?

## Relationship to Sprint

Sprint Mode remains a generic Chat–Work overlay. It can wrap Astra or another suitable capability tier.

Sprint may change the resource posture and pacing of an Astra strategy, but it does not choose Astra automatically, increase mutation authority, expand the docket or turn a bounded brain burst into a full execution run.

Likewise, Astra can be used in any strategy above without Sprint.

## Adapter calibration boundary

This section is empirical and replaceable. It never overrides the canonical
Chat–Work body, the active authority envelope or the claim ceiling.

**Last checked:** 2026-09-10

**Source class:** official product documentation for product behavior; dated
field reports for operational hypotheses.

The current official product documentation distinguishes Chat, Work and Codex
as different experiences and makes model, plan, workspace, rollout, tool and
surface availability conditional. It also treats model usage and resource
burden as task-, input/output-, settings- and mode-sensitive. These are live
calibration inputs, not permissions or stable protocol laws. The router must
probe the actual surface and model before routing work to Astra.

The name `Astra` in this document is a strategy-adapter target/alias. It does
not prove that a user has access to a model, surface, CLI, desktop capability,
connector, allowance, credit pool or any particular product configuration.

Date-sensitive Astra facts belong here, not in the stable router, when they
become necessary for routing. Examples include:

- where Astra is exposed;
- product-specific effort controls;
- current allowance or shared-pool behavior;
- observed tool or harness differences;
- dated operational failure patterns;
- current economic reasons to prefer brain-burst versus sustained execution.

Every volatile fact must be dated and sourced to appropriate current evidence. Anecdotes may inform a risk hypothesis but must not become a universal model property, benchmark or fixed cost law.

A trusted community field report dated 2026-09-09 described Astra expanding
open-ended completeness instructions into very large edge-case and test
sweeps. Treat this as anecdotal operational evidence, not a benchmark or
universal model property. When Astra is selected for sustained or frontier
execution, prefer explicit scope ceilings and stop conditions over vague
requests to “be balanced.”

### Total-work efficiency calibration — 2026-09-10

Recent community field reports converge on a useful operational hypothesis: a cheaper or lower-effort individual call can still be more expensive at task level when it causes extra continuations, repeated context ingestion, repair turns, tool cycles or agent fanout. Conversely, a higher-effort pass can be economically preferable when it resolves the same accepted result in materially fewer loops. Treat this as field evidence and routing guidance, not a fixed performance or pricing law.

The adapter therefore optimizes **total work to accepted state**, not nominal effort per turn.

Use three independent resource controls:

1. **Capability floor** — the lowest capability that can responsibly solve the irreducible task.
2. **Effort ceiling** — the lowest reasoning depth that resolves the current uncertainty without creating disproportionate downstream repair.
3. **Loop budget** — the tolerated burden from continuations, context rereads, tool calls, searches, retries and physical fanout before the route must pause and restructure.

Do not promote `light`, `medium`, `high`, `xhigh`, `ultra`, `fast` or any other product-specific label into universal doctrine. Start with the lowest effort that is plausibly sufficient, but apply a **reasoning-effort inversion test**: if lowering effort increases correction turns, repeated context processing, tool churn, reconstruction cost or total accepted-state latency, restore the higher effort rather than preserving a false local saving.

Apply the same logic to speed modes. A latency-premium mode is justified when human-visible response latency is itself the dominant bottleneck. It is usually poor value when execution time is dominated by external tools, browsing, tests, long-running operations or agent coordination. This is a bottleneck-allocation rule, not a ban on fast modes.

Apply the same logic to agents and parallelism. Physical fanout should earn its coordination tax. Prefer one capable owner when the work is tightly coupled, context-heavy or sequential; use subagents when work units are materially independent, context duplication is bounded and convergence cost is lower than the expected parallel gain. The generic Native Parallelism Gate still governs.

For Astra strategy selection, prefer this sequence:

> **Peak cognition at the bottleneck. Minimum sufficient cognition elsewhere. Minimize total work, not individual-turn expense.**

A route that looks cheaper because one turn is cheaper but requires many more turns is not automatically efficient. A route that looks expensive because one turn uses greater reasoning effort may still be the lower-cost route if it collapses the loop.

Useful current references:

- [ChatGPT Work and Codex](https://help.openai.com/en/articles/20001275-chatgpt-work-and-codex)
- [ChatGPT models](https://learn.chatgpt.com/docs/models)
- [Reasoning models](https://developers.openai.com/api/docs/guides/reasoning)
- [Custom instructions with AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md)
- [Codex CLI](https://learn.chatgpt.com/docs/codex/cli)

The adapter keeps this calibration outside stable Chat–Work law so that a
future model, surface or product change can replace these notes without
redesigning the routing core.

## Failure classes specific to strategy selection

The adapter may classify failures such as:

- `setup_bypass` — Astra strategy or execution began before the required setup envelope was resolved;
- `preset_capture` — a reference preset was silently treated as the user's default operating style;
- `profile_inheritance_overreach` — Chat–Work or a prior Astra profile supplied preferences that were not explicit, persistent or semantically compatible with the current run;
- `autonomy_underfit` — Astra was constrained to judgment when execution autonomy was load-bearing;
- `autonomy_overreach` — Astra received more execution freedom than the task or authority justified;
- `context_underfit` — over-distillation removed context needed for correct frontier work;
- `context_overload` — broad context was supplied without decision-relevant need;
- `capsule_monoculture` — a capsule workflow was applied by habit to a task whose geometry required another strategy;
- `frontier_execution_overkill` — expensive execution was used where a brain burst plus cheaper implementation would have sufficed;
- `effort_underfit_loop_amplification` — lower reasoning effort reduced local cost but increased continuations, repairs, context rereads or tool churn enough to worsen total-work efficiency;
- `fanout_coordination_overhead` — subagents or parallel branches duplicated context or coordination work without sufficient independent-work benefit;
- `latency_premium_mismatch` — a speed-premium mode was used while external tools or execution, rather than model response latency, dominated the run;
- `strategy_surface_mismatch` — the chosen role required tools/persistence unavailable on the selected surface;
- `adapter_staleness` — dated Astra calibration was treated as current after its freshness boundary.

These are routing diagnoses, not claims about the model's private internals.

## Relationship to Chat–Work 5.1

**Current Astra adapter version: 1.2.** Chat–Work itself remains 5.1: this adapter version is subordinate and independently tracked, while the governing router keeps its stable release identity.

Chat–Work 5.1 adds only the generic boundary that makes this adapter
legitimate. The canonical body retains the stable routing laws; this document
supplies optional Astra-specific strategy geometry and calibration. The
adapter is not a new capability, a second registry identity or a replacement
for the canonical portable.

The release is coherent only when:

- an unknown user can choose Astra as brain, reviewer, co-architect, executor or mixed without contradicting the core;
- role, autonomy and mutation authority remain independent;
- corpus breadth changes strategy without fake document-count thresholds;
- capsules remain optional and contextual;
- Sprint remains an independent overlay;
- broad context and sustained execution are allowed when genuinely load-bearing;
- presets remain examples rather than a closed taxonomy;
- volatile Astra facts can change without requiring general-router doctrine to change;
- no native feature, entitlement, benchmark or guaranteed-economics claim is introduced;
- the canonical Chat–Work body remains the single semantic authority.

## Claim ceiling

This adapter is a routing and strategy layer. It does not claim that Astra has
one correct use, that Astra is always the best frontier route, that any user has
access to it, that hidden reasoning can be exposed, that high autonomy is
always beneficial, that broad context always improves results, or that any
specific strategy guarantees better quality or lower cost.

Its purpose is narrower:

> **Preserve Astra's plurality of legitimate work styles while keeping Chat–Work's core model-neutral, auditable and user-configurable.**

<!-- MOON-SOURCE-PUBLIC-STAMP -->

---

> 🌙 **Moon Source** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Source/blob/main/LICENSING.md) · [Use & attribution](https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md) · [Full source (.zip)](https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip) · Questions, suggestions, or proposals? Feel free to contact me at [LuaHelenaMMC@gmail.com](mailto:LuaHelenaMMC@gmail.com).