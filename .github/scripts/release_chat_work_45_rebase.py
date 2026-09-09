from pathlib import Path
import hashlib
import json
import zipfile

ROOT = Path(__file__).resolve().parents[2]
PROTOCOL = ROOT / "portables/chat-work/CHAT_WORK_ROUTING_PROTOCOL_V4.md"
README = ROOT / "README.md"
DOWNLOADS = ROOT / "DOWNLOADS.md"
REGISTRY = ROOT / "registry/public-capabilities.json"
HUMAN_REGISTRY = ROOT / "registry/PUBLIC_CAPABILITIES.md"
VERSIONING = ROOT / "docs/VERSIONING_AND_RELEASES.md"
CHANGELOG = ROOT / "CHANGELOG.md"
PACKAGE = ROOT / "downloads/chat-work-routing-protocol-v4.zip"


def once(text, old, new, label):
    n = text.count(old)
    if n != 1:
        raise SystemExit(f"{label}: expected 1 match, got {n}")
    return text.replace(old, new, 1)

# Canonical Chat–Work 4.5 body/facade/package are copied from the already
# validated release branch before this script runs. Reconcile only the
# cross-repository surfaces against the latest main state.

data = json.loads(REGISTRY.read_text(encoding="utf-8"))
record = next(c for c in data["capabilities"] if c["id"] == "chat-work-routing")
if record["version"] != "4.4-public":
    raise SystemExit(f"expected Chat–Work 4.4-public on rebased main, got {record['version']}")
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
h = once(h, "| chat-work-routing | [Chat–Work Routing Protocol](../portables/chat-work/README.md) | operational routing protocol | 4.4-public | current |", "| chat-work-routing | [Chat–Work Routing Protocol](../portables/chat-work/README.md) | operational routing protocol | 4.5-public | current |", "human registry version")
h = once(h, "https://www.luahelena.com.br/moonsource/downloads/CHAT_WORK_ROUTING_PROTOCOL_V4_MSL_4_4.md", "https://www.luahelena.com.br/moonsource/downloads/CHAT_WORK_ROUTING_PROTOCOL_V4_MSL_4_5.md", "human registry mirror")
h = once(h, "This corrective release keeps Connected Sources at 1.1-public, MSL at 5.0, Chat–Work at 4.4-public, Setup at 3.1, Preflight at 2.0 and Be My Eyes at 1.0-public. MSL's formatting contract is part of the current 5.0 body and release identity.", "This corrective MSL release remains current alongside Connected Sources at 1.1-public, MSL at 5.0, Chat–Work at 4.5-public, Setup at 3.1, Preflight at 2.0 and Be My Eyes at 1.0-public. MSL's formatting contract is part of the current 5.0 body and release identity.", "human registry current versions")
HUMAN_REGISTRY.write_text(h, encoding="utf-8")

r = README.read_text(encoding="utf-8")
r = once(r, "- 🔀 [**Chat–Work Routing Protocol**](portables/chat-work/README.md) — object-routed execution across Chat, Work and Codex, Budget Survivability, Intelligence Distillation Ladder, connector-aware source transport, Chat Postflight, bounded repair, acceptance and delta-only re-entry; current version **4.4-public**.", "- 🔀 [**Chat–Work Routing Protocol**](portables/chat-work/README.md) — object-routed execution across Chat, Work and Codex, Budget Survivability, Intelligence Distillation Ladder, bounded exhaustiveness, scope-amplification recovery, connector-aware source transport, Chat Postflight, bounded repair, acceptance and delta-only re-entry; current version **4.5-public**.", "root README current Chat–Work")
README.write_text(r, encoding="utf-8")

d = DOWNLOADS.read_text(encoding="utf-8")
d = once(d, "The current Be My Eyes capability version is **1.0-public**. The current Connected Sources capability version is **1.1-public**. The current Chat–Work Routing Protocol version is **4.4-public**. It retains the model-neutral Intelligence Distillation Ladder and adds a connector-aware source transport contract for governing source/family, locator, facet, operation, coverage, freshness, mutation authorization, readback and fallback, while preserving the V4 title, canonical filename and current MSL 5.0.", "The current Be My Eyes capability version is **1.0-public**. The current Connected Sources capability version is **1.1-public**. The current Chat–Work Routing Protocol version is **4.5-public**. It retains the model-neutral Intelligence Distillation Ladder and connector-aware source transport, and now adds bounded exhaustiveness plus scope-amplification recovery, while preserving the unversioned human title, V4 canonical filename and current MSL 5.0.", "download hub release prose")
d = once(d, "- **Want configurable Chat ↔ Work ↔ Codex routing?** Download **Chat–Work Routing Protocol** (version **4.4-public**).", "- **Want configurable Chat ↔ Work ↔ Codex routing?** Download **Chat–Work Routing Protocol** (version **4.5-public**).", "download hub chooser")
DOWNLOADS.write_text(d, encoding="utf-8")

v = VERSIONING.read_text(encoding="utf-8")
v = once(v, "Chat–Work tri-surface routing advanced to V4 on 2026-09-06 and its IDL/source-transport subversions to 4.4-public on 2026-09-07.", "Chat–Work tri-surface routing advanced to V4 on 2026-09-06, to the IDL/source-transport subversions through 4.4-public on 2026-09-07, and to bounded-exhaustiveness subversion 4.5-public on 2026-09-09.", "versioning baseline history")
v = once(v, "Chat–Work Routing Protocol (version 4.4-public).", "Chat–Work Routing Protocol (version 4.5-public).", "versioning current standalone")
anchor = "MSL remains 4.3 because the structural grammar did not change.\n\n## Future versions"
release = """MSL remains 4.3 because the structural grammar did not change.

### Chat–Work V4.5-public release — 2026-09-09

Chat–Work V4.5-public is a **material additive-and-superseding portable release**, not an MSL grammar change. It retains the V4.4 connector-aware source transport contract and adds a Bounded Exhaustiveness Guard to the Intelligence Distillation Ladder so open-ended completeness language is compiled into explicit coverage ceilings, stop conditions and scope-expansion rules before expensive sustained or frontier execution.

The release also adds `scope_amplification_failure` and a constrain-before-escalate recovery path. The Astra behavior that motivated the calibration is retained only as dated anecdotal field evidence, not as a benchmark, universal model property or fixed cost claim. The public human title remains **Chat–Work Routing Protocol** and the canonical filename remains `CHAT_WORK_ROUTING_PROTOCOL_V4.md`; 4.5-public is release state, not title identity.

The superseded 4.4-public portable remains recoverable through Git history. MSL remains 5.0 because this release changes the routing/distillation protocol, not the structural passage grammar.

## Future versions"""
v = once(v, anchor, release, "versioning 4.5 release section")
VERSIONING.write_text(v, encoding="utf-8")

c = CHANGELOG.read_text(encoding="utf-8")
anchor = "- Kept MSL at 5.0: this is a corrective content release, not a new semantic generation or parallel patch authority.\n\n"
entry = """- Kept MSL at 5.0: this is a corrective content release, not a new semantic generation or parallel patch authority.

## 2026-09-09 — Chat–Work 4.5 · bounded exhaustiveness

- Added a Bounded Exhaustiveness Guard to the Intelligence Distillation Ladder so open-ended completeness requests are compiled into explicit coverage, stop and scope-expansion boundaries before expensive execution.
- Added `scope_amplification_failure` and a constrain-before-escalate recovery path, separating runaway scope from genuine cognitive insufficiency or raw budget failure.
- Added dated Astra field calibration as anecdotal operational evidence without promoting community reports into a benchmark or universal model law.
- Kept the V4 canonical filename and stable human title while advancing the independently versioned public protocol to 4.5-public.

"""
c = once(c, anchor, entry, "changelog insertion")
CHANGELOG.write_text(c, encoding="utf-8")

with zipfile.ZipFile(PACKAGE) as zf:
    files = [name for name in zf.namelist() if not name.endswith("/")]
    if files != [PROTOCOL.name]:
        raise SystemExit(f"unexpected Chat–Work package members: {files}")
    if zf.read(PROTOCOL.name) != PROTOCOL.read_bytes():
        raise SystemExit("Chat–Work package is not byte-identical to canonical body")

print("rebased Chat–Work 4.5 release surfaces prepared")
print("canonical_sha256", hashlib.sha256(PROTOCOL.read_bytes()).hexdigest())
