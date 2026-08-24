# Public Examples

This directory contains bounded reference implementations of public Moon Source patterns. Examples are inspectable demonstrations, not stable portables, products, SDKs or proof of universal runtime support.

## Browser Console Device

[`browser-console-device/`](browser-console-device/) is an experimental, dependency-free Browser Console Device with a synthetic `localhost` demo.

It demonstrates how a bounded procedure can:

- discover items from a concrete surface;
- deduplicate by stable key;
- load progressively with a stagnation stop;
- enrich through a same-origin session without exporting credentials;
- isolate malformed items instead of aborting the corpus;
- preserve partial results and a live checkpoint;
- emit JSON/CSV receipts and a final readback.

It intentionally does not provide a production crawler, extension, bookmarklet, userscript, cross-origin client, auto-adapter generator or access-control bypass.

The reference remains **experimental** and is not registered as a current portable. Use the component contracts first:

- [Operational Devices](../docs/OPERATIONAL_DEVICES.md)
- [Operational Reliability](../docs/OPERATIONAL_RELIABILITY.md)
- [Failure to Capability — Failure Foundry](../docs/FAILURE_FOUNDRY.md)

## Example boundary

The examples use synthetic or local data only. Do not paste private selectors, endpoints, account data, cookies, tokens, passwords or private corpora into a public example. Keep the adapter separate from the generic device and review the public-boundary and claim files before adapting it to another surface.

<!-- MOON-SOURCE-PUBLIC-STAMP -->

---

> 🌙 **Moon Source** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Use & attribution](https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md) · [Full source (.zip)](https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip)
