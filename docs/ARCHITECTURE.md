# Architecture & governance

How this marketplace is put together, how listings stay safe, and how it's operated. For *contributing* a skill, see [CONTRIBUTING.md](../CONTRIBUTING.md).

## The catalog

The single source of truth is [`.claude-plugin/marketplace.json`](../.claude-plugin/marketplace.json). It declares the marketplace and an array of `plugins` — each one a skill listing. When a user runs `/plugin marketplace add`, the agent clones this repo, reads that file, and resolves each plugin's `source`.

## Source types

A listing's `source` tells the agent where the skill's code is:

| `source` | Shape | Used when |
|----------|-------|-----------|
| inline | `"./plugins/<name>"` | The skill lives in this repo |
| `git-subdir` | `{ "source": "git-subdir", "url", "path", "ref", "sha" }` | The skill is a subfolder of an external repo (our default for external skills) |
| `github` | `{ "source": "github", "repo": "owner/name", "sha" }` | The external repo *is* the plugin (manifest at root) |
| `url` | `{ "source": "url", "url": "...git", "sha" }` | Same, addressed by clone URL |

`prompt-engineering` uses `git-subdir`, because its plugin lives at `plugins/prompt-engineering/` inside its repo.

## Pinning & the security boundary

This is the core design decision.

External sources are **pinned to a full 40-character commit `sha`** — the exact commit a maintainer reviewed. The `ref` (e.g. `main`) is recorded for context, but the `sha` is what users actually get.

```
Contributor's repo (main moves freely)  ──reviewed at──▶  sha X  ──pinned in catalog──▶  users get sha X
                                                                                          (until a new sha is reviewed)
```

Why: a branch is mutable. If we pointed at `main`, a skill that was safe at review time could later ship malicious or broken code straight to users. Pinning the `sha` makes the audited commit the only thing users receive. Updating means a new PR changing the `sha`, which is reviewed again.

CI enforces this: `validate.yml` fails if any non-inline source lacks a valid `sha`.

## Submission & review flow (governance)

```
Contributor opens PR / "Submit a skill" issue
        │
        ▼
Maintainer reviews:  security (injection, exfiltration, covert calls)
                     quality (frontmatter, clear triggers, works)
                     scope (does what it claims)
        │
        ├── changes requested ──▶ contributor updates ──▶ re-review
        │
        ▼
Merge → listing goes live at the reviewed sha
```

The maintainer (via `CODEOWNERS`) is auto-requested on every PR. Nothing enters the catalog without a merge.

## CI

[`.github/workflows/validate.yml`](../.github/workflows/validate.yml) runs on push and PR:

1. **JSON** — every `*.json` parses.
2. **Catalog** — unique kebab-case names, descriptions present, valid `source`, inline paths exist.
3. **SHA pinning** — every external source has a 40-char `sha`.
4. **Inline skills** — any `plugins/*/skills/*/SKILL.md` has valid frontmatter.

Hardening: `permissions: contents: read` (least privilege), and `actions/checkout` pinned by `sha` (supply-chain). Dependabot keeps the action shas current.

## Owned-skill auto-bump

Manually finding a new `sha` and editing JSON is tedious for *your own* skills. [`scripts/bump_skill.py`](../scripts/bump_skill.py) automates it:

```bash
python3 scripts/bump_skill.py prompt-engineering     # bump one skill
python3 scripts/bump_skill.py --owned PhAlves23      # bump all skills under an owner
```

It reads each target's `url` + `ref`, runs `git ls-remote` to get the latest commit, and updates the `sha` in place.

[`.github/workflows/bump-own-skills.yml`](../.github/workflows/bump-own-skills.yml) runs it weekly (and on demand) for skills under the configured `OWNER`, then **opens a PR** with the changes.

**Important:** auto-bump only touches skills under the owner you control. Third-party skills are never auto-bumped — their `sha` changes only through a human-reviewed PR. The auto-bump still opens a PR (never pushes to `main`), so even your own updates pass through review.

## Releasing the marketplace

The marketplace itself is lightweight; "releasing" mostly means merging catalog changes to `main` (users always resolve against `main`). Tag a version if you want a citable snapshot:

```bash
git tag vX.Y.Z -m "vX.Y.Z" && git push origin vX.Y.Z
```

Move `## [Unreleased]` items in `CHANGELOG.md` under the new version heading.
