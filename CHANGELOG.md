# Changelog

All notable changes to this marketplace are documented here. The format is based on
[Keep a Changelog](https://keepachangelog.com/), and this project adheres to
[Semantic Versioning](https://semver.org/).

Note: this changelog tracks the **marketplace and its tooling**, not the individual
skills — each listed skill keeps its own changelog in its own repo.

## [Unreleased]

### Added
- Initial Prompt Cause marketplace with the `prompt-engineering` skill listed via a pinned `git-subdir` source.
- `skill-template/` — a ready-to-copy layout for new skills.
- Security model: external skills must be pinned to a reviewed commit `sha`; the `validate` CI workflow rejects unpinned external sources.
- `SECURITY.md` (disclosure policy + listed-skill safety model) and `CONTRIBUTING.md` with a "Versioning & security" section.
- Repository hardening: least-privilege CI permissions, GitHub Actions pinned by `sha`, `CODEOWNERS`, and Dependabot for actions.
- `scripts/bump_skill.py` + `bump-own-skills` workflow — advances owned skills to their latest commit `sha` and opens a PR for review.
- Marketplace banner (Prompt Cause brand) with editable source under `assets/`.
- `docs/ARCHITECTURE.md` and a professional README (badges, TOC, security model, FAQ, roadmap).
