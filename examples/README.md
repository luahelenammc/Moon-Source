# Public Examples

This directory contains bounded reference implementations of public Moon Source patterns. Examples are inspectable demonstrations, not stable portables, products, SDKs or proof of universal runtime support.

**Concept versus implementation:** the Moon Source methods define the intended procedure. The code and scenarios in this directory show selected, bounded ways to exercise or illustrate it. They do not install the architecture into a user's AI environment or demonstrate a finished product.

**MSL profile:** 5.1-compatible Markdown-native gallery surface; examples remain bounded, experimental or hypothetical as labelled.

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

## Conversational Context — Re-entry, Boundaries & Handoff (synthetic)

[`conversational-context/`](conversational-context/) demonstrates a common longitudinal application problem: how to resume a person's journey after a pause when the prior conversation and the current operational state may differ. The dependency-free Node.js example first selects only authorized API-, query- or spreadsheet-shaped fields, then evaluates a legitimate re-entry and whether a human should review conflicting or missing state.

Try the [runnable synthetic journey](conversational-context/README.md): an old dialogue says module 2, the current approved program state says module 3, and the result names the change without inventing an absence motive. The same fixture family tests revoked consent, unauthorized purposes, cross-person/region isolation and the distinction between `handoff_recommended` and `handoff_requested`. No user data is retrieved, no messages are delivered, and this is not a chatbot, production security control or legal-compliance engine. [Architecture contract](../docs/CONVERSATIONAL_CONTEXT.md).

## Hypothetical application scenarios

[`application-scenarios/`](application-scenarios/) is a fictional didactic gallery showing how Moon Source **could** be applied to common context problems across health and care, public services, customer journeys, company operations, audit, people and learning, third-sector coordination, and living documentation.

Every scenario is explicitly hypothetical and non-evidentiary. It does not describe a real client, organization, implementation, measured impact or independent validation. Read the gallery before adapting an example, and keep private source material, identifiers, credentials and protected operational detail out of public files.

## Example boundary

The examples use synthetic or local data only. Do not paste private selectors, endpoints, account data, cookies, tokens, passwords or private corpora into a public example. Keep the adapter separate from the generic device and review the public-boundary and claim files before adapting it to another surface.

<!-- MOON-SOURCE-PUBLIC-STAMP -->

---

> 🌙 **Moon Source** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Source/blob/main/LICENSING.md) · [Use & attribution](https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md) · [Full source (.zip)](https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip) · Questions, suggestions, or proposals? Feel free to contact me at [LuaHelenaMMC@gmail.com](mailto:LuaHelenaMMC@gmail.com).
