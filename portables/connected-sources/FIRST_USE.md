# Connected Sources — First-Use Guide

_Read this before using the Connected Sources portable._

## What this is for

Connected Sources is a living-source protocol for reaching current external material while keeping access, authority, freshness, permission and readback distinct. It helps an AI work safely from a document, repository or other source that may continue to change.

The portable also works in standalone mode from material you supply directly.

## Nothing is installed

Reading `CONNECTED_SOURCES.md` does not install Google Drive, GitHub, a connector or synchronization. A product may expose a connector, but that capability must be checked in the current environment and authorized by you.

Use the canonical body [CONNECTED_SOURCES.md](CONNECTED_SOURCES.md). This [root FIRST_USE.md](../../FIRST_USE.md) is onboarding support, not a replacement semantic body.

## Say this first

Start with a capability probe:

~~~text
Use Connected Sources for this task.
First tell me whether you can operate in:
1. Standalone Mode from the material I provide,
2. Connected Read Mode for a reachable source,
3. Living Source Mode for an authorized write with readback,
or 4. Federated Source Mode across distinct authorities.

Do not assume a connector, write permission or freshness.
Task: [describe the source and need]
~~~

The protocol's four modes are:

- **Standalone Mode:** work only from supplied material.
- **Connected Read Mode:** reread a reachable source without inferring write permission.
- **Living Source Mode:** perform an authorized bounded write and read it back.
- **Federated Source Mode:** keep different substrates governing different facets.

## What happens next

The AI should identify the source locator, what the source actually governs, the operation requested, coverage and freshness, the mutation boundary and the fallback if the source cannot be reached.

Access is not authority. Read is not write. A successful write is not accepted as current until readback confirms the resulting state.

Google Drive can be a useful ChatGPT document-source route for durable living sources, and GitHub can complement it for executable or repository state. Neither is mandatory, universal or automatically authoritative.

## Minimal example

You want an AI to summarize the current version of a project brief and, only with approval, update one section.

Use Connected Sources and say:

~~~text
Use Connected Sources.
First read the current project brief at [locator].
Tell me which parts of it govern this task and whether you have read-only
or authorized write access. Do not change anything until I approve the exact
bounded mutation; after any write, read it back.
~~~

If the source cannot be reached, use Standalone Mode by providing the relevant excerpt and label it as supplied material.

## Manual actions and unavailable capabilities

You may need to connect an account, authorize a scope, provide a locator, approve a mutation, inspect the readback or perform the edit yourself. The portable cannot create connector access or turn a reachable file into a governing source.

A tool result, cached excerpt or search hit is not proof of freshness or authority by itself.

## What this portable does not claim

- No universal connector support or automatic synchronization.
- No exhaustive retrieval of every related source.
- No autonomous mutation without explicit authorization.
- No guarantee that a reachable source is authoritative.
- No guarantee that connected material is current until the relevant freshness/readback check passes.

## Troubleshooting

If a connector is unavailable, say:

~~~text
Use Standalone Mode.
Work only from the material I paste or attach.
List what would need to be checked manually for a connected or write route.
~~~

If a write was reported, ask for readback of the exact changed locator and verify the resulting state before treating the operation as complete.

<!-- MOON-SOURCE-PUBLIC-STAMP -->

---

> 🌙 **Moon Source** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Source/blob/main/LICENSING.md) · [Use & attribution](https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md) · [Full source (.zip)](https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip)
