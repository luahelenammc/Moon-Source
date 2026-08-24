/*
 * Moon Source — synthetic localhost adapter
 *
 * This adapter is intentionally separate from collector.template.js. It binds
 * the generic device to the demo DOM and a same-origin JSON file only.
 */
(function (global) {
  "use strict";

  var state = { progressive_round_loaded: false };

  function cardMarkup() {
    return [
      '<article class="demo-item" data-item-id="item-003" data-malformed="true">',
      '  <h2>Malformed synthetic item</h2>',
      '  <p data-visible-summary>Intentionally malformed to test fault isolation.</p>',
      '</article>',
      '<article class="demo-item" data-item-id="item-004">',
      '  <h2>Item Four</h2>',
      '  <p data-visible-summary>Visible summary; more metadata lives in the same-origin fixture.</p>',
      '</article>'
    ].join("");
  }

  var adapter = {
    name: "synthetic-localhost-demo",
    version: "0.1.0",
    intended_origin: "http://localhost:8765",
    discovery_strategy: "semantic DOM cards under .demo-item",
    schema_mapping: "demo card + items.json metadata → browser-device item",
    stop_assumptions: "Two consecutive rounds without a new stable key stop discovery.",
    freshness: "Synthetic fixture only; DOM and JSON shape are intentionally local to this example.",
    sameOriginAccess: true,
    forbidden_capabilities: [],

    discover: function (context) {
      return Array.from(context.document.querySelectorAll(".demo-item"));
    },

    stableKey: function (node) {
      var id = node && node.getAttribute && node.getAttribute("data-item-id");
      if (!id) {
        var missing = new Error("Synthetic card has no stable data-item-id.");
        missing.domain = "TARGET";
        throw missing;
      }
      return id;
    },

    extract: function (node) {
      if (node.getAttribute("data-malformed") === "true") {
        var malformed = new Error("Synthetic item is malformed by design.");
        malformed.domain = "TARGET";
        throw malformed;
      }
      var titleNode = node.querySelector("h2");
      var summaryNode = node.querySelector("[data-visible-summary]");
      return {
        id: node.getAttribute("data-item-id"),
        title: titleNode ? titleNode.textContent.trim() : "",
        visible_summary: summaryNode ? summaryNode.textContent.trim() : "",
        source_method: "semantic_dom",
        confidence: "medium",
        warnings: summaryNode ? [] : ["Visible summary is absent from the demo card."],
        errors: []
      };
    },

    enrich: async function (item, context) {
      var payload = await context.fetchSameOriginJson("items.json");
      var records = Array.isArray(payload) ? payload : payload.items;
      var record = (records || []).find(function (candidate) { return candidate.id === item.id; });
      if (!record) {
        return {
          status: "PARTIAL",
          source_method: "semantic_dom",
          confidence: "medium",
          warnings: (item.warnings || []).concat("No same-origin enrichment record exists for this ID.")
        };
      }
      var missingDescription = !record.description;
      return {
        category: record.category || null,
        tags: Array.isArray(record.tags) ? record.tags : [],
        description: record.description || null,
        data: { metadata_source: "same-origin-json", metadata_version: record.metadata_version || "fixture-1" },
        status: missingDescription ? "PARTIAL" : item.status,
        source_method: "semantic_dom+same_origin_json",
        confidence: "high",
        warnings: missingDescription
          ? (item.warnings || []).concat("Enrichment record is present but description is absent.")
          : item.warnings
      };
    },

    loadMore: function (context) {
      if (context.round !== 0 || state.progressive_round_loaded) {
        return { changed: false, reason: "Synthetic demo has no further pages." };
      }
      var container = context.document.querySelector("#demo-list");
      if (!container) {
        var missingContainer = new Error("Synthetic demo list is missing.");
        missingContainer.domain = "TARGET";
        throw missingContainer;
      }
      container.insertAdjacentHTML("beforeend", cardMarkup());
      state.progressive_round_loaded = true;
      return { changed: true, reason: "Synthetic progressive round appended two cards." };
    }
  };

  global.MoonSourceDemoAdapter = adapter;
})(window);

// MOON-SOURCE-PUBLIC-STAMP
// 🌙 Moon Source · Lua Helena Moon Martins Cardoso (Moon) + Áurion (AI-assisted) · Use & attribution: https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md · Full source: https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip
