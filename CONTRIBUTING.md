# Contributing a skill to Prompt Cause

Thanks for wanting to add a skill to the catalog. This guide walks through it even if you've never contributed to open source.

## Table of contents
- [What makes a good skill](#what-makes-a-good-skill)
- [Two ways to contribute](#two-ways-to-contribute)
- [Path A — list your own repo (recommended)](#path-a--list-your-own-repo-recommended)
- [Path B — contribute the skill inline](#path-b--contribute-the-skill-inline)
- [The review process (quality + security)](#the-review-process-quality--security)
- [Skill quality bar](#skill-quality-bar)

## What makes a good skill

A skill is a folder with a `SKILL.md` (a clear `name` + `description` in YAML frontmatter) plus any reference files. It extends an agent with a focused capability. Good skills are:

- **Focused** — one job, done well.
- **Clear-triggering** — the `description` says exactly when to use it, so the agent activates it at the right moment.
- **Self-contained** — works without external services where possible; if it needs tools, it says so.
- **Honest** — claims are accurate; if it's grounded in sources, it cites them.

Use [`skill-template/`](skill-template/) as your starting point.

## Two ways to contribute

| | Path A — your own repo | Path B — inline |
|---|---|---|
| Who maintains it | You | You, via PRs here |
| Where the code lives | Your repository | This repo, under `plugins/` |
| Best for | Skills you want to own/evolve independently | Small skills, or donating to the catalog |

## Path A — list your own repo (recommended)

1. Build your skill in your own repo. The skill must live at a path containing `.../skills/<name>/SKILL.md`, with a plugin manifest at `<plugin-dir>/.claude-plugin/plugin.json`. (Copy the layout from `skill-template/`.)
2. Make your repo public and tag a release.
3. Open a PR here adding an entry to `.claude-plugin/marketplace.json`:
   ```json
   {
     "name": "your-skill",
     "description": "One clear sentence: what it does and when to use it.",
     "source": {
       "source": "git-subdir",
       "url": "https://github.com/you/your-repo.git",
       "path": "plugins/your-skill",
       "ref": "main"
     },
     "category": "productivity",
     "homepage": "https://github.com/you/your-repo"
   }
   ```
   (If your repo *is* the plugin — `plugin.json` at the root — use `"source": {"source": "github", "repo": "you/your-repo"}` instead.)
4. Fill in the PR checklist. CI validates the JSON and that your source resolves.

## Path B — contribute the skill inline

1. Copy `skill-template/plugins/your-skill/` to `plugins/<your-skill>/` and rename.
2. Fill in `plugin.json` and `skills/<your-skill>/SKILL.md`.
3. Add an entry to `marketplace.json` with an inline source:
   ```json
   { "name": "your-skill", "description": "...", "source": "./plugins/your-skill", "category": "productivity" }
   ```
4. Open a PR.

## The review process (quality + security)

Every submission is reviewed before it's listed. **Security is the priority** — a skill runs inside other people's agents, so a malicious one could exfiltrate data or hijack tools. The maintainer checks:

- **No hidden malicious instructions** — prompt injection, data exfiltration, instructions to ignore safety, or to call tools/URLs covertly.
- **Links and scripts are safe** — every URL and any script is inspected.
- **Scope matches the description** — the skill does what it claims, nothing sneaky.
- **Quality bar met** (below).

If anything is unclear, expect questions — that's normal, not rejection.

## Skill quality bar

- [ ] `SKILL.md` has valid frontmatter: `name` (kebab-case) + a clear, trigger-rich `description`.
- [ ] The description states **when to use** the skill, not just what it is.
- [ ] No secrets, credentials, or personal data committed.
- [ ] A `LICENSE` in your repo (Path A) — open-source preferred.
- [ ] It actually works — you tested it in at least one agent.
- [ ] No emoji-as-icon, no marketing fluff; clear and useful.

By contributing inline (Path B), you agree your contribution is licensed under this repo's [MIT License](LICENSE). For Path A, your repo keeps its own license.
