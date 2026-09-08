# Chat–Work — First-Use Guide

_Read this before using Chat–Work for the first time._

Chat–Work is a portable instruction-level routing protocol. It helps an AI read the task, separate surface, model, reasoning effort and context, and coordinate execution and return across Chat, Work and optional Codex.

For Moon Source-wide orientation, start with the [root FIRST_USE.md](../../FIRST_USE.md).

## First, the important boundary

Nothing is installed.

Loading or attaching a Markdown file does not install software, create a native ChatGPT router or grant privileged access to OpenAI's internal routing. Moon Source has no hidden integration with internal ChatGPT systems. Chat–Work can only work with the capabilities and actions that the current product surface actually exposes.

Think of it as a policy layer that the model reads and applies. It is inspectable and portable, not a background service.

## What it can do — and what it cannot do

Chat–Work can:

- recommend the best available surface, model tier, reasoning effort and context route for the task;
- explain why that route fits;
- prepare a handoff for Work, Codex or another available executor;
- tell you when a manual change in the interface is needed;
- structure the return to Chat for verification, acceptance and closure.

It cannot physically switch models, reasoning levels or Chat/Work/Codex surfaces by itself unless the current environment explicitly exposes an actionable switch to the assistant. For ordinary use, expect the protocol to tell you what should change; you make that change manually in the UI. If an environment does expose a direct action, the protocol must still distinguish a requested switch from a switch that actually occurred.

## Which model should I start with?

You do not need a frontier model just to initialize Chat–Work.

Start in Chat with a normal, sufficiently capable general model available to you. Prefer a sustainable default tier rather than pre-escalating to the most expensive or scarce option. Let Chat–Work recommend escalation only when the task's capability floor or reasoning demand actually requires it.

Model names, plans and availability change. Tier language such as “efficient,” “balanced,” “strong” or “frontier” is therefore more durable than assuming one product label. `AUTO` means “let the protocol route this task after reading it”; it does not mean “the interface will switch itself.”

## What exactly should I upload?

The minimum operational file is:

- `CHAT_WORK_ROUTING_PROTOCOL_V4.md`

You should read this `FIRST_USE.md` yourself before starting. If convenient, attach both files to the conversation. This guide explains how to use the protocol; it does not replace it, override it or change its authority.

## What should I say after uploading it?

Use this simple starter prompt:

```text
Read and apply the Chat–Work Routing Protocol to this task.
Start in AUTO.
Before execution, tell me the recommended surface/model/reasoning route and clearly tell me if I need to make any manual switch in the UI.

Task: [describe what you want done]
```

Then replace the bracketed line with a real task. A real task gives the protocol something operational to route; a question about the protocol itself may produce only an explanation or audit.

Minimal example: `Task: Help me route a multi-file documentation change and tell me whether I need to switch surfaces manually.`

## What happens next?

`Chat understands/routes → you make any required manual switch → Work/Codex/another available model executes → the result returns to Chat → Chat verifies and closes`

In practical terms, Chat–Work separates deciding where a task belongs from carrying it out. The human remains the bridge when the product does not expose a direct transition.

## Troubleshooting: “It only audited the session”

That behavior does not mean the protocol is broken.

Loading the file alone does not force a physical model or surface change. An audit-like question can naturally produce an audit, route explanation or session reading. Give the protocol a real task and explicitly ask it to apply the routing protocol operationally. If it recommends a surface or model that is unavailable in your account or current interface, it must say so and give you the closest honest route; it must not pretend that a switch happened.

## What Chat–Work does not promise

- no hidden or privileged OpenAI integration;
- no guaranteed access to Work, Codex or frontier models;
- no automatic entitlement, plan or allowance changes;
- no guaranteed automatic model or surface switching;
- no universal token-savings or quality guarantee;
- no claim that model routing itself was invented here.

## What it is useful for

Used honestly, Chat–Work makes routing policy explicit and inspectable. It helps separate surface, reasoning, capability and context; keep escalation bounded; preserve budget survivability; and return completed work to Chat in a form that can be checked and closed.

<!-- MOON-SOURCE-PUBLIC-STAMP -->

---

> 🌙 **Moon Source** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Source/blob/main/LICENSING.md) · [Use & attribution](https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md) · [Full source (.zip)](https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip)
