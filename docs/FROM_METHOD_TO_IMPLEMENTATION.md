# From a context problem to an implementation

**[Ler em português brasileiro](FROM_METHOD_TO_IMPLEMENTATION.pt-BR.md)**

What happens between "I have a context method" and "this works for someone else"? This page provides a short, testable route through that question. It does not introduce a new Moon Source capability.

## 1. Where the method came from

Moon Source grew out of the creator's own sustained AI workflows across more than 30 personal and professional project workspaces. Long-running work exposed practical failures: having to repeat decisions, retrieving outdated material, or mixing information from different projects. The method evolved through dogfooding: identify a failure, specify ownership and update rules, try them in daily work, inspect the result, and revise. AI assisted development and review under the creator's architectural direction.

**This is actual internal use, not 30 customers, independent deployments, or measured third-party outcomes.** The [canonical public architecture](../ARCHITECTURE.md) describes the method; its [evidence registry](EXISTING_IMPLEMENTATIONS.md) states what can be inspected.

## 2. See what is executable today

Start with the separate [Governed Knowledge Routing Demonstrator](https://www.luahelena.com.br/ia/demos/governed-knowledge/) ([source and tests](https://github.com/luahelenammc/LUAHELENA/tree/main/ia/demos/governed-knowledge/)). It is a small deterministic website using fictional policy records. **It is not an LLM assistant and is maintained in a different repository.**

Try these situations:

| Ask the demo | What to inspect |
|---|---|
| Hotel reimbursement | Current higher-authority policy beats an outdated version and a disagreeing FAQ. |
| Privacy policy | An overdue review prevents the old text from being represented as current. |
| Workplace accommodation | A source can specify the human owner while leaving the individual decision to that person. |
| Remote work | Two active sources of equal authority disagree; the engine escalates rather than guessing. |
| Medical leave | No registered topic supports an answer, so the engine says so. |

Open the **decision trace** and the fictional source register. Check which records matched, which were excluded, which authority was considered, and where escalation occurred. This is evidence of bounded source-routing behavior only. It does not prove that language-model context is universally solved, that a production product exists, or that a client used Moon Source.

## 3. Convert the method into a buildable brief

Before proposing a chatbot, map the actual workflow with a domain owner. Keep the first brief small enough that a separate implementation team can challenge it.

| Field | Write down |
|---|---|
| Problem and people | Who encounters the failure, where it occurs, how it is recognized, and who can validate it. |
| Source and state | Record owners, source locators, currentness rules, version/supersession, and the smallest permissible stored context. |
| Decision boundary | What the system may answer or do, what it must decline, and which human must decide or review. |
| Implementation owner | Required identity/access, integrations, runtime/model (if any), security, maintenance, and the team responsible for building them. |
| Acceptance test | An invented-input scenario with expected output, provenance, conflict handling, escalation and a reproducible readback. |
| Pilot conditions | Consent/privacy approvals, baseline, evaluation measures, right to publish and attribution, if a real pilot is later authorized. |

A possible path is `understand workflow → specify governed context → run synthetic acceptance test → build authorized integration → human review → bounded pilot → evaluate`. A diagram of this path is not evidence that an integration or pilot exists.

## 4. What an honest project conversation sounds like

**How were these methods developed?** From repeated practical failures in long-running internal AI work, then iterative specification, use, critique and public documentation.

**Have you applied them?** Yes, to the creator's own work. Public methods and bounded technical demonstrations are inspectable. No external Moon Source deployment or independently validated client case is established here.

**Can you build my assistant?** The architecture can inform source/state requirements, workflow discovery, human decision boundaries and tests. Whether an assistant is appropriate, and who builds its interface, integrations, operations and security, must be established with the project team. Domain-sensitive use demands its own consent and governance decisions.

The [Moon Source architecture](../ARCHITECTURE.md), [For AI Builders](FOR_AI_BUILDERS.md), [Existing Implementations](EXISTING_IMPLEMENTATIONS.md) and [Evidence and Claims](../EVIDENCE_AND_CLAIMS.md) remain authoritative for their respective facts and boundaries. This guide is a public reading route, not another source of authority.

<!-- MOON-SOURCE-PUBLIC-STAMP -->

---

> 🌙 **Moon Source** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Source/blob/main/LICENSING.md) · [Use & attribution](https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md) · [Full source (.zip)](https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip) · Questions, suggestions, or proposals? Feel free to contact me at [LuaHelenaMMC@gmail.com](mailto:LuaHelenaMMC@gmail.com).
