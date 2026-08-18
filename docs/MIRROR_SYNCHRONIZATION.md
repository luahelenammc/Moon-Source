# Mirror Synchronization

The `Moon-Source` repository is the only semantic and versioning source for the current public portable family. The branded files under `LUAHELENA/moonsource/downloads/` remain convenience mirrors so existing public paths do not break.

## Contract

Each registry entry records:

- the canonical repository path;
- the preserved mirror path and URL;
- the portable version;
- the expected UTF-8 SHA-256 fingerprint of the canonical bytes;
- the checker that detects mismatch.

A mirror is synchronized only when its fetched bytes hash to the canonical fingerprint. A matching filename or matching version string is not sufficient. Apply [Credits & Attribution Ops](CREDITS_ATTRIBUTION_OPS.md) when the mirror is presented outside its canonical repository so the source relationship and semantic authority remain visible.

## Update procedure

1. Update the canonical portable in this repository.
2. Run `python scripts/validate_portables.py` and `python scripts/check_links.py`.
3. Copy the exact canonical UTF-8 bytes to the mapped mirror path in the `LUAHELENA` repository on a branch.
4. Run `python scripts/check_mirror_sync.py` against the remote mirror or `--mirror-root` against a local site checkout.
5. Review the website PR for path preservation, rendering and production safety.
6. Merge only after SHA-256 equality is confirmed.

The 2026-08-16 rebase prepared exact mirror updates in [LUAHELENA PR #11](https://github.com/luahelenammc/LUAHELENA/pull/11), which merged into `main` as `31e1473ead26ba6f23900ad4f7259cbe2bdec7e4`. The mirror files are now in production `main`; canonical and mirror bytes were verified equal on 2026-08-16 after PR #12 and PR #13, and GitHub Pages run `31985711151` completed successfully.

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

Use the [portable registry](../registry/PUBLIC_PORTABLES.md) for canonical paths and fingerprints, the [download hub](../DOWNLOADS.md) for public access, [Credits & Attribution Ops](CREDITS_ATTRIBUTION_OPS.md) for provenance and mirror credit, or [Architecture](../ARCHITECTURE.md) for the responsibilities behind the files.
