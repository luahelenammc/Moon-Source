# Repository Naming and Versioning

## Title, summary and surface coordinates

Moon Source public repositories use three naming/presentation coordinates plus version:

- **Registry title / semantic identity = identity.** A stable name for the capability, method, protocol or family. It remains in registry `title` fields and semantic metadata.
- **Summary title = concise browsing label.** A short label used in repository lists, tables and download hubs. It may omit the project prefix when the surrounding surface already establishes it; intrinsic names such as Moon Source Language remain intact.
- **Surface title = local readable identity.** The title shown in a capability README or canonical body. It combines the summary title with a bounded role qualifier such as `— Moon Source portable`, `— Moon Source component` or `— Moon Source architecture`.
- **Version = state.** A version records generation, compatibility or release maturity separately in dedicated metadata.

These coordinates are presentation layers, not competing semantic authorities. The registry `title` keeps the capability's stable identity; `summary_title` keeps list surfaces compact; `surface_title` makes an individual body self-identifying; and `version` records state.

## Required practice

For current public material:

1. Keep the registry title stable in machine-readable identity and semantic metadata.
2. Use the summary title for compact repository lists, README tables, download hubs and similar browsing surfaces.
3. Use the surface title in each individual capability README and canonical body H1. The role qualifier identifies the Moon Source portable, component or architecture; it is not a version marker.
4. Put release state in a dedicated `version` field, metadata block, registry `version` field, changelog entry, release note or explicit sentence.
5. Keep version-bearing technical coordinates when they are useful or contractually required: canonical filenames, paths, package filenames, URLs, branch names, historical references and compatibility identifiers.
6. When discussing history, name the old generation explicitly and keep it grammatically separate from the current title.
7. Do not globally replace the project name. Explicit project identity, dependency, lineage, licensing and attribution statements retain the full Moon Source name.
8. Do not move a current naming/version rule into a local or private source when the rule governs this public repository family.

Examples:

```text
Registry title: Moon Source Setup
Summary title: Setup
Surface title: Setup — Moon Source portable
Version: 3.1
Canonical path: portables/setup/MOON_SOURCE_SETUP.md
```

```text
Registry title: Moon Source Language
Summary title: Moon Source Language
Surface title: Moon Source Language — Moon Source portable
Version: 5.1
Canonical path: portables/msl/MSL_5_1.md
```

The technical path may preserve a version because it is an identity and compatibility coordinate. The public summary title should not become `Moon Source V2`, and a surface role qualifier should not become `Setup V2`.

## Inheritance

## Inheritance

Future Moon Source-family repositories should copy [the reusable policy template](../templates/REPOSITORY_NAMING_AND_VERSIONING.md), adapt its governed surfaces, and install an automated guard before a public promotion. The repository-level policy and guard are the authority for current public naming; local artifact conventions may add detail but may not reverse this separation.

## Validation

Moon Source validates the registry, canonical first-level headings and dedicated version fields with:

```text
python scripts/check_title_version_separation.py
python scripts/test_title_version_separation.py
```

The guard is intentionally scoped to governed public metadata and headings. It does not ban historical version references, technical filenames or ordinary prose that accurately describes release state.

<!-- MOON-SOURCE-PUBLIC-STAMP -->

---

> 🌙 **Moon Source** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Source/blob/main/LICENSING.md) · [Use & attribution](https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md) · [Full source (.zip)](https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip) · Questions, suggestions, or proposals? Feel free to contact me at [LuaHelenaMMC@gmail.com](mailto:LuaHelenaMMC@gmail.com).
