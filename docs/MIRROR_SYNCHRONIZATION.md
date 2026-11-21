# Mirror Synchronization

**Branch D1 · exact public distribution.** The shared cross-project source-of-truth is [Cross-Source Mirror Sync Protocol](CROSS_SOURCE_MIRROR_PROTOCOL.md). This file retains only Moon Source → website mirror mappings, exact-byte validation, and release operations. It does not govern private F1 frozen runtime dependencies, S1 procedural mirrors, or R1 selective inheritance. Do not duplicate their generic algorithm here.

The Moon Source repository is the semantic and versioning source only for capabilities recorded in its unified registry. Branded files under LUAHELENA/moonsource/downloads/ mirror those current Moon Source bodies and registered standalone distributions. Independent AOP compatibility projections follow a separate pinned-source binding below.

## Contract

Each standalone-distribution record in the unified registry records:

- the canonical current repository path;
- the current mirror path and URL;
  - the capability version, when the capability is independently versioned;
  - the expected UTF-8 SHA-256 fingerprint of the canonical capability bytes;
- the checker that detects mismatch.

A mirror is synchronized only when its fetched bytes hash to the canonical fingerprint. A matching filename or matching version string is not sufficient.

When a new capability generation supersedes an older one, the older body is removed from the live Moon-Source/main tree and its old mirror is removed from the live LUAHELENA/main download tree. Historical generations remain recoverable through Git history and, when useful, immutable tags or releases. The registry-backed mirror layer is a distribution surface, not a compatibility archive. Foreign-source compatibility copies require an explicit binding and separate validation.

Mirroring is also a content-custody and licensing event. Apply [Credits & Attribution Ops](CREDITS_ATTRIBUTION_OPS.md) when an artifact crosses into another repository or public surface so canonical origin, semantic authority, exact-identity status and relevant attribution inheritance remain recoverable. Preserve the applicable license from [LICENSING](../LICENSING.md) and any third-party notice. If the bytes change, stop calling the result an exact mirror and classify the transformation honestly.

A matching fingerprint supports byte identity for the checked artifact. It does not prove authorship, ownership, permission or semantic freshness beyond the compared bytes.

## Update procedure

1. Update the canonical capability body in this repository.
2. Remove any superseded semantic body from the live canonical tree.
3. Run `python scripts/validate_public_capabilities.py` and the preserved link, licensing, stamp and title/version checks.
4. Copy the exact canonical UTF-8 bytes to the mapped current mirror path in the LUAHELENA repository on a branch.
5. Remove any superseded mirror file from the live website download tree.
6. Run `python scripts/check_mirror_sync.py` against the remote mirror or `--mirror-root` against a local site checkout.
7. Review the website PR for current-path integrity, rendering and production safety.
8. Merge only after SHA-256 equality is confirmed.

Historical mirror promotions and their fingerprints remain inspectable in Git history. They do not define the current mirror contract.

The 2026-09-02 Chat–Work V3 promotion is historical. On 2026-09-06, Chat–Work V4 became the current standalone distribution and mirror: the superseded V3 files were removed from both live trees, the exact V4 bytes were copied to the mapped mirror path, and the registry fingerprint was refreshed. On 2026-09-07, Setup advanced to 3.1, Connected Sources was promoted as a method plus 1.0-public standalone distribution, and Chat–Work advanced to 4.4-public; each current standalone distribution is mapped to one exact website mirror, with the superseded Chat–Work 4.3 mirror removed. That historical state still had MSL 4.3; the current MSL mirror now carries MSL 5.1. On 2026-09-09, Chat–Work advanced through 4.9 and 5.0 and then to 5.1 on the same V4 path; the exact 5.1 bytes are mapped to `moonsource/downloads/CHAT_WORK_ROUTING_PROTOCOL_V4_MSL_5_1.md`, while the superseded mirrors remain recoverable through Git history rather than the live website tree.

On 2026-09-24, current canonical bodies, packages and mirrors were normalized to stable semantic paths. MSL is mirrored at `moonsource/downloads/MOON_SOURCE_PUBLIC_PORTABLE_MSL.md`, Preflight at `moonsource/downloads/PREFLIGHT.md`, and Adaptive Orchestration at `moonsource/downloads/ADAPTIVE_ORCHESTRATION_PROTOCOL.md`. At that historical checkpoint, all six standalone packages used version-neutral current filenames. Preflight's 2.3 bytes were refreshed on the website; the current registry fingerprint and exact-byte mirror check now agree. Capability versions did not change.


## Independent AOP compatibility projections

Since 2026-11-20, [Adaptive Orchestration Protocol](https://github.com/luahelenammc/Adaptive-Orchestration-Protocol) owns its semantics, versions, adapters, source skill and canonical release packages. Moon Source is no longer its registry or build authority. Old AOP/Chat–Work Markdown routes in this repository are readable pointers; the composite ZIP, Chat–Work alias ZIP and skill ZIP remain byte-identical compatibility copies. The LUAHELENA AOP card links to the independent project, while its two old Markdown URLs retain exact core bytes for consumers that need the old routes.

The pinned source commit, core/package fingerprints, pointer routes and read-only comparison procedure are bound in [`downloads/external-projections/aop-compatibility.json`](../downloads/external-projections/aop-compatibility.json). Run `python scripts/check_aop_compatibility.py` locally, or pass `--source-root` and `--site-root` to compare the canonical AOP and LUAHELENA repositories. This check does not rebuild or publish external artifacts.

## Mismatch detection

Run from the repository root:

```bash
python scripts/check_mirror_sync.py
```

For a local checkout of the website repository:

```bash
python scripts/check_mirror_sync.py --mirror-root /path/to/LUAHELENA
```

A non-zero exit means at least one canonical current file or current mirror has drifted.

## Public routes

Use the [public capability registry](../registry/PUBLIC_CAPABILITIES.md) for canonical paths, roles and fingerprints, the [download hub](../DOWNLOADS.md) for standalone public access, [Credits & Attribution Ops](CREDITS_ATTRIBUTION_OPS.md) for mirror lineage and content custody, or [Architecture](../ARCHITECTURE.md) for the responsibilities behind the files.


On 2026-09-27, the Chat–Work Routing Protocol identity moved to Adaptive Orchestration Protocol at version 6.1 under the naming-only version rule. The canonical package and exact-byte website mirror used the new identity; the old folder, body, adapter paths, package and mirror became compatibility routes. This is a historical record; AOP authority has since moved to its independent repository.

<!-- MOON-SOURCE-PUBLIC-STAMP -->

---

> 🌙 **Moon Source** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Source/blob/main/LICENSING.md) · [Use & attribution](https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md) · [Full source (.zip)](https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip) · Questions, suggestions, or proposals? Feel free to contact me at [LuaHelenaMMC@gmail.com](mailto:LuaHelenaMMC@gmail.com).
