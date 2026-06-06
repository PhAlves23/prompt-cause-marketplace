<div align="center">

# Prompt Cause — Skill Marketplace

**A curated catalog of AI skills for Claude Code and other agents.**

Add one marketplace, install any skill. Built and curated by [Prompt Cause](https://github.com/PhAlves23).

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Validate](https://github.com/PhAlves23/prompt-cause-marketplace/actions/workflows/validate.yml/badge.svg)](https://github.com/PhAlves23/prompt-cause-marketplace/actions/workflows/validate.yml)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

</div>

---

## Quick start

Add the marketplace once, then install whatever you need:

```
/plugin marketplace add PhAlves23/prompt-cause-marketplace
/plugin install <skill-name>
```

Works in **Claude Code** and **GitHub Copilot CLI** (`copilot plugin marketplace add ...`). For Cursor, Windsurf, Codex, Gemini and OpenCode, each skill's own repo has native install instructions.

## Catalog

| Skill | What it does | Repo |
|-------|--------------|------|
| **prompt-engineering** | Rewrites a raw draft into a production-grade prompt, with a changelog of what changed and why. Grounded in primary sources. | [prompt-engineering-skill](https://github.com/PhAlves23/prompt-engineering-skill) |

_More coming. Want yours here? See [Contributing](#contributing)._

## How this works

Claude Code has a three-level hierarchy:

```
Marketplace  →  contains many Plugins  →  each Plugin contains one or more Skills
```

This repository is the **marketplace** — a catalog (`/.claude-plugin/marketplace.json`) that points at skills. A skill can live:

- **Inline** in this repo, under `plugins/<name>/`, or
- **In its own repository**, referenced here via a `git-subdir` / `url` source.

Either way, users add a single marketplace and install skills individually. You always install only what you want — nothing is forced.

**Security:** externally-hosted skills are pinned to a reviewed commit `sha`. A contributor can change their own repo freely, but those changes don't reach users here until a new `sha` is reviewed and merged. See [Versioning & security](CONTRIBUTING.md#versioning--security).

## Contributing a skill

We welcome community skills. There are two paths:

1. **Keep your skill in your own repo** (recommended) — you maintain it; we just list it in the catalog.
2. **Contribute it inline** — add it under `plugins/` in this repo.

Start from [`skill-template/`](skill-template/) and read [CONTRIBUTING.md](CONTRIBUTING.md) for the full process. Every submission is reviewed for quality and **security** before it's listed — skills run inside other people's environments, so this matters.

## License

[MIT](LICENSE) for the catalog and tooling. Each externally-hosted skill keeps its own license.
