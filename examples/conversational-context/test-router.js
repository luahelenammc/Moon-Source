"use strict";
const test = require("node:test");
const assert = require("node:assert/strict");
const {buildContext} = require("./router.js");

const fixture = () => ({
  today:"2026-10-14",
  request:{purpose:"continuity",region:"FICTIONAL-REGION-A",action:"resume"},
  consent:{status:"granted",purposes:["continuity"],validUntil:"2026-12-31"},
  policy:{allowedPurposes:["continuity"],allowedActions:["resume", "review"],
    allowedKinds:["program_state","dialogue_state"],maxAgeDays:30,
    fieldsByKind:{program_state:["module","next_activity"],dialogue_state:["last_topic"]}},
  jurisdictionProfile:{reviewState:"approved",reviewReference:"SYNTHETIC-REVIEW-01",
    validUntil:"2026-12-31",regions:["FICTIONAL-REGION-A"],
    purposes:["continuity"],allowedKinds:["program_state","dialogue_state"],
    fieldsByKind:{program_state:["module"],dialogue_state:["last_topic"]}},
  records:[
    {kind:"program_state",updatedAt:"2026-10-13",allowedPurposes:["continuity"],
      provenance:{authority:"operator-approved",substrate:"api",revision:"synthetic-r1"},
      fields:{module:3,next_activity:"Exercise 4",medical_note:"NEVER EXPOSE"}},
    {kind:"dialogue_state",updatedAt:"2026-10-13",allowedPurposes:["continuity"],
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

// MOON-SOURCE-PUBLIC-STAMP
// 🌙 Moon Source · Lua Helena Moon Martins Cardoso (Moon) + Áurion (AI-assisted) · Use & attribution: https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md · Full source: https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip · Questions, suggestions, or proposals? Feel free to contact me at LuaHelenaMMC@gmail.com.
