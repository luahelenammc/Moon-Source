from pathlib import Path
import hashlib
import json
import zipfile


def replace_once(text: str, old: str, new: str, label: str) -> str:
    if old not in text:
        raise RuntimeError(f"missing anchor: {label}")
    return text.replace(old, new, 1)


adapter_path = Path("portables/chat-work/astra/CHAT_WORK_ASTRA_ADAPTER.md")
adapter = adapter_path.read_text(encoding="utf-8")

adapter = replace_once(
    adapter,
    "- **status:** current subordinate adapter; optional public guidance\n- **applies to:** Chat–Work Routing Protocol 5.1\n- **effective date:** 2026-09-09\n",
    "- **status:** current subordinate adapter; optional public guidance\n- **version:** 1.2\n- **versioning mode:** independently versioned subordinate submodule; the human title remains unversioned\n- **first public release:** 2026-09-09\n- **last material update:** 2026-09-10\n- **lineage:** 1.0 initial public strategy adapter → 1.1 total-work efficiency calibration → 1.2 mandatory setup/customization contract and tighter Chat–Work integration\n- **applies to:** Chat–Work Routing Protocol 5.1\n- **effective date:** 2026-09-09\n",
    "adapter metadata",
)

setup = """## Astra Setup Contract

Astra must not begin from an author-imposed operating style. **Before this adapter compiles or executes an Astra strategy, an Astra Setup must be resolved.** This gate is mandatory on first activation in a run unless a verified persistent Astra profile already exists and the user explicitly chooses to reuse it.

Setup is not questionnaire debt. Resolve only the preferences that materially change the route. Unknown fields may remain `auto` or inherit Chat–Work only when the user has explicitly accepted that adaptive behavior. A reference preset may be recommended after setup, but it must never be silently treated as the user's default.

The setup may complete in one turn when the user supplies enough configuration. Otherwise, the router presents the smallest decision-bearing proposal and obtains the user's acceptance before Astra execution begins.

Supported setup modes:

- **AUTO** — compile a proposed Astra configuration from the task plus the active Chat–Work profile, disclose the material fields and let the user accept or override it;
- **PROFILE** — reuse a verified persistent Astra profile, while disclosing material run-specific deviations before execution;
- **RUN_OVERRIDE** — apply explicit one-run changes without mutating a reusable profile.

A portable setup shape is:

```yaml
astra_setup:
  mode: AUTO | PROFILE | RUN_OVERRIDE
  persistence: ephemeral | persistent | unknown
  objective: null
  role_preference: auto | judgment | reviewer | co_architect | executor | mixed
  autonomy_preference: auto | read_only | recommend | bounded_mutation | sustained_execution
  context_breadth_preference: auto | micro_capsule | bounded_corpus | broad_corpus | workspace_scale
  coverage_preference: auto | single_delta | sibling_docket | multi_domain | exhaustive_bounded
  reasoning_preference: adaptive | conserve | balanced | deep
  optimization_priority: inherit_chat_work | throughput_per_allowance | quality | latency | balanced
  parallelism_preference: inherit_chat_work | logical_only | bounded | permissive
  mutation_authority: inherit_chat_work | none | bounded_explicit | sustained_explicit
  return_preference: auto | return_capsule | decision_trace | structured_report | artifact | patch | evidence_receipt | mixed
  checkpoints: proportional | aggressive
  stop_condition: null
```

These are preferences and routing inputs, not capability claims. Setup cannot manufacture model availability, surface access, source authority, mutation permission, budget, persistence or safety clearance.

### Setup precedence

When Astra-specific preferences conflict, use this order:

1. safety, authority, evidence and capability-floor constraints;
2. explicit current-run Astra override;
3. explicitly selected persistent Astra profile;
4. active Chat–Work Execution Profile fields that are semantically compatible with Astra;
5. an accepted Astra AUTO proposal;
6. adapter reference presets only as recommendations.

Absence of a preference is not permission to infer one from Moon's habits, a model's prestige, a previous user's workflow or a preset name.

> **No Astra preset is the default. Setup chooses the strategy space; the compiler chooses within it.**

### Persistence boundary

A named Astra profile is reusable only when it is actually stored in a persistent source available to the current environment. Otherwise it is ephemeral. This inherits Chat–Work's Profile Persistence Law: never claim that Astra preferences were saved, remembered or made default without evidence.

Material changes in objective, authority, available surfaces, resource posture or desired autonomy reopen only the affected setup fields. Do not rerun the entire questionnaire ritualistically.

"""

adapter = replace_once(adapter, "## Astra Strategy Profile\n", setup + "## Astra Strategy Profile\n", "setup insertion")
adapter = replace_once(
    adapter,
    "An Astra strategy should be compiled from independent dimensions. The exact syntax is illustrative; the semantic separation is load-bearing.\n\n```yaml\nastra_strategy:\n",
    "After Astra Setup is resolved, the strategy is compiled from independent dimensions. The exact syntax is illustrative; the semantic separation is load-bearing.\n\n```yaml\nastra_strategy:\n  setup_ref: required\n",
    "strategy setup ref",
)
adapter = replace_once(
    adapter,
    "## Reference presets\n\nThese are ergonomic starting points, not closed modes. A compiled strategy may mix fields differently when the task requires it.\n",
    "## Reference presets\n\nThese are ergonomic starting points, not closed modes or defaults. They may be suggested only after Astra Setup has established the user's preferences and task envelope. A compiled strategy may mix fields differently when the task requires it.\n",
    "preset law",
)

old_compiler = """## Astra Strategy Compiler

Resolve the strategy in this order:

1. **Sovereign objective and sovereign object** — what must actually change or be decided?
2. **Astra value test** — would Astra materially improve this task or irreducible slice, and is it actually available?
3. **Role** — judgment, review, co-architecture, execution or mixed?
4. **Autonomy** — how far should Astra carry the work before returning control?
5. **Corpus geometry** — how much context and how many authority domains must remain coherent?
6. **Mutation authority** — what may Astra actually change?
7. **Coverage topology** — one delta, finite docket, multiple domains or explicit bounded exhaustiveness?
8. **Reasoning effort** — what depth is required independently of role/autonomy?
9. **Resource overlay** — normal Budget Survivability or an explicitly activated Sprint/perishable-capacity envelope?
10. **Return geometry** — ruling, trace, report, artifact, patch, receipt or a mixed return?
11. **Checkpoints and stop condition** — where can the run safely stop, salvage or re-enter?
12. **Verification and Chat Postflight** — what observable evidence closes the loop?

The compiler should choose the smallest structure that preserves the task's required autonomy and coherence. It should not force every user through every field when defaults are harmless.
"""
new_compiler = """## Astra Strategy Compiler

Resolve the strategy in this order:

1. **Astra Setup Gate** — which setup mode is active, which user preferences are explicit, which fields may adapt, and has the setup been accepted for this run?
2. **Sovereign objective and sovereign object** — what must actually change or be decided?
3. **Astra value test** — would Astra materially improve this task or irreducible slice, and is it actually available?
4. **Role** — judgment, review, co-architecture, execution or mixed within the accepted setup?
5. **Autonomy** — how far should Astra carry the work before returning control?
6. **Corpus geometry** — how much context and how many authority domains must remain coherent?
7. **Mutation authority** — what may Astra actually change?
8. **Coverage topology** — one delta, finite docket, multiple domains or explicit bounded exhaustiveness?
9. **Reasoning effort** — what depth is required independently of role/autonomy and consistent with the user's resource preference?
10. **Resource overlay** — normal Budget Survivability or an explicitly activated Sprint/perishable-capacity envelope?
11. **Return geometry** — ruling, trace, report, artifact, patch, receipt or a mixed return?
12. **Checkpoints and stop condition** — where can the run safely stop, salvage or re-enter?
13. **Verification and Chat Postflight** — what observable evidence closes the loop?

The compiler should choose the smallest structure that preserves the task's required autonomy and coherence **inside the accepted setup envelope**. It must not silently override user preferences merely because another preset looks more efficient. When a preference conflicts with safety, authority, capability floor or observed availability, disclose the conflict and downroute, request a bounded override or return a blocked condition rather than inventing consent.
"""
adapter = replace_once(adapter, old_compiler, new_compiler, "compiler")

integration = """## Chat–Work integration contract

The Astra adapter is not a parallel router. It is a subordinate strategy layer inside Chat–Work.

Chat–Work resolves the general Execution Profile, Run State, task requirements, authority and capability floor first. When Astra is selected as a possible capability target, the adapter then resolves the **Astra Setup Contract** before compiling model-specific strategy.

This creates a nested setup relationship:

```text
Chat–Work Setup
  → general surface / capability / resource / authority envelope
  → Astra selected as a possible target
    → Astra Setup
      → user-specific role / autonomy / context / effort / fanout / return preferences
      → Astra Strategy Compiler
        → bounded execution or return
  → Chat Postflight
```

Chat–Work may recommend Astra and may prefill an AUTO proposal from explicit profile data, but it must not silently choose Brain Burst, Deep Review, Co-Architect, Executor, Full Run, Decision Sprint, maximum reasoning, maximum autonomy or physical fanout on the user's behalf.

The same user may rationally configure Astra differently for different tasks. A persistent Astra profile is a convenience, not an identity claim or an immutable default.

"""
adapter = replace_once(adapter, "## Relationship to IDL and capsules\n", integration + "## Relationship to IDL and capsules\n", "integration")
adapter = replace_once(
    adapter,
    "- `autonomy_underfit` — Astra was constrained to judgment when execution autonomy was load-bearing;\n",
    "- `setup_bypass` — Astra strategy or execution began before the required setup envelope was resolved;\n- `preset_capture` — a reference preset was silently treated as the user's default operating style;\n- `profile_inheritance_overreach` — Chat–Work or a prior Astra profile supplied preferences that were not explicit, persistent or semantically compatible with the current run;\n- `autonomy_underfit` — Astra was constrained to judgment when execution autonomy was load-bearing;\n",
    "failure classes",
)
adapter = replace_once(
    adapter,
    "## Relationship to Chat–Work 5.1\n\nChat–Work 5.1 adds only the generic boundary that makes this adapter\nlegitimate.",
    "## Relationship to Chat–Work 5.1\n\n**Current Astra adapter version: 1.2.** Chat–Work itself remains 5.1: this adapter version is subordinate and independently tracked, while the governing router keeps its stable release identity.\n\nChat–Work 5.1 adds only the generic boundary that makes this adapter\nlegitimate.",
    "relationship version",
)
adapter_path.write_text(adapter, encoding="utf-8")

legacy_path = Path("docs/CHAT_WORK_ASTRA_ADAPTER.md")
legacy = legacy_path.read_text(encoding="utf-8")
if "**Current adapter version:** 1.2" not in legacy:
    legacy = replace_once(
        legacy,
        "**Canonical adapter:** [`portables/chat-work/astra/CHAT_WORK_ASTRA_ADAPTER.md`](../portables/chat-work/astra/CHAT_WORK_ASTRA_ADAPTER.md)\n",
        "**Canonical adapter:** [`portables/chat-work/astra/CHAT_WORK_ASTRA_ADAPTER.md`](../portables/chat-work/astra/CHAT_WORK_ASTRA_ADAPTER.md)\n\n**Current adapter version:** 1.2\n",
        "legacy version",
    )
legacy_path.write_text(legacy, encoding="utf-8")

core_path = Path("portables/chat-work/CHAT_WORK_ROUTING_PROTOCOL_V4.md")
core = core_path.read_text(encoding="utf-8")
core = core.replace("docs/CHAT_WORK_ASTRA_ADAPTER.md", "portables/chat-work/astra/CHAT_WORK_ASTRA_ADAPTER.md")
if "A subordinate model adapter may require its own setup gate." not in core:
    marker = "portables/chat-work/astra/CHAT_WORK_ASTRA_ADAPTER.md"
    pos = core.find(marker)
    if pos == -1:
        raise RuntimeError("canonical Astra adapter reference not found")
    para_end = core.find("\n\n", pos)
    if para_end == -1:
        raise RuntimeError("canonical adapter paragraph end not found")
    addition = "\n\nA subordinate model adapter may require its own setup gate. Chat–Work's existing Execution Profile, Run State and Profile Persistence laws remain governing: the router may recommend or prefill model-specific preferences, but it must not silently instantiate a user's role, autonomy, reasoning, context, parallelism or return preferences. An explicit adaptive/AUTO choice is a setup choice, not permission to assume a reference preset."
    core = core[:para_end] + addition + core[para_end:]
core_path.write_text(core, encoding="utf-8")

readme_path = Path("portables/chat-work/README.md")
readme = readme_path.read_text(encoding="utf-8")
readme = readme.replace(
    "Astra is an optional subordinate submodule of this Chat–Work portable, not a prescribed work style. Its canonical adapter now lives inside this module at [`astra/CHAT_WORK_ASTRA_ADAPTER.md`](astra/CHAT_WORK_ASTRA_ADAPTER.md).",
    "Astra is an optional subordinate submodule of this Chat–Work portable, not a prescribed work style. Its canonical adapter now lives inside this module at [`astra/CHAT_WORK_ASTRA_ADAPTER.md`](astra/CHAT_WORK_ASTRA_ADAPTER.md) and is independently versioned at **1.2**.",
)
anchor = "When Astra is actually available, Chat–Work can compile it as a judgment brain, broad reviewer, co-architect, bounded executor or sustained full-run surface. Role, autonomy, reasoning depth, context breadth and mutation authority remain separate.\n"
if "Before Astra execution begins, the adapter runs its own compact Setup Contract." not in readme:
    readme = replace_once(
        readme,
        anchor,
        anchor + "\nBefore Astra execution begins, the adapter runs its own compact Setup Contract. No preset is the default: the user may choose AUTO, reuse a verified profile or apply a one-run override, and only then does the strategy compiler select a geometry inside that accepted envelope.\n",
        "readme setup",
    )
readme = readme.replace(
    "- **Optional Astra submodule:** [`astra/CHAT_WORK_ASTRA_ADAPTER.md`](astra/CHAT_WORK_ASTRA_ADAPTER.md)",
    "- **Optional Astra submodule:** [`astra/CHAT_WORK_ASTRA_ADAPTER.md`](astra/CHAT_WORK_ASTRA_ADAPTER.md) · version **1.2**",
)
readme_path.write_text(readme, encoding="utf-8")

root_path = Path("README.md")
root = root_path.read_text(encoding="utf-8")
if "Astra submodule **1.2**" not in root:
    needle = "- 🔀 [**Chat–Work Routing Protocol**](portables/chat-work/README.md) — "
    start = root.find(needle)
    if start != -1:
        end = root.find("\n", start)
        line = root[start:end]
        line = line.replace("current version **5.1**.", "current version **5.1**; optional Astra submodule **1.2**.")
        root = root[:start] + line + root[end:]
root_path.write_text(root, encoding="utf-8")

downloads_path = Path("DOWNLOADS.md")
downloads = downloads_path.read_text(encoding="utf-8")
downloads = downloads.replace(
    "Chat–Work additionally carries its subordinate Astra adapter because that adapter is part of the portable’s internal topology, not a separate capability.",
    "Chat–Work additionally carries its subordinate Astra adapter, currently **1.2**, because that adapter is part of the portable’s internal topology, not a separate capability. Astra 1.2 requires a compact user-resolved setup before model-specific strategy execution; its reference presets are recommendations, never defaults.",
)
downloads_path.write_text(downloads, encoding="utf-8")

registry_path = Path("registry/public-capabilities.json")
data = json.loads(registry_path.read_text(encoding="utf-8"))
chat = next(c for c in data["capabilities"] if c["id"] == "chat-work-routing")
chat["dependencies"] = [
    d.replace(
        "Optional Astra strategy adapter at portables/chat-work/astra/CHAT_WORK_ASTRA_ADAPTER.md; subordinate to the canonical Chat–Work body and not a second capability identity",
        "Optional Astra strategy adapter v1.2 at portables/chat-work/astra/CHAT_WORK_ASTRA_ADAPTER.md; subordinate to the canonical Chat–Work body, independently versioned as a submodule, setup-gated, and not a second capability identity",
    )
    for d in chat["dependencies"]
]
chat["last_material_update_on"] = "2026-09-10"
chat["last_material_update_summary"] = "Integrated the independently versioned Astra Strategy Adapter 1.2 as an internal Chat–Work submodule with a mandatory compact setup/customization contract; Chat–Work remains 5.1 and model-neutral."
chat["distribution"]["canonical_sha256"] = hashlib.sha256(core_path.read_bytes()).hexdigest()
registry_path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

human_registry_path = Path("registry/PUBLIC_CAPABILITIES.md")
if human_registry_path.exists():
    human = human_registry_path.read_text(encoding="utf-8")
    human = human.replace("docs/CHAT_WORK_ASTRA_ADAPTER.md", "portables/chat-work/astra/CHAT_WORK_ASTRA_ADAPTER.md")
    human = human.replace("subordinate Astra strategy guidance", "subordinate Astra Strategy Adapter 1.2 guidance")
    human_registry_path.write_text(human, encoding="utf-8")

impl_path = Path("docs/EXISTING_IMPLEMENTATIONS.md")
if impl_path.exists():
    impl = impl_path.read_text(encoding="utf-8")
    impl = impl.replace("docs/CHAT_WORK_ASTRA_ADAPTER.md", "portables/chat-work/astra/CHAT_WORK_ASTRA_ADAPTER.md")
    impl_path.write_text(impl, encoding="utf-8")

changelog_path = Path("CHANGELOG.md")
changelog = changelog_path.read_text(encoding="utf-8")
entry = """## 2026-09-10 — Astra Strategy Adapter 1.2 · setup and customization contract

- Established explicit independent submodule versioning: **1.0** for the initial accepted public adapter, **1.1** for the Total-Work Efficiency calibration, and **1.2** for this setup/customization integration.
- Added a mandatory compact Astra Setup Contract before model-specific strategy execution, with `AUTO`, verified `PROFILE` reuse and one-run `RUN_OVERRIDE` paths; setup resolves only materially relevant preferences and does not manufacture capability or authority.
- Made Brain Burst, Deep Review, Co-Architect, Executor, Full Run and Decision Sprint reference presets non-default recommendations; the strategy compiler now operates only inside the user-accepted setup envelope.
- Tightened nesting under Chat–Work: general Chat–Work setup/profile/run-state laws govern first, Astra setup resolves model-specific preferences second, and Chat Postflight still closes the loop. Chat–Work remains **5.1** because this is a subordinate adapter release plus clarification of existing setup/profile law, not a new core routing generation.

"""
if "## 2026-09-10 — Astra Strategy Adapter 1.2" not in changelog:
    changelog = replace_once(changelog, "# Changelog\n\n", "# Changelog\n\n" + entry, "changelog")
changelog_path.write_text(changelog, encoding="utf-8")

package = Path("downloads/chat-work-routing-protocol-v4.zip")
with zipfile.ZipFile(package, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
    archive.write(core_path, "CHAT_WORK_ROUTING_PROTOCOL_V4.md")
    archive.write(adapter_path, "astra/CHAT_WORK_ASTRA_ADAPTER.md")
