# Jurisdictional Requirements — Configuration Boundary

**Status:** architecture and evaluation checklist, **not legal advice, an automated legal interpreter, a compliance certification, or a new Moon Source capability.**

Apps operating across multiple countries, states, sectors, purposes or channels cannot assume one privacy rule applies everywhere. Requirements may depend on the operating organization, processing roles, where people are located, the type and source of data, the purpose of each operation, transfers, retention, and the service's legal setting.

There is no such thing as a universally compliant prompt. A model cannot decide legal applicability merely by seeing a person's language, nationality or the location of the company.

## 1. Who owns each decision?

| Role | Owns | Not delegated to a model |
|---|---|---|
| Organization / data controller or corresponding legal role | Identify purposes, processing conditions, responsibilities, actual user population and legal counsel | Legal accountability |
| Qualified legal/privacy review | Determine which federal, state, national and sectoral rules apply, and interpret obligations | Legal applicability and approval |
| Security / product engineering | Implement authenticated access, purpose gating, encryption as appropriate, secure storage, deletion and audit controls | Technical security enforcement |
| Context architect | Translate approved requirements into scoped data, state, conversation and escalation contracts | Legal sign-off or runtime security |
| AI model / assistant | Operate within already provided and enforced boundaries | Self-authorizing new processing or transfers |

Role names vary by legal system; do not assume identical meanings across jurisdictions.

## 2. Review packet for every relevant operating configuration

Before using personal or sensitive information, ask the operator or qualified reviewers to specify:

- **Applicable scope:** countries/states/sector, participants, organization, operators and territorial reach, including uncertainties.
- **Purposes:** what information is processed for which service action, using a documented lawful basis or other relevant legal condition where applicable.
- **Data categories:** operational status, preferences, health-related or other protected information; which fields are actually necessary and why.
- **Actors and vendors:** responsible entity, processors/service providers, hosting, AI model vendors, subprocessors and authorized data recipients.
- **Interaction controls:** what is said to participants, affirmative permissions or other applicable authorization, withdrawal/opt-out, escalation and human support.
- **Retention / deletion:** maximum duration, revocation, archive, logging and participant rights appropriate to the actual framework.
- **Cross-border handling:** storage locations, service routing, transfer conditions and operator-approved restrictions.
- **Approvals and expiry:** named accountable reviewer, version/effective date, pending matters, and review/renewal trigger.

A generic statement that an organization is “LGPD compliant”, “HIPAA compliant”, “GDPR compliant” or “compliant in every US state” without a verified, scoped assessment is not admissible evidence. No specific law applies simply because a person speaks Portuguese or participates in a transnational service.

## 3. Representation of the *reviewed* requirement profile

An implementation may store a small, machine-readable record supplied by the organization. This is **configuration**, not an automated legal determination.

```json
{
  "reviewState": "approved",
  "reviewReference": "SYNTHETIC-REVIEW-01",
  "regions": ["FICTIONAL-REGION-A"],
  "purposes": ["continuity"],
  "validUntil": "2026-12-31",
  "allowedKinds": ["program_state", "dialogue_state"],
  "fieldsByKind": {
    "program_state": ["module"],
    "dialogue_state": ["last_topic"]
  }
}
```

The example uses invented jurisdiction labels and invented dates. Actual profiles must be scoped, reviewed, versioned, protected against unauthorized edits and enforced on the server. A string saying `"approved"` is **not** proof that anyone performed a legitimate legal review. The sample router trusts its provided fixture; it does not verify signatures, reviewer identity or legal validity.

## 4. Fail-closed and change-of-jurisdiction rules

- If the operator cannot identify applicable requirements or their status, **do not enable sensitive context processing** on the basis of assumptions.
- If the participant's region changes or an additional processing purpose is introduced, **re-evaluate the configuration** before expanding data access.
- A permission for one program phase or one channel does not automatically extend to advertising, research, external analytics or unrelated outreach.
- Revocation, expiry and changed authority must affect *future* context assembly; downstream stores and deletion behavior must be implemented and reviewed separately.
- Reject attempts by prompts, retrieved records or the model to override reviewed data-access rules.
- Regulatory applicability may change; include a responsible update owner and expiry/review event rather than treating requirements as permanent.

## 5. Public demonstration and claim boundaries

[The reference selector](../examples/conversational-context/README.md) checks only a **synthetic approval envelope and field allowlists**. It illustrates the expected control point in a software architecture. It provides **no real-world jurisdiction classifier**, counsel-approved rules, proof of consent, secure storage, user authentication, transmission safeguards, deletion service, breach notification, monitoring system or legal compliance.

For its context-input meaning, see [Conversational Context](CONVERSATIONAL_CONTEXT.md); for real source reach and write authorization, see [Connected Sources](CONNECTED_SOURCES.md).

<!-- MOON-SOURCE-PUBLIC-STAMP -->

---

> 🌙 **Moon Source** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Source/blob/main/LICENSING.md) · [Use & attribution](https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md) · [Full source (.zip)](https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip) · Questions, suggestions, or proposals? Feel free to contact me at [LuaHelenaMMC@gmail.com](mailto:LuaHelenaMMC@gmail.com).
