# Browser Console Device

**Status:** experimental reference implementation

**Runtime label:** Authenticated Session Runtime

This example is the first public materialization of an [Operational Device](../../docs/OPERATIONAL_DEVICES.md). It demonstrates a generic, dependency-free browser-console collector bound to a synthetic `localhost` adapter.

It is intentionally not a stable portable. The adapter contract is surface-specific, DOMs and data shapes change, and cross-surface stability has not been demonstrated.

## What the core demonstrates

`collector.template.js` provides a bounded device with:

- explicit adapter binding;
- semantic discovery and stable-key deduplication;
- progressive loading rounds and stagnation stop;
- item and round caps;
- bounded concurrency and optional pacing/jitter;
- same-origin, same-session JSON enrichment when explicitly enabled;
- extraction confidence and source-method recording;
- per-item fault isolation;
- live secret-free checkpointing at `window.__MOON_SOURCE_BROWSER_DEVICE__`;
- partial-corpus preservation;
- JSON and CSV export, download and copy fallback;
- final readback with counts, status and stop reason.

The extraction ladder is adapter-controlled and should prefer, in order:

1. structured application state or explicit JSON;
2. semantic DOM or attributes;
3. metadata;
4. visible-text fallback.

## Adapter contract

The adapter must remain separate from the core and declare:

- name and version;
- intended origin/surface;
- discovery strategy;
- stable ID extraction;
- semantic extraction;
- optional enrichment;
- schema mapping;
- stop and limit assumptions;
- freshness and known-fragility notes;
- same-origin access requirement, if any.

The synthetic adapter in `demo/adapter.js` uses only the local DOM and `demo/items.json`. It includes a duplicate ID, a malformed item, progressive loading, a same-origin enrichment record with missing metadata and a final stagnation stop.

## Run the synthetic demo

Serve the repository from its root so the demo remains on one origin:

```bash
python -m http.server 8765
```

Open:

```text
http://localhost:8765/examples/browser-console-device/demo/
```

The page includes a small harness for the same bounded run. For the console-oriented flow, load the two files in DevTools Console or use the page's already-loaded globals:

```js
const result = await MoonSourceBrowserDevice.run({
  adapter: MoonSourceDemoAdapter,
  maxItems: 20,
  maxRounds: 5,
  maxStagnantRounds: 2,
  concurrency: 2,
  allowSameOriginSession: true
});

MoonSourceBrowserDevice.readback(result);
MoonSourceBrowserDevice.exportJSON(result);
MoonSourceBrowserDevice.exportCSV(result);
```

Expected properties of the synthetic run:

- the duplicate stable ID does not inflate the unique corpus;
- the progressive round adds two cards;
- the malformed card becomes an isolated item error;
- the incomplete metadata record remains `PARTIAL`;
- same-origin enrichment completes for valid records;
- the run keeps going after the malformed item;
- a secret-free checkpoint is written;
- a later round stops on stagnation;
- the final status is `PARTIAL`, not a false completeness claim.

## Session and safety boundary

`credentials: "include"` is used only by the core's same-origin helper when both the run and adapter explicitly opt in. The browser keeps the session credential; the device never reads or exports cookies, tokens, passwords or authorization headers.

The reference device is read-only by default and rejects cross-origin fetches. It does not bypass CAPTCHA, paywalls, access controls, CORS, fingerprinting or rate limits. A `403` or `429` is a stop/reassess signal; repeated challenge statuses reach `ABORTED_BY_GUARDRAIL`.

Account-state mutation, stealth persistence, credential extraction and private adapters are outside this example. A partial valid corpus is a valid bounded result.

## Output

[`output-schema.json`](output-schema.json) defines the secret-free JSON receipt. It includes device and adapter identity, sanitized origin context, timestamps, counts, status, stop reason, item-level provenance/confidence/warnings/errors, run-level findings and the public Moon Source stamp.

## Claim ceiling

This is one synthetic, bounded reference implementation. It does not establish a production crawler, universal browser runtime, automatic adapter generation, cross-site stability, completeness, autonomous operation or external adoption. Keep adapters surface-specific and review [Operational Reliability](../../docs/OPERATIONAL_RELIABILITY.md), [Public Boundary](../../PUBLIC_BOUNDARY.md) and [Evidence and Claims](../../EVIDENCE_AND_CLAIMS.md) before adapting the pattern.

<!-- MOON-SOURCE-PUBLIC-STAMP -->

---

> 🌙 **Moon Source** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Source/blob/main/LICENSING.md) · [Use & attribution](https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md) · [Full source (.zip)](https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip)
