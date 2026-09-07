# Be My Eyes — Contextual Scene Reading

**Be My Eyes** is a Moon Source method for reading human communication as a scene rather than as isolated text.

It helps an AI distinguish what is directly observable from what is inferred, map actors and relationships, notice subtext and power, identify risk and opportunity, test for overread, estimate likely reception and choose a proportionate response axis.

> Read the scene, not the sentence alone. Preserve uncertainty where the scene does not support certainty.

Be My Eyes is not mind-reading. It is a disciplined interface between raw social material and useful action.

## 1. What problem it solves

Messages, threads, screenshots, meeting notes, posts and institutional exchanges often carry more than literal propositions. Meaning can depend on:

- who is speaking to whom;
- what each person is doing, not merely saying;
- prior relationship and asymmetry;
- authority, dependence or audience;
- timing and channel;
- what is conspicuously absent;
- how a message is likely to land;
- which interpretations are plausible but not evidenced.

A language model can fail in opposite directions here. It may flatten the material into paraphrase and miss the human scene, or it may invent motives and treat a plausible story as fact.

Be My Eyes exists between those failures.

## 2. Inputs

The method can operate on bounded material such as:

- a message or email;
- a thread or comment chain;
- a transcribed screenshot;
- meeting or interview notes;
- a public post;
- a log or dialogue excerpt;
- a draft the user plans to send;
- a description of an interaction when the description itself is clearly treated as the available evidence.

If decisive context is missing, the method should name that absence rather than silently manufacture the missing scene.

## 3. Two directions

### Forward read

The user provides material received from another person or environment and asks, in effect:

> What is happening here, and how should I understand or respond to it?

The method reads the incoming scene and may optionally support a response.

### Inverse read

The user provides something they created or plan to send and asks, in effect:

> How is this likely to arrive on the other side?

The method simulates plausible reception without pretending to know the recipient's actual private state.

Forward and inverse reads share the same epistemic discipline. The direction changes; the anti-overread rules do not.

## 4. Epistemic layers

Keep materially different claim classes distinct.

| Layer | Meaning |
|---|---|
| **Observed** | Directly present in the supplied material or otherwise established context |
| **Relational / structural inference** | Supported by interaction pattern, role, timing, wording or known context, but still inferred |
| **Working hypothesis** | Plausible explanation useful for deciding what to check or how cautiously to act |
| **Unknown** | Not supported well enough to resolve |

When several weak cues need calibration, use [Signal Calibration](SIGNAL_CALIBRATION.md). Be My Eyes may consume calibrated inference, but it does not turn inference into observation by repetition.

## 5. Scene map

Before interpreting subtext, reconstruct the smallest useful scene.

Ask:

1. **Actors** — Who is present or materially affected?
2. **Actions** — What is each actor actually doing?
3. **Stated content** — What is explicit?
4. **Relationship** — What relationship, dependency or history matters?
5. **Authority and power** — Who can decide, withhold, expose, punish, reward, ignore or redefine the interaction?
6. **Audience** — Is the exchange private, semi-public, institutional or performative?
7. **Timing and channel** — What does the medium or moment change?
8. **Missing context** — What would materially change the read if known?

The map should remain proportional. A two-line message does not need a constitutional convention.

## 6. Internal read

A useful Be My Eyes read usually answers the following, to the depth the situation deserves:

- **What is happening?** A factual scene reconstruction.
- **What is the relational structure?** Roles, alignment, asymmetry, dependency or audience.
- **What subtext is plausible?** Inference, explicitly marked as inference.
- **What is the main risk?** Misreading, escalation, exposure, oversharing, reputational cost, authority conflict or another context-specific risk.
- **What is the opportunity?** Clarification, trust, leverage, repair, boundary-setting, collaboration, de-escalation or useful silence.
- **Where is overread most tempting?** The story that feels satisfying but outruns the evidence.
- **What should be avoided?** The response move most likely to worsen the scene.
- **What is the best response axis?** The governing posture before wording: clarify, acknowledge, challenge, narrow, defer, document, disengage, ask, or another proportionate action.

Not every read needs all eight fields rendered as headings. They are responsibilities, not a mandatory template.

## 7. Reception read

For an inverse read, prioritize effect over authorial intention.

Check:

- what the recipient is likely to notice first;
- what authority, warmth, distance, confidence or pressure the message conveys;
- which sentence or gesture may carry more weight than the author expects;
- where ambiguity may invite an unintended interpretation;
- whether the message asks too much, too little or the wrong thing for the relationship;
- whether the tone and channel match the actual stakes;
- which alternative readings remain plausible.

A reception read should use bounded language such as **likely**, **may**, **could be read as** or **the strongest plausible read is** when certainty is not available.

## 8. Response drafting is optional

Be My Eyes can stop after the read.

If the user also needs an outgoing message, the draft should be generated **after** the scene has been reconstructed, not before. The draft should preserve the user's actual objective and channel constraints rather than merely imitate the other party's tone.

The method does not require diplomacy, bluntness, warmth or confrontation as a universal style. It determines which posture fits the scene, then the relevant voice or writing system handles wording.

## 9. Compact mode

For ordinary low-stakes material, a compact read is often enough:

```text
Scene:
Strongest read:
Risk / overread:
Best move:
```

For inverse reading:

```text
How it lands:
What works:
Where it may create friction:
Adjustment, if needed:
```

Compact mode is not a weaker epistemic standard. It is only a smaller rendering.

## 10. Anti-overread rules

Be My Eyes must not:

- present motive as fact merely because wording permits it;
- diagnose personality, pathology or hidden intent from thin interaction data;
- treat silence as proof of rejection, agreement, guilt or strategy without supporting context;
- confuse institutional role with private belief;
- turn one emotionally salient cue into the whole explanation;
- assume that the most dramatic interpretation is the most informative;
- collapse multiple plausible readings into false certainty;
- use confidence of prose as evidence.

When the evidence supports several materially different readings, say so and identify what would discriminate between them.

## 11. High-stakes boundary

In legal, clinical, safety, employment, financial or other high-stakes contexts, Be My Eyes may help organize the communication scene, but it does not replace domain evidence, professional standards or the authority that governs the underlying decision.

Use the method to separate observable interaction from interpretation. Do not use it as a shortcut to findings of fact, diagnosis, intent, capacity, liability or risk classification that require a stronger evidentiary process.

## 12. Relationship to adjacent Moon Source components

| Component | Owns | Be My Eyes adds |
|---|---|---|
| [Preflight](PREFLIGHT.md) | shaping the task before execution | scene reading once the communication itself is the object |
| [Signal Calibration](SIGNAL_CALIBRATION.md) | calibrating weak or convergent evidence | a human-interaction scene in which calibrated inference is applied |
| [Responsibility Map](RESPONSIBILITY_MAP.md) | ownership and authority between objects | interpersonal and institutional relation mapping inside the scene |
| [Connected Sources](CONNECTED_SOURCES.md) | access, source/data authority, freshness and connector boundaries | interpretation of the retrieved human communication without changing its authority |
| [Source Operations](SOURCE_OPERATIONS.md) | retrieve, process, metabolize and promote | a bounded processing method; no writeback is implied by the read |
| [Operational Reliability](OPERATIONAL_RELIABILITY.md) | failure-aware execution and receipts | no replacement; Be My Eyes is interpretive, not an execution receipt |

## 13. Public lineage

This component was **promoted on 2026-09-07** from a repeatedly used local/private Moon Source interface also named **Be My Eyes**.

The public promotion preserves the reusable function while removing local identity, private examples, relationship-specific voice, project-specific destinations and any assumption that a draft must be written in one person's style. The donor environment remains authoritative for its own local behavior; this file is the canonical public generalized method.

That transformation follows [Source Operations](SOURCE_OPERATIONS.md): promotion generalizes a proven mechanism without importing its private habitat.

## Claim ceiling

This component supports the claim that Moon Source publishes a bounded contextual scene-reading method for separating observation from inference, mapping actors and relationships, examining subtext, risk, opportunity, overread and likely reception, and selecting a proportionate response axis.

It does not support claims of:

- mind-reading or reliable access to hidden motives;
- psychological diagnosis;
- scientifically validated interpersonal prediction;
- guaranteed recipient reaction;
- automated truth determination;
- replacement of legal, clinical, investigative or other domain-specific evidentiary standards;
- external adoption or measured impact.

Be My Eyes can make a human scene more legible. It cannot subpoena another person's interiority.

<!-- MOON-SOURCE-PUBLIC-STAMP -->

---

> 🌙 **Moon Source** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Source/blob/main/LICENSING.md) · [Use & attribution](https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md) · [Full source (.zip)](https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip)
