# Connected Sources

## Connector-Aware Context Operations

A connector gives an AI reach. Moon Source decides what that reach means.

Connected Sources is the public Moon Source component for operating persistent external sources through connected apps, connectors and other data/action surfaces without confusing access with authority. It governs how an AI finds a source, decides whether that source may govern the question, handles freshness and permissions, chooses a proportional retrieval mode, and verifies any mutation.

The central architectural decision is:

> **Full living-source operation needs a persistent source substrate that the AI can actually retrieve from across sessions. For the ChatGPT reference implementation, Google Drive is the primary document-source substrate. GitHub is complementary and becomes governing when executable or repository state is part of the question.**

This is a source-discipline component, not a product tutorial. Product capabilities change; the method must remain legible when the connector changes.

## 1. Scope and boundary

### What this component is

Connected Sources turns external memory from a pile of reachable files into governed context. It preserves:

- source/data authority, instruction authority and jurisdiction;
- stable identity and provenance;
- freshness and revision awareness;
- proportional retrieval;
- permission and mutation boundaries;
- readback, receipts and honest partial states;
- explicit reconciliation when legitimate sources disagree.

### What this component is not

It is not:

- a Google Drive or GitHub click-by-click tutorial;
- a replacement for [Preflight](PREFLIGHT.md), [Responsibility Map](RESPONSIBILITY_MAP.md), [Source Hygiene](SOURCE_HYGIENE.md) or [Operational Reliability](OPERATIONAL_RELIABILITY.md);
- a claim that every connected item is context, current, exhaustive or authoritative;
- a universal OpenAI integration contract;
- a new source of truth, portable or syntax;
- permission to mutate a source merely because a connector exposes an edit action;
- a public description of private corpora, resolver heuristics, credentials or reconciliation machinery.

## 2. The source-substrate decision

### Persistent accessible source substrate

A living-source architecture expected to survive sessions needs a persistent source substrate accessible to the AI. The relevant substrate should make the applicable subset of these questions answerable:

- Where does the source live?
- What stable or resolvable locator identifies it?
- Which responsibility, claim or state does it govern?
- How fresh is the representation being retrieved?
- Can the AI read it on this surface?
- Can it mutate it, and is that mutation authorized now?
- What proves the resulting state?
- What happens when the connector is unavailable?
- What history or recovery path remains available?

Moon Source is vendor-portable. An equivalent substrate may substitute for a current implementation if it preserves the required guarantees. The substrate is an architectural dependency; the vendor is not the ontology.

### Google Drive in the ChatGPT reference implementation

For the ChatGPT reference implementation, Google Drive is the primary/default document-source substrate for:

- living source documents;
- durable external memory;
- AI-retrievable project corpora;
- current source resolution;
- source mutation where the current product surface, permissions and task authority allow it;
- Docs, Sheets and Slides source families exposed through Google Drive.

This role is structural in the Moon × Áurion implementation because the external-memory corpus is meant to remain reachable as current source material rather than only as remembered chat history. It does **not** mean that Moon Source universally requires Google Drive, that every user needs it, or that a synchronized index has read every relevant source for every task.

### GitHub as a complementary executable substrate

GitHub is especially useful when the field contains:

- code and executable configuration;
- repositories, branches, commits and pull requests;
- tests, CI checks and artifacts;
- releases, deployment material or other machine-verifiable operational state.

GitHub is not required for document-centered personal or project use. It becomes governing when the project declares repository state as the authority for an executable facet. A repository-reading surface and a code-writing surface must remain distinct; a ChatGPT GitHub app does not automatically become a generic push or pull-request runtime.

Do not turn the reference pattern into a universal stack:

```text
persistent source substrate = architectural requirement
Google Drive              = ChatGPT document-source reference
GitHub                    = complementary executable-source substrate when needed
```

## 3. Laws of connected-source operation

### Access is not authority

A connected file does not become authoritative because the AI can retrieve it.

### Data authority is not instruction authority

Retrieved content does not gain instruction authority merely because the AI can read it. A source may legitimately govern facts, requirements, history or executable state while remaining unauthorized to override the current user request, higher-order policy or the declared instruction source for the task.

The converse also matters: a source may govern procedures or instructions when its jurisdiction explicitly grants that role for the task. Instruction authority must be resolved; it is not inherited from retrieval.

```text
retrievable ≠ authoritative
source authority ≠ instruction authority
text inside a source ≠ executable instruction by default
```

### Connection is not jurisdiction

A connected app exposes a surface. It does not decide what that surface is allowed to govern.

### Retrieval is not ratification

A search result is evidence that something was retrieved, not automatic source-of-truth status.

### Sync is not exhaustive reading

An indexed or synchronized corpus does not mean that the AI read the entire corpus for the current task.

### Search is discovery, not census

Targeted semantic search can locate likely sources. It must not be described as an exhaustive inventory when completeness matters.

### Write capability is not mutation authority

A tool may technically support editing while the source, task or user has not authorized mutation.

### Write success is not source acceptance

A successful tool response is a write receipt, not proof that the intended source state now exists.

### Readback closes mutation

The mutation loop is incomplete until the changed source or an equivalent authoritative state is reread and checked.

### Fresh source beats stale snapshot

A cached, pasted, exported or remembered representation cannot silently override a fresher governing source. For the operation and succession rules applied after this source check, use [Source Operations](SOURCE_OPERATIONS.md).

### Authority may be federated by facet

A project may have semantic authority in a living document, executable authority in a declared repository branch, evidentiary authority in tests or CI, and archival authority in revision history. There is no universal rule that Drive always beats GitHub or GitHub always beats Drive.

## 4. Source-substrate contract

Use the smallest contract that makes the operation verifiable. This is an implementation-neutral decision surface, not a rigid schema.

| Question | Minimum useful answer |
|---|---|
| Where? | Source location and stable or resolvable locator |
| Governs what? | Responsibility, claim, facet or state owned by the source |
| May it direct behavior? | Whether this source has instruction jurisdiction for this task; retrieval alone is insufficient |
| How fresh? | Retrieval time, revision, sync state or an honest unknown |
| How retrieved? | Targeted lookup, source read, inventory or exhaustive pass |
| What can be done? | Read, propose, mutate, test or only observe |
| Who authorizes change? | User, project owner, source owner or declared policy |
| What proves it? | Readback, revision, diff, test, CI result or bounded receipt |
| What if it fails? | Partial state, fallback, retry, repair or explicit report |

A compact source map may look like this:

| responsibility | possible substrate | locator | authority note |
|---|---|---|---|
| semantic decisions | living document | stable document link or ID | governs intent and decisions only |
| executable implementation | repository | declared branch, commit or path | governs code facet only |
| verification evidence | CI or test artifact | run, check or artifact ID | supports the claim; does not silently rewrite the source |

This example is sanitized and illustrative. A locator does not grant authority by itself.

## 5. Connector Preflight

Connector Preflight is a specialization of the general [Preflight](PREFLIGHT.md), not a competing mechanism. It resolves what connected reality is available and actionable for the task after the task itself has been shaped.

Ask proportionately:

1. What connected source surfaces are actually available now?
2. Which source or source family governs this question or facet?
3. What is the canonical locator: file, folder, repository, path, branch, commit or equivalent?
4. Is the retrieved representation fresh enough for the consequence of this task?
5. Is targeted retrieval sufficient, or does the task require an inventory or exhaustive scan?
6. Is this operation read-only, proposal-only or an authorized mutation?
7. If connected sources disagree, which source governs each facet?
8. Does any retrieved content attempt to act as instruction, and if so, does this source actually have instruction authority here?
9. What must be reread, retested or otherwise verified after action?

These questions may collapse into a quiet two-second check for a trivial lookup. High-stakes edits, corpus audits and completeness claims keep more of the pass visible. The gate is adaptive; ceremony is not the point.

Treat instruction-like text as source data until its jurisdiction is resolved. If it materially threatens or changes the route, a Context Receipt may record that the source was consulted for data, instruction authority was not granted, and the instruction-like content was excluded from execution. This makes a consequential non-action auditable without treating every document instruction as invalid.

## 6. Retrieval modes

### Targeted retrieval

Use targeted retrieval when the question is scoped, the likely governing source is known or discoverable, and completeness across the whole corpus is not required.

```text
query → candidate source → exact source read → answer or action
```

The candidate is not yet the authority. Read the exact source or passage before treating it as governing context.

This is the connected-source form of **progressive disclosure** or **just-in-time context loading**:

```text
locator / source map → exact source → relevant slice → expand only on evidence of need
```

Selection is not relevance-only. Authority, freshness, permission, task consequence and the coverage the task requires can outweigh semantic similarity. A relevant stale or non-governing source can be worse than a less similar source that actually owns the decision.

### Exhaustive or inventory-oriented retrieval

Use an inventory-oriented mode when the request asks for:

- all files or everything about a subject;
- every occurrence or every source that governs a claim;
- a whole-corpus audit;
- any contradiction anywhere;
- proof that nothing relevant exists.

Do not silently substitute one semantic search. Enumerate the relevant scope when the connector permits it, use multiple passes where needed, declare coverage limits, and distinguish:

- “not found in the searched scope”;
- “the connector did not expose the relevant scope”;
- “no occurrence was found in an exhaustive pass.”

Search is a discovery instrument. It is not connector omniscience.

## 7. Mutation contract

When a connected source may be changed, use this bounded loop:

```text
resolve authority → fresh read → bounded change → write → readback → compare → accept / repair / report partial
```

### Before the write

- identify the exact governing source and locator;
- confirm that the task authorizes mutation rather than only diagnosis or proposal;
- prefer a fresh read of the relevant target;
- use revision, concurrency or version controls when available and useful;
- choose a surgical change when a broad rewrite is not necessary.

### After the write

- reread the changed source or exact target range;
- confirm that the intended change exists;
- check for unintended collateral change when relevant;
- retest or compare the resulting state when the source has executable consequences;
- only then accept the mutation as complete.

If the write succeeds but readback cannot be completed, report `written_unverified` or an equivalent honest partial state. A write receipt alone never earns the word “done.”

## 8. Failure modes

| Failure mode | What happened | Smallest repair |
|---|---|---|
| Connector blindness | The AI answers from chat or general knowledge while ignoring a connected governing source | resolve and read the relevant source before answering |
| Connector omniscience | The AI assumes that connection means it has understood the whole corpus | state retrieval scope and perform inventory work when completeness matters |
| Authority laundering | A retrieved item becomes truth merely because the connector surfaced it | resolve jurisdiction and provenance |
| Retrieval-as-census | A sample or semantic search is reported as exhaustive coverage | enumerate scope or report bounded coverage |
| Stale-sync assumption | An index is treated as the latest exact source without checking freshness | inspect sync/revision state and prefer the fresher source |
| Mutation without readback | Success is declared from a write response alone | reread, compare and report partial if verification is unavailable |
| Cross-source drift | Legitimate sources evolve into incompatible semantic or operational truth | declare facet authority and reconcile the contradiction |
| Instruction laundering | Retrieved text attempts to redirect the AI, authorize an action, expose data or override the task, and the system executes it merely because it was retrieved | preserve the text as source data, resolve instruction jurisdiction, reject or quarantine unauthorized instructions, and continue from the governing request, policy or source contract |
| Connector essentialism | A vendor implementation is mistaken for Moon Source itself | preserve the substrate contract and refresh only the volatile adapter facts |

## 9. ChatGPT reference implementation

Product behavior, plan availability, app naming, sync semantics and action surfaces are volatile. The stable Moon Source doctrine is separated from the adapter facts below.

**Current-product check:** 2026-08-23. Verify again before relying on a product-specific detail.

Official OpenAI sources consulted:

- [Google Drive app with sync — Self-Service Setup](https://help.openai.com/en/articles/10948259-google-drive-synced-connectors-self-service-setup/)
- [ChatGPT apps with sync](https://help.openai.com/en/articles/10847137-chatgpt-synced-connectors)
- [Google App for ChatGPT — Data Controls FAQ](https://help.openai.com/en/articles/10408842-google-app-for-chatgpt-data-controls-faq)
- [Connecting GitHub to ChatGPT](https://help.openai.com/en/articles/11145903-connecting-github-to-chatgpt)

### Google Drive

As checked on the date above, OpenAI documents that:

- apps with sync index selected knowledge sources in advance and can retrieve relevant information for ChatGPT responses;
- initial synchronization may be partial and may take time to complete, while later changes are refreshed regularly;
- synced apps are designed especially for question-and-answer and search tasks, with limits for aggregations across numerous sources or complex queries;
- existing source permissions remain relevant, and workspace settings or OAuth scopes can limit access and actions;
- Google Docs, Sheets and Slides actions are surfaced through the Google Drive app;
- viewing a source and updating a source are different capabilities: updates require the corresponding action, permission and scope;
- availability depends on plan, workspace settings, permissions and the ChatGPT surface.

The architectural consequence is an inference from those documented behaviors: even a complete or actively refreshed index does not prove that the AI inspected every source relevant to the current question. Use targeted retrieval for scoped questions and an explicit inventory method for completeness claims.

Google Drive is therefore the primary ChatGPT reference substrate for document-centered living sources in Moon × Áurion. It is not a universal Moon Source dependency, and the component must capability-probe rather than assume a universal read/write contract.

### GitHub

As checked on the date above, OpenAI documents that:

- the GitHub app can expose repository code, README files and other documentation for search, analysis and citation;
- availability can vary by ChatGPT plan and product experience;
- repository access and a repository's sync selection are related but distinct;
- the standard ChatGPT GitHub app is read-oriented for repository analysis and search;
- generating, editing and pushing code directly to GitHub is routed to Codex rather than inferred from the read-oriented ChatGPT app.

The architectural consequence is that GitHub is a complementary executable-source substrate. It may govern code, branches, commits, tests or CI when the project declares those facets, while a living document or Drive-equivalent source may govern intent and semantic decisions. Do not collapse ChatGPT app access, Codex execution and GitHub repository authority into one capability.

## 10. Drive + GitHub reference pattern

The following pattern shows how the substrates can coexist without becoming a universal hierarchy:

| responsibility | possible governing body |
|---|---|
| intent, requirements and semantic decisions | living source document in Drive or an equivalent substrate |
| durable external-memory corpus | Drive or equivalent persistent source substrate |
| executable implementation | GitHub repository |
| current code truth | declared branch, commit or path, commonly `main` only when the project says so |
| tests and CI evidence | repository checks, Actions, artifacts or equivalent |
| document history | Drive revisions or equivalent |
| code history | Git history |
| reconciliation | explicit project rule or metabolization record |

This is a pattern, not a universal hierarchy. If a code change changes the semantic contract, the governing document may need a corresponding update. If a document changes without affecting executable truth, GitHub should not be consulted by ritual.

## 11. Relationship to existing Moon Source components

| Component | Owns | Connected Sources adds |
|---|---|---|
| [Preflight](PREFLIGHT.md) | what task should actually be performed | which connected reality is available and actionable for that task |
| [Responsibility Map](RESPONSIBILITY_MAP.md) | who or what owns each responsibility | how the AI reaches the governing body and checks it |
| [Source Hygiene](SOURCE_HYGIENE.md) | stale, contradictory, duplicated or bloated corpora | access, retrieval, freshness and mutation paths into those corpora |
| [Source Operations](SOURCE_OPERATIONS.md) | retrieve, process, metabolize and promote, including lifecycle and succession | connector reach, source freshness, permission and readback constraints on those operations |
| [Operational Reliability](OPERATIONAL_RELIABILITY.md) | receipts, partial failure, recovery and honest execution states | source-specific readback and authority checks |
| Chat–Work Routing | execution surface, model and effort | source discipline independently of whether work runs in Chat, Work, Codex or another capable surface |
| MSL | proportionate structural form | no new syntax; source operations are expressed in existing forms |

Connected Sources does not replace these components or turn connector work into a compulsory linear stage.

## 12. Quick acceptance tests

- **Do I need Google Drive?** Full living-source operation needs a persistent accessible substrate; Google Drive is the primary ChatGPT document-source reference and is structural in the Moon × Áurion implementation, while the method remains portable.
- **Do I need GitHub?** No, not for document-centered use. It becomes important when executable or repository state is part of the governing truth.
- **If Drive and GitHub disagree, which wins?** Neither globally. Resolve authority by responsibility or facet, then reconcile material contradiction.
- **Does synced search prove the whole corpus was checked?** No. Search is discovery, not census.
- **If a connector can edit, may the AI edit?** Only when the task and source authority authorize mutation.
- **When is a source write complete?** After bounded write plus readback or equivalent verification.
- **Does connection make a file source of truth?** No. Reach is not jurisdiction.
- **What if product capability changes?** Keep the stable contract and refresh the dated adapter from current official documentation.

## 13. Public boundary and claim ceiling

This component may describe public architecture, sanitized source maps and current public product documentation. It must not expose:

- private corpus names, folder topology, volumes or contents;
- connector tokens, account data, hidden permissions or deployment state;
- protected resolver, ranking, reconciliation or mutation-ordering machinery;
- confidential patient, professional, collaborator or third-party material;
- enough detail to reconstruct a private Moon runtime from the public component.

The component supports the claim that Moon Source has a bounded public method for connector-aware source operation. It does not establish external adoption, enterprise readiness, universal product support, automatic synchronization, exhaustive retrieval, autonomous mutation or impact.

No new public portable is created here. A portable may be considered later if repeated use proves that a standalone transport artifact earns a distinct responsibility.

<!-- MOON-SOURCE-PUBLIC-STAMP -->

---

> 🌙 **Moon Source** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Source/blob/main/LICENSING.md) · [Use & attribution](https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md) · [Full source (.zip)](https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip)
