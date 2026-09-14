# Claims map

| Claim | Class | Evidence or boundary |
|---|---|---|
| MRI scans a bounded folder or ZIP of UTF-8 Markdown/text | observed build behavior | `mri/ingest.py`, tests and CLI run |
| MRI emits typed objects, findings, blueprint, review ledger and exports | observed build behavior | `mri/pipeline.py`, `mri/report.py`, tests |
| Findings carry evidence paths and line ranges | observed build behavior | `mri/models.py`, validator and evidence tests |
| Eight diagnostic families are supported | observed build behavior | `mri/diagnostics.py` and Northstar fixture |
| Northstar recovers 8/8 predeclared families | observed fixture result | `fixtures/northstar/expected_findings.json` and `mri eval` |
| MRI is 100% accurate | prohibited claim | The eval is fixture recovery, not model accuracy |
| Review can record approve/reject/unresolved without source mutation | observed build behavior | `mri/review.py`, API and tests |
| MRI determines truth autonomously | prohibited claim | Authority remains a human decision |
| The project is production-ready or enterprise-ready | prohibited claim | Current server is local-only and bounded |
| MRI handles private or regulated corpora securely | unsupported claim | Public fixture is synthetic; no deployment security review exists |
| Live Swift Compute/GPU integration exists | prohibited claim | No credentials or live operation are present |
| External adoption, finalist or winner status exists | prohibited claim | No such status is claimed |
| Software is Apache-2.0 and documentation/fixtures are CC BY 4.0 | release policy | `LICENSING.md`, `LICENSE` and `NOTICE` |

<!-- MOON-SOURCE-PUBLIC-STAMP -->

---

> 🌙 **Moon Source** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Source/blob/main/LICENSING.md) · [Use & attribution](https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md) · [Full source (.zip)](https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip) · Questions, suggestions, or proposals? Feel free to contact me at [LuaHelenaMMC@gmail.com](mailto:LuaHelenaMMC@gmail.com).
