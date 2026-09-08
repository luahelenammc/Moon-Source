# Public service — citizen journey across departments

> **Status:** hypothetical / fictional didactic scenario. This example illustrates how Moon Source could be applied to a common context problem. It is not evidence of external adoption, implementation, measured impact or independent validation.

## Common problem

A fictional citizen request moves between several departments. Documents are stored in different systems, handoffs occur informally and the citizen repeatedly explains the same situation. Staff cannot easily tell which source governs eligibility, status, responsibility or public communication.

## Why raw “more context” is insufficient

Putting every document into one long summary does not resolve jurisdiction. It can expose internal material unnecessarily, preserve obsolete statuses and hide which department may change which field. More text produces a larger ambiguity surface.

## Moon Source reading of the field

Begin with Preflight and Field to Form: identify the citizen-facing question, the internal decisions and the smallest public response. Apply the Responsibility Map by facet rather than by a single “owner” for the entire journey. Connected Sources can map the systems without treating search reach as authority. Source Hygiene can surface duplicates and stale handoff notes.

## Relevant components and portables

- [Preflight](../../docs/PREFLIGHT.md) for entry-point diagnosis and question threshold.
- [Field to Form](../../docs/FIELD_TO_FORM.md) for bounded public and internal forms.
- [Responsibility Map](../../docs/RESPONSIBILITY_MAP.md) for departmental jurisdiction.
- [Connected Sources](../../docs/CONNECTED_SOURCES.md) for provenance and targeted retrieval.
- [Source Hygiene](../../docs/SOURCE_HYGIENE.md) for stale and duplicated material.
- [MSL 4.3](../../portables/msl/MSL_4_3.md) for a handoff or status packet.

## Possible smallest materialization

Create a journey ledger with one row per active request: citizen-facing identifier, current status source, responsible department, next handoff, documents still required, last verified update and public-safe explanation. Keep internal reasoning, personal data and restricted documents in their governing systems.

## Authority and update rule

Each field has a declared governing department or source. A handoff changes responsibility only when the receiving role accepts it. A public summary can expose status and next step without becoming authoritative for the internal record. When status changes, update the source first, then regenerate or read back the bounded summary.

## Validation and readback

Check that the citizen can understand the next action, that the internal owner is explicit, that links point to the correct source and that the public summary does not disclose restricted material. Reconcile the ledger against current department sources at each material handoff.

## What this scenario does not claim

It does not describe a real public body, citizen, service-level result, reduction in repetition or deployed government system. It is a fictional application sketch.

<!-- MOON-SOURCE-PUBLIC-STAMP -->

---

> 🌙 **Moon Source** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Source/blob/main/LICENSING.md) · [Use & attribution](https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md) · [Full source (.zip)](https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip)
