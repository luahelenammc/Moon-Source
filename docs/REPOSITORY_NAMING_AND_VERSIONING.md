# Repository Naming and Versioning

## Title–version separation

Moon Source public repositories use two different coordinates:

- **Title / name = identity.** A human-facing title names the capability, method, protocol or family and should remain stable across ordinary releases.
- **Version = state.** A version records the current generation, compatibility state or release maturity and belongs in dedicated metadata.

This separation keeps a person-facing name useful after a release advances. It also prevents a registry, website card or document heading from becoming stale merely because the underlying artifact moved from V2 to V3 or from 3.0 to 4.0.

## Required practice

For current public material:

1. Keep the stable title in first-level headings, registry `title` fields, website card labels, navigation labels and human-facing download names.
2. Put release state in a dedicated `version` field, metadata block, registry `version` field, changelog entry, release note or explicit sentence.
3. Keep version-bearing technical coordinates when they are useful or contractually required: canonical filenames, paths, package filenames, URLs, branch names, historical references and compatibility identifiers.
4. When discussing history, name the old generation explicitly and keep it grammatically separate from the current title.
5. Do not move a current naming/version rule into a local or private source when the rule governs this public repository family.

Examples:

```text
Title: Moon Source Language
Version: 5.0
Canonical path: portables/msl/MSL_5_0.md
Package: downloads/moon-source-language-5.0.zip
```

```text
Title: Preflight
Version: 2.0
Canonical path: portables/preflight/PREFLIGHT_V2.md
```

The technical path may preserve a version because it is an identity and compatibility coordinate. The public title should not become `Preflight V2`.

## Inheritance

Future Moon Source-family repositories should copy [the reusable policy template](../templates/REPOSITORY_NAMING_AND_VERSIONING.md), adapt its governed surfaces, and install an automated guard before a public promotion. The repository-level policy and guard are the authority for current public naming; local artifact conventions may add detail but may not reverse this separation.

## Validation

Moon Source validates the registry, canonical first-level headings and dedicated version fields with:

```text
python scripts/check_title_version_separation.py
python scripts/test_title_version_separation.py
```

The guard is intentionally scoped to governed public metadata and headings. It does not ban historical version references, technical filenames or ordinary prose that accurately describes release state.

## Visibility-neutral version tokens

Repository visibility is an orthogonal publication/distribution state, not part of a version token. Moon Source versions therefore use bare release state only. Public/private exposure belongs in repository location, status, boundary and distribution metadata; never append a visibility qualifier to the numeric version.

Removing a legacy visibility qualifier is a bookkeeping-only normalization and does not by itself advance the numeric release. Future accepted updates continue to follow the governing increment rule on the bare number itself.

<!-- MOON-SOURCE-PUBLIC-STAMP -->

---

> 🌙 **Moon Source** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Source/blob/main/LICENSING.md) · [Use & attribution](https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md) · [Full source (.zip)](https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip)
