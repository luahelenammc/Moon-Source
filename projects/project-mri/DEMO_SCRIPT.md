# Project MRI demo script — 2:30 target

Audience: an InfraJam judge who has never seen Moon Source or MSL.

## 0:00–0:20 — Frame the problem

Say:

> AI projects do not only have a retrieval problem. They have an authority problem. An old decision, a copied instruction and a current source can all be retrieved together. MRI shows the conflict before the assistant turns it into an answer.

Click **Start scan**.

## 0:20–0:45 — Show the map

Open **Project map**. Point to the document count, typed objects, finding families and the inventory hashes.

Say:

> The input is a bounded synthetic corpus. MRI records what it read, how many lines each source has and which diagnostics were produced.

## 0:45–1:20 — Follow evidence

Open **Findings**. Choose the storage contradiction. Show the two paths, line ranges and source quotes. Then point to stale authority and the scope leak.

Say:

> A finding is not a verdict. It is a claim with an inspectable trail, an uncertainty statement and a proposed next action.

## 1:20–1:45 — Separate authority from detection

Open **Authority** and **Blueprint**. Show that the latest dated decision is only a candidate and that unresolved ownership/authority remains visible.

Say:

> MRI can rank a candidate. A human still decides whether it governs.

## 1:45–2:05 — Make review explicit

Return to **Findings**. Approve one proposal, reject or defer another. Open **Review** and show the history and `mutation_applied: false`.

Say:

> Approval records intent in a ledger. It does not rewrite the source files.

## 2:05–2:25 — Prove the output

Open **Before / after**, then **Export**. Mention the fixed question and the 8/8 Northstar fixture recovery.

Close with:

> The reusable infrastructure is the governed path from messy context to evidence, authority and human review. The machine is allowed to point at the mess. It is not allowed to quietly declare the mess canonical.

## Recovery

- If the scan is not yet loaded, click **Start scan** again.
- If review state becomes confusing, click **Reset review state**.
- If the browser path is unavailable, run `python -m mri demo --output out/demo` and show `out/demo/report.md` plus `python -m mri eval fixtures/northstar --output evals/northstar`.
- Do not present the optional provider adapter as live. Do not claim model accuracy.
