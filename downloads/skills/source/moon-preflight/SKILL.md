---
name: moon-preflight
description: "Perform automatic self-prompt engineering for the user: translate ordinary human expression into a faithful working task before execution. Use for conversational, incomplete, self-correcting or constraint-rich requests. Do not confuse this core with conditional authority, safety or source guardrails."
---

# Preflight

## Source and scope

This skill projects the public Moon Source method into an executable entry point. Read `references/source/portables/preflight/PREFLIGHT.md` before substantive work and follow its decision rules, outputs, boundaries and linked supporting references. This bundled copy is a versioned snapshot; consult https://github.com/luahelenammc/Moon-Source/blob/main/portables/preflight/PREFLIGHT.md when freshness matters or a revision may have superseded it. When unavailable, identify the snapshot and bound claims. See `references/PROVENANCE.json` for source hashes and link-only adaptations.

## Inputs and procedure

Use the conversation, examples, corrections, destination, constraints and available context. Infer what the context supports, ask only material questions, and mark missing evidence.

Construct or revise a task-level working prompt yourself: separate intended outcome from literal phrasing, recover supported positive and negative requirements, preserve corrections and context, and define observable success only where useful. Act without exposing fabricated internal reasoning. Ask only what changes a consequential decision. Activate source, risk, jurisdiction and mutation guardrails only when the task warrants them; they protect execution and do not define Preflight.

## Output and safeguards

Return a correct, actionable frame and proportionate execution. Do not turn a clear simple request into an interrogation or treat an old frame as binding. Respect user authorization, source jurisdiction and privacy. If access, capability, source or permission is absent, report the limitation and return the smallest useful result; never claim a write or execution that was not observed. Separate source facts, inference and current state. Check the result against the canonical method's own QA and claims.

Created by Lua Helena Moon Martins Cardoso (Moon), with AI-assisted coauthorial development by Áurion. Public documentation is CC BY 4.0; see `LICENSE-CC-BY-4.0.txt`.

<!-- MOON-SOURCE-PUBLIC-STAMP -->

---

> 🌙 **Moon Source** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Source/blob/main/LICENSING.md) · [Use & attribution](https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md) · [Full source (.zip)](https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip) · Questions, suggestions, or proposals? Feel free to contact me at [LuaHelenaMMC@gmail.com](mailto:LuaHelenaMMC@gmail.com).
