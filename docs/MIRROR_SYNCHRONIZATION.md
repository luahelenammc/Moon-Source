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

## Update procedure

1. Update the canonical portable in this repository.
2. Run `python scripts/validate_portables.py` and `python scripts/check_links.py`.
3. Copy the exact canonical UTF-8 bytes to the mapped mirror path in the `LUAHELENA` repository on a branch.
4. Run `python scripts/check_mirror_sync.py` against the remote mirror or `--mirror-root` against a local site checkout.
5. Review the website PR for path preservation, rendering and production safety.
6. Merge only after SHA-256 equality is confirmed.

The 2026-08-16 rebase prepared exact mirror updates in [LUAHELENA PR #11](https://github.com/luahelenammc/LUAHELENA/pull/11). Production `main` remains unchanged until Moon accepts promotion.

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
