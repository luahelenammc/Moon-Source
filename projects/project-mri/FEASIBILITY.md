# Project MRI feasibility

## Current reference build

The project is a standard-library Python pipeline with a local HTTP demo. It runs without a model, account, GPU or external service. The public fixture is synthetic and intentionally small.

The executable body now includes bounded folder/ZIP ingestion, typed extraction, eight diagnostic families, evidence/schema validation, a human review ledger, fixed before/after evaluation and JSON/Markdown export.

## User workflow

1. provide a bounded project corpus;
2. inspect the inventory and source references;
3. open conflicts and authority candidates;
4. approve, reject or defer proposed changes;
5. compare a fixed question before and after;
6. export a traceable report.

## Deployment boundary

The current server binds to `127.0.0.1` and uses a checked-in synthetic fixture. A real deployment would need authentication, corpus isolation, upload policy, retention/deletion controls, observability, secret management and a privacy review before accepting external data.

## Roadmap

1. **Reference build — current:** reproducible local implementation and public-safe fixtures.
2. **Consented pilot — future:** one approved corpus, adjudication protocol, authenticated boundary and measured human agreement.
3. **Provider/runtime extensions — future:** optional adapters, only when a real operation improves the workflow and can be independently verified.

## Out of scope

Autonomous source mutation, unattended approval, broad repository crawling, private corpus ingestion, regulated-data claims, public hosting, production SLOs, model benchmarking and binding third-party account terms.

<!-- MOON-SOURCE-PUBLIC-STAMP -->

---

> 🌙 **Moon Source** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Source/blob/main/LICENSING.md) · [Use & attribution](https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md) · [Full source (.zip)](https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip) · Questions, suggestions, or proposals? Feel free to contact me at [LuaHelenaMMC@gmail.com](mailto:LuaHelenaMMC@gmail.com).
