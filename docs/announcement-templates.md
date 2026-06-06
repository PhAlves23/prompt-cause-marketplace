# Announcement templates — Prompt Cause marketplace

Ready-to-post copy for launching the **marketplace** (the catalog), distinct from any single skill. Adjust tone per channel. Replace links if you fork under a different owner.

> Launch order: start with **one** channel (Reddit r/ClaudeAI fits best), reply to every comment in the first 24h, then expand. Don't blast all channels at once.

---

## 1. Reddit — r/ClaudeAI (also r/cursor, r/ChatGPTCoding)

**Title:** I built an open, curated marketplace of AI skills for Claude Code (one `/plugin marketplace add`, install any skill)

**Body:**

I kept seeing great Claude Code skills scattered across random repos, each with its own install dance. So I built **Prompt Cause** — one curated marketplace you add once, then install any skill from a single catalog.

What makes it different from "a list of links":

- **One source.** `/plugin marketplace add PhAlves23/promptcause-marketplace`, then `/plugin install <skill>`. Done.
- **Curated + security-pinned.** Every skill is reviewed before listing, and external skills are pinned to a reviewed commit `sha` — so a contributor changing their repo later can't silently ship unreviewed code to users. CI rejects any unpinned external source.
- **Open to contributions.** You keep your skill in your own repo; we just list it (pinned). There's a template and a clear submission flow.

First skill in the catalog is **prompt-engineering** (rewrites a raw draft into a production-grade prompt, grounded in primary sources). More coming, and submissions are open.

Also works in GitHub Copilot CLI, and each skill documents native install for Cursor, Windsurf, Codex, Gemini, and OpenCode.

MIT, contributions welcome: https://github.com/PhAlves23/promptcause-marketplace

Happy to answer questions or take suggestions on what skills to add next.

---

## 2. X / Twitter (thread)

**1/** I open-sourced **Prompt Cause** — a curated marketplace of AI skills for Claude Code.

Add one marketplace, install any skill:
`/plugin marketplace add PhAlves23/promptcause-marketplace`

🧵

**2/** Why a marketplace, not one-repo-per-skill?
- One source for users
- Install only what you want
- Open to community skills — but every listing is reviewed and version-pinned

**3/** Security is built in: external skills are pinned to a reviewed commit `sha`. A contributor can't change their repo and silently push unreviewed code to users. CI enforces the pin.

**4/** First skill: prompt-engineering (turns a rough draft into a production-grade prompt). More coming — submissions open.

MIT: https://github.com/PhAlves23/promptcause-marketplace

---

## 3. Hacker News (Show HN)

**Title:** Show HN: A curated, security-pinned marketplace of AI skills for Claude Code

**Body:**

Skills for AI coding agents are spreading across individual repos, each with its own install steps and no review. I built a single curated catalog instead.

Design points:
- **One marketplace, granular installs.** Add it once; install only the skills you want.
- **Security-pinned listings.** External skills are pinned to a reviewed commit `sha`; post-review changes in a contributor's repo don't reach users until a new `sha` is reviewed. CI rejects unpinned external sources. Repo is hardened too (least-privilege CI, actions pinned by sha, Dependabot, branch protection).
- **Open contribution.** Keep your skill in your repo; submit a PR adding a pinned catalog entry.

MIT: https://github.com/PhAlves23/promptcause-marketplace

Feedback welcome — especially on the review/pinning model.

---

## 4. LinkedIn

I open-sourced **Prompt Cause**, a curated marketplace of AI skills for Claude Code and other agents.

Instead of hunting down individual repos, you add one marketplace and install any skill from a single catalog — with a review-and-pin process that keeps third-party skills safe to run.

It's MIT-licensed, open to community contributions, and the first skill (prompt-engineering) is already live. If you build with LLMs, I'd love your feedback.

https://github.com/PhAlves23/promptcause-marketplace

---

## 5. Submit to community directories

Open a PR/issue adding the marketplace to these curated lists (check each repo's format first):
- `ComposioHQ/awesome-claude-plugins`
- `Chat2AnyLLM/awesome-claude-plugins`
- `GetBindu/awesome-claude-code-and-skills`
- claudemarketplaces.com (submit form)

---

## Operations checklist (do these around launch)

- [ ] **Upload the social preview** (manual, one-time): repo → Settings → General → Social preview → upload `assets/banner.png`. Makes shared links show the banner.
- [ ] Post to **one** channel first (Reddit r/ClaudeAI), reply to comments within 24h.
- [ ] Submit to the directories above.
- [ ] When a skill PR arrives: audit (security + quality), then merge **pinned to a sha**.
- [ ] Activate GitHub Sponsors once there's traction.
- [ ] Keep Discussions alive (answer fast; close the loop idea → issue → PR).
