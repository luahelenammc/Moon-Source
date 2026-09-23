# GPT-6 Sol / Luna Strategy Adapter — Chat–Work

*Dated executor calibration for the GPT-6 family*

## Meta

- **status:** current subordinate adapter
- **adapter version:** 1.0
- **as of:** 2026-09-23
- **governing capability:** [Chat–Work Routing Protocol](../CHAT_WORK_ROUTING_PROTOCOL_V4.md)
- **scope:** GPT-6 Sol and GPT-6 Luna routing in Work, Codex and API-shaped reasoning about executor choice
- **authority:** subordinate; the canonical Chat–Work body wins on conflict
- **volatility:** high; availability, model menus, reasoning controls, plan/workspace exposure and usage economics must be rechecked
- **product boundary:** not OpenAI policy, not a benchmark ranking system and not a guarantee about ChatGPT allowance consumption
- **creator:** Lua Helena Moon Martins Cardoso (Moon)
- **AI-assisted coauthorial development:** Áurion
- **license:** CC BY 4.0 under the repository licensing terms

## 1. Why this adapter exists

GPT-6 changes the practical executor geometry without changing Chat–Work's stable laws.

At launch, OpenAI positions:

- **GPT-6 Luna** as the efficient model for focused, high-volume work;
- **GPT-6 Sol** as the stronger model for complex coding and agentic workflows;
- **GPT-6 Astra** as the most capable model for the hardest end-to-end work.

This does **not** create a required Luna → Sol → Astra staircase. It gives the router overlapping executor options whose best use depends on task geometry, reasoning effort, surface, correction cost and available resources.

The core semantic tiers remain:

`efficient | balanced | strong | frontier`

A named model can span more than one semantic tier. A semantic tier does not require a dedicated named model.

## 2. Official launch facts

As of 2026-09-23:

- GPT-6 Sol and GPT-6 Luna are available in **ChatGPT Work and Codex** for eligible paid plans, subject to rollout and workspace settings.
- They are **not yet ordinary Chat models**. Chat and Work/Codex model menus are separate surfaces.
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

Sol is not automatically the default because a task is important. It is selected when the **irreducible execution geometry** is strong.

## 5. The overlap zone: balanced is not a missing product

GPT-6 currently has no named Terra model in the released family. Do not manufacture one.

A `balanced` Chat–Work route can legitimately compile to, for example:

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

### Codex

Prefer Codex when the sovereign object is a repository, codebase, tests, terminal state, build, runtime, migration or deployment-oriented engineering state.

- Luna is a strong default for well-specified implementation, repetitive fixes, tests and bounded refactors.
- Sol is preferred for difficult debugging, broad refactors, architecture-bearing implementation and complex agentic coding.

### Chat

At launch, GPT-6 Sol/Luna are not exposed as ordinary Chat models. Chat remains the controller/postflight surface using the best suitable **Chat-available** model. Never report a GPT-6 Sol/Luna Chat switch unless the product actually exposes it.

## 8. Context law

The 1.05M context window is a **capacity ceiling, not a context target**.

Keep Context Diet active:

- send the smallest context that preserves the decision;
- prefer source references and targeted retrieval over dumping entire corpora;
- keep authority and freshness metadata with transported sources;
- preserve reusable stable prefixes when API caching matters;
- split or distill when large context creates distraction or makes correction expensive.

The API's >272K long-context price step is useful evidence that very large prompts have real economics, but it is **API pricing**, not a Work/Codex allowance formula.

## 9. Economics boundary

At standard short-context API rates, Sol is 20× Luna per input token and 20× Luna per output token.

That ratio is useful for API deployment planning. It must **not** be copied into ChatGPT Work/Codex allowance math.

ChatGPT usage can depend on model, task, reasoning effort, tool work, plan and workspace policy. Unless the product exposes a reliable run-level usage measure, Chat–Work should reason qualitatively:

- use Luna for bulk where it clears the floor;
- use Sol where stronger reasoning reduces total correction/retry work;
- use Astra only under the canonical frontier gate and its own adapter when available;
- never claim a fixed “one Sol = N Luna” rule for Work/Codex.

## 10. Default routing matrix

| Workload geometry | Preferred starting route | Escalate when |
|---|---|---|
| Focused extraction / classification / transformation | Luna · low/medium | reasoning, not source/tool failure, remains insufficient |
| Bounded multi-step artifact work | Luna · medium/high | ambiguity or correction cost becomes load-bearing |
| Dense but bounded judgment with clear inputs | Luna · high/max or Sol · low/medium | choose by total-work efficiency |
| Narrow code patch / tests / mechanical refactor | Codex + Luna · medium/high | debugging/architecture becomes genuinely hard |
| Complex repo-wide engineering / hard debugging | Codex + Sol · high/xhigh | irreducible frontier judgment remains |
| Long connector/computer workflow with stable decisions | Work + Luna · medium/high | trajectory branches require repeated strong judgment |
| Multi-app agentic workflow with uncertain recovery | Work + Sol · high/xhigh | frontier cognition materially changes outcome |
| High-consequence review / architecture | Sol · xhigh/max | Astra burst/full route passes canonical frontier gate |

Reasoning labels are recommendations only when the current surface actually exposes them.

## 11. Failure and re-entry

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
- preserve tests, receipts and Chat Postflight.

## 12. Locality and migration note

This adapter describes the GPT-6 family **as observed at the dated release state**. Future Chat availability, changed usage pools, new family members, repricing or changed effort controls can alter the calibration without changing the canonical Chat–Work architecture.

A future model release should update or supersede this adapter rather than spraying model names through the stable core.

## 13. Official sources

- OpenAI — Introducing GPT-6 Sol and Luna: https://openai.com/index/introducing-gpt-6-sol-and-luna/
- OpenAI API — GPT-6 Sol: https://developers.openai.com/api/docs/models/gpt-6-sol
- OpenAI API — GPT-6 Luna: https://developers.openai.com/api/docs/models/gpt-6-luna
- OpenAI API — GPT-6 model guidance: https://developers.openai.com/api/docs/guides/latest-model
- OpenAI API — Pricing: https://developers.openai.com/api/docs/pricing
- OpenAI Help — ChatGPT Release Notes: https://help.openai.com/en/articles/6825453-chatgpt-release-notes

## Final law

> **Luna buys throughput; Sol buys stronger judgment inside execution. Raise effort when effort is the missing ingredient, route directly to Sol when strong reasoning is already load-bearing, and never turn API price ratios into imaginary Work allowance mathematics. The model is an executor choice; the sovereign object still chooses the surface.**

<!-- MOON-SOURCE-PUBLIC-STAMP -->

---

> 🌙 **Moon Source** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Source/blob/main/LICENSING.md) · [Use & attribution](https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md) · [Full source (.zip)](https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip) · Questions, suggestions, or proposals? Feel free to contact me at [LuaHelenaMMC@gmail.com](mailto:LuaHelenaMMC@gmail.com).
