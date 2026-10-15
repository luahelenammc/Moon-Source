"use strict";
const test = require("node:test");
const assert = require("node:assert/strict");
const {buildContext} = require("./router.js");

const fixture = () => ({
  today:"2026-10-14",
  request:{purpose:"continuity",region:"FICTIONAL-REGION-A",subjectKey:"FICTIONAL-SUBJECT-A",action:"resume"},
  consent:{status:"granted",purposes:["continuity"],validUntil:"2026-12-31"},
  policy:{allowedPurposes:["continuity"],allowedActions:["resume", "review"],
    allowedKinds:["program_state","dialogue_state"],maxAgeDays:30,
    fieldsByKind:{program_state:["module","next_activity"],dialogue_state:["last_topic"]}},
  jurisdictionProfile:{reviewState:"approved",reviewReference:"SYNTHETIC-REVIEW-01",
    validUntil:"2026-12-31",regions:["FICTIONAL-REGION-A"],
    purposes:["continuity"],allowedKinds:["program_state","dialogue_state"],
    fieldsByKind:{program_state:["module"],dialogue_state:["last_topic"]}},
  records:[
    {kind:"program_state",subjectKey:"FICTIONAL-SUBJECT-A",region:"FICTIONAL-REGION-A",updatedAt:"2026-10-13",allowedPurposes:["continuity"],
      provenance:{authority:"operator-approved",substrate:"api",revision:"synthetic-r1"},
      fields:{module:3,next_activity:"Exercise 4",medical_note:"NEVER EXPOSE"}},
    {kind:"dialogue_state",subjectKey:"FICTIONAL-SUBJECT-A",region:"FICTIONAL-REGION-A",updatedAt:"2026-10-13",allowedPurposes:["continuity"],
      provenance:{authority:"operator-approved",substrate:"query",revision:"synthetic-r3"},
      fields:{last_topic:"Returning after a gap",raw_transcript:"NEVER EXPOSE"}}
  ]
});
const run=(edit)=>{const f=fixture();edit?.(f);return buildContext(f);};

test("minimum permitted conversational context is produced without raw notes",()=>{
 const result=run();
 assert.equal(result.status,"ready");
 assert.equal(result.context.length,2);
 assert.deepEqual(result.context.map(x=>x.fields),[{module:3},{last_topic:"Returning after a gap"}]);
 assert.doesNotMatch(JSON.stringify(result),/medical_note|raw_transcript|NEVER EXPOSE/);
 assert.deepEqual(result.context.map(x=>x.provenance.substrate),["api","query"]);
});
test("withdrawn or missing consent blocks output",()=>{
 assert.equal(run(f=>f.consent.status="withdrawn").reason,"consent_missing_or_expired");
 assert.equal(run(f=>f.consent.purposes=[]).status,"blocked");
});
test("expired consent blocks output",()=>{
 assert.equal(run(f=>f.consent.validUntil="2026-10-12").status,"blocked");
});
test("unreviewed or expired jurisdiction profile blocks output",()=>{
 assert.equal(run(f=>f.jurisdictionProfile.reviewState="pending").reason,"jurisdiction_review_required");
 assert.equal(run(f=>f.jurisdictionProfile.validUntil="2026-10-01").status,"blocked");
});
test("unknown region cannot inherit another region's approval",()=>{
 assert.equal(run(f=>f.request.region="FICTIONAL-REGION-B").reason,"jurisdiction_review_required");
});
test("purpose and action must both be allowed",()=>{
 assert.equal(run(f=>f.request.purpose="marketing").reason,"not_authorized_by_policy");
 assert.equal(run(f=>f.request.action="medical_advice").reason,"unsupported_request");
});
test("explicit human handoff does not expose participant context",()=>{
 const r=run(f=>f.request.action="human_handoff");
 assert.equal(r.status,"escalate");
 assert.deepEqual(r.context,[]);
});
test("stale or future-dated records never silently govern",()=>{
 assert.equal(run(f=>f.records.forEach(x=>x.updatedAt="2025-01-01")).reason,
   "no_authorized_current_context");
 assert.equal(run(f=>f.records.forEach(x=>x.updatedAt="2027-01-01")).status,"escalate");
});
test("unapproved records are excluded",()=>{
 const r=run(f=>f.records[0].provenance.authority="unknown");
 assert.equal(r.status,"ready");
 assert.equal(r.context.length,1);
 assert.equal(r.context[0].kind,"dialogue_state");
});
test("spreadsheet-shaped sources are allowed under same authority rules",()=>{
 const r=run(f=>f.records[1].provenance.substrate="spreadsheet");
 assert.equal(r.status,"ready");
 assert.equal(r.context[1].provenance.substrate,"spreadsheet");
});
test("current conflicting records trigger human review",()=>{
 const r=run(f=>f.records.push({...f.records[0],
   fields:{module:6},provenance:{authority:"operator-approved",substrate:"api",revision:"synthetic-r2"}}));
 assert.equal(r.status,"escalate");
 assert.equal(r.reason,"conflicting_current_state");
 assert.deepEqual(r.context,[]);
});
test("higher freshness wins and provenance stays visible",()=>{
 const r=run(f=>f.records.push({...f.records[0],updatedAt:"2026-10-14",
   fields:{module:4},provenance:{authority:"operator-approved",substrate:"query",revision:"synthetic-r4"}}));
 assert.equal(r.status,"ready");
 assert.equal(r.context[0].fields.module,4);
 assert.equal(r.context[0].provenance.revision,"synthetic-r4");
});
test("nested or very long text fails safe",()=>{
 const r=run(f=>f.records[1].fields.last_topic="x".repeat(300));
 assert.equal(r.status,"ready");
 assert.equal(r.context.length,1);
});
test("malformed record set blocks, rather than overflowing the trace",()=>{
 const r=run(f=>f.records=new Array(21).fill(f.records[0]));
 assert.equal(r.status,"blocked");
 assert.equal(r.reason,"invalid_contract");
});

test("records from another subject never enter the chosen conversational context",()=>{
 const r=run(f=>f.records.push({...f.records[0],subjectKey:"FICTIONAL-SUBJECT-B",
   updatedAt:"2026-10-14",fields:{module:99}}));
 assert.equal(r.status,"ready");
 assert.equal(r.context[0].fields.module,3);
 assert.doesNotMatch(JSON.stringify(r),/FICTIONAL-SUBJECT-B|99/);
});
test("records from another region are excluded even with a valid request profile",()=>{
 const r=run(f=>f.records.push({...f.records[0],region:"FICTIONAL-REGION-B",
   updatedAt:"2026-10-14",fields:{module:99}}));
 assert.equal(r.status,"ready");
 assert.equal(r.context[0].fields.module,3);
});
test("no subject reference blocks context assembly",()=>{
 const r=run(f=>delete f.request.subjectKey);
 assert.equal(r.status,"blocked");
 assert.equal(r.reason,"unsupported_request");
});


const {evaluateContinuity} = require("./continuity.js");

const journey = () => {
  const input = fixture();
  input.request.actorScope = "continuity_operator";
  input.consent.subjectKey = input.request.subjectKey;
  input.consent.region = input.request.region;
  input.policy.allowedActorScopes = ["continuity_operator"];
  input.policy.handoffOwner = "program_reviewer";
  input.policy.allowedKinds.push("preference");
  input.policy.fieldsByKind.program_state.push("next_activity");
  input.policy.fieldsByKind.dialogue_state.push("last_known_module", "last_seen_on");
  input.policy.fieldsByKind.preference = ["interaction_style"];
  input.jurisdictionProfile.allowedKinds.push("preference");
  input.jurisdictionProfile.fieldsByKind.program_state.push("next_activity");
  input.jurisdictionProfile.fieldsByKind.dialogue_state.push("last_known_module", "last_seen_on");
  input.jurisdictionProfile.fieldsByKind.preference = ["interaction_style"];
  input.records[1].fields = {
    last_topic:"Returning after a gap", last_known_module:2,
    last_seen_on:"2026-09-25", raw_transcript:"NEVER EXPOSE"
  };
  input.records.push({
    kind:"preference",subjectKey:input.request.subjectKey,region:input.request.region,
    updatedAt:"2026-10-01", allowedPurposes:["continuity"],
    provenance:{authority:"operator-approved",substrate:"query",revision:"pref-r1"},
    fields:{interaction_style:"concise", private_note:"NEVER EXPOSE"}
  });
  return input;
};
const runJourney = (edit) => {const input=journey(); edit?.(input);return evaluateContinuity(input);};

test("re-entry composes prior/current/preference with authorized context only",()=>{
  const output=runJourney();
  assert.equal(output.status,"ready");
  assert.equal(output.reentry.continuity,"operational_state_changed");
  assert.equal(output.reentry.operationalUpdatedDuringGap,true);
  assert.equal(output.reentry.daysSinceLastInteraction,19);
  assert.equal(output.reentry.nextStep.kind,"candidate_for_application_review");
  assert.equal(output.reentry.applicablePreference.revision,"pref-r1");
  assert.equal(output.handoff,null);
  assert.doesNotMatch(JSON.stringify(output),/NEVER EXPOSE|raw_transcript|private_note/);
});
test("valid unchanged operational state can resume after a gap",()=>{
  const output=runJourney(f=>f.records[1].fields.last_known_module=3);
  assert.equal(output.status,"ready");
  assert.equal(output.reentry.continuity,"module_unchanged");
});
test("expired operational state never governs re-entry",()=>{
  const output=runJourney(f=>f.records[0].validUntil="2026-10-01");
  assert.equal(output.status,"escalate");
  assert.equal(output.reason,"current_operational_state_unavailable");
  assert.equal(output.handoff.state,"handoff_recommended");
  assert.deepEqual(output.context,[]);
});
test("operational updates during absence are observable, not motives",()=>{
  const output=runJourney();
  assert.equal(output.reentry.operationalUpdatedDuringGap,true);
  assert.doesNotMatch(JSON.stringify(output),/abandon|illness|disengaged|unmotivated/);
});
test("equally current conflicting operational states require human review",()=>{
  const output=runJourney(f=>f.records.push({...f.records[0],
    fields:{module:7,next_activity:"Exercise 8"},
    provenance:{authority:"operator-approved",substrate:"api",revision:"other-r2"}}));
  assert.equal(output.reason,"conflicting_current_state");
  assert.equal(output.handoff.state,"handoff_recommended");
  assert.equal(output.handoff.responsibleRole,"program_reviewer");
  assert.deepEqual(output.context,[]);
});
test("missing authorized current operational information recommends review",()=>{
  const output=runJourney(f=>f.records=f.records.filter(x=>x.kind!=="program_state"));
  assert.equal(output.reason,"current_operational_state_unavailable");
  assert.equal(output.handoff.delivery,"not_attempted");
});
test("revoked consent prevents re-entry even if status still says granted",()=>{
  const output=runJourney(f=>f.consent.revokedAt="2026-10-14");
  assert.equal(output.status,"blocked");
  assert.equal(output.handoff,null);
  assert.deepEqual(output.context,[]);
});
test("unapproved marketing purpose cannot reuse continuity permission",()=>{
  const output=runJourney(f=>f.request.purpose="marketing");
  assert.equal(output.status,"blocked");
  assert.equal(output.reason,"not_authorized_by_policy");
});
test("cross-subject and cross-region records cannot contaminate re-entry",()=>{
  const output=runJourney(f=>{
    f.records.push({...f.records[0],subjectKey:"FICTIONAL-SUBJECT-B",
      updatedAt:"2026-10-14",fields:{module:88}});
    f.records.push({...f.records[0],region:"FICTIONAL-REGION-B",
      updatedAt:"2026-10-14",fields:{module:99}});
  });
  assert.equal(output.status,"ready");
  assert.equal(output.context.find(x=>x.kind==="program_state").fields.module,3);
  assert.doesNotMatch(JSON.stringify(output),/FICTIONAL-SUBJECT-B|FICTIONAL-REGION-B|88|99/);
});
test("explicit human request is requested, never delivered",()=>{
  const output=runJourney(f=>f.request.action="human_handoff");
  assert.equal(output.status,"escalate");
  assert.equal(output.handoff.state,"handoff_requested");
  assert.equal(output.handoff.delivery,"not_attempted");
  assert.deepEqual(output.handoff.reviewPacket.contextFields,[]);
});
test("unauthorized external action stops without fictional notification",()=>{
  const output=runJourney(f=>f.request.action="send_notification");
  assert.equal(output.status,"blocked");
  assert.equal(output.handoff,null);
  assert.equal(output.next,"stop");
});
test("per-purpose and per-request field gates only narrow access",()=>{
  const output=runJourney(f=>{
    f.records[0].fieldsByPurpose={continuity:["module"]};
    f.request.fieldSelection={program_state:["module"],dialogue_state:["last_seen_on"],
      preference:["interaction_style"]};
  });
  assert.equal(output.status,"ready");
  assert.deepEqual(output.context[0].fields,{module:3});
  assert.equal(output.reentry.nextStep.kind,"confirm_with_application_owner");
  assert.doesNotMatch(JSON.stringify(output),/Exercise 4|Returning after a gap/);
});
test("field values and subject keys cannot leak into trace or review packet",()=>{
  const output=runJourney(f=>f.records[0].fields.next_activity="NEVER EXPOSE");
  assert.equal(output.status,"ready");
  assert.doesNotMatch(JSON.stringify(output.trace),/NEVER EXPOSE|FICTIONAL-SUBJECT-A/);
  assert.equal(output.handoff,null);
});
test("repeating same decision never creates fictional state or side effects",()=>{
  const input=journey();
  const original=JSON.stringify(input);
  assert.deepEqual(evaluateContinuity(input),evaluateContinuity(input));
  assert.equal(JSON.stringify(input),original);
});
test("actor scope and consent subject binding cannot be bypassed",()=>{
  assert.equal(runJourney(f=>f.request.actorScope="marketing_operator").reason,
    "actor_scope_not_authorized");
  assert.equal(runJourney(f=>f.consent.subjectKey="FICTIONAL-SUBJECT-B").reason,
    "consent_scope_mismatch");
});
test("effective and age limits exclude expired preferences",()=>{
  const output=runJourney(f=>{
    f.policy.maxAgeDaysByKind={preference:5};
    f.records[0].effectiveFrom="2026-10-01";
  });
  assert.equal(output.status,"ready");
  assert.equal(output.reentry.applicablePreference,null);
  assert.ok(output.reentry.gaps.includes("current_preference_not_available"));
});
test("same-day state precedence requires explicit operator policy",()=>{
  const output=runJourney(f=>{
    f.policy.substratePriorityByKind={program_state:["api","query","spreadsheet"]};
    f.records.push({...f.records[0],fields:{module:9,next_activity:"Other"},
      provenance:{authority:"operator-approved",substrate:"spreadsheet",revision:"low-r1"}});
  });
  assert.equal(output.status,"ready");
  assert.equal(output.context[0].fields.module,3);
});
test("unknown prior state is a bounded gap, not invented history",()=>{
  const output=runJourney(f=>delete f.records[1].fields.last_known_module);
  assert.equal(output.status,"ready");
  assert.equal(output.reentry.continuity,"unverified");
  assert.ok(output.reentry.gaps.includes("prior_module_not_available"));
});
test("no viable records recommends handoff with zero field payload",()=>{
  const output=runJourney(f=>f.records=[]);
  assert.equal(output.reason,"no_authorized_current_context");
  assert.deepEqual(output.context,[]);
  assert.deepEqual(output.handoff.reviewPacket.contextFields,[]);
});

test("out-of-scope records do not affect even trace counts",()=>{
  const baseline=runJourney();
  const mixed=runJourney(f=>{
    f.records.push({...f.records[0],subjectKey:"FICTIONAL-SUBJECT-B"});
    f.records.push({...f.records[1],region:"FICTIONAL-REGION-B"});
  });
  assert.deepEqual(mixed.trace,baseline.trace);
});
test("calendar-impossible dates are rejected rather than normalized",()=>{
  assert.equal(runJourney(f=>f.today="2026-02-31").status,"blocked");
  assert.equal(runJourney(f=>f.records[0].validUntil="2026-02-31").status,"escalate");
});

// End-to-end synthetic illustration: evaluateContinuity(journey())
// => approved context for three kinds; operational module changed from 2 to 3;
// no conjecture about absence; next activity remains an application-review
// candidate; no outbound message or human handoff is performed.

// MOON-SOURCE-PUBLIC-STAMP
// 🌙 Moon Source · Lua Helena Moon Martins Cardoso (Moon) + Áurion (AI-assisted) · Use & attribution: https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md · Full source: https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip · Questions, suggestions, or proposals? Feel free to contact me at LuaHelenaMMC@gmail.com.
