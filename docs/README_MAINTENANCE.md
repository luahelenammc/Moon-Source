# README maintenance contract

A README is a reader-facing orientation surface. It explains what its repository, module or example is for, where to begin, what is current, what the limits are, and where the authoritative material lives.

## Keep chronological history out

Do not use a README as a rolling update log. Sections such as *Recent changes*, *What changed in 6.1*, *Latest updates*, release notes, and version history belong in a dedicated history surface.

Use the existing owner for each kind of record:

- [`CHANGELOG.md`](../CHANGELOG.md) records repository-wide releases and material maintenance changes.
- [`registry/PUBLIC_CAPABILITIES.md`](../registry/PUBLIC_CAPABILITIES.md) and [`registry/public-capabilities.json`](../registry/public-capabilities.json) own the public capability inventory, current status and material-update chronology.
- A capability-specific `CHANGELOG.md`, such as [`portables/msl/CHANGELOG.md`](../portables/msl/CHANGELOG.md), owns its release history when that file exists.

Do not copy the same history into a README. A short link to the relevant changelog or registry is appropriate. Keep current facts that a reader needs to use or identify the artifact, such as its current version, compatibility route or status.

## Access and first-use language

Whenever a README, public catalog or onboarding document explains how an AI can use Moon Source, lead with **Plan A: pass the public GitHub repository/canonical-file URL to an AI with retrieval access**, requesting the smallest task-relevant source set and verifying which files were opened. **Plan B:** download/attach the relevant ZIP only if direct retrieval is unsupported, unavailable, incomplete, or an offline/reproducible snapshot is needed. Do not say or imply that a ZIP is universally required, that all AI systems can crawl links, or that reading grants activation, access permissions or mutation authority. [Reusable reader instructions](USE_WITH_AI.md).

Keep this rule visible in entry surfaces without duplicating it as a new large section in every specialist document. For portable READMEs, a concise link-first line with ZIP fallback is sufficient. Do not change licensing, semantic version, authority or package contents merely because access wording changes.

## Change rule

When an accepted change warrants a history record under the repository's release and registry rules, update the owning changelog or registry as part of that change. Keep the README focused on orientation, first use, current behavior and boundaries. Do not generate a *recent changes* digest in a README.

The four translated root READMEs are derived mirrors of [`README.md`](../README.md). They must follow its content and section structure; they are not separate places for localized updates or release history. Follow the [translation contract](README_TRANSLATIONS.md) when the canonical README changes.

For reader-facing prose, apply the [public editorial policy](PUBLIC_EDITORIAL_POLICY.md): present current functionality and practical limitations, not unpublished project work or internal publication decisions.

## Validation

Run `python scripts/moon_source.py readmes` for the focused check and `python scripts/moon_source.py validate` for the complete repository gate. The check rejects common changelog-style README headings and the retired generated-digest marker. It cannot detect history written under every possible heading, so review must still confirm that README prose serves a reader-facing purpose.

This is repository maintenance policy. It creates no public capability and does not by itself change a capability version.

<!-- MOON-SOURCE-PUBLIC-STAMP -->

---

> 🌙 **Moon Source** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Source/blob/main/LICENSING.md) · [Use & attribution](https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md) · [Full source (.zip)](https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip) · Questions, suggestions, or proposals? Feel free to contact me at [LuaHelenaMMC@gmail.com](mailto:LuaHelenaMMC@gmail.com).
