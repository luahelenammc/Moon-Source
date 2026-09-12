# 🗂️ Lifecycle Workspace Router — Moon Source component

The Lifecycle Workspace Router is a public Moon Source method for organizing collaborative file workspaces so that people and AI can tell what arrived, who actually needs to act, what state an artifact is in, which revision was reviewed, and where the durable source lives — without pretending that folder location proves authorship, ownership or authority.

Its central rule is:

> **Artifact identity and provenance come first; lifecycle and action state determine workspace projection. Folder placement is an operational view, not the source of truth about who created or owns an idea.**

This method is provider-neutral. Google Drive and Google Sheets are useful examples because they expose folders, files, IDs, revisions and human-readable tables, but the architecture does not require them.

Canonical public repository: https://github.com/luahelenammc/Moon-Source

Created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion**.

## Scope

Use this capability when a collaborative workspace has become hard to read because one physical tree is being asked to represent several different things at once: origin, authorship, ownership, topic, review status, decision state, next action and archive history.

The method separates those dimensions instead of forcing them into folder names.

It is:

- a workspace-routing and lifecycle method;
- a way to keep a common intake surface without creating common obligation;
- a way to give each participant an explicit personal action queue;
- a way to project lifecycle state into folders while preserving richer metadata elsewhere;
- a way to record read, review and validation state against real artifact revisions;
- a way to keep one durable source-of-record while exposing pointers in several queues;
- a migration and reconciliation pattern with receipts and provider readback.

It is not:

- a database of record by default;
- proof of authorship, legal ownership, consent or approval;
- automatic synchronization between providers;
- a universal workflow taxonomy;
- permission for AI to invent human decisions or validation state;
- evidence that a person read or approved something merely because the file was reachable;
- a replacement for the authority rules of the organization, project or domain using it.

## The four planes

A useful implementation separates four planes.

### 1. Shared Intake

Shared Intake is the common arrival surface for material that is new, untriaged or not yet assigned to a next actor.

It can contain:

- newly arrived material;
- external submissions;
- objects whose classification is not yet resolved;
- genuinely collective items still awaiting triage;
- items whose next actor is not yet known.

The invariant is:

```text
shared_intake != common_obligation
```

Presence in Shared Intake does not mean everyone must read, review or answer.

### 2. Personal Action Queues

A personal Inbox or queue should mean one thing:

> **There is an explicit action currently assigned to this person.**

It should not mean “this person uploaded the file”, “this person owns the idea”, or “this file is about this person”.

Common action classes can include:

- `READ`
- `REVIEW`
- `DECISION`
- `REVISION`
- `REQUEST_INFO`
- explicit acknowledgement when genuinely required

FYI, reference and general-interest material should not create queue debt unless acknowledgement is itself the requested action.

```text
originator != assignee
folder_presence != task
FYI != review_debt
```

When a response resolves the requested action, the queue entry should close or advance. An actionable Inbox that retains resolved items indefinitely stops functioning as a queue and becomes an archive.

### 3. Lifecycle Surface

The artifact source can have one operational location that answers a narrow question:

> **What is happening with this artifact now?**

A minimal reference topology is:

```text
Workspace/
├── 00. Inbox/
│   ├── 00. Shared Inbox/
│   └── <personal queues>/
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

This is a reference, not a mandatory ontology. Do not create empty infrastructure merely for symmetry. A smaller workspace may need fewer states; a specialized domain may need different labels.

Folder movement changes the workflow projection. It does not silently change authorship, ownership or semantic authority.

### 4. Operations Dashboard

A table or spreadsheet can carry the multidimensional state that a folder tree cannot represent honestly.

Useful views include:

- what arrived;
- who needs to act;
- which action is requested;
- who has read, reviewed or validated;
- which revision was reviewed or validated;
- whether an earlier validation became stale;
- where the source-of-record lives;
- current lifecycle state;
- duplicate and lineage relationships;
- recent routing events;
- next action.

The dashboard is a human projection, not intrinsic authority.

```text
dashboard_state != source_authority
```

## One durable source, many pointers

Prefer:

```text
one canonical artifact
+ zero-or-more queue pointers
+ dashboard rows
```

Do not duplicate the payload merely to make the same object visible to several people.

If one artifact requires action from several participants, each queue can contain a pointer, shortcut or queue record referencing the same source-of-record.

```text
duplicate_pointer != duplicate_artifact
```

A renamed or convenience copy does not automatically become a new semantic object. Near-duplicate detection is a review aid, not deletion authority.

## Identity and provenance

Where the substrate allows it, preserve enough metadata to distinguish the object from its current location:

- stable artifact ID;
- provider file ID;
- canonical title;
- originator;
- author or authors;
- owner or custodian;
- contributors;
- artifact class;
- topic or tags;
- requested action;
- required readers or reviewers;
- lifecycle state;
- current revision or hash;
- lineage parent;
- `supersedes` / `superseded_by`;
- `copy_of` / related artifacts;
- timestamps;
- classification confidence when AI-assisted inference is involved.

Unknown is a valid state. Do not convert missing evidence into operational fiction.

## Read, review and validation stamps

Human states that normally disappear into chat should be made explicit when they matter.

A practical stamp model can separate:

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

### Outcome

- `GO` / `ACCEPT`
- `MODIFY` / `REVISION_REQUIRED`
- `NO_GO` / `REJECT`
- `ABSTAIN` when the domain uses it

### Freshness

- `FRESH`
- `STALE`
- `UNKNOWN`

The core law is:

```text
read != review != validate
```

Reading is not approval. Review is not necessarily validation. A material validation should point to the object and revision that were actually seen.

## Revision-bound validation

When an approval, validation or decision depends on concrete content, record the revision or hash if the provider exposes one.

A useful stamp can include:

- artifact/file ID;
- reviewed revision or hash;
- reviewer;
- requested action;
- outcome;
- timestamp;
- response or receipt link.

If a later material edit creates a new revision, the earlier validation should not be silently projected onto the new content.

```text
validation(revision_n) != validation(revision_n+1)
```

If the effect of a change cannot be determined safely, mark the validation `STALE` or `UNKNOWN`, or request a new review instead of inventing continuity.

## A practical dashboard schema

A spreadsheet implementation can use a small set of tabs.

### `DASHBOARD`

Human summary: Shared Intake count, actions by person, pending reviews or decisions, stale validations, revision-needed items and recently resolved work.

### `ARTIFACTS`

One row per canonical artifact: identity, origin, authorship, custody, requested action, lifecycle state, current revision, canonical path, timestamps and next action.

### `ACTION_QUEUE`

One row per actionable request per recipient, for example:

- `queue_id`
- `artifact_id`
- source URL
- action
- `requested_by`
- `assigned_to`
- queue state
- source revision
- what is needed
- response URL
- resolution

### `REVIEW_STAMPS`

One row per `artifact × reviewer × revision/scope`, recording awareness, review state, outcome, reviewed revision, current revision, freshness, timestamps and response/receipt.

### `ROUTING_LOG`

Append-oriented events such as `CREATE`, `MOVE`, `ROUTE`, `QUEUE`, `DEQUEUE`, `SUPERSEDE`, `ARCHIVE` and `RECONCILE`, including old/new path, reason and readback.

### `LINEAGE_DUPLICATES`

Relationships such as `EXACT_DUPLICATE`, `COPY_OF`, `REVISION_OF`, `SUPERSEDES`, `DERIVED_FROM`, `NEAR_DUPLICATE` and `DISTINCT`.

### `LISTS_CONFIG` — optional

Controlled vocabularies for dropdowns. Utility does not become authority merely because it is centralized.

## Routing and reconciliation

Use deterministic rules when the state can be derived without creative interpretation, including:

- provider IDs and timestamps;
- known paths;
- exact duplicate checks when supported;
- queue creation/removal after explicit events;
- revision mismatch;
- lifecycle projection;
- provider readback and receipts.

AI may assist with bounded classifications such as artifact class, topic, near-duplicate candidates, delta summaries or likely requested action. Those suggestions do not independently create ownership, validation, consent or human decisions.

```text
LLM_suggestion != human_state
```

Reconciliation compares the intended control projection with the real provider state. A routing operation is not complete merely because a write call returned success.

## Queue / reply loop

A compact operational loop is:

```text
artifact arrives
→ Shared Intake
→ triage
→ canonical source routed to lifecycle surface
→ personal queue pointer(s) created only for explicit actions
→ dashboard/stamps initialized
→ person reads/reviews/decides
→ response preserved
→ material stamp bound to exact revision when appropriate
→ queue item resolved
→ next queue created only when genuinely needed
→ lifecycle/log projection updated
→ provider readback
```

The loop should preserve the difference between the durable artifact, the action request and the human response.

## Durable file layer, signaling layer

When a durable collaborative workspace is available, prefer creating and updating canonical artifacts there rather than making a chat attachment the primary source.

A useful communication split is:

```text
workspace = durable_file_layer
chat = signaling_and_link_layer
attachment = exception
```

A robust handoff looks like:

```text
write or update canonical artifact in workspace
→ update the relevant dashboard / queue / stamp projection
→ read back the provider state
→ produce a shareable source-of-record link
→ use chat or messaging to signal the link and requested action
→ recipient works from the durable source
→ response / receipt returns to the workspace
→ queue, stamps and lifecycle projection advance
```

When the provider supports these steps, do not declare the handoff complete before the durable write, control-projection update, readback and shareable link are all available.

```text
send_success = provider_write + control_projection_update + readback + shareable_link
```

Attachments and transient previews remain valid fallbacks when the durable provider is unavailable, but they should not silently become a competing canonical copy. Provider and connector behavior is date-, permission- and implementation-sensitive; probe what is actually available rather than assuming support.

## Duplicates, versions and archive

Prefer one canonical identity per artifact.

- exact copy is not new evidence;
- renamed copy is not automatically a new artifact;
- convenience copies should point back to the canonical object;
- near-duplicate is a candidate relationship, not automatic deletion authority;
- a material revision should not be collapsed into an exact duplicate;
- preserve lineage before destructive cleanup.

When a former current object becomes superseded, preserve its relationship to the successor. Archive should reduce active-surface noise without erasing useful provenance.

## Safe migration

For an existing messy workspace:

1. census the provider state;
2. identify stable provider IDs;
3. classify obvious duplicate and lineage relationships conservatively;
4. create only the minimal target structure;
5. populate the dashboard without inventing historical states;
6. dry-run routing where risk justifies it;
7. use reversible moves that preserve file identity where possible;
8. reconstruct human review stamps only from explicit evidence;
9. read back the provider after bounded batches;
10. record a migration receipt or postflight.

A useful migration receipt can answer:

```text
old_path → new_path → why → provider_readback
```

Ambiguous items should be staged or quarantined rather than destructively forced into a false category.

## Provenance and promotion boundary

This public method was developed by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion**, then generalized through real collaborative use.

Collaborative testing is not a provenance reset. During promotion into this public capability, mechanisms whose traceable origin belonged to external collaborators — or whose origin remained materially ambiguous — were intentionally excluded rather than anonymized and absorbed.

The public capability therefore represents a provenance-cleared generalization of Moon / Moon × Áurion material. It is not a transcript of a particular shared workspace, does not claim ownership of collaborators' systems, and does not treat convergence during a joint experiment as evidence that all converged mechanisms share one author.

```text
shared_testbed != shared_authorship
usefulness != ownership
ambiguous_provenance → disclose_or_exclude
```

This provenance screen is a good-faith evidentiary boundary, not a claim of infallibility. If stronger provenance evidence later shows that a published element materially originated elsewhere, the correct response is to correct lineage, attribution, scope or content rather than preserve a false ownership claim.

## Claim ceiling

The Lifecycle Workspace Router organizes and makes collaborative workspaces more legible. By itself it does not prove:

- authorship or legal ownership;
- consent or approval;
- that a person actually read something without evidence;
- correctness of artifact content;
- completeness of a provider census;
- automatic synchronization between providers;
- that a spreadsheet is a database of record;
- that physical location defines authority;
- external adoption, measured impact or universal workflow superiority.

## Compact laws

```text
Shared Intake = common entry, not common debt
Personal Inbox = explicit action queue
Lifecycle folder = operational projection
Spreadsheet = multidimensional human projection
originator != assignee
location != authorship
location != ownership
read != review != validate
validation binds to revision
duplicate != second artifact
LLM suggestion != human state
UNKNOWN != permission to invent
workspace = durable_file_layer
chat = signaling_and_link_layer
move → receipt → provider readback
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
