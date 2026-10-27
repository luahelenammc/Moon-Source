# Adaptive Orchestration GPT-6 Sol/Luna Strategy Adapter

*Dated executor calibration for the GPT-6 family*

## Meta

- **status:** current subordinate adapter
- **adapter version:** 1.9
- **as of:** 2026-10-26
- **governing capability:** [Adaptive Orchestration Protocol](../ADAPTIVE_ORCHESTRATION_PROTOCOL.md)
- **scope:** GPT-6.1 Sol and GPT-6 Sol/Luna routing across Chat, Work and Codex where available, with dated Chat-vs-Work model-variant boundaries, heterogeneous subagent topology, child-model inheritance/overrides, token-economy profiles, behavioral-fit calibration, commitment-bearing decision routing and API/product-boundary reasoning about executor choice
- **authority:** subordinate; the canonical Adaptive Orchestration body wins on conflict
- **volatility:** high; availability, model menus, reasoning controls, plan/workspace exposure and usage economics must be rechecked
- **product boundary:** not OpenAI policy, not a benchmark ranking system and not a guarantee about ChatGPT allowance consumption
- **creator:** Lua Helena Moon Martins Cardoso (Moon)
- **AI-assisted coauthorial development:** Áurion
- **license:** CC BY 4.0 under the repository licensing terms

## 1. Why this adapter exists

GPT-6 changes the practical executor geometry, and current subagent support makes heterogeneous model delegation a first-class execution option under Adaptive Orchestration 6.4. The 6.4 core is surface-neutral, behavior-aware and commitment-aware: Sol/Luna topology does not require Chat to be the control root when Work or Codex can retain objective, convergence and postflight, and capability sufficiency does not erase behavioral-fit or commitment-fit differences between executors.

At launch, OpenAI positions:

- **GPT-6 Luna** as the efficient model for focused, high-volume work;
- **GPT-6 Sol** as the stronger model for complex coding and agentic workflows;
- **GPT-6 Astra** as the most capable model for the hardest end-to-end work.

This does **not** create a required Luna → Sol → Astra staircase. It gives the router overlapping executor options whose best use depends on task geometry, reasoning effort, surface, correction cost and available resources.

The core semantic tiers remain:

`efficient | balanced | strong | frontier`

A named model can span more than one semantic tier. A semantic tier does not require a dedicated named model.

## 2. GPT-6.1 Sol update — 2026-09-29

OpenAI introduced **GPT-6.1 Sol** on 2026-09-29. Current official guidance describes it as delivering capabilities comparable to GPT-6 Astra and as **near-Astra across coding, computer use and professional work**. Astra remains the recommended option for the hardest scientific research.

GPT-6.1 Sol is rolling out in **ChatGPT Work and Codex** and is not an ordinary Chat model. Availability remains plan-, workspace- and rollout-dependent.

For the OpenAI API **Standard / short-context** text-token regime, the current GPT-6.1 Sol model page and pricing table list:

| Model | Input | Cached input | Output |
|---|---:|---:|---:|
| GPT-6.1 Sol | $2.00 | $0.10 | $10.00 |
| GPT-6 Astra | $10.00 | $1.00 | $50.00 |

Within that API pricing regime, GPT-6.1 Sol is therefore **5× cheaper on uncached input and output** and **10× cheaper on cached input** than Astra. This ratio is a dated API-pricing fact, not a ChatGPT Work/Codex allowance conversion, credit-rate claim or proof that every product run consumes exactly one fifth as much plan usage.

### Maximum Token Economy and Plus Economy frontier preference — 2026-10-26 rebase

**Activation:** `Maximum Token Economy` remains an explicit **opt-in public Execution Profile**. `Plus Economy` means that economic preference *within a verified/selected Plus-plan run*; **Plus entitlement alone does not silently opt the user in**. This is a calibrated profile preference, **not a universal model tier**, not the default in balanced/quality profiles, and not a promise of computer-use tools, child-model controls or fixed Work credits.

**Frontier-default rule, exclusively in these economic/Plus profile contexts:** when the task is genuinely frontier-shaped, **GPT-6.1 Terra is the first model to test or select at an appropriate effort** if it is exposed on the required Work/Codex surface and a bounded capability, behavioral-fit and commitment-risk check predicts acceptable results. `frontier` describes the *workload requirement*, **not a claim Terra has the highest frontier capability**. Do not lower task acceptance, omit necessary review or send a high-risk irreducible decision to Terra merely to obey the preset.

**Preference by work geometry, not a universal staircase:**

1. Keep **GPT-6 Luna** for verifiable focused/bulk work when sufficient. Its API input/output unit prices are much lower than Terra's; never promote routine Luna work to Terra just because the Plus profile has a frontier default.
2. Within **frontier-shaped work** under the economic Plus profile, **try Terra 6.1 first** at medium effort when uncertainty and harness allow; use a representative micro-probe when a bad architectural/creative/legal/technical commitment could cause replay. Terra is an efficient *candidate*, not a demonstrated equal substitute for Sol or Astra on every workload.
3. **Route straight to GPT-6.1 Sol** where the task has a known stronger-than-Terra floor: large, ambiguous refactors, demanding multi-domain inference, architecture that evolves during execution, hard coding or irreducible decision authority. A prior reliable same-task comparison or intolerable retry cost can justify Sol without a sacrificial Terra run.
4. **Route to Astra** where evidence or explicit user preference warrants its hardest-work capability, aesthetic or architectural leadership, scientific judgment, deep review, or end-to-end execution. Astra is not restricted to a tiny burst and is never blocked by an economy preset when acceptance risk requires it.
5. **Escalate on accepted-output economics**: compare expected retries, elapsed time, tool churn, source reload, human review and quality failure, *not* just model API token sticker prices. A targeted Sol/Astra judgment may be cheaper than repeated unsuccessful Terra attempts. Failures caused by access, source, permissions, specification or harness must be repaired rather than classified as model intelligence.
6. **Preserve control-root continuity** and use real compatible child workers where supported; neither the Plus label nor model announcement grants automatic subagent routing or UI switches.

**Effort gate:** medium is the starting *probe setting*, not a rigid default for every request; low may outperform it economically on simple tasks, high/max only with verified acceptance gain. Max-effort Terra can narrow the cost advantage through token verbosity; do not assume API 50% unit price implies 50% cheaper accepted tasks or Work credits. The current official Plus usage guidance does not provide a Terra per-five-hour numeric message band; **do not invent one**.

**Baseline exceptions:** outside the opt-in economic profile, preserve the ordinary AOP routing and Astra strategy plurality. The older 2026-09-29 Sol-first economy rule is superseded **only for the explicitly chosen economic/Plus frontier default**; Sol remains a strong executor and a justified immediate escalation when Terra cannot satisfy the task.

**Sources and provenance:** [OpenAI Terra release, 2026-10-26](https://openai.com/index/introducing-gpt-6-1-terra/); [Artificial Analysis Terra release](https://artificialanalysis.ai/models/releases/gpt-6-1-terra); [Work/Codex usage guidance](https://help.openai.com/en/articles/20001516-managing-usage-with-gpt-6-astra-in-work-and-codex). [Terra adapter](ADAPTIVE_ORCHESTRATION_GPT6_TERRA_ADAPTER.md) owns the detailed dated calibration. Provider benchmarks and user-shared Reddit reactions are different evidentiary classes.

### GPT-6 Sol behavioral-fit field signal — 2026-09-29 review

The community material that triggered this calibration concerns the **original GPT-6 Sol**, not GPT-6.1 Sol. Its useful contribution is therefore a field signal about workload fit, not evidence about GPT-6.1 behavior.

Do **not** transfer those observations forward to GPT-6.1 Sol. GPT-6.1 is a distinct dated model update. OpenAI's 2026-09-29 system-card addendum evaluates GPT-6 Sol and GPT-6.1 Sol separately, and current official guidance continues to recommend comparing models on representative tasks rather than assuming behavior from family name or benchmark rank.

The stable routing consequence is model-neutral: use the **Behavioral Fit Gate** when style, source fidelity, tool restraint, initiative, role consistency or verification behavior is load-bearing. A bounded representative micro-probe is preferable to a full sacrificial run when behavior is uncertain and drift would be costly.

A useful behavior contract can state, subject to higher-priority safety/evidence requirements:

- transform supplied material rather than relitigating it when the task is transformation;
- preserve supplied facts and source boundaries unless verification is requested or required;
- do not browse, source-hunt or broaden tool use merely by habit when the task and governing rules do not call for it;
- preserve the requested voice, role and structural constraints;
- avoid unsolicited meta-commentary or scope expansion.

If the selected model clears the capability floor but repeatedly misses that behavior contract, use `SIDE_ROUTE_MODEL_FOR_FIT` to another available executor with better observed fit. This is not automatic capability escalation. For GPT-6.1 Sol specifically, no negative behavioral conclusion is imported from the original GPT-6 Sol reports; its existing Maximum Token Economy calibration remains governed by current GPT-6.1 evidence and representative workload testing.

Community reactions can justify a probe. They do not establish that GPT-6 Sol is globally worse, that GPT-6.1 Sol inherits the same behavior, or that any model has a permanent style rank.

### Comparative capability and total-outcome calibration — 2026-10-24

**Classification:** dated model evidence and workload-routing inference; not a revision of AOP's stable routing laws, not a model ranking, and not a claim about ChatGPT credits.

**Evidence with comparable configurations.** The OpenAI September 2026 GPT-6.1 Sol release reports parity with Astra on DeepSWE v1.1 at about one-fifth of the cost and an OSWorld 2.0 offline-set gap of 2.1 percentage points at max effort at about one-seventh of the cost per task. It also explicitly keeps Astra ahead on its hardest scientific research evaluation. Independent Artificial Analysis Max-vs-Max measurements report Intelligence Index 52 vs 53 (Sol vs Astra), AutomationBench-AA 65% vs 68%, Terminal-Bench 4.0 56% vs 59%, SciCode 54% vs 56%, GDP.pdf 31% vs 31%, output tokens/task 38k vs 27k, time/task about 706 vs 476 seconds, and mean cost/task $0.72 vs $3.26. Results are snapshot- and harness-dependent; benchmark aggregates do not imply semantic interchangeability on every task.

**Creative coding caution.** Vals AI Vibe Code Bench reports 88.93% for Sol vs 89.59% for Astra with OpenHands, but different mean run times and task costs ($6.23 / 1h15m vs $38.51 / 39m04s). The test supports broad vibe-code competence, **not** controlled parity for photorealistic 3D games, sophisticated animation, aesthetic direction or Unreal/Blender artifact quality. A visually compelling Astra demo is not itself a controlled A/B evaluation against Sol. For such jobs use the same stack, tools, asset/license budget, prompt, time window, acceptance tests, browser/engine QA and screenshot/video inspection before deciding whether an Astra premium buys a meaningful quality or iteration gain.

**Operational choice in Maximum Token Economy (opt-in only):**

1. Probe the *capability floor* and *artifact class*: code correctness, 3D world composition, interaction/gameplay, visual coherence, tool/harness constraints and acceptance quality are separate dimensions. Do not equate headline intelligence with reliable art direction.
2. Prefer Sol 6.1 as a strong root / initial 3D implementation executor when permitted and available; use Luna only for separable, verifiable bulk. Keep the task's existing competent control root.
3. Observe a bounded vertical slice, not just code output: build/run, inspect playability, responsiveness, camera, physics, UI, assets, performance and visual fidelity. Debug tool failures and underspecified requirements before blaming model capability.
4. Apply an **outcome-normalized escalation gate**: compare expected completed-and-accepted cost, latency, reviewer burden, retries/replay and irreversible commitments. The 5× API unit-price difference is not a 5× guaranteed task saving; Sol may emit more tokens and take longer. ChatGPT allowances are governed separately.
5. Move *only the stubborn delta* to Astra if the Sol result misses a material acceptance threshold despite a bounded repair, or when aesthetic/architectural judgment, hard scientific work, high-stakes ambiguity or strong evidence from same-task evaluation favors Astra. Astra may serve as root, co-architect, creative/visual critic, targeted debugger or final integrator; do not force it into a tiny brain-burst role.
6. After Astra's decision or repair, return implementation and regression work to the cheapest sufficient authorized executor, unless continuity/replay cost makes a sustained Astra run more efficient.

**Explicit non-claim:** Sol being able to generate a complex 3D game's code does not prove it can produce every Astra 3D demo with identical creative quality, tools or one-shot reliability. The inverse universal superiority claim is also unsupported.

**Recalibration triggers:** representative same-task A/B tests, new agentic/creative benchmarks, new model revisions or effort settings, substantial price/token/latency shifts, changed Work/Codex surface controls, or observed repeated acceptance failures. Do not refresh public model evidence on each ordinary AOP invocation.

**Public sources:** [OpenAI GPT-6.1 Sol](https://openai.com/index/introducing-gpt-6-1-sol/); [OpenAI GPT-6 model selection](https://developers.openai.com/api/docs/models); [Artificial Analysis Sol Max vs Astra Max](https://artificialanalysis.ai/models/comparisons/gpt-6-1-sol-vs-gpt-6-astra); [Vals AI Vibe Code Bench](https://www.vals.ai/benchmarks/vibe-code).

## 2A. Official GPT-6 launch facts

As of 2026-09-23 for the original GPT-6 Sol/Luna launch:

- GPT-6 Sol and GPT-6 Luna are available in **ChatGPT Work and Codex** for eligible paid plans, subject to rollout and workspace settings.
- At this September launch they were **not yet ordinary Chat models**. That historical fact was superseded for Chat by the 2026-10-07 rollout below; the menus and harnesses remain distinct.
- API model IDs are `gpt-6-sol` and `gpt-6-luna`.
- Both API models expose reasoning levels from `none` through `max`; the exact reasoning controls shown in ChatGPT depend on plan, workspace and surface.
- Both expose a **1,050,000-token context window** and **128,000 max output tokens** in the API.
- GPT-6 Sol knowledge cutoff: **2026-04-20**.
- GPT-6 Luna knowledge cutoff: **2026-05-18**.
- Standard short-context API pricing is **$2 input / $10 output per 1M tokens for Sol** and **$0.10 input / $0.50 output for Luna**. Cached reads are priced at 10% of uncached input.
- API prompts above **272K input tokens** use long-context pricing for the full request.
- OpenAI reports improved prompt caching for GPT-6 and says changing reasoning effort or tool availability can preserve earlier cached context.
- OpenAI reports improved alignment versus GPT-5.6 counterparts, including fewer misleading coding-work claims.

These are dated product facts. They do not become permanent routing law.

## 2B. GPT-6 in Chat — October 7, 2026 deployment correction

OpenAI launched GPT-6 in the Chat tab on **2026-10-07** for Plus, Pro, Business and Enterprise, expanding rollout to Free and Go from **2026-10-08**, subject to account/workspace rollout and controls. **GPT-6 Sol powers Chat for eligible paid tiers; GPT-6 Luna powers Chat for Free/Go.** The ordinary Chat selector presents **GPT-6**, not separately selectable Sol/Luna model IDs. For paid tiers, GPT-6 Sol powers available Instant-to-Extra-High reasoning levels; Pro is a distinct Astra-backed tier. Do not infer a universal list of effort controls from family names or subscription hints.

**Crucial model-variant boundary:** OpenAI identifies the October Chat GPT-6 Sol/Luna releases as **conversation-tuned versions distinct from the September Sol/Luna models still powering Work and Codex**. September executor benchmarks, API prices, context-window specifications, observed agentic behavior and child-model configuration must not automatically be attributed to the October Chat variants. Nor does Intelligent UI or an answer that streams while thinking establish filesystem/computer control, subagent spawning or delegated execution in Chat.

Routing effect: **Chat can now be the competent GPT-6 Sol/Luna control root and finish tasks entirely in Chat** when its observed tools, scope and verification are sufficient. Prefer the current competent root; move to Work/Codex only for a material harness, locality, sustained-execution, permission, delegation or verification requirement. Sol/Luna describe model families and task-fit hypotheses, not a forced surface migration or permission to claim invisible model switching. GPT-6.1 Sol remains a separate Work/Codex option where exposed, not a Chat menu synonym.

Sources: [OpenAI, GPT-6 and Intelligent UI for everyone (2026-10-07)](https://openai.com/index/gpt-6-for-everyone/); [OpenAI, October GPT-6 Sol/Luna system-card update](https://deploymentsafety.openai.com/gpt-6-october/model-data-and-training); [OpenAI, GPT-6 and other models in ChatGPT](https://help.openai.com/en/articles/20001354-gpt-6-and-other-models-in-chatgpt).

## 3. Benchmark signal, not benchmark government

Useful launch signals include:

- GPT-6 Sol xhigh: **33.2% on AutomationBench** in OpenAI's reported comparison.
- GPT-6 Sol max: **68.8% on DeepSWE 1.1**.
- GPT-6 Luna max: **66.6% on DeepSWE 1.1**.
- GPT-6 Sol xhigh: **60.5% on OSWorld 2.0 offline**.
- OpenAI reports that Luna at higher effort substantially improves factuality and can match GPT-5.6 Sol on its internal factuality evaluation at much lower API cost.

These results justify a wider Luna capability envelope and a stronger Sol execution role. They do not prove universal superiority, predict one user's Work allowance consumption or authorize routing by benchmark prestige.

## 4. The practical split

### GPT-6 Luna — default bulk executor

Prefer Luna when the task is focused, bounded or repeatable and the main value comes from sustained throughput rather than unusually hard judgment.

Strong Luna-shaped work includes:

- extraction, classification, transformation and synthesis over many items;
- bounded research and document production with clear acceptance criteria;
- repetitive connector/tool workflows;
- routine verification and readback;
- well-specified multi-step execution;
- narrow or moderately complex code changes with a known target;
- high-volume artifact work;
- implementation after a harder architecture decision has already been made.

Luna remains a strong default for bounded or high-volume artifact production once the artifact's commitment-bearing architecture is sufficiently resolved. Volume alone does not make Luna the right executor to close an open-ended art-direction, information-architecture or representation choice.

Luna may use higher reasoning effort when the task is still Luna-shaped but requires more care. Do not treat `Luna` as synonymous with low reasoning.

### GPT-6 Sol — strong executor / co-architect

Prefer Sol when reasoning is load-bearing *inside* execution rather than merely before it.

Strong Sol-shaped work includes:

- complex coding or repo-wide engineering;
- difficult debugging with competing hypotheses;
- agentic workflows with branching state and error recovery;
- architecture that must be invented while implementation proceeds;
- multi-application professional workflows where judgment changes the next action;
- ambiguous source reconciliation with material consequences;
- migrations or refactors where a wrong local choice creates expensive downstream correction;
- high-consequence final review where Luna's result is plausible but not sufficiently trustworthy.

Sol may also receive a bounded commitment-bearing decision when materially different directions remain plausible and a wrong closure would drive substantial downstream rework. Sol need not own the later bulk implementation when a cheaper sufficient executor can carry it after the choice is settled.

When the implementation is Luna-shaped but one upstream commitment carries high leverage, keep Luna as root or implementer where appropriate and side-route or up-route only that decision when the live gate justifies it. This is a conditional route, not a permanent Luna-to-Sol hierarchy or a claim that Sol is always the better design arbiter.

Sol is not automatically the default because a task is important. It is selected when the **irreducible execution geometry** is strong.

## Surface-neutral topology calibration

Under Adaptive Orchestration 6.1, the Sol/Luna pattern is independent from a mandatory Chat return loop. A Sol root in Work or Codex may delegate bounded volume to Luna, converge the result and perform Control-Root Postflight on the same surface when the harness supports it. Chat → Work/Codex → Chat remains valid when the named Adaptive Orchestration Loop Profile is active or the user prefers Chat continuity.

A model change, child spawn and surface transition are separate events. Prefer internal child routing first; preserve the current competent root when possible; request a human-visible surface switch only when the required harness, permission, capability floor or verification path cannot be satisfied internally.

## 5. The overlap zone: balanced is not a missing product

**October 26 correction:** GPT-6.1 Terra now exists in Work/Codex and is governed by the separate [Terra Strategy Adapter](ADAPTIVE_ORCHESTRATION_GPT6_TERRA_ADAPTER.md). A balanced route may consider Terra when observed capability and task acceptance justify it; the model name does not force a universal middle tier.

A `balanced` Adaptive Orchestration route can legitimately compile to, for example:

- **Luna + high/max effort** when the task is bounded but cognitively dense;
- **Sol + low/medium effort** when the task benefits from stronger base capability but does not require sustained high reasoning;
- another observed model/effort combination that clears the capability floor more efficiently.

The router chooses a **capability result**, not a product-label symmetry.

## 6. Effort-before-tier, without sacrificial failure

The stable preference remains: if the model is appropriate and the insufficiency is reasoning depth, adjust reasoning effort before escalating the tier.

But this is not a ritual.

Do **not** force Luna to fail first when the task geometry already makes a strong-tier executor the lower-total-work route. Direct Sol routing is justified when:

1. the task is intrinsically complex/agentic rather than merely long;
2. reasoning and execution are tightly coupled;
3. the likely cost of a plausible-but-wrong intermediate result is high;
4. correction would require replaying substantial tool work or repository state;
5. Sol is available and Budget Survivability passes.

The optimization target is **verified useful delta per total work**, not the cheapest first turn.

## 7. Surface law

Model choice does not choose the surface.

### Work

Prefer Work when the sovereign object is connected research, multi-file knowledge production, document/artifact production, browser/computer workflows or sustained connector-mediated execution.

- Luna is the default candidate for bounded high-volume Work.
- Sol becomes the default candidate when the Work trajectory itself requires strong ongoing judgment, branching recovery or co-architecture.
- When Work exposes subagent delegation, prefer Sol-as-root with Luna workers for independent bulk before asking the user to change the whole Work model.

### Codex

Prefer Codex when the sovereign object is a repository, codebase, tests, terminal state, build, runtime, migration or deployment-oriented engineering state.

- Luna is a strong default for well-specified implementation, repetitive fixes, tests and bounded refactors.
- Sol is preferred for difficult debugging, broad refactors, architecture-bearing implementation and complex agentic coding.
- Codex exposes the strongest current control surface for heterogeneous subagents: global child defaults, per-spawn overrides and custom agent files can separate root and child models when the active release exposes those controls.

### Chat

Since the October 2026 rollout, Chat may use **GPT-6 Sol** for eligible paid users or **GPT-6 Luna** for Free/Go under the **GPT-6** Chat label, where actually exposed. Chat can own reasoning, convergence and Control-Root Postflight without a Work/Codex handoff when its available tools and verification satisfy the task. The October conversation variants are not the September Work/Codex executor variants; preserve the surface's actual tool, delegation and model-control limits. Never pretend to select a model or spawn workers when the UI/runtime cannot do so.

## 8. Heterogeneous subagent topology

Current official subagent guidance supports a root/child split rather than requiring every child to inherit the root model.

### Default strong-root pattern

For most demanding Codex work, start with Sol as the root and delegate narrow or high-volume branches to Luna:

```text
Sol root
├─ Luna / high → exploration, search, evidence gathering
├─ Luna / high → tests, logs, repetitive verification
├─ Luna / high → documentation or mechanical implementation
└─ Sol root     → convergence, hard debugging, architecture, final validation
```

This is the preferred default when the root needs strong planning but most child work is bounded.

### Frontier-root pattern

When Astra is justified as the root, do not automatically duplicate Astra across every branch. Prefer:

```text
Astra root
├─ Luna workers → volume, scans, extraction, routine tool work
├─ Sol specialists → ambiguous or architecture-bearing branches
└─ Astra root → decomposition, arbitration, exceptional judgment, final synthesis
```

The Astra adapter owns the frontier-specific geometry. This adapter owns the Luna/Sol child roles.

### Inheritance and override

If no child model or child reasoning effort is configured, current subagent behavior may inherit the parent model and effort. Heterogeneous delegation therefore requires an explicit child policy when cost separation matters.

In current Codex configuration, the `[agents]` block can set `default_subagent_model`, `default_subagent_reasoning_effort` and a concurrency ceiling. Custom agent files can pin their own model and effort. Explicit spawn settings, configured defaults and parent inheritance form a precedence chain; verify the active client's behavior instead of assuming that a configuration was honored.

For ChatGPT Work, prompt for the intended delegation topology and child model/effort when the UI/runtime exposes that capability. Work is hosted and does not expose the same local configuration surface as Codex.

### Fresh-child context preference

When a heterogeneous child only needs a bounded task packet, prefer a fresh or deliberately partial child context rather than cloning the entire parent history. This reduces context duplication and preserves the economic point of using a cheaper worker.

Current Codex Multi-Agent V2 guidance also warns that full-history forks inherit the parent model and reasoning effort and do not accept model/effort overrides. Treat this as dated implementation calibration, not permanent protocol law.

### Fanout law

The point is not “more agents.” The point is **more useful work per expensive root token**.

- use Luna workers for read-heavy, independent and verifiable units;
- promote only failed or genuinely difficult branches to Sol;
- keep parallel write ownership disjoint or serialize mutation;
- cap fanout and depth;
- return summaries/evidence rather than raw intermediate noise;
- compare total work to accepted state, not per-call sticker price.

## 9. Context law

The 1.05M context window is a **capacity ceiling, not a context target**.

Keep Context Diet active:

- send the smallest context that preserves the decision;
- prefer source references and targeted retrieval over dumping entire corpora;
- keep authority and freshness metadata with transported sources;
- preserve reusable stable prefixes when API caching matters;
- split or distill when large context creates distraction or makes correction expensive.

The API's >272K long-context price step is useful evidence that very large prompts have real economics, but it is **API pricing**, not a Work/Codex allowance formula.

## 10. Economics boundary

### 10.1 Standard short-context API price vector

For the dated 2026-09-23 calibration, use the official **Standard / short-context** text-token rates per 1M tokens:

| Model | Input | Output |
|---|---:|---:|
| GPT-6 Luna | $0.10 | $0.50 |
| GPT-5.6 Luna | $0.20 | $1.20 |
| GPT-6 Sol | $2.00 | $10.00 |
| GPT-5.6 Sol | $4.00 | $20.00 |
| GPT-6 Astra | $10.00 | $50.00 |

Long-context, Batch, Flex, Fast, regional-processing and tool-call prices are separate regimes and must be recalculated from current official pricing rather than inferred from this table.

### 10.2 Mixed-workload cost equation

Let:

- `I` = uncached input tokens in millions;
- `O` = output tokens in millions;
- `pᵢ(m)` = standard short-context input price of model `m`;
- `pₒ(m)` = standard short-context output price of model `m`.

Then the text-token API cost proxy is:

`C(m; I, O) = pᵢ(m)·I + pₒ(m)·O`

This proxy intentionally excludes cached-input effects, cache writes, tools, regional uplifts and non-Standard service tiers unless those terms are explicitly added.

For two models `A` and `B`, define:

`R(A:B | I,O) = C(A;I,O) / C(B;I,O)`

If `R = 20`, model A costs 20× model B for that workload. The savings from moving from A to B are:

`Savings(A→B) = 1 - C(B;I,O)/C(A;I,O)`

### 10.3 Constant-ratio relations

Some pairs have proportional input/output prices, so their ratio is independent of the input/output mix:

- `R(GPT-6 Sol : GPT-6 Luna) = 20×`
- `R(GPT-6 Astra : GPT-6 Sol) = 5×`
- `R(GPT-6 Astra : GPT-6 Luna) = 100×`
- `R(GPT-5.6 Sol : GPT-6 Luna) = 40×`
- `R(GPT-6 Astra : GPT-5.6 Sol) = 2.5×`
- `R(GPT-5.6 Sol : GPT-6 Sol) = 2×`

Equivalent savings readings:

- GPT-6 Luna is **95% cheaper** than GPT-6 Sol;
- GPT-6 Sol is **80% cheaper** than GPT-6 Astra;
- GPT-6 Luna is **99% cheaper** than GPT-6 Astra;
- GPT-6 Luna is **97.5% cheaper** than GPT-5.6 Sol;
- GPT-6 Sol is **50% cheaper** than GPT-5.6 Sol.

### 10.4 Generation-over-generation Luna equation

GPT-5.6 Luna → GPT-6 Luna is not perfectly proportional because output fell more than input:

`R(6 Luna : 5.6 Luna | I,O) = (0.10I + 0.50O) / (0.20I + 1.20O)`

Therefore:

- input-only: GPT-6 Luna costs **50%** of GPT-5.6 Luna → **50% cheaper**;
- output-only: GPT-6 Luna costs **41.67%** of GPT-5.6 Luna → **58.33% cheaper**;
- any mixed workload falls between those endpoints.

By contrast:

`R(6 Sol : 5.6 Sol) = 0.5`

so GPT-6 Sol is exactly **50% cheaper** than GPT-5.6 Sol for any uncached text-token input/output mix under this price regime.

### 10.5 Cross-generation ratios that depend on workload mix

For GPT-6 Sol versus GPT-5.6 Luna:

`R(6 Sol : 5.6 Luna | I,O) = (2I + 10O) / (0.20I + 1.20O)`

This ranges from **10×** for input-only work to **8.33×** for output-only work.

For GPT-6 Astra versus GPT-5.6 Luna:

`R(6 Astra : 5.6 Luna | I,O) = (10I + 50O) / (0.20I + 1.20O)`

This ranges from **50×** for input-only work to **41.67×** for output-only work.

For GPT-5.6 Sol versus GPT-5.6 Luna:

`R(5.6 Sol : 5.6 Luna | I,O) = (4I + 20O) / (0.20I + 1.20O)`

This ranges from **20×** for input-only work to **16.67×** for output-only work.

### 10.6 Luna-normalized price index

Using GPT-6 Luna as `1.0`:

| Model | Input-price index | Output-price index |
|---|---:|---:|
| GPT-6 Luna | 1× | 1× |
| GPT-5.6 Luna | 2× | 2.4× |
| GPT-6 Sol | 20× | 20× |
| GPT-5.6 Sol | 40× | 40× |
| GPT-6 Astra | 100× | 100× |

This makes the current economic geometry explicit:

`GPT-6 Luna = 1 → GPT-6 Sol = 20 → GPT-6 Astra = 100`

with GPT-5.6 Luna and Sol sitting at `2/2.4` and `40` respectively.

### 10.7 Routing interpretation

The large price gap does **not** create a compulsory routing staircase.

Use the equations to estimate **API cost pressure**, then combine them with capability floor, correction/retry cost and task geometry:

- prefer Luna for bulk where it clears the floor;
- prefer Sol when stronger reasoning inside execution is expected to reduce replay, correction or failure enough to justify the premium;
- use Astra only under the canonical frontier gate and its own adapter when available;
- do not force Luna to fail merely because it is cheaper;
- do not promote to Sol or Astra merely because the task is important.

The optimization target is not minimum first-turn cost:

`Preferred route = argmin(expected total cost to verified acceptance)`

where expected total cost includes the probability-weighted cost of retries, correction, repeated tool work, context reconstruction and higher-tier bursts when material.

### 10.8 ChatGPT allowance firewall

These equations are **API price equations only**.

They must **not** be copied into ChatGPT Work/Codex allowance math. ChatGPT usage can depend on model, task, reasoning effort, tool work, plan and workspace policy. Unless the product exposes a reliable run-level conversion, never infer rules such as:

- `1 Sol Work run = 20 Luna Work runs`;
- `1 Astra run = 5 Sol runs`;
- allowance percentage consumed = API token-cost ratio.

The token-price ratios can inform qualitative economic intuition; they cannot manufacture product telemetry.

## 11. Default routing matrix

| Workload geometry | Preferred starting route | Escalate when |
|---|---|---|
| Focused extraction / classification / transformation | Luna · low/medium, or Luna workers under a stronger root | reasoning, not source/tool failure, remains insufficient |
| Bounded multi-step artifact work | Luna · medium/high | ambiguity or correction cost becomes load-bearing |
| Dense but bounded judgment with clear inputs | Luna · high/max or Sol · low/medium | choose by total-work efficiency |
| Narrow code patch / tests / mechanical refactor | Codex + Luna · medium/high | debugging/architecture becomes genuinely hard |
| Complex repo-wide engineering / hard debugging | Codex + Sol root · medium/high, Luna workers for bounded branches | irreducible frontier judgment remains |
| Long connector/computer workflow with stable decisions | Work + Luna · medium/high | trajectory branches require repeated strong judgment |
| Multi-app agentic workflow with uncertain recovery | Work + Sol root, Luna workers when independent bulk exists | frontier cognition materially changes outcome |
| High-consequence review / architecture | Sol · xhigh/max | Astra burst/full route passes canonical frontier gate |

Reasoning labels are recommendations only when the current surface actually exposes them.

## 12. Failure and re-entry

When Luna underperforms:

1. classify the failure;
2. repair source, authority, tool, context or specification failures first;
3. if the failure is cognitive and Luna is still the right executor geometry, raise effort when available;
4. if a named irreducible reasoning delta remains, route that delta or the execution to Sol;
5. return to the lowest sufficient tier after the hard delta is resolved.

When Sol underperforms:

- do not automatically expand context or autonomy;
- isolate the remaining hard delta;
- use Astra only if available, justified by the frontier gate and permitted by the active Astra adapter/user profile;
- preserve tests, receipts and Control-Root Postflight.

## 13. Locality and migration note

This adapter describes the GPT-6 family **as observed at the dated release state**. The October 2026 Chat rollout alters the availability and variant boundary, not the canonical routing architecture. Future usage pools, model releases, repricing and effort-control changes still require a fresh probe.

A future model release should update or supersede this adapter rather than spraying model names through the stable core.

## 14. Official sources

- OpenAI — Introducing GPT-6 Sol and Luna (September Work/Codex release): https://openai.com/index/introducing-gpt-6-sol-and-luna/
- OpenAI — GPT-6 and Intelligent UI for everyone (October Chat release): https://openai.com/index/gpt-6-for-everyone/
- OpenAI — October GPT-6 Sol/Luna deployment safety update: https://deploymentsafety.openai.com/gpt-6-october/model-data-and-training
- OpenAI API — GPT-6 Sol: https://developers.openai.com/api/docs/models/gpt-6-sol
- OpenAI API — GPT-6 Luna: https://developers.openai.com/api/docs/models/gpt-6-luna
- OpenAI API — GPT-6 model guidance: https://developers.openai.com/api/docs/guides/latest-model
- OpenAI API — Model selection: https://developers.openai.com/api/docs/guides/model-selection
- OpenAI API — Pricing: https://developers.openai.com/api/docs/pricing
- OpenAI Help — ChatGPT Release Notes: https://help.openai.com/en/articles/6825453-chatgpt-release-notes
- OpenAI — Subagents: https://learn.chatgpt.com/docs/agent-configuration/subagents
- OpenAI Codex source — current `[agents]` configuration fields: https://github.com/openai/codex/blob/main/codex-rs/config/src/config_toml.rs

## Final law

> **Luna buys throughput; Sol buys stronger judgment inside execution. Keep Sol at the bottleneck, delegate bounded bulk to Luna when the harness can do so, and promote only the difficult branch. Capability does not guarantee behavioral fit: probe representative work when behavior is load-bearing, and side-route before up-routing when the mismatch is behavioral rather than cognitive. Never turn API price ratios into imaginary Work allowance mathematics. The sovereign object chooses the surface; the delegation topology chooses where each unit of cognition is spent.**

<!-- MOON-SOURCE-PUBLIC-STAMP -->

---

> 🌙 **Moon Source** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Source/blob/main/LICENSING.md) · [Use & attribution](https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md) · [Full source (.zip)](https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip) · Questions, suggestions, or proposals? Feel free to contact me at [LuaHelenaMMC@gmail.com](mailto:LuaHelenaMMC@gmail.com).