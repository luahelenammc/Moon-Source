# Moon Source — First-Use Guide

_Read this before deciding what to load, attach or “install” from Moon Source._

Moon Source is a public context architecture for human–AI work. It is a repository of reusable methods, portable instructions, supporting documents and governance patterns for deciding what should exist, what governs, what travels and what stays current.

It is not one application, one model, a mandatory runtime or a hidden ChatGPT integration. Most public materials are instruction and context artifacts: an AI can read them and apply their method, but reading a Markdown file does not install a service.

## Do I need to install anything?

Usually, no.

The repository and its portable ZIP packages do not install a background service, create memory, connect an account or switch a model or product surface. A downstream tool may have its own installation or connector flow; that is a separate, explicit capability and must not be inferred from the presence of a Moon Source file.

For a first use, choose the smallest useful portable and provide its canonical file to the AI. You do not need to load the whole repository.

## The three first-use routes

| Situation | Start here |
|---|---|
| You are a human deciding what Moon Source is and where to begin | This guide, then the relevant portable's `FIRST_USE.md` |
| An AI receives the whole repository or the complete ZIP | `MOON_SOURCE_AI_KERNEL.md`, then the smallest relevant canonical files |
| You have one concrete need | The smallest matching portable and its `FIRST_USE.md` |

For a full-repository handoff, the AI-side entry point is [MOON_SOURCE_AI_KERNEL.md](MOON_SOURCE_AI_KERNEL.md). This root guide is the human orientation layer; it does not replace the kernel or any canonical portable body.

## Choose the smallest portable

| Need | First-use guide | Canonical body |
|---|---|---|
| Set up proportionate context for a person or project | [Setup `FIRST_USE.md`](portables/setup/FIRST_USE.md) | [MOON_SOURCE_SETUP.md](portables/setup/MOON_SOURCE_SETUP.md) |
| Reconstruct what a person means before execution | [Preflight `FIRST_USE.md`](portables/preflight/FIRST_USE.md) | [PREFLIGHT_V2.md](portables/preflight/PREFLIGHT_V2.md) |
| Read a message, image, thread or draft as a human scene | [Be My Eyes `FIRST_USE.md`](portables/be-my-eyes/FIRST_USE.md) | [BE_MY_EYES.md](portables/be-my-eyes/BE_MY_EYES.md) |
| Reach current external material without confusing access with authority | [Connected Sources `FIRST_USE.md`](portables/connected-sources/FIRST_USE.md) | [CONNECTED_SOURCES.md](portables/connected-sources/CONNECTED_SOURCES.md) |
| Choose a proportionate source, handoff, packet or protocol form | [MSL `FIRST_USE.md`](portables/msl/FIRST_USE.md) | [MSL_4_3.md](portables/msl/MSL_4_3.md) |
| Route work across Chat, Work, Codex or another available surface | [Chat–Work `FIRST_USE.md`](portables/chat-work/FIRST_USE.md) | [CHAT_WORK_ROUTING_PROTOCOL_V4.md](portables/chat-work/CHAT_WORK_ROUTING_PROTOCOL_V4.md) |

The guide explains first use. The canonical body remains the semantic authority. A `README.md` or ZIP wrapper should orient delivery, not create a second version of the method.

## A normal first run

1. Open the matching `FIRST_USE.md`.
2. Read its plain-language boundary and manual-action notes.
3. Provide the linked canonical body to the AI, by attaching it, pasting it or using an already available repository copy.
4. Use the guide's starter prompt and add the real task.
5. Let the AI explain the next step before assuming that a connector, switch, write or persistent source is available.

A portable can be useful standalone. Loading the entire repository is optional and should be justified by the task.

## Generic starter prompt

If you are unsure which portable fits, start with:

~~~text
I need help with [describe the need].
Recommend the smallest Moon Source portable for this task.
Do not load the whole repository unless it is necessary.
Tell me which canonical file to provide, what I should say first,
and what may require a manual action.
~~~

## What Moon Source does not silently grant

- Access to a connector, repository, account, model, plan, memory store or product surface.
- Permission to read or mutate a source merely because it is reachable.
- A guarantee that an AI has loaded every file in a ZIP or understands the whole architecture.
- A universal runtime, automatic synchronization or privileged OpenAI routing.
- Authority for a support guide to override the canonical semantic body.

When a product cannot perform a requested step, the honest next action is a manual step, an explicit capability check or a smaller standalone route.

## Minimal example

You want an AI to understand what you mean before answering, but your request is conversational and unfinished.

Use [Preflight `FIRST_USE.md`](portables/preflight/FIRST_USE.md), provide [PREFLIGHT_V2.md](portables/preflight/PREFLIGHT_V2.md), and say:

~~~text
Apply Preflight to my next request.
First reconstruct the intended outcome, corrections and constraints.
Ask only what would change the route.
Request: [my real request]
~~~

You do not need to provide the full Moon Source repository for that task.

## If the first result feels too architectural

Say:

~~~text
Use only the smallest matching Moon Source portable.
Explain the result in ordinary language.
Do not load the whole repository or invent a connector, switch or persistent memory.
~~~

Then give a concrete task or correction. The method should become proportionate to the need, not a new vocabulary burden.

<!-- MOON-SOURCE-PUBLIC-STAMP -->

---

> 🌙 **Moon Source** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Source/blob/main/LICENSING.md) · [Use & attribution](https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md) · [Full source (.zip)](https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip)
