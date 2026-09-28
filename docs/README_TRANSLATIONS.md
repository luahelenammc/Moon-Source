# README translation contract

The root `README.md` is the only canonical semantic README. The translations make the public entry point easier to use; they are derived mirrors and do not become separate sources of authority. If wording differs, the English README governs until the affected translation is corrected.

## Supported mirrors

| Locale | Language | Stable path |
|---|---|---|
| `pt-BR` | Brazilian Portuguese | `translations/README.pt-BR.md` |
| `es` | Spanish | `translations/README.es.md` |
| `zh-CN` | Simplified Chinese | `translations/README.zh-CN.md` |
| `ru` | Russian | `translations/README.ru.md` |

Each mirror declares its locale, source path, contract path and SHA-256 fingerprint for the exact current bytes of `README.md`. The fingerprint detects stale source state; it does not prove linguistic correctness.

## Updating the README

A material change to the root README is incomplete until all four governed translations are updated in the same pull request and the translation check passes.

1. Finish the canonical English change, including its language selector.
2. Translate the complete README in section order. Do not summarize, omit qualifications or add claims.
3. Rebase internal links from the translation directory by adding `../` to root-relative targets. Keep external links, filenames, paths, commands, identifiers, versions and proper names intact.
4. Refresh the same canonical SHA-256 metadata in all four translations after the English README bytes are final.
5. Preserve the language-navigation block, structural markers, code fences and exact public stamp.
6. Run `python scripts/moon_source.py translations`, then `python scripts/moon_source.py validate`.

The language-navigation block is bounded by `MOON-SOURCE-LANGUAGE-NAV:START` and `MOON-SOURCE-LANGUAGE-NAV:END`. The root README links to every mirror. Each translation links back to English and to all sibling languages.

## What to translate

Translate human-facing prose, headings, table labels, examples and visible diagram labels into natural language for the locale. Keep stable capability names where they function as identities. Preserve code, commands, URLs, repository coordinates, filenames, paths, identifiers, automation markers and version values. A translation must retain the source's section order, heading levels, tables, lists, quotes and link targets.

## Validation and review

The repository validator checks that every mirror exists, has the correct locale and source declaration, carries the current source fingerprint, contains the required navigation and automation markers, preserves structural coverage and protected literals, and points to the same links after relative-link rebasing.

On pull requests, if `README.md` changes, the validator compares the pull-request diff with its base and requires all four translation paths to change in that same pull request. Local and push validation check current-state freshness without depending on GitHub event variables. The existing link, public-stamp and REUSE checks remain part of normal validation.

These deterministic checks establish presence, freshness, co-change and structural integrity. They cannot prove semantic fidelity. Reviewers remain responsible for checking that each language preserves the source's facts, limits, authority relationships and degree of certainty.

## Adding or retiring a language

To add a language, update this contract, the stable-path map, the root and translated language selectors, the validator and its regression tests, and provide a complete reviewed mirror with current metadata in the same change. Keep filenames stable; do not introduce date- or version-based translation directories.

To retire a language, remove it from the required path map and every language selector in a reviewed maintenance change, and explain the scope in the changelog. Do not leave a stale link or an ungoverned file presented as current.

This is repository-maintenance infrastructure. It does not create a public capability or, by itself, justify a capability-version change.

<!-- MOON-SOURCE-PUBLIC-STAMP -->

---

> 🌙 **Moon Source** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Source/blob/main/LICENSING.md) · [Use & attribution](https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md) · [Full source (.zip)](https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip) · Questions, suggestions, or proposals? Feel free to contact me at [LuaHelenaMMC@gmail.com](mailto:LuaHelenaMMC@gmail.com).
