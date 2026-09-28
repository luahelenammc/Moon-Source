# Moon Source for AI Builders

Moon Source is a governed-context architecture. It helps a system decide which sources matter, which source governs each responsibility, what may enter active context, what may be changed and how a consequential result is checked.

This guide explains where those decisions sit beside an existing AI stack. It is a presentation guide, not an SDK, runtime or new capability. The [Architecture](../ARCHITECTURE.md), [Moon Source AI Kernel](../MOON_SOURCE_AI_KERNEL.md) and linked capability bodies remain authoritative for their own responsibilities.

## Where it sits

~~~mermaid
flowchart LR
    human["Human request"] --> harness["Existing agent harness / runtime"]
    sources["Persistent sources"] --> access["Connector, search, RAG or other retrieval"]
    harness -->|"requests material"| access
    access -->|"candidate material, with locator and freshness when available"| governance["Moon Source-informed context governance"]
    governance -->|"bounded context and authority decision"| harness
    harness <--> model["Model"]
    harness --> action["Authorized tool action"]
    action -->|"readback"| sources
~~~

This is a responsibility map, not a deployed integration. Moon Source supplies public methods and boundaries; an existing harness performs the loop, a retrieval layer finds material, tools perform authorized actions, and a model reasons or generates. Products may combine these roles.

| Part of the stack | Responsibility | Moon Source boundary |
|---|---|---|
| Model | Reasons over supplied context and generates output. | Moon Source does not supply the model or prove a model’s memory. |
| Harness or runtime | Runs loops, tool calls, execution state and control flow. | Moon Source can inform the context and acceptance contracts; it is not the runtime. |
| RAG, search or vector store | Finds candidate material and may rank or retrieve it. | Retrieval does not decide which source governs or whether a result is current. |
| Persistent source or memory store | Keeps material available beyond one interaction. | Persistence alone does not establish authority, scope, provenance or freshness. |
| MCP, connector or tool | Exposes bounded read or action capability. | Reach is not permission to mutate, semantic ownership or proof of full coverage. |
| System prompt or instruction layer | Provides behavior rules to the model. | General behavior instructions do not replace current project facts or source ownership. |
| Moon Source | Organizes authority, responsibility, context scope, freshness, provenance, mutation boundaries and continuity. | It is a reference architecture and set of public methods, not a hosted service or universal integration. |

## Three integration patterns

### 1. Agent or harness loop

For a task that needs governed context, an existing harness can apply this responsibility sequence:

1. Reconstruct the request when its meaning is materially unclear or self-correcting. Use [Preflight](../portables/preflight/PREFLIGHT.md) when that changes the task.
2. Resolve which sources own the relevant facts or decisions. A source can govern one facet without governing the whole project.
3. Retrieve only the material the task needs, keeping its locator, revision or freshness status when available.
4. Give the model bounded context and let the existing harness execute the actual loop and tools.
5. Before a write, check authorization and scope. After a consequential write, reread the source or use an equivalent verification.

[Operational Reliability](OPERATIONAL_RELIABILITY.md) helps with diagnosis, bounded mutation and recovery when those concerns matter. Not every prompt needs all five steps.

### 2. RAG or other retrieval

A RAG index can make source material findable. It does not make every retrieved passage authoritative.

- Preserve the source identity and the facet it governs.
- Check whether the index or excerpt is fresh enough for the claim.
- Treat conflicting passages as a jurisdiction question, not a vote.
- State the retrieval coverage honestly. Search can discover material without proving a complete inventory.

Moon Source can inform how an application uses its retrieval layer. It does not provide a RAG engine, vector database or retrieval API.

### 3. Persistent memory and connected sources

A store can persist context while leaving unanswered who owns it, which parts remain current and who may change it.

Use [Moon Source Setup](../portables/setup/MOON_SOURCE_SETUP.md) to choose a small personal or project context. Consider [Connected Sources](CONNECTED_SOURCES.md) only when a persistent substrate and an authorized access surface actually exist. Use [Source Operations](SOURCE_OPERATIONS.md) when material needs to be retrieved, transformed, integrated into a governing source or deliberately generalized.

After an authorized material change, verify the resulting state. [Operational Reliability](OPERATIONAL_RELIABILITY.md) is useful when execution can fail partway or needs a receipt and recovery route. None of these documents imply a native connector for a particular framework or vendor.

## Compositions that may help

The routes below are conditional compositions, not a master workflow. Stop when the current responsibility is handled.

| Situation | Possible route | Why the next method enters | Authority stays with | Do not load the next method when… |
|---|---|---|---|---|
| A request is messy, then the user needs durable personal or project context | [Preflight](../portables/preflight/PREFLIGHT.md) → [Setup](../portables/setup/MOON_SOURCE_SETUP.md) | Preflight resolves the intended task; Setup enters only if a reusable context setup is actually needed. | The human’s current request and the source that owns each project fact. | The request is already clear or no persistent setup would help. |
| A current external source must inform a task | [Connected Sources](CONNECTED_SOURCES.md) → [Source Operations](SOURCE_OPERATIONS.md) | Connected Sources governs reach, freshness, scope and authority; Source Operations enters only to process or change material. | The designated source owner for the relevant facet. | Supplied material is enough, or no source action is warranted. |
| A corpus is stale, duplicated or contradictory | [Source Hygiene](SOURCE_HYGIENE.md) → [Source Operations](SOURCE_OPERATIONS.md) | Hygiene diagnoses the corpus; operations handles a confirmed retrieve, transformation, mutation or promotion. | The current governing source and the person authorized to change it. | There is no material corpus finding or evidence does not support mutation. |
| A context packet must cross a source, model or surface boundary | [Moon Source Language](../portables/msl/MOON_SOURCE_LANGUAGE.md) | MSL shapes a bounded passage when structure and semantic preservation matter. | The originating source remains authoritative; the packet is a transport surface. | The next interaction needs only ordinary conversation. |
| Routing across roots, surfaces, models or workers changes the execution plan | [Adaptive Orchestration Protocol](../portables/adaptive-orchestration/README.md) | AOP separates control root, execution surface, model capability, effort and delegation. | The competent control root and the sources it is authorized to use. | The task is small and its execution route is already obvious. |

The composition is complete when the needed responsibility has been handled. A link between methods does not make them mandatory neighbours.

## A review lens, not a score

When reviewing a context design, ask whether authority, freshness, provenance, duplication, contradiction, retrieval scope, mutation permission, readback, context load and human legibility are clear enough for this task. These are observational questions, not a validated metric or a universal quality score. Explain material gaps; do not manufacture a number.

## Inspect bounded examples

- [First-use project-context walkthrough](../examples/first-use-project-context.md) is a fictional, static example of authority and freshness decisions.
- [Browser Console Device](../examples/browser-console-device/README.md) is an experimental synthetic reference implementation with a runnable `localhost` demo and a read-only default.
- [Application-scenario gallery](../examples/application-scenarios/) is explicitly hypothetical.
- [Existing Implementations and Projections](EXISTING_IMPLEMENTATIONS.md) distinguishes public artifacts from implementation and adoption claims.

To inspect the full source before integrating, start with the [AI Kernel](../MOON_SOURCE_AI_KERNEL.md). For a bounded task, load the smallest relevant canonical body instead of treating the repository as one large prompt.

<!-- MOON-SOURCE-PUBLIC-STAMP -->

---

> 🌙 **Moon Source** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Source/blob/main/LICENSING.md) · [Use & attribution](https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md) · [Full source (.zip)](https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip) · Questions, suggestions, or proposals? Feel free to contact me at [LuaHelenaMMC@gmail.com](mailto:LuaHelenaMMC@gmail.com).
