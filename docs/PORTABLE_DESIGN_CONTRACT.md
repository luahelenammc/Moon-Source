# Portable Design Contract

A public portable must be independently readable within its declared scope.

## Required metadata

Each current portable should identify:

- title;
- version;
- status;
- language;
- author and creator;
- Moon Source lineage;
- canonical repository path;
- Moon Source public surface;
- Moon's professional context;
- dependencies;
- freshness caveats;
- attribution and usage boundary;
- route to [Credits & Attribution Ops](CREDITS_ATTRIBUTION_OPS.md) for content identity, intellectual lineage, mirrors, adaptations, generated derivatives, permission scope and evidentiary continuity;
- important non-claims.

## Content contract

A portable should:

- explain its function before its architecture;
- state who it is for;
- define what it does and does not do;
- preserve enough context to be useful on its own;
- name the authority or source lineage behind its claims;
- avoid private dependencies;
- distinguish current state from historical material;
- keep platform-specific facts date-sensitive when needed;
- preserve source lineage and identify local adaptation when an external resource materially shaped the portable;
- make canonical identity recoverable after transport;
- preserve relevant disclosure and permission boundaries when the portable moves into another surface;
- avoid implying universal validity, adoption or impact without evidence.

## Canonicalization

A portable has one canonical **current** path in this repository. The active repository tree exposes only the latest public generation of each portable family. Superseded portable files must not remain beside the current version in `main`, under compatibility filenames or in an archive directory that ships with the current tree.

Historical generations remain recoverable through Git history and, when useful, immutable tags or releases. Historical recoverability is a version-control responsibility, not a reason to keep stale operational files in the live corpus.

A website or other surface may mirror the current portable for convenience, but the mirror must preserve version, content identity and links back to the canonical repository. Superseded mirrors should be removed from the live download surface when the new generation is promoted.

If the portable is transformed rather than mirrored byte-for-byte, describe the transformation honestly and preserve the upstream canonical identity. Use [Credits & Attribution Ops](CREDITS_ATTRIBUTION_OPS.md) when the resulting artifact needs a derivative or custody record.

## Distribution semantics

Portability is a distribution role, not a second semantic authority. When a capability is both structural and portable, the portable may be the single canonical active body and must not require a `docs/` twin. The registry represents that capability in the portable inventory, while the non-portable component inventory remains for capabilities that are not current portables.

Use this canonicalization guard:

```text
one capability
→ one active semantic body
→ optional structural, portable, mirror, package and adapter surfaces
```

A distinct adapter is permitted only when it owns volatile or surface-specific implementation facts that should not become stable doctrine. Mirrors and packages carry exact current bytes for delivery; history belongs to version control.

A link labeled **Download** should trigger the platform's file-download route rather than merely opening a rendered or inline raw document. Browse/open links and download links are different interface promises and should be labeled accordingly.

For GitHub-hosted current `.md` portables, Moon Source uses GitHub's `github.com/<owner>/<repo>/raw/refs/heads/<branch>/<path>` download route in user-facing download surfaces. The canonical repository path remains the semantic identity; the download URL is a delivery route.

## First-use contract

A public portable is distribution-complete only when a newcomer can use it correctly without already understanding Moon Source.

Every current and future public portable must expose this embedded entry path:

~~~text
canonical portable body = semantic authority
README.md = family identity, orientation and newcomer onboarding
package = canonical body + README.md
~~~

The README's `## First use` section is support material, not a second semantic body. It may explain current use, boundaries, manual actions and product-sensitive expectations, but it cannot silently change the portable's semantic contract. Operational claims remain subordinate to the canonical body and to dated adapter notes where applicable.

Each README's embedded section must tell a newcomer, in plain language:

- what the portable is for;
- whether anything is installed;
- which exact canonical file to provide to an AI;
- what to say first;
- what should happen next;
- what may require a manual action or unavailable capability;
- what the portable does not claim or do.

Each embedded section must include a copy-paste starter prompt, a minimal example, a short troubleshooting path, a link to the canonical body and a route back to the root README's `#first-use` anchor. If the portable depends on an external capability, the section must distinguish an instruction from an actually available integration. If the interface cannot perform a step, the section must say so.

The validator and package contract enforce the presence of `README.md`, its `## First use` section and the byte identity of the canonical file and README inside the package. Future portables should not be promoted as distribution-complete without a usable embedded entry path.

## Reuse

Current Moon Source portables are Moon-authored open content under CC-BY-4.0 unless a file-level or third-party notice says otherwise. Use, copying, adaptation and redistribution are governed by the applicable standard license and the routes in [LICENSING.md](../LICENSING.md). [Credits & Attribution Ops](CREDITS_ATTRIBUTION_OPS.md) preserves content identity, lineage, transformation history, permission scope and attribution; it is a provenance layer, not a replacement license. Independent implementations of abstract ideas or methods are not converted into copyright-exclusive works by this statement.

## Mirror synchronization

A mirror may exist for access, but it is never a second semantic source. Preserve the mapped current path, version and exact canonical bytes. Record the expected SHA-256 fingerprint in `registry/public-portables.json` and verify it with `scripts/check_mirror_sync.py`.

The live mirror surface should expose only the latest generation of each portable family. Historical mirror URLs are not part of the current mirror contract.

A matching fingerprint supports exact byte identity for that artifact. It does not prove authorship, ownership or legal permission.

## Public routes

Use the [portable registry](../registry/PUBLIC_PORTABLES.md) for canonical files and fingerprints, the [download hub](../DOWNLOADS.md) for distribution, [Credits & Attribution Ops](CREDITS_ATTRIBUTION_OPS.md) for intellectual lineage and content custody, or [Architecture](../ARCHITECTURE.md) for the underlying responsibilities.

<!-- MOON-SOURCE-PUBLIC-STAMP -->

---

> 🌙 **Moon Source** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Source/blob/main/LICENSING.md) · [Use & attribution](https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md) · [Full source (.zip)](https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip)
