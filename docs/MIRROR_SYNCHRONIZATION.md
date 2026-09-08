# Mirror Synchronization

The Moon Source repository is the only semantic and versioning source for public capabilities. The branded files under LUAHELENA/moonsource/downloads/ are convenience mirrors of the current standalone distributions only.

## Contract

Each standalone-distribution record in the unified registry records:

- the canonical current repository path;
- the current mirror path and URL;
  - the capability version, when the capability is independently versioned;
  - the expected UTF-8 SHA-256 fingerprint of the canonical capability bytes;
- the checker that detects mismatch.

A mirror is synchronized only when its fetched bytes hash to the canonical fingerprint. A matching filename or matching version string is not sufficient.

When a new capability generation supersedes an older one, the older body is removed from the live Moon-Source/main tree and its old mirror is removed from the live LUAHELENA/main download tree. Historical generations remain recoverable through Git history and, when useful, immutable tags or releases. The mirror layer is a distribution surface, not a compatibility archive.

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

The 2026-09-02 Chat–Work V3 promotion is historical. On 2026-09-06, Chat–Work V4 became the current standalone distribution and mirror: the superseded V3 files were removed from both live trees, the exact V4 bytes were copied to the mapped mirror path, and the registry fingerprint was refreshed. On 2026-09-07, Setup advanced to 3.1, Connected Sources was promoted as a method plus 1.0-public standalone distribution, and Chat–Work advanced to 4.4-public; each current standalone distribution is mapped to one exact website mirror, with the superseded Chat–Work 4.3 mirror removed. MSL remains 4.3.

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

<!-- MOON-SOURCE-PUBLIC-STAMP -->

---

> 🌙 **Moon Source** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Source/blob/main/LICENSING.md) · [Use & attribution](https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md) · [Full source (.zip)](https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip)
