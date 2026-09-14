# Evals and evidence integrity

## Commands

```bash
python -m unittest discover -s tests -v
python -m mri eval fixtures/northstar --output evals/northstar
```

The first command covers the pipeline, review ledger, export, web routes and hostile ingestion cases. The second runs the fixed Northstar fixture.

## Northstar golden fixture

`fixtures/northstar/expected_findings.json` predeclares eight diagnostic families and the evidence paths required for a match:

- exact duplicate;
- near duplicate;
- contradiction;
- stale authority;
- unclear authority;
- missing owner;
- orphaned decision;
- scope/jurisdiction leak.

The current clean run recovers **8/8** cases. The metric is `fixture_recovery_rate`: expected cases recovered with their required evidence paths divided by expected cases.

This is fixture recovery, not model accuracy, benchmark superiority, production reliability, generalization or proof that any proposed authority is substantively correct.

## Negative case

`fixtures/clean_corpus/` is deliberately free of supported conflicts and is expected to produce zero findings. Keeping a negative case in the same test run prevents the demo from treating every corpus as broken.

## Observable before/after proxy

The demo asks a fixed storage-authority question. The pre-MRI proxy selects the oldest matching decision; the post-MRI proxy selects the latest dated candidate while preserving owner, authority and evidence fields. The result exposes candidate counts, distinct values and attached evidence.

It is a reproducibility aid for the synthetic fixture, not a health score and not a benchmark.

## Evidence integrity

The validator requires every finding to contain:

- a supported finding family;
- a supported severity and detection mode;
- a non-empty title, reason and proposed action;
- at least one source reference;
- a valid path and positive line range.

The test suite additionally checks that evidence paths and line ends are valid against the loaded fixture, that findings have unique IDs and that review records refer only to existing findings.

## Gaps

The eval does not measure retrieval over real repositories, model calibration, human agreement, latency, cost, deployment security, regulated-data handling or external-provider output. Those require a consented corpus and a separate review.
