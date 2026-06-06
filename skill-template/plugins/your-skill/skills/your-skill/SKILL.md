---
name: your-skill
description: Optimizes/does X for Y. Use when the user says "<trigger phrase>", asks to <do the thing>, or <situation that should activate this skill>. Replace this with a clear, trigger-rich sentence — it's what makes the agent fire the skill at the right time.
license: MIT
---

# Your Skill

One short paragraph: what this skill produces and the value it adds. State up front whether it *does* the task or *advises* on it.

## When to use

- Bullet the concrete situations that should trigger this skill.
- Be specific — vague triggers lead to over- or under-activation.

## Workflow

1. **Step one** — what to do first.
2. **Step two** — …
3. **Deliver** — the exact output the user gets.

## Output format

Describe (or show) the exact shape of the result. Example:

```
## Result
<the deliverable>

## Notes
- <anything the user should know>
```

## Guidelines

- Keep instructions positive ("do X") over negative ("don't do Y").
- Calibrate effort to complexity; don't over-engineer simple cases.
- If you make factual or technique claims, cite the source in a `references/` file.

## References (optional)

Put deep material in `references/*.md` and load it on demand:

- `references/example.md` — load when <condition>.
