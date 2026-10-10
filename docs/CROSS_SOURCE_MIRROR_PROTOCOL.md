<!-- SPDX-FileCopyrightText: 2026 Lua Helena Moon Martins Cardoso (Moon) -->
<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# Cross-Source Mirror Sync Protocol

**Status:** shared maintenance contract · **Scope:** explicitly registered mirrors and derived projections · **Owner:** Lua Helena Moon Martins Cardoso (Moon) · **AI-assisted coauthor:** Áurion

This is the **single public methodological authority for cross-source mirror synchronization**, maintained in Moon Source. It is a governance contract, **not** a new standalone capability, mandatory application runtime, continuous synchronization service, or permission to access another project's private files.

Projects adopt the contract through a short binding identifying their own source, downstream consumer, mirror class, ownership, credentials/access boundary and validation rules. The binding owns local facts; it must **not copy this procedure**. One shared method can have several sovereign implementations.

## 1. Distinguish the branches

| Branch | Meaning | Acceptance evidence |
|---|---|---|
| **D1 · exact distribution** | Canonical public artifact is delivered byte-for-byte to a public website, downloads path, package or repository mirror. | Identical SHA-256 of specified bytes, current path/manifest, matching license/custody and public readback. |
| **F1 · frozen public method dependency** | An authorized local consumer runs an immutable public source family as an operational fast path. The public body governs its *imported method*, while local overlays remain sovereign. | Verified source-file set/manifest/version, complete frozen snapshot, local binding reconciliation and private readback. |
| **S1 · procedural/runtime projection** | A skill or executable procedural contract is deliberately projected into another supported surface or a fallback mirror. | Equivalence of relevant procedure/activation, correct runtime-versus-fallback claim, source authority, target readback. |
| **R1 · semantic reference or selective inheritance** | A public method influences a sovereign local derivative without requiring a literal copy. | Explicit provenance and selected delta; no automatic frozen snapshot, no claim of byte identity. |

An entity can have several **separately registered** relationships. **A reference is not a mirror.** Do not promote R1 to F1 simply because the names match. A locally originated public projection must not reverse the flow of authority when the public derivative is re-imported.

## 2. Registry and ownership

A binding is eligible only when it declares, at the smallest sovereign destination:

- **identity:** relationship ID, branch class, source owner/repository/canonical path, optional registry entry;
- **scope:** exact file or allowlisted family, relevant package dependencies, exclusion rules, tracked version and verifiable source fingerprint(s);
- **consumer:** owning project, private/public boundary, exact mirror destination, local authority and any stronger constraints;
- **release trigger:** which public update or explicit refresh makes synchronization due;
- **write capability:** who may mutate the consumer, and how that authority is verified; no assumption that public CI can edit private Docs;
- **acceptance:** validation commands/checks, expected postflight/readback and failure owner.

Private file IDs, credentials, personal corpora, biometric material, and reserved implementation logic belong **only in the private registry**, never in public repo files. A public project may link to this protocol and say that owner-authorized consumers exist without publishing their locations.

## 3. One update transaction, conditional branches

At the **start of a public update execution**, inspect the public change's actual touched artifact scope and the registered dependent relationships. Do not infer a material module update from an unrelated repository HEAD change.

If a registered source artifact is updated, the **same update execution** owes downstream reconciliation before claiming complete *cross-source* closure:

1. **Preflight:** resolve the source of truth, affected mirror bindings, owner permissions, content/visibility constraints and accepted baseline; guard against unrelated changes.
2. **Build and validate:** commit or prepare the canonical source through its own release gates; validate appropriate tests, fingerprints, packaging and licensing. Changes to an exact distribution must satisfy D1; changing a frozen family must satisfy F1's source-set contract.
3. **Diff:** compare the *governed source bytes/file manifest* against each registered destination. An unchanged governed artifact is `no_delta`; no rewrite simply because the repository commit, unrelated readme, or neighboring module changed.
4. **Project:** update only the authorized dependent mirror or projection. F1 replaces its **public literal frozen section/family coherently**, updates version/path/per-file digests and minimally reconciles affected consumer bindings. Keep the consumer's independent local source, identity, taste, state, private heuristics and strict permissions unchanged.
5. **Readback:** compare the target's observed content/manifest and version with the accepted source and check that protected local material remains intact. A GitHub CI pass cannot prove a Google Docs write.
6. **Close:** record scope, origin version/commit, per-artifact identity, destination receipt and one of `synced`, `no_delta`, `pending_blocked`, `failed_validation` or `not_applicable`. Public publication may succeed while downstream closure remains open; report this distinction truthfully.

**No action in a different account, project, repository or document is implied by an upstream commit.** If the current operator lacks a private connector or permission, stop the downstream mutation at `pending_blocked`, preserve the last verified mirror, and supply a bounded continuation handoff naming the correct private destination **only to an authorized private operator**. Do not backfill success claims, leak credentials, or silently roll back an otherwise legitimate public release.

## 4. Execution triggers and freshness

**Trigger:** the owner-authorized execution is already creating, editing, promoting, releasing, verifying or explicitly synchronizing the governed source; or an explicit user instruction requests a refresh. An independently observed changed public version may trigger a bounded reconciliation in a context that is already authorized to update the private consumer.

**Not a trigger:** ordinary use of an F1 snapshot, unrelated repo changes, a timer, periodic monitoring, GitHub Actions reaching into private Drive, a speculative freshness tax, or a broad unconditional crawl across all projects.

Ordinary runtime uses the existing verified local snapshot. A consumer is permitted to remain stale **between eligible observations**, but not to claim current sync if an eligible update was seen and downstream readback did not happen. Dated factual claims (product availability, models, law, prices, etc.) require separate current-source checking when material; freezing a method does not freeze reality.

## 5. Precedence, privacy and branch invariants

- The publisher governs its public canonical method. The consumer governs its own living local state, overlays, permissions, private experience and destination.
- For F1, **literal public bytes remain distinct from local annotations**; never weave local extensions into a section claimed to be the exact public snapshot. Source replacement is not a whole-document overwrite.
- For D1, exact equality is mandatory; an adapted file is a derivative, not a byte mirror.
- For S1, describe native activation separately from fallback execution. A documented procedure does not prove a skill is installed or running.
- For R1, cite provenance and extract only an eligible change; do not manufacture a mirrored copy.
- Multiple simultaneous consumers produce **separate receipts**. A failure in one cannot be concealed by another passing.
- The output must be recoverable and idempotent: repeat with unchanged source → `no_delta`, not another patch appendix.
- Public repositories must not include private connector URLs, tokens, personal data, hidden profile details, or an implied automatic background service.

## 6. Known adoption routes

The **Moon Source** repository governs this shared method and specializes D1 website distribution in [Mirror Synchronization](MIRROR_SYNCHRONIZATION.md). It contains public method sources used by F1 consumers (including Preflight and Adaptive Orchestration) without owning those consumers' private overlays.

The **Moon Cortex** repository may adopt F1 for selected public modules such as Probability Calibration and Moon Image Cortex. Its [Module Design Contract](https://github.com/luahelenammc/Moon-Cortex/blob/main/docs/MODULE_DESIGN_CONTRACT.md) governs what makes a public module publishable; this protocol governs the **cross-source aftercare** when an explicitly registered consumer exists. Cortex does not inherit Moon Source as its domain authority or a mandatory runtime.

Cross-repository relationships require explicit scope and authorization. A local mirror remains a cache; it does not replace the canonical source or imply that another repository governs it.

Procedural Personal Skill mirrors and independently managed website exact-byte mirrors continue to use their own native validation. A future project opts in with a binding, never by copying this entire file.

## 7. Acceptance test

A conformant implementation demonstrates: unchanged source → `no_delta`; relevant public change → verified mirror and readback; unrelated HEAD change → no spurious refresh; missing private access → `pending_blocked`; invalid package → `failed_validation`; local customization conflict → protected overlay unchanged; exact D1 bytes differ → mirror status unverified; repeated update → idempotent; no scheduled task or private disclosure was introduced.

**One law, typed branches, registered consumers, independent authority and receipts.**

<!-- MOON-SOURCE-PUBLIC-STAMP -->

---

> 🌙 **Moon Source** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Source/blob/main/LICENSING.md) · [Use & attribution](https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md) · [Full source (.zip)](https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip) · Questions, suggestions, or proposals? Feel free to contact me at [LuaHelenaMMC@gmail.com](mailto:LuaHelenaMMC@gmail.com).
