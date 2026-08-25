# Knowledge & data — living documentation

> **Status:** hypothetical / fictional didactic scenario. This example illustrates how Moon Source could be applied to a common context problem. It is not evidence of external adoption, implementation, measured impact or independent validation.

## Common problem

A fictional project has documents, spreadsheets, AI chats and code. Different surfaces govern different facets, duplicate summaries become stale and the team wants AI assistance without exhaustive ingestion or silent mutation.

## Why raw “more context” is insufficient

A single mega-summary flattens repository, document and conversation responsibilities. It also makes freshness hard to see: a correct answer from yesterday may be wrong after a code or policy change. Exhaustive retrieval is costly and still does not resolve authority.

## Moon Source reading of the field

Use Connected Sources to map the source substrate, jurisdiction, retrieval scope, freshness and mutation authority. Use Source Hygiene to identify duplicated summaries and orphaned decisions. Use Operational Reliability for read-only diagnosis, bounded writes, receipts and recovery. Use MSL 4.3 when a packet or registry is actually needed.

## Relevant components and portables

- [Connected Sources](../../docs/CONNECTED_SOURCES.md) for federated source access.
- [Source Hygiene](../../docs/SOURCE_HYGIENE.md) for staleness and duplication.
- [Operational Reliability](../../docs/OPERATIONAL_RELIABILITY.md) for safe operation and readback.
- [Responsibility Map](../../docs/RESPONSIBILITY_MAP.md) for facet-level ownership.
- [MSL 4.3](../../portables/msl/MSL_4_3.md) for a bounded registry or continuity packet.

## Possible smallest materialization

Create a source map by facet: repository for executable state, document for policy or meaning, spreadsheet for current structured data, and conversation for discovery or unresolved discussion. Add targeted retrieval rules and a compact freshness/readback receipt rather than duplicating the corpus.

## Authority and update rule

Authority is federated by facet. The connector carries reach, not ownership. AI may retrieve, summarize or propose a mutation within its granted scope; an authorized source owner approves changes. After a material update, read back the target source and refresh only dependent summaries.

## Validation and readback

Verify that each answer can identify its governing source, that retrieval is no broader than needed, that stale summaries are visibly bounded and that the repository and document surfaces are not silently conflated. Test both a read-only path and a rejected unauthorized mutation.

## What this scenario does not claim

It does not claim a universal connector, autonomous synchronization, exhaustive knowledge graph, adoption or measured productivity impact. It is a fictional living-documentation pattern.

<!-- MOON-SOURCE-PUBLIC-STAMP -->

---

> 🌙 **Moon Source** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Source/blob/main/LICENSING.md) · [Use & attribution](https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md) · [Full source (.zip)](https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip)
