# Security policy

## Scope

Project MRI is a local, bounded reference implementation. It is not a hosted service and should not be given private or regulated corpora without an independent deployment review.

## Current protections

- ZIP traversal and symlink rejection;
- bounded file count, member size and expanded corpus size;
- UTF-8/text-only ingestion;
- no execution of ingested files;
- no mutation of the original corpus;
- local-only HTTP binding;
- no credentials in fixtures or repository files.

## Reporting

Please do not publish a suspected vulnerability with private data. Open a GitHub issue with a minimal synthetic reproduction, or contact Lua through the public address listed in the repository profile.

## Non-goals

The current protections do not establish tenant isolation, encryption policy, retention compliance, authorization, sandboxing of a deployment or secure processing of sensitive documents.

<!-- MOON-SOURCE-PUBLIC-STAMP -->

---

> 🌙 **Moon Source** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Source/blob/main/LICENSING.md) · [Use & attribution](https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md) · [Full source (.zip)](https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip) · Questions, suggestions, or proposals? Feel free to contact me at [LuaHelenaMMC@gmail.com](mailto:LuaHelenaMMC@gmail.com).
