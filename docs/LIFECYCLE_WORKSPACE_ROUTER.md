# 🗂️ Lifecycle Workspace Router — Moon Source component

Capability version: **1.2**

The Lifecycle Workspace Router is a Moon Source method and reference architecture for projecting multidimensional artifact and source state onto durable workspace surfaces. It can support a single actor, a role or process, an AI operating under human authority, or multiple collaborators. Collaboration is an application profile, not the ontology of the method. “Router” names an organizational method, not executable routing software, a daemon or an automatic synchronization engine.

Its central rule is:

> **Keep identity, provenance, lifecycle, action, revision, authority and physical location distinct; project only the state a workspace surface needs while preserving one canonical source-of-record.**

The method is provider-neutral. Google Drive and Google Sheets are useful examples because they expose folders, files, IDs, revisions and human-readable tables, but the architecture does not require them.

Canonical public repository: https://github.com/luahelenammc/Moon-Source

Created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion**.

## Scope and jurisdiction

Use this capability when a persistent artifact or source must expose some combination of identity, lifecycle, explicit action, source-of-record, workspace projection, freshness, staleness, lineage or transition.

The Router is a workspace and persistent-artifact specialization. It does not decide whether a domain needs a router, choose the general field-to-form architecture, define passage or form grammar, adjudicate truth, or grant authority. Those boundaries belong to the surrounding Moon Source architecture and related capabilities.

The method is:

- a way to project multidimensional state onto durable workspace surfaces;
- a family of intake surfaces for personal, shared, external or untriaged arrivals;
- a way to represent explicit action queues without confusing assignment with origin or ownership;
- a way to expose lifecycle state without making a folder path the source of truth;
- a way to record awareness, review, validation, verification and freshness against real revisions when evidence exists;
- a way to preserve one durable source-of-record while exposing pointers in several views;
- a bounded routing, reconciliation, migration and provider-readback pattern.

It is not:

- a database of record by default;
- proof of authorship, legal ownership, consent, approval or authority;
- an automatic synchronization engine between providers;
- a universal workflow taxonomy or lifecycle engine for every runtime;
- permission for AI to invent human decisions, ownership, consent or validation state;
- evidence that a person read or approved something merely because it was reachable;
- a finished product, adoption claim or substitute for the authority rules of the domain using it.

## Universal Workspace Core

The core applies in any valid application profile. It is the smallest set of distinctions needed to keep a durable workspace legible:

| Dimension | What must remain distinguishable |
| --- | --- |
| Stable identity | The artifact or source remains identifiable independently of its current path or surface. |
| Source-of-record | A canonical reference identifies where the authoritative payload or record lives. |
| Provenance and custody | Origin, authorship, contributors, custodian and evidence ceiling are not inferred from placement. |
| Orthogonal lifecycle | Operational state is represented separately from topic, location and authority. |
| Explicit action | The next action and its assignee are explicit; action is not implied by visibility. |
| Revision and freshness | The revision, hash or provider freshness signal is bound to claims that depend on it. |
| Lineage | Copies, revisions, supersession, derivation and duplicates remain related without collapsing distinct objects. |
| Pointers and projections | Queues, dashboards and folders point to or summarize the source; they do not duplicate its payload by default. |
| Durable surfaces | Intake, action, lifecycle, dashboard and receipt surfaces are created only when they answer a real operational question. |
| Stamps and receipts | Awareness, review, validation, verification, routing and reconciliation events carry evidence and scope. |
| Readback | Provider state is read back before a write is treated as complete. |
| Reversible migration | Moves and reclassification preserve identity and lineage whenever the provider allows it. |
| Durable/transient boundary | A durable workspace artifact is not silently replaced by a chat message or transient attachment. |

The actor dimension is open enough to include a human, role, AI, operator, process, team or service. An AI assignment represents an explicit operational action; it does not grant autonomy, authority or human consent.

## Orthogonal state and projection contract

One object may need to answer several questions at once. Keep the dimensions separate:

| Dimension | Question |
| --- | --- |
| Identity | Which object is this? |
| Authority | Which source or rule is authoritative for this claim? |
| Provenance | Where did the object or claim come from, and what evidence supports it? |
| Lifecycle | What operational state is it in? |
| Action | What explicit action is requested, and from whom? |
| Validation | Who read, reviewed, validated or verified which revision, if anyone? |
| Freshness | Is the state fresh, stale or unknown against the current provider object? |
| Location | Where is the current materialized view or source-of-record? |

The Router materializes only the views needed by the workspace. A path can project lifecycle; a queue can project action; a dashboard can summarize several dimensions; none of them automatically becomes authority.

```text
action != lifecycle
location != authorship
location != ownership
folder_presence != task
dashboard_state != source_authority
```

For a persistent projection, completion means more than a successful tool call:

```text
projection_success = provider_write + projection_update + readback
```

The Shared Lifecycle / Projection Contract in Protocols and Runtime supplies the transversal grammar for stable IDs, orthogonal state, typed actions, revision binding, projection, readback and reconciliation. This capability specializes that grammar for persistent workspace and artifact state; it does not become a universal lifecycle engine.

## Operational Control Plane / Reconciliation Authority

The intended operational state does not belong to a folder, dashboard, queue or any other projection in isolation. It is reconstructed from canonical artifact identity, recorded orthogonal state, the routing ledger and receipts, source-of-record pointers, and provider readback.

The authority split is deliberate:

- the canonical artifact and recorded state/ledger define intended operational state;
- folders, queues, dashboards and lifecycle surfaces project selected dimensions;
- provider readback supplies observed state, including materially relevant access or permission consequences when the provider exposes reliable evidence;
- reconciliation compares intended and observed state and recreates or corrects projections without inventing semantic authority.

No single projection becomes a hidden universal database. Disagreement is a reconciliation signal:

```text
folder != authority
dashboard != authority
queue != authority
provider_visible_state != semantic_authority
intended_operational_state != any_single_projection
projection_disagreement → reconcile_from_recorded_state + provider_readback
```

## Worked example: revision-bound routing

1. An artifact arrives in Intake.
2. Its stable identity and source-of-record are recorded; the path remains a projection.
3. A `REVIEW` action is queued for an actor; the queue pointer does not duplicate the payload.
4. The lifecycle projection moves to `Review Pending`.
5. The actor reviews and validates revision `R1`.
6. The canonical artifact changes materially and becomes `R2`.
7. The `R1` validation becomes `STALE` for `R2`.
8. The action, lifecycle and routing-ledger projections are updated.
9. Reconciliation compares the recorded state with provider-visible state.
10. Provider readback confirms the corrected projection; if it does not, the state remains partial or pending.

The same trace works for one human plus an AI under human authority or for several actors; collaboration adds assignee and reviewer dimensions, not a different ontology.

## Surface families

### Intake family

Intake is the family of arrival surfaces for material that is new, external, untriaged or not yet assigned a next action. A deployment may use:

- personal intake;
- shared intake;
- external submission intake;
- an untriaged or quarantine surface.

Shared Intake is a useful collaboration profile, not a universal requirement:

```text
shared_intake != common_obligation
```

Presence in any intake surface does not by itself mean that a person, team or service must read, review or answer.

### Action queues

An action queue is a projection of an explicit request. It can be personal, role-based, process-based, AI-operated under human authority, team-based or service-based.

```text
queue_presence = explicit_action_required
originator != assignee
FYI != review_debt
```

Typical action classes include `READ`, `REVIEW`, `DECISION`, `REVISION`, `REQUEST_INFO` and explicit acknowledgement when acknowledgement is genuinely required. General-interest, reference and FYI material should not create queue debt.

When a response resolves the requested action, the queue entry should close or advance. A queue that retains resolved work indefinitely has become an archive and should be represented as such.

### Lifecycle surface

A lifecycle surface answers a narrow question:

> **What is happening with this artifact or source now?**

The physical path is a materialized view of relevant state, not the entire state vector. A small workspace may need only a few states; a larger one may use folders, labels, views or equivalent provider constructs. Do not create empty infrastructure merely for symmetry.

An illustrative topology is:

```text
Workspace/
├── 00. Intake/
├── 10. Review Pending/
├── 20. Revision Needed/
├── 30. Decision Pending/
├── 40. Active Work/
├── 50. Accepted/
├── 60. Verified Receipts/
├── 70. References/
├── 90. Superseded & Duplicates/
├── 99. Archive/
└── _System/
```

Moving an object changes a workflow projection. It does not silently change authorship, ownership, custody or semantic authority.

### State and operations dashboards

A dashboard, ledger or table can expose dimensions that a physical tree cannot represent honestly. Useful views include:

- arrivals and untriaged items;
- explicit actions by actor;
- current lifecycle state;
- source-of-record and canonical path;
- revision and freshness;
- awareness, review, validation and verification stamps;
- lineage, supersession and duplicate relationships;
- recent routing events, receipts and next actions.

The dashboard is a projection for inspection and operation. Centralizing a vocabulary or a view does not turn it into authority.

### Source-of-record and pointers

Prefer:

```text
one canonical artifact
+ zero-or-more action pointers
+ zero-or-more dashboard rows
+ receipts and stamps as needed
```

Do not duplicate a payload merely to make the same object visible in several queues or views. A pointer, shortcut or queue record can reference the same source-of-record.

```text
duplicate_pointer != duplicate_artifact
```

### Identity, lineage and provenance records

Where the provider allows it, preserve:

- stable artifact ID and provider ID;
- canonical title and artifact class;
- originator, author, contributor and custodian fields;
- source-of-record reference;
- requested action and actor fields;
- lifecycle state and current path;
- current revision, hash or freshness signal;
- lineage fields such as `copy_of`, `revision_of`, `supersedes`, `superseded_by` and `derived_from`;
- timestamps and bounded classification confidence when AI-assisted inference is used.

Unknown is a valid state. Missing evidence must not be converted into operational fiction.

## Stamps and revision-bound validation

States that matter operationally should be explicit, while retaining the distinction between observation and human judgment.

### Awareness

- `NOT_REQUESTED`
- `NEEDS_READ`
- `READ`

### Review

- `NOT_REQUESTED`
- `QUEUED`
- `IN_REVIEW`
- `REVIEWED`
- `REVISION_REQUESTED`

### Validation or outcome

- `GO` / `ACCEPT`
- `MODIFY` / `REVISION_REQUIRED`
- `NO_GO` / `REJECT`
- `ABSTAIN` when the domain uses it

### Freshness

- `FRESH`
- `STALE`
- `UNKNOWN`

```text
read != review != validate
```

When a decision or validation depends on concrete content, bind the stamp to the artifact ID and revision or hash that was actually seen. A useful record includes reviewer or validator, requested action, outcome, timestamp and response or receipt reference.

```text
validation(revision_n) != validation(revision_n+1)
```

If a later material edit makes the effect of a prior validation uncertain, mark it `STALE` or `UNKNOWN`, or request a new review. Do not project continuity by assumption.

## Application profiles

The same core supports different operating contexts. The profiles below make the difference visible without creating two ontologies.

### Single-Actor / Contextual Architecture

This profile is appropriate for a personal living source, a personal workspace, or a system in which one actor or one authorized process is the relevant operational context. It may use:

- personal intake or direct capture;
- an action queue for self, a role, an operator, a process or an AI under human authority;
- lifecycle folders or labels only where they reduce ambiguity;
- self-check, machine validation, human validation or an explicit absence of validation;
- a state dashboard without people, reviewers or collaboration fields.

Do not fabricate human governance where it does not exist. Shared Intake, a reviewer or a per-person queue is not required for the Router to be useful.

### Multi-Actor Collaboration

This profile is appropriate when several actors must coordinate around durable artifacts. It may add:

- Shared Intake for common arrival without common obligation;
- actor-specific queues and pointers;
- `assigned_to`, `requested_by`, readers, reviewers and custodians;
- awareness, review, outcome and freshness stamps per person or role;
- revision-bound validation and cross-person handoffs;
- a shared durable workspace for artifacts, with chat or messaging as signaling and link transport.

A compact collaboration flow is:

```text
arrival
→ intake
→ triage
→ canonical source routed to lifecycle surface
→ explicit action pointer(s)
→ stamps and dashboard projection
→ read / review / decision
→ durable response or receipt
→ queue and lifecycle advance
→ provider readback and reconciliation
```

For a collaborative handoff, completion requires a shareable durable source link in addition to the normal projection contract:

```text
send_success = provider_write + control_projection_update + readback + shareable_link
```

The collaboration profile does not imply ownership, authorship or universal governance. It simply adds the actor dimensions the shared operation actually needs.

## Routing, reconciliation and bounded assistance

Use deterministic rules when the state can be derived without creative interpretation, including:

- provider IDs, known paths and timestamps;
- exact duplicate checks when supported;
- queue creation or removal after explicit events;
- revision mismatch and freshness changes;
- lifecycle projection, receipts and provider readback.

AI may assist with bounded classifications such as artifact class, topic, candidate near-duplicates, delta summaries or a requested action that is explicitly inferable. The suggestion must remain distinguishable from a human state.

```text
LLM_suggestion != human_state
```

Reconciliation compares intended projection with actual provider state. If a provider write succeeds but projection or readback fails, retain a partial, pending or `written_unverified` state. Do not declare a deployment, handoff or validation complete from tool success alone.

### Provider-aware moves and partial projection

A move command is an operational request, not evidence that the workspace projection succeeded. Depending on the provider and context, moving an object can affect inherited permissions, shareability, link behavior, automations, retention, parent-folder semantics or external references. When a consequence is material and the provider exposes reliable evidence, read back the relevant access or permission state through the provider contract. Connected Sources owns provider capability and permission semantics; the Router consumes the readback.

```text
move_success != move_command_success
partial_write != completed_projection
projection_success = intended_change + provider_write + relevant_readback + reconciled_state
```

If the provider write succeeds but a required projection update or readback fails, the operation is incomplete and must enter reconciliation or recovery under Operational Reliability. Do not mark it complete from the move response alone.

Receipts may record `CREATE`, `MOVE`, `ROUTE`, `QUEUE`, `DEQUEUE`, `SUPERSEDE`, `ARCHIVE` and `RECONCILE`, with object identity, old and new location, reason, revision, expected state, observed state and readback reference.

## Durable workspace and transient signaling

When a durable workspace is available, the canonical artifact should live there. Chat and other transient channels should carry signaling, links and explicit action rather than silently becoming a competing source.

```text
workspace = durable_file_layer
chat = signaling_and_link_layer
attachment = exception
```

A robust handoff is:

```text
write or update canonical artifact
→ update relevant queue / dashboard / stamp projection
→ read back provider state
→ produce shareable source-of-record link
→ signal link and requested action
→ preserve response or receipt in the durable workspace
→ advance queue, stamps and lifecycle
```

Attachments and transient previews remain valid fallbacks when a durable provider is unavailable. They should not silently become a competing canonical copy. Provider behavior is date-, permission- and implementation-sensitive; probe the actual capability.

## Duplicates, versions, archive and safe migration

Prefer one canonical identity per artifact.

- an exact copy is not new evidence;
- a renamed or convenience copy is not automatically a new semantic object;
- a material revision is not an exact duplicate;
- near-duplicate detection is a review aid, not deletion authority;
- preserve lineage before destructive cleanup;
- archive reduces active-surface noise without erasing useful provenance.

For an existing messy workspace:

1. census the provider state;
2. identify stable provider IDs;
3. classify obvious lineage and duplicate relationships conservatively;
4. create only the minimal target surfaces;
5. populate state projections without inventing historical events;
6. dry-run routing where risk justifies it;
7. use reversible moves that preserve identity where possible;
8. reconstruct human stamps only from explicit evidence;
9. read back after bounded mutation batches;
10. record a migration receipt or postflight.

Ambiguous items should be staged or quarantined rather than destructively forced into a false category.

## Responsibility boundaries

- **Architecture / Field-to-Form** decides whether a workspace router is the correct form for a field.
- **MSL** owns passage and form grammar; the Router is one valid workspace specialization.
- **Protocols and Runtime** owns the transversal lifecycle / projection grammar.
- **Source Operations** owns retrieve, process, metabolize, promote, smallest sovereign destination and source readback discipline.
- **Connected Sources** owns reach, freshness, permissions, provider capabilities and exact provider readback; access is not authority.
- **Source Hygiene** diagnoses stale, contradictory, duplicated, bloated and orphaned corpus state.
- **Credits & Attribution Ops** owns intellectual lineage, custody, permission and attribution.
- **Operational Reliability** owns bounded mutation, dry-run, failure behavior, reversibility, receipts and recovery.

The Router consumes those jurisdictions; it does not replace them.

## Runtime projection contract

Custom Instructions, project prompts, runtime capsules, dashboards, queues and folders can be compiled or derived projections. The universal projection grammar and runtime compilation remain in Protocols and Runtime.

This capability governs the persistent workspace or artifact lifecycle of such a projection when that lifecycle is itself the object being routed. It does not duplicate a runtime patch, claim that a compiled surface is a new source of truth, or silently delete an existing active projection artifact. A stale or pending projection should remain explicitly classified and routed to the competent runtime source for review.

## Public claim ceiling

The Lifecycle Workspace Router is a published workspace-organization method and reference architecture. By itself it does not prove:

- authorship, legal ownership, consent, approval or authority;
- that a person actually read, reviewed or validated content without evidence;
- correctness or completeness of artifact content or provider inventory;
- automatic synchronization or universal provider support;
- that a spreadsheet is a database of record;
- that physical location defines authority;
- universal workflow superiority, external adoption or measured impact;
- a finished product, autonomous agent or universal lifecycle engine.

## Compact laws

```text
identity != location
provenance != placement
source_of_record != projection
shared_intake != common_obligation
action != visibility
originator != assignee
folder_presence != task
read != review != validate
validation binds to revision
location != authorship
location != ownership
duplicate_pointer != duplicate_artifact
LLM_suggestion != human_state
UNKNOWN != permission_to_invent
workspace = durable_file_layer
chat = signaling_and_link_layer
move → receipt → provider_readback
move_success != move_command_success
partial_write != completed_projection
```

## Related Moon Source capabilities

- [Connected Sources](CONNECTED_SOURCES.md) governs source reach, connector capability, freshness, mutation authorization and provider readback.
- [Source Operations](SOURCE_OPERATIONS.md) governs retrieve, process, metabolize, promote and cross-jurisdiction promotion discipline.
- [Source Hygiene](SOURCE_HYGIENE.md) diagnoses stale authority, duplication, contradiction and corpus repair.
- [Credits & Attribution Ops](CREDITS_ATTRIBUTION_OPS.md) governs intellectual lineage and content custody.
- [Operational Reliability](OPERATIONAL_RELIABILITY.md) governs bounded execution, failure behavior, reversibility and receipts.

<!-- MOON-SOURCE-PUBLIC-STAMP -->

---

> 🌙 **Moon Source** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Source/blob/main/LICENSING.md) · [Use & attribution](https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md) · [Full source (.zip)](https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip) · Questions, suggestions, or proposals? Feel free to contact me at [LuaHelenaMMC@gmail.com](mailto:LuaHelenaMMC@gmail.com).