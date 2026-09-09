from pathlib import Path
import hashlib
import json
import zipfile

ROOT = Path(__file__).resolve().parents[2]
PROTOCOL = ROOT / "portables/chat-work/CHAT_WORK_ROUTING_PROTOCOL_V4.md"
README = ROOT / "portables/chat-work/README.md"
REGISTRY = ROOT / "registry/public-capabilities.json"
HUMAN_REGISTRY = ROOT / "registry/PUBLIC_CAPABILITIES.md"
CHANGELOG = ROOT / "CHANGELOG.md"
PACKAGE = ROOT / "downloads/chat-work-routing-protocol-v4.zip"


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"{label}: expected exactly 1 match, got {count}")
    return text.replace(old, new, 1)


p = PROTOCOL.read_text(encoding="utf-8")

p = replace_once(p, "## Public Portable Edition · Version 4.4-public", "## Public Portable Edition · Version 4.5-public", "edition version")
p = replace_once(p, "https://www.luahelena.com.br/moonsource/downloads/CHAT_WORK_ROUTING_PROTOCOL_V4_MSL_4_4.md", "https://www.luahelena.com.br/moonsource/downloads/CHAT_WORK_ROUTING_PROTOCOL_V4_MSL_4_5.md", "website mirror")
p = replace_once(p, "- **version:** 4.4-public", "- **version:** 4.5-public", "meta version")
p = replace_once(p, "- **protocol semantics as of:** 2026-09-07", "- **protocol semantics as of:** 2026-09-09", "semantics date")
p = replace_once(p, "- **product/model calibration as of:** 2026-09-06; recheck official documentation before relying on volatile names, availability, limits or pricing", "- **product/model calibration as of:** 2026-09-09; recheck official documentation before relying on volatile names, availability, limits or pricing", "calibration date")
p = replace_once(p, "- **governed dimensions:** execution profile, object geometry, execution surface, capability tier, reasoning effort, continuity/locality, execution envelope, budget survival, distillation, return closure and claim ceiling", "- **governed dimensions:** execution profile, object geometry, execution surface, capability tier, reasoning effort, continuity/locality, execution envelope, budget survival, distillation, bounded exhaustiveness, return closure and claim ceiling", "governed dimensions")
p = replace_once(p, "- **supersedes:** Chat–Work Routing Protocol V4, version 4.3-public, while retaining the V4 public generation and canonical filename", "- **supersedes:** Chat–Work Routing Protocol V4, version 4.4-public, while retaining the V4 public generation and canonical filename", "supersedes")
p = replace_once(p, "- **MSL dependency:** Moon Source Language 5.0; the protocol remains independently versioned at 4.4-public.", "- **MSL dependency:** Moon Source Language 5.0; the protocol remains independently versioned at 4.5-public.", "MSL dependency")

p = replace_once(
    p,
    "The V4.2 subversion added the profile-conditioned route principle. V4.3 added a distillation principle. V4.4 adds a connector-aware source transport contract:\n\n> **Escalate only the irreducible delta; return only the decision-bearing delta.**\n\n> **Transport source references with authority, freshness and fallback; a locator is not authority.**",
    "The V4.2 subversion added the profile-conditioned route principle. V4.3 added a distillation principle. V4.4 added a connector-aware source transport contract. V4.5 adds bounded exhaustiveness and scope-amplification recovery:\n\n> **Escalate only the irreducible delta; return only the decision-bearing delta.**\n\n> **Transport source references with authority, freshness and fallback; a locator is not authority.**\n\n> **Bound completeness before expensive execution; discovering scope is not permission to execute all of it.**",
    "mother-law lineage",
)

p = replace_once(
    p,
    "Community reports can reveal operational failure modes such as unexpectedly rapid allowance burn, but anecdotes never become fixed pricing or performance constants in the protocol.",
    "Community reports can reveal operational failure modes such as unexpectedly rapid allowance burn, but anecdotes never become fixed pricing or performance constants in the protocol.\n\nAs a dated field calibration on 2026-09-09, a trusted community report described Astra expanding open-ended completeness instructions into very large edge-case and test sweeps. Treat this as anecdotal operational evidence, not a benchmark or universal model property. When Astra is selected for sustained or frontier execution, prefer explicit scope ceilings and stop conditions over vague requests to \"be balanced.\"",
    "Astra field calibration",
)

anchor = "Do not carry the full conversation or repository merely because it is available. Exclude duplicated history, settled implementation bulk, raw tool logs, already-closed questions and speculative context without a named role. Compression is invalid if it removes load-bearing authority, constraints, evidence, uncertainty or provenance.\n\n#### Tier ROI and No Mandatory Staircase"
guard = """Do not carry the full conversation or repository merely because it is available. Exclude duplicated history, settled implementation bulk, raw tool logs, already-closed questions and speculative context without a named role. Compression is invalid if it removes load-bearing authority, constraints, evidence, uncertainty or provenance.

#### Bounded Exhaustiveness Guard

Open-ended completeness language can amplify scope even when the selected model is cognitively sufficient. Before expensive sustained execution or a frontier burst, compile phrases such as `all edge cases`, `exhaustive`, `fully comprehensive`, `cover everything` or equivalent wording into an explicit coverage contract.

```yaml
bounded_exhaustiveness:
  coverage_mode: representative_risk_weighted | exhaustive_bounded
  coverage_ceiling:
    named_domains: []
    max_new_case_classes: null
    test_budget_or_growth_rule: null
  stop_condition: null
  scope_expansion: explicit_authorization_required
  discovered_out_of_scope: defer_and_report
```

The default is `representative_risk_weighted`: cover the highest-risk and decision-relevant classes first, then stop when the named acceptance boundary is satisfied. Use `exhaustive_bounded` only when exhaustiveness is genuinely required and the bounded domain is explicit. "Be balanced" may be useful conversational guidance, but it is not a computable execution boundary and must not substitute for these fields when runaway completeness would be costly.

Enumeration is not execution. A model may map a wider edge-case landscape without gaining authority to investigate, implement or test every discovered branch. Newly discovered classes outside the active ceiling go to `deferred_candidates` unless scope expansion is explicitly authorized.

If the run materially expands investigation, testing or implementation beyond the decision-bearing delta without an explicit ceiling or authorization, classify the incident as `scope_amplification_failure`. This is distinct from `cognitive_failure` and from raw `budget_or_resource_failure`: resource burn may be a consequence of an unbounded objective rather than evidence that the model lacks capability.

Recovery order for `scope_amplification_failure`:

1. preserve verified work and salvageable artifacts;
2. redistill the irreducible delta;
3. narrow the coverage envelope;
4. set an explicit stop condition and scope-expansion rule;
5. resume on the same or lower sufficient tier unless independent evidence shows a genuine capability deficit.

> **Scope blowout is not itself evidence that the delta needs a stronger model. Constrain first; escalate only if the bounded delta still exceeds the current route.**

#### Tier ROI and No Mandatory Staircase"""
p = replace_once(p, anchor, guard, "bounded exhaustiveness insertion")

p = replace_once(
    p,
    "    underfit_after_burst: false\n    overkill_suspected: false\n    returned_to_lower_tier: true",
    "    underfit_after_burst: false\n    overkill_suspected: false\n    scope_amplification_detected: false\n    returned_to_lower_tier: true",
    "distillation receipt",
)

p = replace_once(
    p,
    "A Frontier Full Run is justified only when decomposition would destroy coherence, the Budget Survivability Gate passes, sustained frontier capability is materially load-bearing and salvage/checkpoints exist.",
    "A Frontier Full Run is justified only when decomposition would destroy coherence, the Budget Survivability Gate passes, sustained frontier capability is materially load-bearing and salvage/checkpoints exist. When the selected frontier route shows literal scope-expansion pressure, apply the Bounded Exhaustiveness Guard before authorizing the run.",
    "frontier guard",
)

p = replace_once(
    p,
    "When an IDL cycle is active, the handoff additionally names the irreducible delta, the Decision Capsule, the selected target tier and the Return Capsule boundary. These fields are conditional; tiny tasks do not need an empty distillation ceremony.",
    "When an IDL cycle is active, the handoff additionally names the irreducible delta, the Decision Capsule, the selected target tier, the Return Capsule boundary and any Bounded Exhaustiveness contract that materially limits the run. These fields are conditional; tiny tasks do not need an empty distillation ceremony.",
    "readiness prose",
)

p = replace_once(
    p,
    "distillation:\n  active: false\n  delta_id: null\n  unresolved_question: null\n  target_tier: null\n  decision_capsule: null\n  return_capsule_required: false",
    "distillation:\n  active: false\n  delta_id: null\n  unresolved_question: null\n  target_tier: null\n  decision_capsule: null\n  coverage_mode: representative_risk_weighted\n  coverage_ceiling: null\n  stop_condition: null\n  scope_expansion: explicit_authorization_required\n  return_capsule_required: false",
    "readiness schema",
)

p = replace_once(
    p,
    "  distillation:\n    active: false\n    delta_id: null\n    target_tier: null\n    decision_capsule: null\n    return_capsule: null\n    reentry_owner: null",
    "  distillation:\n    active: false\n    delta_id: null\n    target_tier: null\n    decision_capsule: null\n    coverage_mode: representative_risk_weighted\n    coverage_ceiling: null\n    stop_condition: null\n    scope_expansion: explicit_authorization_required\n    return_capsule: null\n    reentry_owner: null",
    "handoff schema",
)

p = replace_once(
    p,
    "- `workflow_or_fanout_failure`\n- `budget_or_resource_failure`\n- `cognitive_failure`",
    "- `workflow_or_fanout_failure`\n- `scope_amplification_failure`\n- `budget_or_resource_failure`\n- `cognitive_failure`",
    "failure class",
)

p = replace_once(
    p,
    "6. record a Budget Incident Receipt when resource conditions materially shaped the failure.",
    "6. if scope amplification occurred, redistill and bound coverage before retry;\n7. record a Budget Incident Receipt when resource conditions materially shaped the failure.",
    "salvage recovery",
)

p = replace_once(
    p,
    "- `4.4-public` is the current semantic subversion of that generation, not a new V5 title or filename;\n- `4.3-public` is superseded by this subversion and remains recoverable through Git history;\n- `4.2-public`, `4.1-public` and earlier 4.x subversions remain historical lineage recoverable through Git history;\n- `4.0-public` and V3 remain historical lineage;\n- the live repository and website each expose one canonical V4 file;\n- MSL is currently 5.0; this protocol remains independently versioned at 4.4-public;",
    "- `4.5-public` is the current semantic subversion of that generation, not a new V5 title or filename;\n- `4.4-public` is superseded by this subversion and remains recoverable through Git history;\n- `4.3-public`, `4.2-public`, `4.1-public` and earlier 4.x subversions remain historical lineage recoverable through Git history;\n- `4.0-public` and V3 remain historical lineage;\n- the live repository and website each expose one canonical V4 file;\n- MSL is currently 5.0; this protocol remains independently versioned at 4.5-public;",
    "lifecycle version",
)

p = replace_once(
    p,
    "- Apply IDL: isolate the irreducible delta, choose the least-expensive sufficient target, allow justified direct tier jumps and return only the decision-bearing ruling.",
    "- Apply IDL: isolate the irreducible delta, choose the least-expensive sufficient target, allow justified direct tier jumps and return only the decision-bearing ruling.\n- Compile open-ended completeness into a bounded coverage mode, ceiling, stop condition and explicit scope-expansion rule before expensive sustained or frontier execution.",
    "safe operating rule",
)

p = replace_once(
    p,
    "When a named irreducible delta exceeds the current route, compile a Decision Capsule, choose the least-expensive sufficient target without forcing intermediate tiers, request a bounded ruling, return to the lowest sufficient tier and verify.",
    "When a named irreducible delta exceeds the current route, compile a Decision Capsule, choose the least-expensive sufficient target without forcing intermediate tiers, request a bounded ruling, return to the lowest sufficient tier and verify. Before expensive frontier execution, compile open-ended completeness language into an explicit coverage mode, ceiling, stop condition and scope-expansion rule.",
    "installation prompt",
)

p = replace_once(
    p,
    "Spend intelligence where it changes the outcome. Escalate only the irreducible delta and return only the decision-bearing delta.",
    "Spend intelligence where it changes the outcome. Bound completeness before expensive execution. Escalate only the irreducible delta and return only the decision-bearing delta.",
    "final law",
)

PROTOCOL.write_text(p, encoding="utf-8")

r = README.read_text(encoding="utf-8")
r = replace_once(r, "including execution profiles, connector-aware source transport, Budget Survivability, the Intelligence Distillation Ladder and Chat Postflight.", "including execution profiles, connector-aware source transport, Budget Survivability, the Intelligence Distillation Ladder, bounded exhaustiveness and Chat Postflight.", "README feature list")
r = replace_once(r, "- **Version:** 4.4-public", "- **Version:** 4.5-public", "README version")
README.write_text(r, encoding="utf-8")

data = json.loads(REGISTRY.read_text(encoding="utf-8"))
record = next(c for c in data["capabilities"] if c["id"] == "chat-work-routing")
if record["version"] != "4.4-public":
    raise SystemExit(f"registry expected 4.4-public, got {record['version']}")
record["function"] = "Route by sovereign object and workload shape across Chat, Work and optional Codex using configurable execution profiles, observed surface availability, capability floors, Budget Survivability, the model-neutral Intelligence Distillation Ladder, bounded exhaustiveness, scope-amplification recovery, connector-aware source transport, bounded micro-bursts, decision-bearing return capsules, Chat Postflight and delta-only re-entry"
record["claim_ceiling"] = "Published Chat–Work V4 protocol, subversion 4.5-public; operational routing heuristic only, not an OpenAI policy, benchmark, guaranteed savings/quality claim or proof that a native chat-work-router V4 skill is installed"
record["version"] = "4.5-public"
record["last_material_update_on"] = "2026-09-09"
record["last_material_update_summary"] = "Added bounded exhaustiveness and scope-amplification recovery to the Intelligence Distillation Ladder, with Astra-specific behavior retained as dated anecdotal calibration rather than universal model law."
record["freshness"] = "protocol semantics as of 2026-09-09; product/model calibration as of 2026-09-09; recheck volatile product behavior, model names, prices, availability and usage pools"
record["supersedes"] = "4.4-public"
record["distribution"]["mirror_path"] = "moonsource/downloads/CHAT_WORK_ROUTING_PROTOCOL_V4_MSL_4_5.md"
record["distribution"]["mirror_url"] = "https://www.luahelena.com.br/moonsource/downloads/CHAT_WORK_ROUTING_PROTOCOL_V4_MSL_4_5.md"
record["distribution"]["canonical_sha256"] = hashlib.sha256(PROTOCOL.read_bytes()).hexdigest()
REGISTRY.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

h = HUMAN_REGISTRY.read_text(encoding="utf-8")
h = replace_once(h, "| chat-work-routing | [Chat–Work Routing Protocol](../portables/chat-work/README.md) | operational routing protocol | 4.4-public | current |", "| chat-work-routing | [Chat–Work Routing Protocol](../portables/chat-work/README.md) | operational routing protocol | 4.5-public | current |", "human registry version")
h = replace_once(h, "https://www.luahelena.com.br/moonsource/downloads/CHAT_WORK_ROUTING_PROTOCOL_V4_MSL_4_4.md", "https://www.luahelena.com.br/moonsource/downloads/CHAT_WORK_ROUTING_PROTOCOL_V4_MSL_4_5.md", "human registry mirror")
h = replace_once(h, "Connected Sources at 1.1-public, MSL at 5.0, Chat–Work at 4.4-public, Setup at\n3.1, Preflight at 2.0 and Be My Eyes at 1.0-public.", "Connected Sources at 1.1-public, MSL at 5.0, Chat–Work at 4.5-public, Setup at\n3.1, Preflight at 2.0 and Be My Eyes at 1.0-public.", "human registry current versions")
HUMAN_REGISTRY.write_text(h, encoding="utf-8")

c = CHANGELOG.read_text(encoding="utf-8")
if not c.startswith("# Changelog\n\n"):
    raise SystemExit("unexpected changelog header")
entry = """# Changelog

## 2026-09-09 — Chat–Work 4.5 · bounded exhaustiveness

- Added a Bounded Exhaustiveness Guard to the Intelligence Distillation Ladder so open-ended completeness requests are compiled into explicit coverage, stop and scope-expansion boundaries before expensive execution.
- Added `scope_amplification_failure` and a constrain-before-escalate recovery path, separating runaway scope from genuine cognitive insufficiency or raw budget failure.
- Added dated Astra field calibration as anecdotal operational evidence without promoting community reports into benchmark or universal model law.
- Kept the V4 canonical title and filename while advancing the independently versioned public protocol to 4.5-public.

"""
CHANGELOG.write_text(entry + c[len("# Changelog\n\n"):], encoding="utf-8")

with zipfile.ZipFile(PACKAGE, "w", compression=zipfile.ZIP_DEFLATED) as zf:
    zf.write(PROTOCOL, arcname=PROTOCOL.name)

with zipfile.ZipFile(PACKAGE) as zf:
    files = [name for name in zf.namelist() if not name.endswith("/")]
    if files != [PROTOCOL.name]:
        raise SystemExit(f"unexpected package members: {files}")
    if zf.read(PROTOCOL.name) != PROTOCOL.read_bytes():
        raise SystemExit("package body is not byte-identical to canonical protocol")

print("Chat–Work 4.5 release prepared")
print("canonical_sha256", hashlib.sha256(PROTOCOL.read_bytes()).hexdigest())
