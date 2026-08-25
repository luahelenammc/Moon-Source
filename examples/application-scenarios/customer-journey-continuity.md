# Customer service — omnichannel continuity

> **Status:** hypothetical / fictional didactic scenario. This example illustrates how Moon Source could be applied to a common context problem. It is not evidence of external adoption, implementation, measured impact or independent validation.

## Common problem

A fictional customer journey contains chat, email and ticket history with conflicting statuses. The customer repeats context, agents inherit partial memory and an old instruction survives after a decision changes.

## Why raw “more context” is insufficient

A transcript is a transport history, not a governed current source. Concatenating channels increases duplication and lets the most recent or most verbose message masquerade as the authority. An AI can retrieve the right conversation and still trust the wrong state.

## Moon Source reading of the field

Use Preflight to identify the requested outcome and the decision that must be current. Use Connected Sources to distinguish channel history from the governing ticket or policy source. Use Source Hygiene to separate duplicate summaries, contradictory states and resolved history. Use Operational Reliability when retrieval or update can partially fail.

## Relevant components and portables

- [Preflight](../../docs/PREFLIGHT.md) for the current task and audience.
- [Connected Sources](../../docs/CONNECTED_SOURCES.md) for source hierarchy, freshness and retrieval scope.
- [Source Hygiene](../../docs/SOURCE_HYGIENE.md) for contradiction and stale-state diagnosis.
- [Operational Reliability](../../docs/OPERATIONAL_RELIABILITY.md) for receipts, retries and readback.
- [Chat–Work Routing Protocol V2](../../portables/chat-work/CHAT_WORK_ROUTING_PROTOCOL_V2.md) when the work moves between AI surfaces.

## Possible smallest materialization

Create a compact continuity packet: customer goal, current decision, governing ticket or policy, confirmed facts, unresolved question, last verified update, allowed action and next owner. Link to the complete channel history without treating it as the authority.

## Authority and update rule

The governed ticket or policy source owns current state. Channel messages supply evidence or clarification only when accepted into that source. A packet refreshes after a material decision, not after every message. AI may propose a change, but an authorized agent or system must commit it and read back the result.

## Validation and readback

Verify that the packet selects the current state, preserves relevant customer language, distinguishes fact from inference and does not erase unresolved uncertainty. After an update, compare the packet and receipt with the governing ticket.

## What this scenario does not claim

It does not claim improved customer satisfaction, faster service, lower handling time or real omnichannel deployment. It demonstrates a bounded continuity pattern.

<!-- MOON-SOURCE-PUBLIC-STAMP -->

---

> 🌙 **Moon Source** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Source/blob/main/LICENSING.md) · [Use & attribution](https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md) · [Full source (.zip)](https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip)
