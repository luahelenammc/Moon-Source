# Mirror Synchronization

The `Moon-Source` repository is the only semantic and versioning source for the current public portable family. The branded files under `LUAHELENA/moonsource/downloads/` remain convenience mirrors so existing public paths do not break.

## Contract

Each registry entry records:

- the canonical repository path;
- the preserved mirror path and URL;
- the portable version;
- the expected UTF-8 SHA-256 fingerprint of the canonical bytes;
- the checker that detects mismatch.

A mirror is synchronized only when its fetched bytes hash to the canonical fingerprint. A matching filename or matching version string is not sufficient.

Mirroring is also a content-custody event. Apply [Credits & Attribution Ops](CREDITS_ATTRIBUTION_OPS.md) when an artifact crosses into another repository or public surface so canonical origin, semantic authority, exact-identity status and relevant attribution inheritance remain recoverable. If the bytes change, stop calling the result an exact mirror and classify the transformation honestly.

A matching fingerprint supports byte identity for the checked artifact. It does not prove authorship, ownership, permission or semantic freshness beyond the compared bytes.

## Update procedure

1. Update the canonical portable in this repository.
2. Run `python scripts/validate_portables.py` and `python scripts/check_links.py`.
3. Copy the exact canonical UTF-8 bytes to the mapped mirror path in the `LUAHELENA` repository on a branch.
4. Run `python scripts/check_mirror_sync.py` against the remote mirror or `--mirror-root` against a local site checkout.
5. Review the website PR for path preservation, rendering and production safety.
6. Merge only after SHA-256 equality is confirmed.

The 2026-08-16 rebase prepared exact mirror updates in [LUAHELENA PR #11](https://github.com/luahelenammc/LUAHELENA/pull/11), which merged into `main` as `31e1473ead26ba6f23900ad4f7259cbe2bdec7e4`. The mirror files were verified equal after PR #12 and PR #13, and GitHub Pages run `31985711151` completed successfully.

The 2026-08-17 repository-wide public-stamp release changed the canonical portable bytes. Their SHA-256 fingerprints were refreshed and the three branded mirrors were copied directly from `Moon-Source/main` in [LUAHELENA PR #18](https://github.com/luahelenammc/LUAHELENA/pull/18), merged as `055a413490273c1df26f89f9a011b5a33ec907c2`. Post-copy Git blob identities matched the canonical files byte-for-byte: Setup `2891435ad98f17940edbd761fd7b3bed83af4bbb`, MSL `dfb5e327e9813ad9dd3db15f5030efa21083edbd`, and Chat–Work `a74f0c20c56d81640512bf7fe78cc96e5adda548`.

## Mismatch detection

Run from the repository root:

```bash
python scripts/check_mirror_sync.py
```

For a local checkout of the website repository:

```bash
python scripts/check_mirror_sync.py --mirror-root /path/to/LUAHELENA
```

A non-zero exit means at least one canonical file or mirror has drifted.

## Public routes

Use the [portable registry](../registry/PUBLIC_PORTABLES.md) for canonical paths and fingerprints, the [download hub](../DOWNLOADS.md) for public access, [Credits & Attribution Ops](CREDITS_ATTRIBUTION_OPS.md) for mirror lineage and content custody, or [Architecture](../ARCHITECTURE.md) for the responsibilities behind the files.

<!-- MOON-SOURCE-PUBLIC-STAMP -->

---

> 🌙 **Moon Source** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Use & attribution](https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md) · [Full source (.zip)](https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip)
