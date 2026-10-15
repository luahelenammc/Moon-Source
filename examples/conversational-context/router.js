"use strict";

/**
 * Synthetic conversational-context composition.
 * A deterministic filter; NOT a chatbot, law engine, consent provider, or
 * security boundary. Caller must supply trusted operator-side configuration.
 * Do not feed real people, identifiers, health data, or private conversations.
 */
const KINDS = Object.freeze(["program_state", "dialogue_state", "preference"]);
const ACTIONS = Object.freeze(["resume", "review", "human_handoff"]);
const safeDate = (value) => typeof value === "string" && /^\d{4}-\d{2}-\d{2}$/.test(value)
  && !Number.isNaN(Date.parse(value + "T00:00:00Z"))
  && new Date(value + "T00:00:00Z").toISOString().slice(0,10) === value;
const dayNumber = (value) => Date.parse(value + "T00:00:00Z") / 86400000;
const isPlainObject = (value) => value !== null && typeof value === "object"
  && !Array.isArray(value) && Object.getPrototypeOf(value) === Object.prototype;
const contains = (list, value) => Array.isArray(list) && list.includes(value);
const safeText = (value) => (typeof value === "string" && value.length <= 160)
  || (typeof value === "number" && Number.isFinite(value))
  || typeof value === "boolean";
const denied = (reason) => ({
  status: "blocked", reason, context: [], next: "operator_review",
  trace: [{step: "gate", result: reason}]
});
const escalate = (reason, trace) => ({
  status: "escalate", reason, context: [], next: "human_review", trace
});

/**
 * @param {object} input Strictly synthetic fixture with input.request,
 * input.consent, input.policy, input.jurisdictionProfile, input.records, input.today.
 * @returns {object} Approved minimum structured context, never a response to send.
 */
function buildContext(input) {
  if (!isPlainObject(input) || !safeDate(input.today))
    return denied("invalid_input");
  const {request, consent, policy, jurisdictionProfile: legal, records, today} = input;
  if (!isPlainObject(request) || !isPlainObject(consent) || !isPlainObject(policy)
      || !isPlainObject(legal) || !Array.isArray(records) || records.length > 20)
    return denied("invalid_contract");
  const {purpose, region, action, subjectKey} = request;
  if (!contains(ACTIONS, action) || typeof region !== "string"
      || !region || typeof subjectKey !== "string" || !subjectKey
      || typeof purpose !== "string" || !purpose)
    return denied("unsupported_request");
  if (action === "human_handoff")
    return escalate("human_requested", [{step: "handoff", result: "explicit"}]);
  if (!contains(policy.allowedPurposes, purpose) || !contains(policy.allowedActions, action))
    return denied("not_authorized_by_policy");
  // Optional actor scope narrows the existing approval envelope; it cannot
  // expand purposes or bypass subject/region isolation.
  if (Array.isArray(policy.allowedActorScopes) &&
      (!contains(policy.allowedActorScopes, request.actorScope) ||
       (Array.isArray(consent.allowedActorScopes) &&
        !contains(consent.allowedActorScopes, request.actorScope))))
    return denied("actor_scope_not_authorized");
  if ((consent.subjectKey !== undefined && consent.subjectKey !== subjectKey) ||
      (consent.region !== undefined && consent.region !== region))
    return denied("consent_scope_mismatch");
  if (consent.revokedAt !== undefined &&
      (!safeDate(consent.revokedAt) || consent.revokedAt <= today))
    return denied("consent_missing_or_expired");
  if (consent.validFrom !== undefined &&
      (!safeDate(consent.validFrom) || consent.validFrom > today))
    return denied("consent_missing_or_expired");
  // In production, action classification cannot be trusted to a user's flag alone.
  // An application must perform content and clinical-scope safety checks upstream.
  if (consent.status !== "granted" || !contains(consent.purposes, purpose)
      || !safeDate(consent.validUntil) || consent.validUntil < today)
    return denied("consent_missing_or_expired");
  // A checked profile is an operator-provided requirement record, not legal advice
  // or proof of compliance with any country/state/sector laws.
  if (legal.reviewState !== "approved" || !contains(legal.regions, region)
      || !contains(legal.purposes, purpose) || !safeDate(legal.validUntil)
      || legal.validUntil < today || typeof legal.reviewReference !== "string"
      || !legal.reviewReference)
    return denied("jurisdiction_review_required");

  const trace = [{step: "gate", result: "eligible"}];
  const context = [];
  const skipped = {};
  const countSkip = (reason) => { skipped[reason] = (skipped[reason] || 0) + 1; };
  for (const kind of KINDS) {
    if (!contains(policy.allowedKinds, kind) || !contains(legal.allowedKinds, kind))
      continue;
    const candidates = records.filter((record) => record && record.kind === kind && record.subjectKey === subjectKey && record.region === region);
    const eligible = [];
    const maxAge = policy.maxAgeDaysByKind?.[kind] ?? policy.maxAgeDays;
    for (const item of candidates) {
      if (!isPlainObject(item) || item.subjectKey !== subjectKey || item.region !== region
          || !isPlainObject(item.fields) || !isPlainObject(item.provenance)
          || item.provenance.authority !== "operator-approved"
          || !contains(["api", "query", "spreadsheet"], item.provenance.substrate)
          || !safeDate(item.updatedAt) || item.updatedAt > today
          || !Number.isInteger(maxAge) || maxAge < 0
          || dayNumber(today) - dayNumber(item.updatedAt) > maxAge
          || (item.validUntil !== undefined &&
              (!safeDate(item.validUntil) || item.validUntil < today))
          || (item.effectiveFrom !== undefined &&
              (!safeDate(item.effectiveFrom) || item.effectiveFrom > today))
          || typeof item.provenance.revision !== "string"
          || !/^[a-zA-Z0-9._:-]{1,80}$/.test(item.provenance.revision)
          || !contains(item.allowedPurposes, purpose)) {
        countSkip("ineligible_record"); continue;
      }
      const a = Array.isArray(policy.fieldsByKind?.[kind]) ? policy.fieldsByKind[kind] : [];
      const b = Array.isArray(legal.fieldsByKind?.[kind]) ? legal.fieldsByKind[kind] : [];
      const purposeFields = item.fieldsByPurpose === undefined ? a :
        (Array.isArray(item.fieldsByPurpose?.[purpose]) ? item.fieldsByPurpose[purpose] : []);
      const requestedFields = request.fieldSelection === undefined ? a :
        (Array.isArray(request.fieldSelection?.[kind]) ? request.fieldSelection[kind] : []);
      const allowed = a.filter((key) => b.includes(key) &&
        purposeFields.includes(key) && requestedFields.includes(key) &&
        Object.hasOwn(item.fields, key));
      const fields = {};
      for (const key of allowed) {
        if (/^[a-z][a-z0-9_]{0,39}$/.test(key) && safeText(item.fields[key])) {
          fields[key] = item.fields[key];
        } else countSkip("unsafe_or_unallowlisted_value");
      }
      if (!Object.keys(fields).length) { countSkip("no_permitted_fields"); continue; }
      eligible.push({kind, fields, updatedAt:item.updatedAt,
        provenance:{substrate:item.provenance.substrate, revision:item.provenance.revision}});
    }
    if (!eligible.length) {
      trace.push({step: kind, result: "no_eligible_record"});
      continue;
    }
    eligible.sort((a,b) => b.updatedAt.localeCompare(a.updatedAt) ||
      a.provenance.revision.localeCompare(b.provenance.revision));
    let latest = eligible.filter((x) => x.updatedAt === eligible[0].updatedAt);
    // Only an explicit operator-configured substrate precedence can resolve a
    // same-date disagreement. Missing or tied precedence retains escalation.
    const priority = policy.substratePriorityByKind?.[kind];
    if (Array.isArray(priority) && latest.length > 1) {
      const ranked = latest.map((item) => ({
        item, rank:priority.indexOf(item.provenance.substrate)
      }));
      if (ranked.every((x) => x.rank >= 0)) {
        const best = Math.min(...ranked.map((x) => x.rank));
        latest = ranked.filter((x) => x.rank === best).map((x) => x.item);
      }
    }
    if (latest.length > 1 && latest.some((x) =>
      JSON.stringify(x.fields) !== JSON.stringify(latest[0].fields)))
      return escalate("conflicting_current_state", [
        ...trace, {step:kind, result:"conflict", count:latest.length}
      ]);
    context.push(latest[0]);
    trace.push({step:kind, result:"selected", candidates:eligible.length});
  }
  if (!context.length)
    return escalate("no_authorized_current_context", trace);
  // No side effects, no outbound messages, no participant identifiers, no raw
  // conversation transcript, and no runtime/model access are supplied here.
  trace.push({step:"complete", result:"bounded_context", fields:
    context.reduce((n,x) => n+Object.keys(x.fields).length,0), skipped});
  return {status:"ready", reason:"context_available", context,
    next:"application_review", trace};
}
module.exports = {buildContext};

// MOON-SOURCE-PUBLIC-STAMP
// 🌙 Moon Source · Lua Helena Moon Martins Cardoso (Moon) + Áurion (AI-assisted) · Use & attribution: https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md · Full source: https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip · Questions, suggestions, or proposals? Feel free to contact me at LuaHelenaMMC@gmail.com.
