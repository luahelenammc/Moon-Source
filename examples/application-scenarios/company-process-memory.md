# Company operations — process memory and AI adoption

> **Status:** hypothetical / fictional didactic scenario. This example illustrates how Moon Source could be applied to a common context problem. It is not evidence of external adoption, implementation, measured impact or independent validation.

## Common problem

A fictional operations team performs a recurring process through a mixture of SOPs, chat messages, spreadsheets and the memory of two experienced people. An AI assistant retrieves contradictory instructions, and nobody knows which material is current.

## Why raw “more context” is insufficient

Ingesting every conversation preserves local exceptions without deciding whether they remain valid. A spreadsheet may be current for a threshold while an SOP governs the sequence. The AI does not become an authority because it can see both.

## Moon Source reading of the field

Use Source Hygiene to inventory authority, freshness, duplication and orphaned decisions. Use Responsibility Map to distinguish source, procedure, device and owner. Use Procedural Projection when a stable method deserves a reusable procedure. Use Connected Sources for targeted retrieval and Operational Reliability for bounded mutation. Setup 3.0 can route a smaller personal or project context when the team is not ready for a larger corpus.

## Relevant components and portables

- [Source Hygiene](../../docs/SOURCE_HYGIENE.md) for corpus diagnosis.
- [Responsibility Map](../../docs/RESPONSIBILITY_MAP.md) for authority and ownership.
- [Procedural Projection](../../docs/PROCEDURAL_PROJECTION.md) for source-to-procedure separation.
- [Connected Sources](../../docs/CONNECTED_SOURCES.md) for retrieval scope and freshness.
- [Operational Reliability](../../docs/OPERATIONAL_RELIABILITY.md) for safe execution and receipts.
- [Setup 3.0](../../portables/setup/MOON_SOURCE_SETUP.md) for proportionate entry.

## Possible smallest materialization

Create an authority table for the process: governing source, procedure version, exception owner, review cadence, AI retrieval scope, mutation gate and last readback. Keep chat as provenance and discovery unless a decision is explicitly promoted into the procedure or source.

## Authority and update rule

Each process facet has one governing source. The procedure describes how to act; it does not silently become the source of every fact. An AI may summarize or propose a change, but a named owner approves material changes. The next review is triggered by a process change, contradiction, failed execution or scheduled freshness check.

## Validation and readback

Test the smallest representative questions against the authority table, verify that stale instructions are visibly demoted, and inspect the receipt after any mutation. Confirm that a new team member can find the current source without relying on the two experienced people.

## What this scenario does not claim

It does not claim successful AI adoption, process improvement, productivity gains or enterprise validation. It is a fictional way to make the authority problem inspectable.

<!-- MOON-SOURCE-PUBLIC-STAMP -->

---

> 🌙 **Moon Source** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Source/blob/main/LICENSING.md) · [Use & attribution](https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md) · [Full source (.zip)](https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip)
