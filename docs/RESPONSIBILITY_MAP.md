# Responsibility Map

The following objects can work together, but they do not perform the same job.

| Object | Public reading | Primary responsibility | It is not |
|---|---|---|---|
| Field | The real situation | Supply the context that must be understood | A document template |
| Source | Governed context | Hold facts, decisions, rules or material with an authority boundary | Every note ever written |
| Living source | Updateable governed context | Keep scope, freshness, owner and active state visible | A chat transcript |
| Connected source | Reachable governed external context | Expose a source through a connector while preserving authority, jurisdiction, freshness, provenance and verification | Authority merely because it is reachable |
| Source substrate | Persistent accessible source body | Preserve stable identity, retrieval, freshness, permissions and history for living-source operation | A vendor-specific ontology or automatic source of truth |
| Connector / app | Bounded access or action surface | Carry read, search or authorized action capability between the AI and a substrate | Mutation authority, exhaustive understanding or semantic ownership |
| Project | Bounded work domain | Define purpose, jurisdiction, participants and outputs | A single task |
| Procedure | Reusable way of working | Describe how an operation is performed | A source of truth for all facts |
| Skill | [Portable procedural projection](PROCEDURAL_PROJECTION.md) | Trigger and execute a reusable procedure | A magical capability or private corpus |
| Operational device | Bounded operational embodiment | Execute a reusable procedure on a named surface with state, guards, failure behavior and receipts | Semantic authority, unrestricted automation or new privilege |
| Task | One bounded action or recurring obligation | Move a project or source through a concrete next step | A project architecture |
| Handoff | Transfer of responsibility and state | Let another person, model or thread continue safely | A complete backup of the corpus |
| Packet / capsule | Bounded transport envelope | Carry objective, state, limits, provenance and next actions | A new authority by itself |
| Bridge | Translation between systems | Preserve meaning across jurisdictions without owning either source | Silent authority transfer |
| Ledger / registry | Structured record | Track decisions, identities, versions, checkpoints or lineage | A full narrative archive |
| Intellectual custody / Credits & Attribution Ops | Immaterial-asset protection layer | Keep content identity, origin, authorship, canonicality, transformations, permission boundaries, derivatives, attribution and evidence recoverable as material moves or changes | A licence, legal rights resolver, ownership proof or enforcement mechanism |
| Attribution record | Public or bounded lineage output | Carry the proportionate credit and lineage facts a material descendant needs | The whole custody system or a grant of permission |
| Protocol | Repeatable operating rule | Set conditions, sequence, boundaries and acceptance | A runtime implementation |
| Runtime | Callable operating capacity | Execute a bounded operation and return observable state or receipts | A synonym for documentation |
| Public surface | Human-facing entry point | Explain, distribute or route public material | The semantic source of truth |
| Archive / legacy | Preserved history | Retain prior states without governing the present | The current active source |
| MSL | Adaptive structural grammar | Choose proportionate form and preserve structural laws | A container, runtime or universal ontology |

## Use the responsibility map

Apply the map to an existing set of files, objects or workflows before creating new categories:

```text
Use the Moon Source Responsibility Map on the system below.

For each important item, identify:
1. what responsibility it currently appears to perform;
2. what responsibility it should own;
3. whether it is overloaded, duplicated or carrying another object's authority;
4. which object should remain authoritative;
5. the smallest repair: split, merge, relabel, bridge, handoff, protocol, archive or no change;
6. what must remain current and what should be demoted to lineage or archive.

Prioritize repairing ownership and transport. Do not generate every Moon Source object type unless the field requires it.

System:
[paste the file list, folder layout, workflow or object descriptions]
```

If the field itself is still unclear, begin with [Field to Form](FIELD_TO_FORM.md). If a structural artifact or handoff is needed, use [MSL 4.3](../portables/msl/MSL_4_3.md). If a procedure needs a concrete execution surface, use [Operational Devices](OPERATIONAL_DEVICES.md) with [Operational Reliability](OPERATIONAL_RELIABILITY.md). If intellectual material needs identity, lineage or custody protection while it moves, changes, forks, mirrors or passes through AI, use [Credits & Attribution Ops](CREDITS_ATTRIBUTION_OPS.md). If the unresolved issue is where ChatGPT work should run, use the [Chat–Work Routing Protocol V2](../portables/chat-work/CHAT_WORK_ROUTING_PROTOCOL_V2.md).

**Download the full public Moon Source:** [complete repository (.zip)](https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip). For individual files and portables, use the [download hub](../DOWNLOADS.md).

## Reading rule

When two objects appear to overlap, ask which responsibility is actually changing. Similar content does not make the objects interchangeable.

<!-- MOON-SOURCE-PUBLIC-STAMP -->

---

> 🌙 **Moon Source** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Source/blob/main/LICENSING.md) · [Use & attribution](https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md) · [Full source (.zip)](https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip)
