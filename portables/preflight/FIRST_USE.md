# Preflight — First-Use Guide

_Read this before using the Preflight portable._

## What this is for

Preflight reconstructs what a human is actually trying to accomplish before an AI acts on literal, messy, incomplete or conversational wording. It is useful when the intended outcome, corrections, constraints or desired tone are easy to miss.

It is an interpretation-and-routing layer. It is not a permanent change to ChatGPT, an installation or a replacement for your judgment.

## Nothing is installed

Reading or attaching `PREFLIGHT_V2.md` does not install a service, change a model, create memory or make the AI read hidden context. The portable works from the request and material actually available in the current conversation.

Use the canonical body [PREFLIGHT_V2.md](PREFLIGHT_V2.md). This [root FIRST_USE.md](../../FIRST_USE.md) is onboarding support, not a second semantic authority.

## Say this first

Provide the canonical file and use one of these starts:

~~~text
Apply Preflight to my next request.
First reconstruct the intended outcome, corrections and constraints.
Ask only questions that would change the route.

Request: [describe what I want]
~~~

You can also request a mode explicitly:

- `Preflight` — reconstruct intent, then continue when the route is clear.
- `Silent` — use the method without displaying the full reconstruction unless needed.
- `Preflight only` — show the reconstruction and stop before execution.
- `Show reconstructed task` — make the working task explicit.
- `Deep` — use heavier analysis when ambiguity or consequence makes it worthwhile.

## What happens next

The AI should identify the likely outcome, preserve corrections and constraints, ask only route-changing questions and then use ordinary language for the answer or action. It should not turn every low-risk request into an architectural interview.

You can correct the reconstruction directly. A correction is more useful than pretending the first inference was certain.

## Minimal example

You say:

~~~text
I want to post this update. Make it stronger and warm, but not needy
or like I am begging for approval.
~~~

A useful Preflight reconstruction might be: create a public-facing update with confident warmth, preserve the substance, avoid pleading language and show the revised draft before posting. It should then ask only for missing information that would change that route.

## Manual actions and unavailable capabilities

Preflight can clarify and prepare. It cannot publish, send, switch a product surface or perform an unavailable action unless the current environment explicitly exposes that action and you authorize it. If the AI cannot see an image, file or prior message, paste, attach or describe it.

For consequential tasks, approve the reconstructed task before an external write or other irreversible step.

## What this portable does not claim

- It does not read hidden thoughts or know intent with certainty.
- It does not guarantee how another person will react.
- It does not permanently change ChatGPT or install a global behavior.
- It does not replace professional judgment, evidence or explicit authorization.
- It is not a formal specification of every future request.

## Troubleshooting

If the response becomes too architectural, say:

~~~text
Preflight only. Use ordinary language.
Reconstruct my intended outcome, corrections and constraints in a few lines,
then stop. Do not load the whole Moon Source repository.
~~~

If the reconstruction is wrong, correct the outcome or constraint directly and ask the AI to update the working task.

<!-- MOON-SOURCE-PUBLIC-STAMP -->

---

> 🌙 **Moon Source** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Source/blob/main/LICENSING.md) · [Use & attribution](https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md) · [Full source (.zip)](https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip)
