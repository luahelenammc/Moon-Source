# Repository Naming and Versioning Template

Use this template when a Moon Source-family repository needs a public rule for naming and releases.

## Title–version separation

**Title / name = identity.** Keep the human-facing title stable across ordinary releases.

**Version = state.** Record the current generation, compatibility state or release maturity separately in metadata, registry fields, release notes and changelog entries.

## Governed surfaces

Apply the stable title to:

- first-level document headings;
- registry `title` fields;
- website cards and navigation labels;
- human-facing download labels.

Keep version markers where they are technical coordinates or historical facts:

- dedicated `version` metadata;
- canonical filenames, paths and package filenames;
- compatibility identifiers, branches and release records;
- historical prose that is explicitly about an earlier generation.

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
