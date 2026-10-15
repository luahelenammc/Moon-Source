"use strict";

/**
 * Journey re-entry and human-handoff decision over the existing approved
 * buildContext envelope. Synthetic, deterministic, read-only; not an action
 * dispatcher, consent authority, legal assessment or security boundary.
 */
const {buildContext} = require("./router.js");

const validDate = (date) => typeof date === "string" &&
  /^\d{4}-\d{2}-\d{2}$/.test(date) &&
  !Number.isNaN(Date.parse(date + "T00:00:00Z")) &&
  new Date(date + "T00:00:00Z").toISOString().slice(0,10) === date;
const daysBetween = (before, after) =>
  (Date.parse(after + "T00:00:00Z") - Date.parse(before + "T00:00:00Z")) / 86400000;

/**
 * Only a configured role, never an inferred person or destination, is shown.
 * No packet is sent, delivered, accepted or resolved by this function.
 */
function handoff(reason, state, policy) {
  const role = typeof policy?.handoffOwner === "string" &&
    /^[a-z][a-z0-9_-]{0,63}$/.test(policy.handoffOwner)
    ? policy.handoffOwner : null;
  return {
    state, reason, responsibleRole:role,
    delivery:"not_attempted",
    reviewPacket:{reason, contextFields:[], requiresAuthorizedRetrieval:true}
  };
}

/**
 * @param {object} input Trusted application-supplied synthetic input accepted
 * by buildContext. Optional dialogue fields: last_known_module, last_seen_on.
 * @returns {object} Advisory decision; never sends a message or performs work.
 */
function evaluateContinuity(input) {
  // The existing router remains the sole permission and field gate.
  const selection = buildContext(input);
  const trace = selection.trace.slice();
  if (selection.reason === "human_requested") {
    trace.push({step:"handoff",result:"requested_not_delivered"});
    return {status:"escalate",reason:"human_requested",context:[],
      reentry:null,handoff:handoff("human_requested","handoff_requested",input?.policy),
      next:"await_authorized_human_process",trace};
  }
  if (selection.status === "blocked") {
    trace.push({step:"continuity",result:"stopped"});
    return {...selection,reentry:null,handoff:null,next:"stop",trace};
  }
  if (selection.status === "escalate") {
    trace.push({step:"handoff",result:"recommended_not_delivered"});
    return {...selection,reentry:null,context:[],
      handoff:handoff(selection.reason,"handoff_recommended",input?.policy),
      next:"human_review",trace};
  }
  if (input.request.action !== "resume") {
    trace.push({step:"continuity",result:"review_only"});
    return {...selection,reentry:null,handoff:null,trace};
  }
  const operational = selection.context.find((x) => x.kind === "program_state");
  const dialogue = selection.context.find((x) => x.kind === "dialogue_state");
  const preference = selection.context.find((x) => x.kind === "preference");

  if (!operational) {
    trace.push({step:"handoff",result:"operational_state_unavailable"});
    return {status:"escalate",reason:"current_operational_state_unavailable",
      context:[],reentry:null,
      handoff:handoff("current_operational_state_unavailable",
        "handoff_recommended",input.policy),
      next:"human_review",trace};
  }

  const previousKnown = dialogue && Object.hasOwn(dialogue.fields,"last_known_module");
  const currentKnown = Object.hasOwn(operational.fields,"module");
  const previousSeen = dialogue?.fields.last_seen_on;
  const hasSeen = validDate(previousSeen) && previousSeen <= input.today;
  const changed = previousKnown && currentKnown
    ? !Object.is(dialogue.fields.last_known_module,operational.fields.module)
    : null;
  const updatedDuringGap = hasSeen && operational.updatedAt > previousSeen;
  const gaps = [];
  if (!previousKnown) gaps.push("prior_module_not_available");
  if (!hasSeen) gaps.push("last_interaction_date_not_available");
  if (!preference) gaps.push("current_preference_not_available");
  const nextActivity = Object.hasOwn(operational.fields,"next_activity");
  if (!nextActivity) gaps.push("next_activity_not_available");

  // Values are not copied into trace, handoff, or extra context. They remain
  // solely in the selector's permitted fields; every other output is metadata.
  const reentry = {
    previous:{source:dialogue ? "dialogue_state" : null,
      revision:dialogue?.provenance.revision ?? null,
      knownModule:!!previousKnown},
    current:{source:"program_state",revision:operational.provenance.revision,
      updatedAt:operational.updatedAt},
    continuity:changed === null ? "unverified" :
      changed ? "operational_state_changed" : "module_unchanged",
    operationalUpdatedDuringGap:!!updatedDuringGap,
    daysSinceLastInteraction:hasSeen ? daysBetween(previousSeen,input.today) : null,
    applicablePreference:preference ? {source:"preference",
      revision:preference.provenance.revision} : null,
    gaps,
    nextStep:nextActivity ?
      {kind:"candidate_for_application_review",source:"program_state",
        field:"next_activity"} :
      {kind:"confirm_with_application_owner"}
  };
  trace.push({step:"reentry",result:"evaluated",continuity:reentry.continuity,
    gapCount:gaps.length});
  return {...selection,reason:"continuity_assessed",reentry,handoff:null,
    trace};
}

module.exports = {evaluateContinuity};

// MOON-SOURCE-PUBLIC-STAMP
// 🌙 Moon Source · Lua Helena Moon Martins Cardoso (Moon) + Áurion (AI-assisted) · Use & attribution: https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md · Full source: https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip · Questions, suggestions, or proposals? Feel free to contact me at LuaHelenaMMC@gmail.com.
