# Repository Naming and Versioning Template

Use this template when a Moon Source-family repository needs a public rule for naming and releases.

## Title, summary and surface coordinates

Use three naming/presentation coordinates plus version:

- **Registry title / semantic identity.** The stable capability, method, protocol or family name.
- **Summary title.** The concise label used by lists, tables, download hubs and navigation cards.
- **Surface title.** The individual README and canonical-body H1, combining the summary title with a bounded `— Moon Source portable`, `— Moon Source component` or `— Moon Source architecture` qualifier.
- **Version.** The separate generation, compatibility or release state. It does not encode visibility, audience, distribution or habitat.

Keep these coordinates distinct. A concise summary does not create a new capability identity, a surface qualifier is not a version, and a version is not a visibility label.

## Stable canonical artifact naming and directory geometry

For every living/current module, capability, method, protocol, engine, portable or other semantic body, canonical filenames and paths identify the stable semantic object. Put current version state in artifact metadata, registries, changelogs, tags, releases and other explicit version surfaces. An ordinary version bump must not require a canonical rename.

Current package and mirror paths follow the same rule unless their versioned identity is intentionally immutable. Do not create version-, model- or release-specific directory branches when one stable semantic container is sufficient. Version-bearing current paths need a documented semantic reason, such as a schema or compatibility generation that remains valid in parallel.

Preserve historical snapshots, immutable release archives, migrations, explicit compatibility generations, external versioned standards and other genuinely parallel identities. When a current canonical path moves, repair references, registry entries, package members, hashes and governed mirrors, then read back the current surfaces. Do not leave active compatibility twins by default. Naming-only cleanup does not advance the semantic version.

## Governed surfaces

Use the coordinates deliberately:

- registry `title` fields and semantic metadata: stable registry title;
- repository lists, tables, cards and download hubs: summary title;
- individual capability READMEs and canonical bodies: surface title;
- metadata, release notes and changelogs: version;
- status/distribution/visibility metadata: audience and delivery state;
- canonical filenames, paths, current package filenames and current mirror paths: stable semantic identity; version markers require a documented semantic exception;
- historical URLs, branches, frozen release archives and compatibility identifiers: preserve their version when it is part of the historical or compatibility identity.

Current version identifiers must not contain audience, visibility or habitat labels such as `public`, `private` or `local`. Represent those properties separately. A version-bearing current technical path also needs a documented semantic exception; otherwise retain the old coordinate only in history or an intentionally immutable artifact.

Preserve full Moon Source naming in explicit project identity, dependency, lineage, licensing and attribution statements. Do not make a global textual replacement.

## Local adoption

Replace the placeholders below, then add a repository-level guard and tests before public promotion:

```text
Registry title: [stable semantic identity]
Summary title: [concise browsing label]
Surface title: [readable body title with Moon Source role]
Current version: [release state only]
Visibility: [public | private | other, if needed]
Distribution: [standalone | repository-only | other, if needed]
Canonical path: [technical path, if applicable]
Registry entry: [path or identifier]
Website/public surface: [path or URL, if applicable]
Validation command: [guard command]
```

The repository rule governs current public naming. A local artifact convention may preserve version information in a current path only for a documented semantic exception; it must not let ordinary release changes fossilize a canonical name or create version-specific directories without need.

<!-- MOON-SOURCE-PUBLIC-STAMP -->

---

> 🌙 **Moon Source** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Source/blob/main/LICENSING.md) · [Use & attribution](https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md) · [Full source (.zip)](https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip) · Questions, suggestions, or proposals? Feel free to contact me at [LuaHelenaMMC@gmail.com](mailto:LuaHelenaMMC@gmail.com).
