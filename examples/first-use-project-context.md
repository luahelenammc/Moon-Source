# First-use project context: conflicting launch dates

> **Status:** fictional, synthetic walkthrough. It illustrates how a reader could inspect source authority and freshness. It is not a client case, an executed connector session, an implementation report or evidence of impact.

A project team keeps asking an AI when a launch is scheduled. Different files and chats mention different dates.

## Supplied source set

| Source | What it says | Visible status |
|---|---|---|
| Current project plan | Launch is approved for October 14. | Owned by the project lead and marked current. |
| Earlier meeting notes | Launch was planned for October 7. | Dated before the current plan; no longer marked active. |
| Team chat | “Maybe move it to October 21 if the vendor slips.” | A proposal. The chat contains no approval or changed plan. |

The dates are invented for this example. The table does not describe a real project.

## Read the task

A person asks: “Which date should I use? The AI has given me different answers in different chats.”

The immediate need is to identify the approved date and explain why the other dates do not currently govern. It is not yet a request to rewrite the project plan or build a new knowledge system.

## Smallest useful response

- **Approved date:** October 14.
- **Governing source:** the current project plan, which is owned by the project lead and marked current.
- **Why the other dates differ:** October 7 appears in older notes; October 21 is only a proposal in chat.
- **Still unknown:** whether the vendor condition has changed or the proposal was later approved. Check with the project lead or the current plan before treating October 21 as a decision.

This is an example of resolving source authority for one fact. It does not treat recency, search ranking or the amount of repeated text as a vote.

## One repeatable check

Ask the AI:

~~~text
Which launch date is approved?
Name the source that governs that date, say why the other dates do not,
and list anything you could not verify from the supplied material.
Do not update any source.
~~~

A useful bounded answer identifies October 14 from the current project plan, describes the other dates as superseded or proposed, and marks the unresolved vendor condition. If the AI cannot see the source status, it should say so instead of guessing.

If the project lead later approves a change, update the governing plan only with the right authorization, then reread it. A chat message by itself does not rewrite the plan.

## Where to go next

- [Setup](../portables/setup/MOON_SOURCE_SETUP.md) helps choose a small context for a person or project.
- [Source Hygiene](../docs/SOURCE_HYGIENE.md) covers stale, duplicate and contradictory material.
- [Connected Sources](../docs/CONNECTED_SOURCES.md) applies when current external sources and an available, authorized access surface are part of the task.
- [Source Operations](../docs/SOURCE_OPERATIONS.md) governs source changes and readback.

<!-- MOON-SOURCE-PUBLIC-STAMP -->

---

> 🌙 **Moon Source** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Source/blob/main/LICENSING.md) · [Use & attribution](https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md) · [Full source (.zip)](https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip) · Questions, suggestions, or proposals? Feel free to contact me at [LuaHelenaMMC@gmail.com](mailto:LuaHelenaMMC@gmail.com).
