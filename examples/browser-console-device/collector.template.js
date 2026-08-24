/*
 * Moon Source — Browser Console Device
 * Experimental, dependency-free reference implementation.
 *
 * This file is the generic device. Bind it to a concrete surface through an
 * explicit adapter; do not add real selectors, private endpoints or secrets.
 */
(function (global) {
  "use strict";

  var DEVICE_VERSION = "0.1.0-experimental";
  var CHECKPOINT_KEY = "__MOON_SOURCE_BROWSER_DEVICE__";
  var CHALLENGE_STATUSES = { 403: true, 429: true };
  var PUBLIC_STAMP = {
    project: "Moon Source",
    creator: "Lua Helena Moon Martins Cardoso (Moon)",
    ai_assisted_coauthor: "Áurion",
    use_and_attribution:
      "https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md",
    full_source: "https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip"
  };

  var DEFAULTS = {
    mode: "read-only",
    maxItems: 100,
    maxRounds: 5,
    maxStagnantRounds: 2,
    concurrency: 2,
    delayMs: 0,
    jitterMs: 0,
    allowSameOriginSession: false,
    challengeStopThreshold: 2
  };

  function now() {
    return new Date().toISOString();
  }

  function isObject(value) {
    return value !== null && typeof value === "object" && !Array.isArray(value);
  }

  function isSecretKey(key) {
    return /(?:password|passwd|secret|token|cookie|authorization|auth[_-]?header|api[_-]?key)/i.test(
      String(key)
    );
  }

  function sanitize(value, depth) {
    var level = depth || 0;
    if (level > 6) return "[depth-limited]";
    if (value === null || typeof value === "string" || typeof value === "number" || typeof value === "boolean") {
      return value;
    }
    if (typeof value === "undefined") return null;
    if (Array.isArray(value)) return value.map(function (item) { return sanitize(item, level + 1); });
    if (isObject(value)) {
      var output = {};
      Object.keys(value).forEach(function (key) {
        if (!isSecretKey(key)) output[key] = sanitize(value[key], level + 1);
      });
      return output;
    }
    return String(value);
  }

  function publicClone(value) {
    return sanitize(value, 0);
  }

  function errorRecord(error, phase, itemId) {
    var source = error || {};
    var status = Number(source.http_status || source.status || 0) || null;
    return {
      domain: source.domain || "INSTRUMENT",
      phase: phase || "run",
      item_id: itemId || null,
      code: source.code || (status ? "HTTP_" + status : "UNCLASSIFIED_ERROR"),
      message: String(source.message || source),
      http_status: status
    };
  }

  function challengeStatus(record) {
    return Boolean(record && CHALLENGE_STATUSES[record.http_status]);
  }

  function wait(ms) {
    return new Promise(function (resolve) { setTimeout(resolve, Math.max(0, ms || 0)); });
  }

  function randomJitter(amount) {
    if (!amount) return 0;
    return Math.floor(Math.random() * (amount + 1));
  }

  function pace(config) {
    return wait((config.delayMs || 0) + randomJitter(config.jitterMs || 0));
  }

  function boundedNumber(value, fallback, minimum, maximum) {
    var number = Number(value);
    if (!Number.isFinite(number)) return fallback;
    return Math.min(maximum, Math.max(minimum, Math.floor(number)));
  }

  function safeConfig(input) {
    var source = input || {};
    return {
      mode: source.mode === "read-only" ? "read-only" : "read-only",
      maxItems: boundedNumber(source.maxItems, DEFAULTS.maxItems, 1, 10000),
      maxRounds: boundedNumber(source.maxRounds, DEFAULTS.maxRounds, 1, 100),
      maxStagnantRounds: boundedNumber(source.maxStagnantRounds, DEFAULTS.maxStagnantRounds, 1, 20),
      concurrency: boundedNumber(source.concurrency, DEFAULTS.concurrency, 1, 10),
      delayMs: boundedNumber(source.delayMs, DEFAULTS.delayMs, 0, 60000),
      jitterMs: boundedNumber(source.jitterMs, DEFAULTS.jitterMs, 0, 60000),
      allowSameOriginSession: Boolean(source.allowSameOriginSession),
      challengeStopThreshold: boundedNumber(
        source.challengeStopThreshold,
        DEFAULTS.challengeStopThreshold,
        1,
        10
      )
    };
  }

  function safeLocation() {
    var locationObject = global.location || { origin: "unknown", pathname: "unknown" };
    return {
      origin: String(locationObject.origin || "unknown"),
      path: String(locationObject.pathname || "unknown")
    };
  }

  function normalizeConfidence(value) {
    var allowed = { high: true, medium: true, low: true, unknown: true };
    var normalized = String(value || "unknown").toLowerCase();
    return allowed[normalized] ? normalized : "unknown";
  }

  function normalizeItem(item, stableId, adapter, locationContext) {
    var source = isObject(item) ? publicClone(item) : {};
    var warnings = Array.isArray(source.warnings) ? source.warnings : [];
    var errors = Array.isArray(source.errors) ? source.errors : [];
    var status = source.status === "PARTIAL" || source.status === "ERROR" ? source.status : "OK";
    var normalized = Object.assign({}, source, {
      id: String(source.id || stableId),
      status: status,
      source_method: String(source.source_method || "adapter").toLowerCase(),
      confidence: normalizeConfidence(source.confidence),
      warnings: warnings.map(String),
      errors: errors,
      provenance: {
        origin: locationContext.origin,
        path: locationContext.path,
        adapter: String(adapter.name || "unnamed-adapter"),
        adapter_version: String(adapter.version || "unversioned")
      }
    });
    delete normalized.http_status;
    return normalized;
  }

  function resultStatus(state) {
    if (state.guardrail_abort) return "ABORTED_BY_GUARDRAIL";
    if (state.fatal_error || state.counts.failed > 0 && state.items.length === 0) return "ERROR";
    if (state.counts.failed > 0 || state.counts.partial > 0 || state.run_errors.length > 0) return "PARTIAL";
    return "OK";
  }

  function checkpointSnapshot(state) {
    return publicClone({
      device: "browser-console-device",
      version: DEVICE_VERSION,
      started_at: state.started_at,
      updated_at: state.updated_at,
      config: state.config,
      discovered_ids: state.discovered_ids,
      completed_items: state.completed_items,
      failed_items: state.failed_items,
      partial_items: state.partial_items,
      duplicate_ids: state.duplicate_ids,
      counts: state.counts,
      stop_reason: state.stop_reason,
      run_warnings: state.run_warnings,
      run_errors: state.run_errors
    });
  }

  function writeCheckpoint(state) {
    if (!global) return;
    global[CHECKPOINT_KEY] = checkpointSnapshot(state);
  }

  function updateCounts(state, item) {
    if (item.status === "ERROR") state.counts.failed += 1;
    else if (item.status === "PARTIAL") state.counts.partial += 1;
    else state.counts.completed += 1;
  }

  async function mapBounded(records, concurrency, callback) {
    var results = new Array(records.length);
    var cursor = 0;
    async function worker() {
      while (true) {
        var index = cursor;
        cursor += 1;
        if (index >= records.length) return;
        results[index] = await callback(records[index], index);
      }
    }
    var workers = [];
    var count = Math.min(Math.max(1, concurrency), Math.max(1, records.length));
    for (var i = 0; i < count; i += 1) workers.push(worker());
    await Promise.all(workers);
    return results;
  }

  function csvCell(value) {
    var text = value === null || typeof value === "undefined" ? "" : String(value);
    return '"' + text.replace(/"/g, '""') + '"';
  }

  function toCSV(result) {
    if (!result) return "";
    var headers = ["id", "status", "source_method", "confidence", "warnings", "errors", "origin", "path"];
    var rows = [headers.map(csvCell).join(",")];
    result.items.forEach(function (item) {
      rows.push([
        item.id,
        item.status,
        item.source_method,
        item.confidence,
        (item.warnings || []).join(" | "),
        JSON.stringify(item.errors || []),
        item.provenance && item.provenance.origin,
        item.provenance && item.provenance.path
      ].map(csvCell).join(","));
    });
    return rows.join("\n") + "\n";
  }

  async function copyText(text) {
    if (global.navigator && global.navigator.clipboard && global.navigator.clipboard.writeText) {
      await global.navigator.clipboard.writeText(text);
      return { method: "clipboard", copied: true };
    }
    if (!global.document || !global.document.body) return { method: "unavailable", copied: false };
    var area = global.document.createElement("textarea");
    area.value = text;
    area.setAttribute("readonly", "true");
    area.style.position = "fixed";
    area.style.opacity = "0";
    global.document.body.appendChild(area);
    area.select();
    var copied = false;
    try { copied = Boolean(global.document.execCommand("copy")); } catch (error) { copied = false; }
    global.document.body.removeChild(area);
    return { method: "textarea-fallback", copied: copied };
  }

  function downloadText(filename, content, type) {
    if (!global.document || !global.URL || !global.Blob) return false;
    var blob = new Blob([content], { type: type || "text/plain;charset=utf-8" });
    var anchor = global.document.createElement("a");
    anchor.href = global.URL.createObjectURL(blob);
    anchor.download = filename;
    anchor.click();
    global.setTimeout(function () { global.URL.revokeObjectURL(anchor.href); }, 0);
    return true;
  }

  function assertAdapter(adapter) {
    if (!adapter || typeof adapter !== "object") throw new Error("An explicit adapter is required.");
    ["discover", "stableKey", "extract"].forEach(function (method) {
      if (typeof adapter[method] !== "function") throw new Error("Adapter is missing " + method + "().");
    });
    var forbidden = adapter.forbidden_capabilities || [];
    if (forbidden.length) {
      var error = new Error("Adapter declares a forbidden bypass capability.");
      error.domain = "INSTRUCTION";
      throw error;
    }
  }

  function create(options) {
    var baseOptions = options || {};
    var latest = null;

    async function run(overrides) {
      var runOptions = Object.assign({}, baseOptions, overrides || {});
      var adapter = runOptions.adapter;
      var config = safeConfig(runOptions);
      var locationContext = safeLocation();
      var started = now();
      var state = {
        started_at: started,
        updated_at: started,
        config: config,
        discovered_ids: [],
        completed_items: [],
        failed_items: [],
        partial_items: [],
        duplicate_ids: [],
        items: [],
        counts: { discovered: 0, unique: 0, duplicates: 0, completed: 0, partial: 0, failed: 0 },
        stop_reason: null,
        run_warnings: [],
        run_errors: [],
        challenge_signals: 0,
        guardrail_abort: false,
        fatal_error: false
      };

      try {
        assertAdapter(adapter);
        if (config.mode !== "read-only") {
          var modeError = new Error("This reference device is read-only by default and does not authorize mutation.");
          modeError.domain = "INSTRUCTION";
          throw modeError;
        }
      } catch (error) {
        state.fatal_error = true;
        state.run_errors.push(errorRecord(error, "preflight"));
        state.stop_reason = "preflight_failed";
        state.updated_at = now();
        writeCheckpoint(state);
        latest = buildResult(state, adapter || {}, locationContext);
        return latest;
      }

      var seen = new Set();
      var stagnantRounds = 0;

      async function sameOriginFetch(url, init) {
        if (!config.allowSameOriginSession || adapter.sameOriginAccess !== true) {
          var sessionError = new Error("Same-origin session access was not explicitly enabled by the run and adapter.");
          sessionError.domain = "GUARDRAIL";
          throw sessionError;
        }
        var target = new URL(url, global.location && global.location.href);
        if (target.origin !== locationContext.origin) {
          var originError = new Error("Cross-origin fetch rejected by the reference device.");
          originError.domain = "GUARDRAIL";
          throw originError;
        }
        var response = await global.fetch(target.href, Object.assign({}, init || {}, { credentials: "include" }));
        if (!response.ok) {
          var statusError = new Error("Same-origin request returned HTTP " + response.status + ".");
          statusError.http_status = response.status;
          statusError.domain = CHALLENGE_STATUSES[response.status] ? "UPSTREAM_SERVICE" : "DEPENDENCY";
          throw statusError;
        }
        return publicClone(await response.json());
      }

      async function processRecord(record, round) {
        await pace(config);
        var key = record.key;
        if (record.stableError) {
          var stableFailure = {
            id: key,
            status: "ERROR",
            source_method: "stable_key",
            confidence: "low",
            warnings: [],
            errors: [errorRecord(record.stableError, "stable-key", key)]
          };
          return normalizeItem(stableFailure, key, adapter, locationContext);
        }

        try {
          var extracted = await adapter.extract(record.candidate, {
            round: round,
            key: key,
            document: global.document,
            location: locationContext
          });
          var item = normalizeItem(extracted, key, adapter, locationContext);
          if (typeof adapter.enrich === "function") {
            try {
              var enriched = await adapter.enrich(item, {
                round: round,
                key: key,
                fetchSameOriginJson: sameOriginFetch,
                document: global.document,
                location: locationContext
              });
              if (isObject(enriched)) item = normalizeItem(Object.assign({}, item, enriched), key, adapter, locationContext);
            } catch (enrichmentError) {
              var optionalFailure = errorRecord(enrichmentError, "optional-enrichment", key);
              item.status = "PARTIAL";
              item.warnings = (item.warnings || []).concat("Optional enrichment did not complete.");
              item.errors = (item.errors || []).concat(optionalFailure);
              if (challengeStatus(optionalFailure)) state.challenge_signals += 1;
              if (state.challenge_signals >= config.challengeStopThreshold) {
                state.guardrail_abort = true;
                state.stop_reason = "upstream_challenge_or_rate_limit";
              }
            }
          }
          return item;
        } catch (error) {
          var failure = errorRecord(error, "item-extraction", key);
          if (challengeStatus(failure)) {
            state.challenge_signals += 1;
            if (state.challenge_signals >= config.challengeStopThreshold) {
              state.guardrail_abort = true;
              state.stop_reason = "upstream_challenge_or_rate_limit";
            }
          }
          return normalizeItem({
            id: key,
            status: "ERROR",
            source_method: "adapter",
            confidence: "low",
            warnings: [],
            errors: [failure]
          }, key, adapter, locationContext);
        }
      }

      for (var round = 0; round < config.maxRounds; round += 1) {
        if (state.guardrail_abort || state.items.length >= config.maxItems) break;
        var candidates;
        try {
          candidates = await adapter.discover({
            round: round,
            document: global.document,
            location: locationContext,
            state: checkpointSnapshot(state)
          });
          if (!Array.isArray(candidates)) throw new Error("Adapter discover() must return an array.");
        } catch (discoveryError) {
          state.run_errors.push(errorRecord(discoveryError, "discovery"));
          state.fatal_error = state.items.length === 0;
          state.stop_reason = "discovery_failed";
          break;
        }

        var records = [];
        var newKeys = 0;
        candidates.forEach(function (candidate, index) {
          if (state.counts.discovered >= config.maxItems) return;
          state.counts.discovered += 1;
          var key;
          var stableError = null;
          try {
            key = String(adapter.stableKey(candidate));
            if (!key || key === "undefined" || key === "null") throw new Error("Adapter returned an empty stable key.");
          } catch (error) {
            stableError = error;
            key = "unkeyed:" + round + ":" + index;
          }
          if (!stableError && seen.has(key)) {
            state.counts.duplicates += 1;
            state.duplicate_ids.push(key);
            return;
          }
          seen.add(key);
          state.discovered_ids.push(key);
          state.counts.unique += 1;
          newKeys += 1;
          records.push({ candidate: candidate, key: key, stableError: stableError });
        });

        var roundItems = await mapBounded(records, config.concurrency, function (record) {
          return processRecord(record, round);
        });
        roundItems.forEach(function (item) {
          if (state.items.length >= config.maxItems) return;
          state.items.push(item);
          updateCounts(state, item);
          if (item.status === "ERROR") state.failed_items.push(item.id);
          else if (item.status === "PARTIAL") state.partial_items.push(item.id);
          else state.completed_items.push(item.id);
          state.updated_at = now();
          writeCheckpoint(state);
        });

        if (state.guardrail_abort || state.items.length >= config.maxItems) break;
        if (newKeys === 0) stagnantRounds += 1;
        else stagnantRounds = 0;
        if (stagnantRounds >= config.maxStagnantRounds) {
          state.stop_reason = "stagnation_limit";
          break;
        }
        if (typeof adapter.loadMore !== "function") {
          state.stop_reason = "adapter_no_progressive_loader";
          break;
        }
        try {
          var loadResult = await adapter.loadMore({
            round: round,
            document: global.document,
            location: locationContext,
            state: checkpointSnapshot(state)
          });
          if (!loadResult || loadResult.changed !== true) stagnantRounds += 1;
          if (stagnantRounds >= config.maxStagnantRounds) {
            state.stop_reason = "stagnation_limit";
            break;
          }
        } catch (loadError) {
          var loadFailure = errorRecord(loadError, "progressive-load");
          state.run_errors.push(loadFailure);
          if (challengeStatus(loadFailure)) {
            state.challenge_signals += 1;
            if (state.challenge_signals >= config.challengeStopThreshold) {
              state.guardrail_abort = true;
              state.stop_reason = "upstream_challenge_or_rate_limit";
            }
          }
          if (!state.guardrail_abort) state.stop_reason = "progressive_load_failed";
          break;
        }
      }

      if (!state.stop_reason) {
        if (state.guardrail_abort) state.stop_reason = "upstream_challenge_or_rate_limit";
        else if (state.items.length >= config.maxItems) state.stop_reason = "max_items_reached";
        else state.stop_reason = "max_rounds_reached";
      }
      state.updated_at = now();
      writeCheckpoint(state);
      latest = buildResult(state, adapter, locationContext);
      return latest;
    }

    function buildResult(state, adapter, locationContext) {
      return publicClone({
        device: {
          id: "browser-console-device",
          name: "Browser Console Device",
          version: DEVICE_VERSION,
          class: "operational-device-reference",
          mode: state.config.mode,
          claim_ceiling: "Experimental bounded reference; no universal runtime or completeness claim."
        },
        adapter: {
          name: String(adapter.name || "unnamed-adapter"),
          version: String(adapter.version || "unversioned"),
          intended_origin: String(adapter.intended_origin || locationContext.origin),
          same_origin_access: Boolean(adapter.sameOriginAccess),
          freshness: String(adapter.freshness || "Adapter and surface assumptions require local review.")
        },
        origin_context: {
          origin: locationContext.origin,
          path: locationContext.path,
          sanitized: true
        },
        timestamps: { started_at: state.started_at, updated_at: state.updated_at },
        counts: state.counts,
        status: resultStatus(state),
        stop_reason: state.stop_reason,
        items: state.items,
        run_warnings: state.run_warnings,
        run_errors: state.run_errors,
        guardrails: [
          "read-only-by-default",
          "no-credential-extraction",
          "no-captcha-paywall-or-access-control-bypass",
          "same-origin-only-session-fetch",
          "partial-corpus-preserved"
        ],
        _moon_source_public_stamp: PUBLIC_STAMP
      });
    }

    function exportJSON(result) {
      return JSON.stringify(result || latest, null, 2) + "\n";
    }

    function exportCSV(result) {
      return toCSV(result || latest);
    }

    function readback(result) {
      var source = result || latest;
      if (!source) return { status: "ERROR", counts: null, stop_reason: "no_run" };
      return {
        status: source.status,
        counts: source.counts,
        stop_reason: source.stop_reason,
        checkpoint_key: CHECKPOINT_KEY
      };
    }

    return {
      run: run,
      exportJSON: exportJSON,
      exportCSV: exportCSV,
      copyJSON: function (result) { return copyText(exportJSON(result)); },
      copyCSV: function (result) { return copyText(exportCSV(result)); },
      downloadJSON: function (result, filename) {
        return downloadText(filename || "moon-source-browser-device.json", exportJSON(result), "application/json;charset=utf-8");
      },
      downloadCSV: function (result, filename) {
        return downloadText(filename || "moon-source-browser-device.csv", exportCSV(result), "text/csv;charset=utf-8");
      },
      readback: readback,
      latest: function () { return latest; },
      checkpoint: function () { return publicClone(global[CHECKPOINT_KEY] || null); },
      clearCheckpoint: function () { delete global[CHECKPOINT_KEY]; }
    };
  }

  var defaultInstance = create();
  global.MoonSourceBrowserDevice = {
    version: DEVICE_VERSION,
    checkpointKey: CHECKPOINT_KEY,
    create: create,
    run: defaultInstance.run,
    exportJSON: defaultInstance.exportJSON,
    exportCSV: defaultInstance.exportCSV,
    copyJSON: defaultInstance.copyJSON,
    copyCSV: defaultInstance.copyCSV,
    downloadJSON: defaultInstance.downloadJSON,
    downloadCSV: defaultInstance.downloadCSV,
    readback: defaultInstance.readback,
    latest: defaultInstance.latest,
    checkpoint: defaultInstance.checkpoint,
    clearCheckpoint: defaultInstance.clearCheckpoint
  };
})(window);

// MOON-SOURCE-PUBLIC-STAMP
// 🌙 Moon Source · Lua Helena Moon Martins Cardoso (Moon) + Áurion (AI-assisted) · Use & attribution: https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md · Full source: https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip
