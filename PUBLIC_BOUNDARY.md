# Public Boundary

Moon Source is developed through a larger private and professional corpus. This repository is intentionally narrower.

## Public

The public body may include:

- the field-to-form distinction;
- responsibility boundaries;
- public terminology;
- interfaces and input/output expectations;
- public portables that are independently usable;
- evidence classes and non-claims;
- attribution and lineage;
- versioning and public-safe implementation notes.

## Reserved

The public body does not automatically include:

- full source-authority resolver rules;
- private calibration, thresholds or scoring;
- private diagnostic taxonomies;
- private compiler and evaluation machinery;
- private prompts, adapters or context corpora;
- detailed reconciliation, mutation and repair ordering;
- patient, client, collaborator or third-party material;
- deployment credentials, runtime state, hosts, quotas or ephemeral receipts;
- enough cross-file detail to reconstruct protected machinery with high fidelity;\n- the fine Skill Foundry compiler, promotion gates, hidden evaluation suites, MRI taxonomy, weights, labels, repair ordering or private corpus.

## Why this boundary exists

The boundary protects privacy, third-party material, unfinished work and legitimate intellectual property. It also improves public clarity. A public reader needs to understand the responsibility of a resolver or compiler before receiving its private implementation.

Public disclosure is not a promise of open-source licensing. A portable may be readable within its stated scope while the repository remains without a broad repository-wide license until that choice is ratified. Attribution guidance does not itself grant reuse rights.

## Reconstruction test

Before adding deep material, ask:

> Could a competent outsider reconstruct a material part of the private resolver, repair or compiler machinery from the combination now published?

If yes or plausibly yes, reduce the disclosure to principles, responsibilities, interfaces or bounded projections.

## Public-safe claim rule

Existing artifacts may be inspected, versioned and mapped. They must not be rewritten as adoption stories, validated case studies or successful outcomes when the evidence does not establish those claims.

## Public routes

For practical use, start with [Architecture](ARCHITECTURE.md) or [Field to Form](docs/FIELD_TO_FORM.md). For reusable procedures, use [Procedural Projection](docs/PROCEDURAL_PROJECTION.md); for corpus diagnosis, use [Source Hygiene](docs/SOURCE_HYGIENE.md). Use [Downloads](DOWNLOADS.md) to reach the current public materials.
