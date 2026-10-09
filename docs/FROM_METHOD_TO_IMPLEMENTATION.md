# From method to implementation

Moon Source began as dogfooding: repeated context and continuity problems in the creator's own projects led to methods that were tried, revised and documented through day-to-day work. The public repository makes those methods inspectable. It does **not** turn them into a ready-made assistant, runtime, SDK or externally validated product.

This guide answers three practical questions a collaborator, technical lead or recruiter can reasonably ask: **How was the method developed? Where does it work today? What would it take to implement it elsewhere?** It is a reading and translation route, not a new Moon Source capability or independent source of authority.

## 1. Start from a failure you can observe

Consider a project where an AI assistant repeatedly follows an obsolete policy because several chat transcripts and documents disagree.

- **Problem:** a newer decision exists, but an older document still looks plausible.
- **Context responsibility:** establish the source owner, effective version, review date, supersession and the human who resolves a conflict.
- **Useful behavior:** refer to the current authoritative source; make uncertainty explicit when competing top-authority sources conflict.
- **Acceptance test:** when the obsolete document is retrieved, the system must not silently promote it to current policy.

The example is illustrative. Source selection, access, state storage and execution still require a concrete implementation.

## 2. Separate the kinds of evidence

| Evidence level | What can honestly be said | What it does not establish |
|---|---|---|
| Public method | Moon Source documents structures for context, source authority, freshness, provenance and handoffs. | Executable software, reliability or adoption by third parties. |
| Real self-use | The creator uses and iterates on those methods in her own AI workflows and project sources. | Independent customer deployments or measured user outcomes. |
| Bounded technical demonstration | A standalone [Governed Knowledge Routing Demonstrator](https://www.luahelena.com.br/ia/demos/governed-knowledge/) shows deterministic handling of synthetic source records; [source and tests](https://github.com/luahelenammc/LUAHELENA/tree/main/ia/demos/governed-knowledge/) are inspectable in a **separate professional-site repository**. | An LLM assistant, clinical application, production RAG, universal Moon Source runtime or external adoption. |
| External pilot | A partner and project would have to agree on scope, responsibilities, consent, evaluation and what actually gets built. | No external pilot or result is claimed by this guide. |
| Evaluated outcome | A bounded pilot could define measures and compare observed results with an appropriate baseline. | No impact, retention improvement or other effect has been measured here. |

For the repository's own available artifacts, read [Existing Implementations and Projections](EXISTING_IMPLEMENTATIONS.md) and [Evidence and Claims](../EVIDENCE_AND_CLAIMS.md). The companion demonstrator is external to this repository and is a **small synthetic implementation of related governance ideas**, not a deployment of a Moon Source product.

## 3. Translate a context method into an implementation contract

A useful first deliverable is a short **context-to-implementation brief** for the actual people and process. It should be reviewed with both a domain owner and a technical owner.

| Question | Minimum specification |
|---|---|
| Whose problem? | User, task, current workflow, concrete point of failure and human stakeholders. |
| Which sources govern? | Owner, locator, authority, currentness, version, update and supersession rules. |
| What can the system remember or transmit? | Smallest consented state, retention limit, exclusions and recovery path. |
| What does the assistant do? | Observable permitted actions, prohibited actions, escalation and human decision rights. |
| Who implements what? | Context architecture and acceptance criteria versus product engineering, integrations, infrastructure and security. |
| How will anyone know it works? | Test fixtures, failure cases, readback, maintenance responsibility and pilot measures if authorized. |

A candidate pipeline is:

`real workflow → source/state contract → minimal synthetic test → approved harness and integrations → human review → bounded pilot → evaluation`

Moon Source may inform the source/state contract, context selection, uncertainty and evaluation boundaries. The chosen product stack must supply storage, identity, interface, connectivity, authentication, model invocation if needed, execution controls and security. A diagram of that pipeline is not evidence that those connections exist.

## 4. One small test before the big proposal

Using **only invented data**, write three source records: a current rule, an obsolete version and a conflicting note. Give each record a source owner, date and authority. Specify the expected answer and the required escalation when there is no reliable winner.

A reviewer should be able to check four things without trusting a persuasive AI explanation: **which source governed, why, what was excluded and what happened under conflict**. The public [Governed Knowledge Routing Demonstrator](https://www.luahelena.com.br/ia/demos/governed-knowledge/) illustrates a related deterministic test; it is not a real integration or a substitute for system-specific testing.

Only then discuss whether the project needs a conversational assistant at all. In sensitive fields, do not insert personal or health data into prototype prompts without an approved privacy, consent, access and human-oversight design.

## 5. A useful claim for an external conversation

> I created Moon Source to solve context continuity problems in my own work. I use its methods, publish the reference architecture and can show a limited technical demonstration of related source-governance behavior. Turning that into an application for other users requires joint discovery, an implementation team and tests in the real domain. An external case study would be built and assessed, not assumed.

This preserves a meaningful distinction: **authored method → lived internal use → inspectable bounded behavior → proposed external application → externally observed outcome**. Each stage needs different evidence.

**Further routes:** [Start Here](../START_HERE.md) · [For AI Builders](FOR_AI_BUILDERS.md) · [Architecture](../ARCHITECTURE.md) · [Existing Implementations](EXISTING_IMPLEMENTATIONS.md).

<!-- MOON-SOURCE-PUBLIC-STAMP -->

---

> 🌙 **Moon Source** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Source/blob/main/LICENSING.md) · [Use & attribution](https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md) · [Full source (.zip)](https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip) · Questions, suggestions, or proposals? Feel free to contact me at [LuaHelenaMMC@gmail.com](mailto:LuaHelenaMMC@gmail.com).
