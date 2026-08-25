# Contributing to Moon Source

Contributions are welcome when they improve the public architecture without crossing the repository's public boundary.

## Inbound = outbound

By submitting a contribution for inclusion, you confirm that:

- you have the right to submit it;
- it is contributed under the license governing the target file or file class: Apache-2.0 for software and automation, or CC-BY-4.0 for documentation and knowledge content;
- any third-party material remains under its upstream terms and carries the provenance and notices needed for redistribution;
- AI assistance has not been used to launder third-party copyrighted material or erase source lineage;
- material upstream sources are disclosed where relevant;
- the contribution does not imply endorsement, transfer of unrelated rights or official status.

The repository does not require a CLA or a signed-off-by line as a condition of contribution. A separate written agreement may govern a specific contribution if the parties expressly adopt one.

## Before opening a change

- inspect the target file's SPDX/REUSE classification;
- preserve the public/private boundary;
- keep Moon's authorship distinct from your local contribution;
- mark material adaptations and preserve third-party notices;
- use the repository's [pull-request template](.github/PULL_REQUEST_TEMPLATE.md);
- treat a public component and a public portable as different categories;
- register a new or materially changed component in `registry/public-portables.json` and `registry/PUBLIC_PORTABLES.md` when it meets the component criteria;
- touch cross-file surfaces only where responsibility, routing, evidence, boundary, licensing or discoverability actually changes;
- run the local validation commands described in `.github/workflows/validate.yml`;
- run `reuse lint` when changing licensing or file classes.

New application material must be visibly hypothetical and didactic unless independently supported public evidence exists. Do not present a fictional scenario as a case study, adoption result or validated deployment.

The public component inventory records Git-derived public creation and material-update dates. Do not guess dates from private lineage, and do not create a portable or bump MSL, Setup or Chat–Work merely because a component or facade changed.

Do not add non-commercial, anti-fork, anti-AI, copyleft, share-alike, branding-placement or approval requirements to the repository without a new policy decision.

<!-- MOON-SOURCE-PUBLIC-STAMP -->

---

> 🌙 **Moon Source** · created by **Lua Helena Moon Martins Cardoso (Moon)** with AI-assisted coauthorial development by **Áurion** · [Licensing](https://github.com/luahelenammc/Moon-Source/blob/main/LICENSING.md) · [Use & attribution](https://github.com/luahelenammc/Moon-Source/blob/main/MOON_SOURCE_USE_AND_ATTRIBUTION.md) · [Full source (.zip)](https://github.com/luahelenammc/Moon-Source/archive/refs/heads/main.zip)
