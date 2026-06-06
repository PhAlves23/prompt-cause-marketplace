# Security Policy

This marketplace lists skills that run **inside other people's AI agents**. That makes security a first-class concern — both for what we list and how this repo is operated.

## How listed skills are kept safe

1. **Review before listing.** Every skill is reviewed before it enters the catalog — for hidden instructions (prompt injection, data exfiltration, covert tool/URL calls), unsafe scripts, and scope that doesn't match its description.
2. **Pinned commits.** Externally-hosted skills are pinned to a reviewed commit `sha`. A contributor can change their own repo freely, but those changes do **not** reach users here until a new `sha` is reviewed and merged. See [CONTRIBUTING — Versioning & security](CONTRIBUTING.md#versioning--security).
3. **Re-review on update.** Updating a listed skill means a new PR changing the `sha`, which is reviewed again.
4. **CI enforcement.** The `validate` workflow rejects any external source that isn't pinned to a full commit `sha`.

## Reporting a vulnerability

If you find a problem — a malicious or compromised skill in the catalog, or an issue with this repo's tooling — report it privately first:

1. Use GitHub's **[Report a vulnerability](https://github.com/PhAlves23/prompt-cause-marketplace/security/advisories/new)** (Security → Advisories), or
2. Open a minimal public issue asking the maintainer to make private contact, without disclosing exploit details.

Please do **not** post a working exploit publicly before it's addressed. Include: what's affected, steps to reproduce, and the impact you foresee.

## For users

- A skill is third-party content. Install skills you trust; review a skill's source repo if in doubt.
- This catalog reduces risk through review + pinning, but **no marketplace can guarantee third-party code is safe** — treat it as defense-in-depth, not a guarantee.
