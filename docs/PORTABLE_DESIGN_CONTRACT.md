# Portable Design Contract

A public portable must be independently readable within its declared scope.

## Required metadata

Each current portable should identify:

- title;
- version;
- status;
- language;
- author and creator;
- Moon Source lineage;
- canonical repository path;
- Moon Source public surface;
- Moon's professional context;
- dependencies;
- freshness caveats;
- attribution and usage boundary;
- route to the [Credits & Attribution Ops Protocol](CREDITS_ATTRIBUTION_OPS.md) for reuse, adaptation, mirroring and generated-output credit;
- important non-claims.

## Content contract

A portable should:

- explain its function before its architecture;
- state who it is for;
- define what it does and does not do;
- preserve enough context to be useful on its own;
- name the authority or source lineage behind its claims;
- avoid private dependencies;
- distinguish current state from historical material;
- keep platform-specific facts date-sensitive when needed;
- preserve source lineage and identify local adaptation when an external resource materially shaped the portable;
- avoid implying universal validity, adoption or impact without evidence.

## Canonicalization

A portable has one canonical path in this repository. A website or other surface may mirror it for convenience, but the mirror must preserve version, content identity and links back to the canonical repository.

## Reuse

Use of a portable is governed by its own stated terms and any other applicable permission. [Credits & Attribution Ops](CREDITS_ATTRIBUTION_OPS.md) explains how to preserve authorship, lineage and local adaptation when a use is permitted; it does not grant rights by itself. A repository-wide open-source license is not assumed unless one is explicitly added later.


## Mirror synchronization

A mirror may exist for access and backward-compatible URLs, but it is never a second semantic source. Preserve the mapped path, version and exact canonical bytes. Record the expected SHA-256 fingerprint in `registry/public-portables.json` and verify it with `scripts/check_mirror_sync.py`.

## Public routes

Use the [portable registry](../registry/PUBLIC_PORTABLES.md) for canonical files and fingerprints, the [download hub](../DOWNLOADS.md) for distribution, [Credits & Attribution Ops](CREDITS_ATTRIBUTION_OPS.md) for bounded reuse and provenance, or [Architecture](../ARCHITECTURE.md) for the underlying responsibilities.

<!-- MOON-SOURCE-PUBLIC-STAMP -->

---

> 🌙 **Moon Source** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Use & attribution](https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md) · [Full source (.zip)](https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip)
