# Skill template

Copy this folder to start a new skill. It's the minimum valid layout.

```
plugins/your-skill/
├── .claude-plugin/
│   └── plugin.json              # plugin manifest (name, version, description…)
└── skills/your-skill/
    ├── SKILL.md                 # the skill: frontmatter + workflow
    └── references/              # optional: deep docs loaded on demand
```

## Steps
1. Copy `plugins/your-skill/` and rename `your-skill` everywhere (folder names, `plugin.json` `name`, `SKILL.md` frontmatter `name`).
2. Write `SKILL.md`:
   - `name`: kebab-case, matches the folder.
   - `description`: one sentence that says **what it does and when to use it** — this is what makes the agent trigger it. Include trigger phrases.
   - Body: the instructions/workflow the agent follows.
3. Keep `SKILL.md` lean; put deep material in `references/` and point to it, so it loads only when needed.
4. Test it: drop the folder in `~/.claude/skills/` (rename to just `your-skill/`) and try triggering it in Claude Code.
5. Submit it — see [CONTRIBUTING.md](../CONTRIBUTING.md).

## Tips
- One job per skill. Focused beats broad.
- Write the `description` from the user's intent ("Use when the user wants to…").
- Cite sources if you make factual/technique claims.
