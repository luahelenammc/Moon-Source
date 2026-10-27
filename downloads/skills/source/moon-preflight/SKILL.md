---
name: moon-preflight
description: "Reconstruct what a person means and intends before acting. Use for People who want to speak naturally to AI without translating themselves into prompt-engineering language, especially when a request contains examples, corrections, implicit constraints, negative requirements or tangled context. Do not turn a clear simple request into an interrogation or treat an old frame as binding."
---

# Preflight

## Source and scope

This skill projects the public Moon Source method into an executable entry point. Read `references/source/portables/preflight/PREFLIGHT.md` before substantive work and follow its decision rules, outputs, boundaries and linked supporting references. This bundled copy is a versioned snapshot; consult https://github.com/luahelenammc/Moon-Source/blob/main/portables/preflight/PREFLIGHT.md when freshness matters or a revision may have superseded it. When unavailable, identify the snapshot and bound claims. See `references/PROVENANCE.json` for source hashes and link-only adaptations.

## Inputs and procedure

Use the conversation, examples, corrections, destination, constraints and available context. Infer what the context supports, ask only material questions, and mark missing evidence.

Separate the underlying job from suggested form; retain negative requirements and corrections; resolve material ambiguity from context where possible; ask only what changes the decision; adjust the active frame when evidence warrants. Apply the branches and guardrails in the canonical reference rather than treating this concise router as the full method.

## Output and safeguards

Return a correct, actionable frame and proportionate execution. Do not turn a clear simple request into an interrogation or treat an old frame as binding. Respect user authorization, source jurisdiction and privacy. If access, capability, source or permission is absent, report the limitation and return the smallest useful result; never claim a write or execution that was not observed. Separate source facts, inference and current state. Check the result against the canonical method's own QA and claims.

Created by Lua Helena Moon Martins Cardoso (Moon), with AI-assisted coauthorial development by Áurion. Public documentation is CC BY 4.0; see `LICENSE-CC-BY-4.0.txt`.
