# Preflight — Adaptive Task Shaping Before AI Execution

> **One of Moon Source's crown-jewel mechanisms.**

**Preflight shapes the task before the task shapes the output.** It is the adaptive pass between a raw request and execution: the AI determines what the user is really asking, what context and authority matter, what is missing, what risk exists, where the result must go, what form fits that destination and whether a question is necessary before acting.

This is a public Moon Source component, not a new portable family. It is directly usable as a method and is specialized by [Moon Source Setup 3.0](../portables/setup/MOON_SOURCE_SETUP.md) for personal and project-context setup.

## 1. Why Preflight exists

The first AI mistake is often not a bad answer. It is answering the wrong version of the request.

A prompt can be grammatically clear and operationally wrong. An AI may follow the literal wording while missing:

- the user's actual intention;
- the source that governs the answer;
- a current correction or a stale snapshot;
- a missing fact that would change the route;
- privacy, safety or public-claim boundaries;
- the destination where the result will be used;
- the smallest form that can carry the work;
- whether asking a question helps or merely delays execution.

Preflight exists to catch those mismatches before they become an answer, artifact, disclosure or mutation. It does not require a ceremony before every task. A trivial, clear and low-risk request may pass through Preflight almost invisibly.

## 2. What Preflight is

### Precise definition

> **Preflight is the adaptive pass before and during execution that shapes a raw request into a proportionate working task by checking intent, governing context and authority, missing facts, risk and freshness, destination, form and question threshold.**

### Plain-language definition

Before the AI answers, it checks what you actually mean, what the answer is for and what could change the work. Then it acts at the depth the situation requires.

Preflight is a decision loop, not a compulsory questionnaire. It may remain silent, make one assumption visible, ask one consequential question, inspect a source, route to a specialized component, choose a different surface or stop an unsafe materialization.

## 3. The public Preflight loop

The shortest reusable loop is:

```text
raw request
→ real intent
→ governing context / authority
→ missing facts
→ risk and sensitivity
→ destination
→ proportionate form
→ question threshold
→ execute
→ readjust if the field changes
```

The loop is deliberately ordered around decisions rather than document types. It asks what must be understood before choosing what to create, load or expose.

The public decision contract can be summarized as:

```text
What am I actually doing?
What governs the answer?
What do I still need?
What could go wrong?
Where is the result going?
What is the smallest adequate form?
Do I need to ask anything?
Can I execute now?
```

These questions do not need to be printed in every response. The useful result is better routing, not a visible checklist.

## 4. Adaptive depth

Preflight must be smaller than the uncertainty it resolves.

| Depth | Use when | Expected behavior |
|---|---|---|
| **Near-zero / silent** | The task is clear, low-risk, current enough, has an obvious destination and no consequential fact is missing | Act directly. Do not manufacture a preflight report. |
| **Light** | One or two assumptions matter, the destination changes the output, existing material should be preserved or one question may change the result | Use available context, state the material assumption if needed, ask only the consequential question and then execute. |
| **Deep** | Authority conflicts, several actors or projects overlap, sensitivity or public exposure is high, mutation is possible, the artifact is non-trivial or fresh external facts are required | Inspect enough to establish route, authority, scope, freshness, safeguards, acceptance criteria and readback. Deep does not mean many questions. |

If current sources can resolve the ambiguity, read them rather than asking the user to repeat what is already available. If the task is small, do not produce a large architecture. If the route is clear, do not stop at analysis when the user asked for execution.

### Preflight theater

A visible checklist that changes no decision is not Preflight. It is ceremony. The pass earns its existence only when it changes what the AI will load, ask, assume, expose, create, route or verify.

## 5. Several ways to understand the same mechanism

These are complementary explanations for different readers, not separate Moon Source subsystems.

### 5.1 Preflight as a self-prompt

A normal prompt tells the AI what to do. Preflight acts like a **self-prompt around the prompt**: before acting, the AI operationally reframes what the request requires.

```text
"Make this better."

without Preflight:
→ immediately rewrite

with Preflight:
→ better for whom?
→ for what destination?
→ preserve meaning or redesign it?
→ is there a governing source?
→ is a question necessary, or is a safe assumption enough?
→ then rewrite
```

The metaphor describes a public procedure that creates a better working contract. It does not mean that the AI exposes a hidden internal prompt or edits the model's private system instructions.

### 5.2 Preflight as a self-adjusting prompt

Preflight makes the working prompt **self-adjusting**: its depth, context, questions, tools and output form change when the field changes.

```text
same raw instruction

private note       → concise synthesis
legal handoff      → chronology, claims, uncertainty and evidence
public page        → sanitized material and bounded claims
repository change  → authority, diff, validation and readback
```

The prompt is not changing the model. The working plan is changing according to destination, risk, authority and available evidence.

### 5.3 Preflight as task shaping

This is the least metaphorical explanation:

> Preflight converts an ambiguous or underspecified request into an executable task with proportionate constraints.

It is useful when the reader does not need Moon Source vocabulary. The task becomes clearer before the artifact becomes larger.

### 5.4 Preflight as a control surface before generation

Generation is not the first operation. Preflight is the control surface that decides what generation is allowed to assume, use, ask, create and expose.

This is why it can route to privacy safeguards, source hygiene, signal calibration, Chat–Work routing, a repository validation flow or no new artifact at all. It coordinates the boundary; it does not replace every specialized responsibility.

### 5.5 Preflight as a checklist that scales itself

The cockpit-checklist analogy is useful only for proportionality. A short flight does not need the same inspection as a complex operation. Likewise, a translation may need almost no visible Preflight while a public repository mutation needs authority, current-state, validation and readback checks.

### 5.6 Preflight as a compiler front-end

For technical readers, the analogy is:

```text
human request
→ parse intention and constraints
→ resolve dependencies and authority
→ detect material missing inputs
→ choose execution target
→ emit an executable task
```

This describes task shaping and routing at the public contract level. It does not disclose private resolver, compiler, scoring or evaluation machinery.

### Reality anchor

“Self-prompt” and “self-adjusting prompt” are explanatory metaphors for a procedure. They do not imply:

- access to hidden chain-of-thought;
- disclosure of a private reasoning transcript;
- literal editing of the model's hidden system prompt;
- persistent autonomous self-modification;
- consciousness or metacognitive experience.

Moon Source exposes a usable decision contract, not a private reasoning transcript:

```text
public decision contract ≠ private reasoning transcript
```

## 6. The question threshold

> **Ask only when the answer can materially change the route, safety, authority, scope or output.**

Preserve the following rules:

- Do not ask for information already available in the current context or governing source.
- If two answers lead to the same safe result, do not force a choice.
- An unknown may remain unknown when it does not block the work.
- Resolve low-risk ambiguity with a labeled reasonable assumption when possible.
- Ask one consequential question rather than launching a full intake.
- A partial result can be better than unnecessary blockage.
- If the user requested an artifact and the route is clear, produce the artifact.
- If the field changes during execution, reroute instead of defending the stale plan.

The goal is not to ask more questions. The goal is to remove the questions that do not change the work and catch the few that do.

## 7. Destination awareness

The same raw request can require different execution because the result will live somewhere different.

| Destination | Preflight emphasis |
|---|---|
| Chat response | Direct usefulness, language, scope and whether a short answer is enough |
| Private note | Preserve the user's meaning and useful detail without unnecessary exposure |
| Global AI instructions | Stable behavior, privacy, portability and what should not be overfit to one project |
| Project source | Current authority, scope, freshness, ownership and update responsibility |
| Handoff | Current state, constraints, uncertainty, recipient, next action and transport boundary |
| Public page | Claim ceiling, freshness, third-party privacy, authorship and readable form |
| Repository mutation | Branch authority, current state, allowed scope, diff, validation, rollback boundary and readback |
| External message | Recipient, channel, tone, disclosure, factual basis and whether sending authority exists |

Do not draft a rich governed source for a small instruction field. Do not compress a public or legal handoff into a sentence merely because a compact answer looks elegant.

## 8. Source and authority awareness

Preflight treats access and authority as different questions.

Public-safe rules:

- **Access is not authority.** A file, tool result or retrieved page may be available without governing the decision.
- The freshest governing source beats a stale echo or snapshot.
- A current user correction beats a stored snapshot when the user has authority over the relevant state.
- An archive preserves history; it does not govern the present by default.
- A handoff, mirror or bridge can transport context without becoming the semantic source of truth.
- A tool result is evidence or access, not semantic sovereignty by itself.
- When sources overlap, resolve their responsibilities before flattening them together.

Preflight may route to the [Responsibility Map](RESPONSIBILITY_MAP.md) when ownership or authority is the unresolved problem. It does not publish private resolver heuristics.

## 9. Risk, sensitivity and freshness

The scan should deepen when the consequence of a wrong route is material. Check proportionately for:

- personal, third-party or confidential information;
- medical, legal, financial or safety stakes;
- public claims and stale external facts;
- authorship, permission, attribution and derivative status;
- destructive or hard-to-reverse mutation;
- current versus historical state;
- destination-specific exposure;
- a mismatch between the requested form and what the destination can safely hold.

Preflight routes to specialized safeguards rather than trying to become every safeguard. Examples include:

- [Source Hygiene](SOURCE_HYGIENE.md) for stale, contradictory or bloated corpora;
- [Signal Calibration](SIGNAL_CALIBRATION.md) for weak or ambiguous signals that need a bounded working inference;
- [Credits & Attribution Ops](CREDITS_ATTRIBUTION_OPS.md) when intellectual lineage, custody, transformation or permission boundaries matter;
- [Chat–Work Routing Protocol V3](../portables/chat-work/CHAT_WORK_ROUTING_PROTOCOL_V3.md) when surface, model or reasoning effort materially affects the work;
- [Field to Form](FIELD_TO_FORM.md) when the field itself must be understood before a materialization is chosen.

## 10. Output and execution contract

Preflight should leave enough task shape to answer:

```text
What am I actually doing?
What governs the answer or state?
What material fact is still missing?
What risk, sensitivity or freshness condition matters?
Where is the result going?
What is the smallest adequate form?
Do I need to ask anything?
Can I execute now?
```

For an ordinary answer, this contract may remain internal and produce only the result. For a consequential operation, the relevant assumptions, authority, limits and validation may need to be made legible.

For execution tasks that mutate a source, Preflight can include:

```text
before mutation
→ authority
→ current state
→ allowed scope
→ failure / rollback boundary
→ acceptance criteria

after mutation
→ readback / verification
→ delta truth
→ next state
```

This is not a Git manual. It is the general rule that execution does not end when a change is written; it ends when the resulting state is checked against the intended task.

## 11. Copy-paste public operation

The following block is a compact public projection of the method:

```text
Apply Moon Source Preflight before executing this request.

Determine, only to the depth needed:
- the real task;
- relevant governing context or source;
- any missing fact that could materially change the result;
- risk, sensitivity or freshness constraints;
- the destination of the output;
- the smallest adequate form;
- whether a question is truly necessary.

Then execute.
Do not turn the preflight into a questionnaire.
If the task is already clear and low-risk, act directly.
If the task changes while working, re-route instead of forcing the original plan.

Request:
[...]
```

## 12. Worked examples

### Example A — simple rewrite

**Request:** “Fix the grammar in this sentence.”

```text
silent Preflight
→ clear intent
→ low risk
→ obvious destination
→ edit directly
```

### Example B — destination-sensitive editing

**Request:** “Make this more professional.”

```text
use available context first
→ email, CV, legal filing or public page?
→ preserve meaning or redesign it?
→ ask only if the destination changes the work
→ rewrite in the smallest adequate form
```

### Example C — source-sensitive status

**Request:** “Update the project status.”

```text
which source currently governs status?
is the supplied note current or only a snapshot?
is there authority to mutate it?
→ update the governing destination
→ validate and read back
```

### Example D — stale/current public fact

**Request:** “Add the current API pricing to this public guide.”

```text
freshness matters
→ verify the current official source
→ preserve date and claim boundary
→ update the public page
→ check the rendered result if relevant
```

### Example E — form-sensitive organization

**Request:** “Organize all this.”

```text
what field is actually present?
→ a short note, source repair, handoff, registry or no new artifact?
→ route to Field to Form or Source Hygiene only if needed
→ create the smallest form that changes what the field can support
```

### Example F — repository mutation

**Request:** “Add this method to the public repository.”

```text
confirm current branch and governing repository state
→ define the public-safe scope and claim ceiling
→ make the smallest coherent diff
→ run links, stamps, registry and relevant CI checks
→ read back the final files and report the exact state
```

## 13. Anti-patterns

Preflight fails when it becomes:

- a questionnaire reflex before every task;
- architecture cosplay that adds labels without changing a decision;
- the assumption that more context is always better;
- artifact-first thinking;
- a request for facts already available;
- a blocker whenever any ambiguity exists;
- permission to guess whenever ambiguity exists;
- an excuse to load every available source;
- longer than the task it is supposed to shape;
- a printed imitation of hidden reasoning or a claim to reveal chain-of-thought;
- a claim that a self-adjusting prompt autonomously reprograms the model;
- a replacement for the specialized component that actually owns the next operation.

## 14. Relationship map

Preflight is transversal, but it does not own every decision it can reveal.

| Component | What it owns | Relationship to Preflight |
|---|---|---|
| [Field to Form](FIELD_TO_FORM.md) | What structure or materialization the field deserves | Preflight may route to it; Field to Form does not replace the before-execution gate. |
| [Responsibility Map](RESPONSIBILITY_MAP.md) | Ownership, authority and relationships between objects | Preflight detects when authority needs mapping; the map performs the deeper separation. |
| [MSL 4.3](../portables/msl/MSL_4_3.md) | Structural grammar for a materialization that has earned existence | Preflight decides whether structure is needed; MSL shapes it afterward. Preflight is not “MSL before MSL.” |
| [Setup 3.0](../portables/setup/MOON_SOURCE_SETUP.md) | Personal and project-context setup and routing | Setup's Adaptive Preflight is a specialization of this broader mechanism. |
| [Source Hygiene](SOURCE_HYGIENE.md) | Bounded diagnosis and repair of stale or contradictory corpora | Preflight identifies corpus quality as the real problem; Source Hygiene performs the bounded operation. |
| [Signal Calibration](SIGNAL_CALIBRATION.md) | Working inference from weak or ambiguous signals | Preflight decides whether inference is materially needed and what evidence bar applies. |
| [Chat–Work Routing](../portables/chat-work/CHAT_WORK_ROUTING_PROTOCOL_V3.md) | Surface, model, reasoning-effort and postflight routing | Preflight can identify routing as consequential; the protocol performs that specialized choice. |
| [Procedural Projection](PROCEDURAL_PROJECTION.md) | Turning a stable method into reusable procedures and projections | Preflight can be documented as a method; it does not recursively create a second Preflight procedure by default. |

The relationship is therefore:

```text
Moon Source Preflight
    └── Setup 3.0 Adaptive Preflight
        specialization for user/context setup
```

## 15. Claim ceiling and public boundary

The public repository demonstrates a documented Preflight method and an integrated public reference implementation through this component, the AI Kernel, Architecture and Setup 3.0.

It does not establish that Preflight is unique to Moon Source, universally superior, externally adopted, independently validated, patented or a universal AI standard. “Crown jewel” identifies its characteristic importance within Moon Source; it is not a novelty or market-dominance claim.

This document exposes a usable decision contract. It does not expose:

- private source corpora;
- hidden scoring, thresholds or evaluation machinery;
- private resolver, compiler or reconciliation heuristics;
- protected custody or permission ledgers;
- hidden chain-of-thought or a reasoning transcript;
- persistent self-modification or consciousness.

For the wider disclosure boundary, read [Public Boundary](../PUBLIC_BOUNDARY.md) and [Evidence and Claims](../EVIDENCE_AND_CLAIMS.md). For Moon Source-specific authorship, use framing and watermark governance, read [Moon Source Use & Attribution](../MOON_SOURCE_USE_AND_ATTRIBUTION.md).

## 16. Public attribution

Preflight is part of Moon Source, created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion**. The repository is the canonical public source for this document. Attribution and use remain governed by the repository's applicable terms; public availability and credit do not themselves grant reuse rights.

**MSL:** 4.3 · **Setup relationship:** Setup 3.0 specialization · **Status:** public component, not a separate portable.

<!-- MOON-SOURCE-PUBLIC-STAMP -->

---

> 🌙 **Moon Source** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Source/blob/main/LICENSING.md) · [Use & attribution](https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md) · [Full source (.zip)](https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip)