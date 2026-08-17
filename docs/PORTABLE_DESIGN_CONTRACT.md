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
- avoid implying universal validity, adoption or impact without evidence.

## Canonicalization

A portable has one canonical path in this repository. A website or other surface may mirror it for convenience, but the mirror must preserve version, content identity and links back to the canonical repository.

## Reuse

Use of a portable is governed by its own stated terms and any other applicable permission. Attribution guidance explains how credit should be preserved when a use is permitted; it does not grant rights by itself. A repository-wide open-source license is not assumed unless one is explicitly added later.


## Mirror synchronization

A mirror may exist for access and backward-compatible URLs, but it is never a second semantic source. Preserve the mapped path, version and exact canonical bytes. Record the expected SHA-256 fingerprint in `registry/public-portables.json` and verify it with `scripts/check_mirror_sync.py`.
