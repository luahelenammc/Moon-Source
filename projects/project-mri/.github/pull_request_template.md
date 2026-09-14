## What changed?

<!-- Describe the smallest useful change. Link the relevant finding or issue. -->

## Verification

- [ ] `python -m unittest discover -s tests -v`
- [ ] `python -m mri eval fixtures/northstar --output <temporary-directory>`
- [ ] The change preserves bounded ingestion and evidence line ranges.
- [ ] No credentials, private corpus, or unverified provider claim was added.

## Claim boundary

- [ ] Any new performance, accuracy, or production claim has a reproducible
  test and an evidence source.
- [ ] Human review remains required before an action is accepted.
