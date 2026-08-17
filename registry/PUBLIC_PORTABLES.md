# Public Portables

These are the current public portables in the Moon Source family. Each has one canonical path in this repository.

| ID | Title | Version | Status | Function | Canonical path |
|---|---|---:|---|---|---|
| moon-source-setup | Moon Source Setup | 2.0 | current | Guided personal context setup | portables/setup/MOON_SOURCE_SETUP.md |
| moon-source-language | Moon Source Language | 4.3 | current | Adaptive structural grammar for context work | portables/msl/MSL_4_3.md |
| chat-work-routing | Chat–Work Routing Protocol V2 | 2.0-public | current | Surface, model and reasoning-effort routing | portables/chat-work/CHAT_WORK_ROUTING_PROTOCOL_V2.md |

## Website mirrors

The current branded website keeps convenience copies under:

- https://www.luahelena.com.br/moonsource/downloads/MOON_SOURCE_SETUP.md
- https://www.luahelena.com.br/moonsource/downloads/MOON_SOURCE_PUBLIC_PORTABLE_MSL_4_3.md
- https://www.luahelena.com.br/moonsource/downloads/CHAT_WORK_ROUTING_PROTOCOL_V2_MSL_4_3.md

These paths are mirrors for access. The repository paths above are the canonical semantic sources for the current public family.

## Freshness

Setup and MSL are general public documents, but their wording can evolve. Chat–Work contains product and model calibration that must be rechecked before being treated as current fact.

## Legacy policy

A superseded version should remain recoverable through Git history, an archive path or a preserved website URL where feasible. It should be marked superseded rather than silently deleted.


## Mirror synchronization contract

The repository paths in the table are the only current semantic sources. The branded website paths are convenience mirrors preserved for compatibility.

Each registry entry records the mirror path, mirror URL, portable version and canonical SHA-256 fingerprint. Run `python scripts/check_mirror_sync.py` after any portable or mirror change. The 2026-08-16 rebase prepared exact mirror updates in [LUAHELENA PR #11](https://github.com/luahelenammc/LUAHELENA/pull/11); production remains unchanged pending explicit Moon acceptance.
