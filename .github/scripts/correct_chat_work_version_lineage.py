from pathlib import Path
import hashlib
import json
import zipfile

ROOT = Path(__file__).resolve().parents[2]
PROTOCOL = ROOT / "portables/chat-work/CHAT_WORK_ROUTING_PROTOCOL_V4.md"
CW_README = ROOT / "portables/chat-work/README.md"
ROOT_README = ROOT / "README.md"
DOWNLOADS = ROOT / "DOWNLOADS.md"
REGISTRY = ROOT / "registry/public-capabilities.json"
HUMAN_REGISTRY = ROOT / "registry/PUBLIC_CAPABILITIES.md"
VERSIONING = ROOT / "docs/VERSIONING_AND_RELEASES.md"
CHANGELOG = ROOT / "CHANGELOG.md"
PACKAGE = ROOT / "downloads/chat-work-routing-protocol-v4.zip"


def once(text, old, new, label):
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"{label}: expected exactly one match, got {count}")
    return text.replace(old, new, 1)

# Lineage audit after the last correctly numbered Chat–Work release (4.4-public):
# 1) c637a576 — self-onboarding canonical-body integration => 4.5
# 2) d513b84c — MSL 5.0 canonical dependency/reference alignment => 4.6
# 3) 7b50a4d7 — bounded exhaustiveness / scope-amplification recovery => 4.7
# The current 4.5 label therefore skipped two required +0.1 increments.

p = PROTOCOL.read_text(encoding="utf-8")
p = once(p, "## Public Portable Edition · Version 4.5-public", "## Public Portable Edition · Version 4.7-public", "protocol edition")
p = once(p, "CHAT_WORK_ROUTING_PROTOCOL_V4_MSL_4_5.md", "CHAT_WORK_ROUTING_PROTOCOL_V4_MSL_4_7.md", "protocol mirror path")
p = once(p, "- **version:** 4.5-public", "- **version:** 4.7-public", "protocol version metadata")
p = once(p, "- **supersedes:** Chat–Work Routing Protocol V4, version 4.4-public, while retaining the V4 public generation and canonical filename", "- **supersedes:** Chat–Work Routing Protocol V4, published label 4.5-public; this 4.7-public correction restores two previously skipped +0.1 lineage increments while retaining the V4 public generation and canonical filename", "protocol supersedes")
p = once(p, "the protocol remains independently versioned at 4.5-public.", "the protocol remains independently versioned at 4.7-public.", "protocol MSL dependency version")
p = once(
    p,
    "The V4.2 subversion added the profile-conditioned route principle. V4.3 added a distillation principle. V4.4 added a connector-aware source transport contract. V4.5 adds bounded exhaustiveness and scope-amplification recovery:",
    "The V4.2 subversion added the profile-conditioned route principle. V4.3 added a distillation principle. V4.4 added a connector-aware source transport contract. Under the corrected +0.1 lineage, V4.5 accounts for the self-onboarding canonical-body integration, V4.6 for the MSL 5.0 canonical dependency/reference alignment, and V4.7 adds bounded exhaustiveness and scope-amplification recovery:",
    "protocol lineage sentence",
)
PROTOCOL.write_text(p, encoding="utf-8")

r = CW_README.read_text(encoding="utf-8")
r = once(r, "- **Version:** 4.5-public", "- **Version:** 4.7-public", "portable README version")
CW_README.write_text(r, encoding="utf-8")

# Machine registry.
data = json.loads(REGISTRY.read_text(encoding="utf-8"))
record = next(c for c in data["capabilities"] if c["id"] == "chat-work-routing")
if record["version"] != "4.5-public":
    raise SystemExit(f"expected current Chat–Work version 4.5-public, got {record['version']}")
record["version"] = "4.7-public"
record["claim_ceiling"] = record["claim_ceiling"].replace("4.5-public", "4.7-public")
record["last_material_update_summary"] = "Lineage-corrected to 4.7-public after auditing two previously skipped +0.1 canonical-body updates; current semantics retain bounded exhaustiveness and scope-amplification recovery with Astra behavior treated as dated anecdotal calibration."
record["supersedes"] = "4.5-public"
record["distribution"]["mirror_path"] = record["distribution"]["mirror_path"].replace("_4_5.md", "_4_7.md")
record["distribution"]["mirror_url"] = record["distribution"]["mirror_url"].replace("_4_5.md", "_4_7.md")
record["distribution"]["canonical_sha256"] = hashlib.sha256(PROTOCOL.read_bytes()).hexdigest()
REGISTRY.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

# Current human-facing surfaces.
h = HUMAN_REGISTRY.read_text(encoding="utf-8")
h = h.replace("4.5-public", "4.7-public")
h = h.replace("CHAT_WORK_ROUTING_PROTOCOL_V4_MSL_4_5.md", "CHAT_WORK_ROUTING_PROTOCOL_V4_MSL_4_7.md")
HUMAN_REGISTRY.write_text(h, encoding="utf-8")

root = ROOT_README.read_text(encoding="utf-8")
root = root.replace("4.5-public", "4.7-public")
ROOT_README.write_text(root, encoding="utf-8")

d = DOWNLOADS.read_text(encoding="utf-8")
d = d.replace("4.5-public", "4.7-public")
DOWNLOADS.write_text(d, encoding="utf-8")

# Version policy + corrected release lineage.
v = VERSIONING.read_text(encoding="utf-8")
v = v.replace("4.5-public", "4.7-public")
v = v.replace("### Chat–Work V4.5-public release — 2026-09-09", "### Chat–Work V4.7-public release — 2026-09-09")
rule_anchor = "12. One capability has one canonical semantic body. Architectural role and standalone distribution are independent dimensions. Mirrors and packages are delivery surfaces, and a distinct adapter is allowed only for volatile or surface-specific facts.\n"
rule_insert = rule_anchor + "13. Every accepted update to an independently versioned capability's canonical body or operative contract advances that capability by **+0.1**. A bookkeeping-only correction that restores previously skipped version increments does not recursively create another bump.\n"
v = once(v, rule_anchor, rule_insert, "versioning +0.1 rule")
lineage_anchor = "The superseded 4.4-public portable remains recoverable through Git history. MSL remains 5.0 because this release changes the routing/distillation protocol, not the structural passage grammar.\n"
lineage_note = lineage_anchor + "\n**Lineage correction:** the last correctly numbered Chat–Work release was 4.4-public. The self-onboarding canonical-body integration is counted as 4.5, the MSL 5.0 canonical dependency/reference alignment as 4.6, and the bounded-exhaustiveness update as 4.7. The repository had preserved 4.4 across the first two updates under an older semantic-only bump convention; this correction restores the project's +0.1-per-module-update rule without fabricating parallel historical artifacts.\n"
v = once(v, lineage_anchor, lineage_note, "versioning lineage note")
VERSIONING.write_text(v, encoding="utf-8")

c = CHANGELOG.read_text(encoding="utf-8")
c = once(c, "## 2026-09-09 — Chat–Work 4.5 · bounded exhaustiveness", "## 2026-09-09 — Chat–Work 4.7 · bounded exhaustiveness + lineage correction", "changelog heading")
c = once(c, "- Kept the V4 canonical filename and stable human title while advancing the independently versioned public protocol to 4.5-public.", "- Kept the V4 canonical filename and stable human title while correcting the independently versioned public protocol to 4.7-public. The audit counts the self-onboarding canonical-body integration as 4.5, the MSL 5.0 canonical dependency/reference alignment as 4.6, and this bounded-exhaustiveness update as 4.7.", "changelog lineage")
CHANGELOG.write_text(c, encoding="utf-8")

# Rebuild the canonical-body-only package after the metadata correction.
with zipfile.ZipFile(PACKAGE, "w", compression=zipfile.ZIP_DEFLATED) as zf:
    zf.write(PROTOCOL, arcname=PROTOCOL.name)

print("Chat–Work version lineage corrected to 4.7-public")
print("canonical_sha256", hashlib.sha256(PROTOCOL.read_bytes()).hexdigest())
