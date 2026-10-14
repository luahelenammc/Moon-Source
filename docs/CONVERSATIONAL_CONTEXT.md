# Conversational Context — Applied Integration Contract

**Status:** reusable architecture composition and synthetic technical reference. This is **not** a seventeenth Moon Source capability, a standalone portable, an LLM, a runtime, a product, or a real-world deployment.

A consumer chat window is one possible interface for AI. A product may instead assemble state from APIs, queries, spreadsheets, conversation events, and a program database. The context problem has not disappeared: it has moved into the interaction among **person, dialogue, governed operational state, permissions, and human decisions**.

This guide defines a small implementation contract for that interaction. It is subordinate to [Field to Form](../ARCHITECTURE.md), [Connected Sources](CONNECTED_SOURCES.md), [Procedural Projection](PROCEDURAL_PROJECTION.md), [Operational Devices](OPERATIONAL_DEVICES.md), and [Operational Reliability](OPERATIONAL_RELIABILITY.md). Do not copy their semantic contracts into a competing module.

## 1. What changes in an API-native product?

| Dimension | A document-centered assistant may ask | A conversational application must also ask |
|---|---|---|
| Information | Which document or source governs this claim? | Which API/query/state field describes the person's *current* situation? |
| Temporal context | Is a document current? | Has the person's program state changed since the previous exchange? |
| Continuity | What should persist between chats? | What may be carried from this interaction into the next one, for how long, and under which purpose? |
| Instructions | Can a retrieved source be trusted? | Can user text, a database cell, or a tool response issue instructions to the system? **No, not by being retrieved.** |
| Boundary | Who may update the source? | Who may message, record, notify, change a state, or refer to a human? |
| Evaluation | Was the right source chosen? | Did the next interaction maintain the permitted context without false inference or unwanted intervention? |

These are related responsibilities, not an assertion that conversational products are simpler, have less context, or should abandon source governance.

## 2. Smallest interaction-context contract

Treat each piece of context as a governed object, not as an unbounded chat transcript. A production schema may vary, but its responsibilities should remain inspectable:

| Field / facet | Intended responsibility |
|---|---|
| Scoped subject reference | A pseudonymous key resolved only by an authorized application; not public personal identity |
| Purpose and action | Why context is requested, and what the application may actually do |
| Session / dialogue state | Last relevant conversation state, distinct from raw transcript and from authoritative program records |
| Operational state | Current milestone, status or scheduled event returned from an approved system |
| Source provenance | Originating substrate (API, query, spreadsheet, etc.), owner, revision and effective time |
| Freshness and conflicts | Explicit currentness, supersession, contradictory states and unknowns |
| Data minimization | Field allowlists and purpose restrictions, not “store everything for later” |
| Consent and organizational authorization | Revocation, channel, permitted processing purpose, actor rights and retention |
| Jurisdictional requirements | Externally approved, versioned applicable profile; absence blocks sensitive processing |
| Human boundary | Cases that cannot be decided by the model, notification/handoff owner and readback |
| Acceptance evidence | Synthetic fixtures, expected output, prohibited disclosures and measurable test result |

A profile is a **configuration supplied by the operating organization**, not proof that legal duties are satisfied. See [Jurisdictional Requirements](JURISDICTIONAL_REQUIREMENTS.md).

## 3. Modular execution without autonomy inflation

A Moon Source protocol is a reusable procedural specification. Depending on the environment it can be:

- read and followed by a compatible model when the relevant public method is loaded;
- translated by an engineering team into application rules, validators, state machines, prompts, structured tool interfaces or operator workflows;
- bound to a named execution surface through an adapter and [Operational Device](OPERATIONAL_DEVICES.md).

The repository itself does not install those behaviors, connect a database, provide identity or permissions, enforce legal compliance, host an autonomous agent, or guarantee that arbitrary models follow instructions. A **protocol's portability** and **a runtime's enforceability** are different properties.

The existing registry remains at its published capability set. This is a **composition of known responsibilities** for an emerging application shape, not a new registry identity.

## 4. Recommended separation of responsibilities

```text
User turn and operating context
    ↓
Application authentication + purpose, consent and region resolution
    ↓
Approved policy and jurisdiction requirement profile
    ↓
Authorized reads: API / query / spreadsheet / event store
    ↓
Context router: select allowed current state, isolate lower-trust text
    ↓
Human escalation gate, policy engine and conversational runtime
    ↓
Optional LLM to produce an answer within the constrained context
    ↓
Application checks, authorized actions, logging / readback
```

**Hard boundary:** the application, not the LLM, must enforce identity, consent, field-level permissions, data retention, lawful processing and tool-action authorization. A model may help formulate a message, but should never be treated as the sole access-control or legal-compliance layer. Retrieved data remains data, not a source of new instructions.

A database query can return current values without establishing that all queries, spreadsheet cells and free text are correct or authoritative. The source owner and facet-specific precedence need to be defined by the product team.

## 5. Synthetic reference you can execute

The [conversational-context example](../examples/conversational-context/README.md) implements a **small deterministic context selector** with fabricated program and dialogue records. It does not generate conversation; it selects a minimal structure the application *could* review before calling a model.

Run its regression tests using Node.js:

```bash
node --test examples/conversational-context/test-router.js
```

Included gates: explicit consent and expiry; purpose and action allowlists; operator-supplied reviewed jurisdiction profile; source provenance; record age and conflict; intersection of policy/legal field allowlists; refusal or human escalation; no raw transcript or personal identifiers in the result. The test deliberately does not connect to real systems or process real data.

## 6. Conversational pilot acceptance template

Choose one short fictional dialogue and one controlled change of state. For each turn record:

1. permitted purpose, actor/channel, applicable reviewed requirements and revocation state;
2. data requested, data actually retrieved, which fields were excluded and why;
3. last accepted state, new authoritative state and any contradiction;
4. next permitted response or explicit handoff, including a stop line for out-of-scope requests;
5. expected trace, human reviewer, failure outcome and retention behavior.

**Do not infer why a person stopped replying** from a missing event. Do not reinterpret an expired goal as a present preference. Do not infer clinical conditions, legal status or eligibility from sparse user activity.

Before any pilot with real participants, the operator must obtain the relevant approvals, privacy/security controls, responsible engineering review and jurisdiction-specific legal advice where required. A safe synthetic example does not establish readiness for deployment or measured benefit.

## Claim ceiling

Public contract + deterministic synthetic routing tests support **documented architecture** and **bounded executable behavior**. They do not establish an independently deployable chatbot, an integrated third-party system, medical effectiveness, statutory compliance, legal opinion, security certification, accessibility certification, real-user adoption or outcome improvement.

<!-- MOON-SOURCE-PUBLIC-STAMP -->

---

> 🌙 **Moon Source** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Source/blob/main/LICENSING.md) · [Use & attribution](https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md) · [Full source (.zip)](https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip) · Questions, suggestions, or proposals? Feel free to contact me at [LuaHelenaMMC@gmail.com](mailto:LuaHelenaMMC@gmail.com).
