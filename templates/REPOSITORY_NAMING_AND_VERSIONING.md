# Repository Naming and Versioning Template

Use this template when a Moon Source-family repository needs a public rule for naming and releases.

## Title, summary and surface coordinates

Use three naming/presentation coordinates plus version:

- **Registry title / semantic identity.** The stable capability, method, protocol or family name.
- **Summary title.** The concise label used by lists, tables, download hubs and navigation cards.
- **Surface title.** The individual README and canonical-body H1, combining the summary title with a bounded `— Moon Source portable`, `— Moon Source component` or `— Moon Source architecture` qualifier.
- **Version.** The separate generation, compatibility or release state.

Keep these coordinates distinct. A concise summary does not create a new capability identity, and a surface qualifier is not a version.

## Governed surfaces

Use the coordinates deliberately:

- registry `title` fields and semantic metadata: stable registry title;
- repository lists, tables, cards and download hubs: summary title;
- individual capability READMEs and canonical bodies: surface title;
- metadata, release notes and changelogs: version;
- canonical filenames, paths, package filenames, URLs, branches and compatibility identifiers: technical coordinates, which may retain version markers.

Preserve full Moon Source naming in explicit project identity, dependency, lineage, licensing and attribution statements. Do not make a global textual replacement.

## Local adoption

Replace the placeholders below, then add a repository-level guard and tests before public promotion:

```text
Registry title: [stable semantic identity]
Summary title: [concise browsing label]
Surface title: [readable body title with Moon Source role]
Current version: [release state]
Canonical path: [technical path, if applicable]
Registry entry: [path or identifier]
Website/public surface: [path or URL, if applicable]
Validation command: [guard command]
```

The repository rule governs current public naming. A local artifact convention may preserve version information in technical coordinates but must not turn that coordinate into the current human-facing title or a second semantic identity.

## Local adoption

## Local adoption

Replace the placeholders below, then add a repository-level guard and tests before public promotion:

```text
Stable title: [human-facing identity]
Current version: [release state]
Canonical path: [technical path, if applicable]
Registry entry: [path or identifier]
Website/public surface: [path or URL, if applicable]
Validation command: [guard command]
```

The repository rule governs current public naming. A local artifact convention may preserve version information in technical coordinates but must not turn that coordinate into the current human-facing title.

<!-- MOON-SOURCE-PUBLIC-STAMP -->

---

> 🌙 **Moon Source** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Source/blob/main/LICENSING.md) · [Use & attribution](https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md) · [Full source (.zip)](https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip) · Questions, suggestions, or proposals? Feel free to contact me at [LuaHelenaMMC@gmail.com](mailto:LuaHelenaMMC@gmail.com).
