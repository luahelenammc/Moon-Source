# InfraJam 2026 submission copy — Project MRI

## Project name

Project MRI

## One-line pitch

See what your AI is being asked to believe: MRI finds stale, conflicting and ownerless context before it becomes an answer.

## Problem

AI-enabled projects accumulate decisions, instructions and notes that remain individually plausible but collectively incompatible. A retrieval system can surface all of them without knowing which source governs. The failure happens before generation: the project has no inspectable authority map.

## Solution

Project MRI scans a bounded project corpus, extracts typed claims/rules/decisions/facts, diagnoses duplication and authority leaks with source evidence, proposes a source-of-truth blueprint, records human review and exports a traceable result. Its repair path is deliberately proposal-only.

## Track

Open Source. MRI is a new, executable reference implementation of governed context infrastructure. It is also useful as a developer workflow because it has a one-command CLI, a local web review surface and machine-readable output.

## What was built

- bounded Markdown/text folder and ZIP ingestion;
- path traversal, symlink, size, count and UTF-8 safety checks;
- deterministic typed extraction;
- eight evidence-backed diagnostic families;
- source-of-truth blueprint and proposal-only repair plan;
- approve, reject and unresolved review ledger;
- fixed before/after question set;
- JSON/Markdown export and resettable demo;
- Northstar fixture with 8/8 predeclared-family recovery;
- CI and public-safe licensing/attribution map.

## Innovation

The differentiator is governance of context rather than retrieval volume: explicit authority, freshness, provenance, contradiction visibility and human review are treated as infrastructure.

## Technical complexity

The build combines bounded ingestion, typed extraction, evidence locators, deterministic diagnostics, schema validation, review state, reproducible evaluation and portable exports. The architecture has an extension seam for future providers without making a provider responsible for truth.

## Usefulness

MRI catches the moment when a project asks an AI to trust two incompatible instructions. It gives a developer a concrete path from mess to evidence to an explicit authority decision before that conflict becomes code or architecture.

## Presentation

The demo moves through: messy synthetic corpus → inventory → contradiction evidence → authority candidates → human review → sandbox record → fixed before/after output.

## Human oversight

MRI does not silently canonicalize, delete history or modify the input corpus. Review states record intent; `mutation_applied` remains false.

## Limitations

This is a bounded local reference build over synthetic fixtures. It is not a production connector, autonomous repair engine, compliance system, benchmark of model accuracy, private-data security claim or live Swift Compute integration.

## Run

```bash
python -m unittest discover -s tests -v
python -m mri demo --output out/demo
python -m mri eval fixtures/northstar --output evals/northstar
python server.py
```

## Authorship and lineage

Created and designed by **Lua Helena Moon Martins Cardoso (Moon)**, with AI-assisted coauthorial development by **Áurion**. MRI is a public-safe derived/reference implementation of principles developed in Moon Source.

- Moon Source: <https://github.com/luahelenammc/Moon-Source>
- Public architecture: <https://www.luahelena.com.br/moonsource/?lang=en>
- Professional context: <https://www.luahelena.com.br/ia/?lang=en>
