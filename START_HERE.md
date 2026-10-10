# Start Here

AI does not need a pile of everything about you. It needs the small amount of context that fits the task, with a clear idea of where that context came from and when it should change.

This page is a plain-language route into Moon Source. You can start with the problem you have; the names of the methods come later.

If you are evaluating this work for a team, a product or an interview, [From method to implementation](docs/FROM_METHOD_TO_IMPLEMENTATION.md) separates real self-use, inspectable demonstrations and the work still required for an external application.

## Make a first move

**Plan A:** copy the public [Moon Source Setup URL](https://github.com/luahelenammc/Moon-Source/blob/main/portables/setup/MOON_SOURCE_SETUP.md) into an AI conversation that can open GitHub links. Ask the AI to retrieve the canonical entry and its First use section, then use this prompt:

~~~text
Use Moon Source Setup for this task.
Look at the material I provide and identify the smallest context setup
that would help with this problem.
Tell me where it should live, what should stay out,
and how I can test and update it.
My problem: [describe it in ordinary words]
~~~

**Plan B:** if that AI cannot retrieve the link, attach the [Setup ZIP](downloads/moon-source-setup.zip) or paste the canonical text. [Access guide](docs/USE_WITH_AI.md).

Setup is a public method you can paste into a conversation. It does not install an app, create permanent memory or connect a source by itself. You may need to attach material or save the result where the AI can reach it next time.

## Find the smallest route

| If this sounds familiar | First useful move | Start with | Avoid |
|---|---|---|---|
| “AI keeps forgetting my project.” | Pick the current goal, key decisions and one place that should own them. Ask what needs an update when the project changes. | [Setup](portables/setup/MOON_SOURCE_SETUP.md) | Pasting every chat into one summary and hoping it stays current. |
| “I keep repeating the same things about myself.” | Name only the recurring preferences or context that would change the AI’s response. Decide where each item should live. | [Setup](portables/setup/MOON_SOURCE_SETUP.md) | Saving sensitive or one-off details just because they are available. |
| “Different chats or documents contradict each other.” | Choose one disputed fact and check who owns it, which source is current and whether the latest statement is a decision or a suggestion. | [Source Hygiene](docs/SOURCE_HYGIENE.md) | Blending the statements or treating the newest message as automatically authoritative. |
| “I don’t know what belongs in custom instructions.” | Separate general preferences about how the AI should work from facts that belong to one project. | [Setup](portables/setup/MOON_SOURCE_SETUP.md) | Putting every project detail into one global instruction box. |
| “I have too many notes and files.” | Look for duplicates, outdated sources and decisions with no visible owner before writing a shorter summary. | [Source Hygiene](docs/SOURCE_HYGIENE.md) | Making a mega-summary before deciding what still matters. |
| “I want AI to use current files.” | Check whether the AI can reach the actual source, what part it can read and whether the source is fresh enough for this task. | [Connected Sources](docs/CONNECTED_SOURCES.md) | Assuming a search result, connector or old copy is current and authoritative. |
| “I need to move context to another AI or thread.” | Carry the task, current state, governing sources, uncertainty and next step in a bounded handoff. | [Moon Source Language](portables/msl/MOON_SOURCE_LANGUAGE.md) | Copying the whole archive when only a small part needs to travel. |

These routes are starting points, not a required sequence. If the task is already clear, use the relevant method directly. If it is not, begin with the human need and let the smallest route emerge.

## What not to assume

- A model does not automatically remember material across separate conversations.
- A source that the AI can reach is not automatically allowed to govern every question.
- A connected account does not mean every file is readable or writable.
- A written method does not make a feature run in every AI product.
- More context is useful only when it changes the work in a relevant way.

If an answer seems wrong, ask which source and date support it, what the AI could actually read and what remains uncertain. For a persistent change, ask who can authorize it and how the changed source will be reread.

## Choose a deeper route

- [For AI builders](docs/FOR_AI_BUILDERS.md) explains how Moon Source fits beside models, harnesses, retrieval, memory and tools.
- [Field-to-Form Architecture](ARCHITECTURE.md#field-to-form) opens the full method.
- [Moon Source AI Kernel](MOON_SOURCE_AI_KERNEL.md) guides an AI receiving the repository.
- [The example gallery](examples/application-scenarios/) contains fictional worked scenarios.
- [The repository](README.md) returns to the complete public map.

<!-- MOON-SOURCE-PUBLIC-STAMP -->

---

> 🌙 **Moon Source** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Source/blob/main/LICENSING.md) · [Use & attribution](https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md) · [Full source (.zip)](https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip) · Questions, suggestions, or proposals? Feel free to contact me at [LuaHelenaMMC@gmail.com](mailto:LuaHelenaMMC@gmail.com).
