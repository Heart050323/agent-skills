---
name: skill-sync
description: Port skills between Codex (~/.codex/skills) and Claude (~/.claude/skills) so both agents share one skill set. Use after creating, editing, or installing any skill, and when the user asks to sync or share skills across agents.
version: 1.0.0
metadata:
  short-description: Sync skills between Codex and Claude
---

# Skill Sync

Every skill lives in both `~/.codex/skills/<name>/` and `~/.claude/skills/<name>/`. The two copies are **ports, not mirrors**: same behavior, each phrased in its host's dialect. After any skill is created, edited, or installed on one side, port it to the other before finishing the task.

## Porting procedure

1. Identify the fresher side by SKILL.md modification time (`stat -f %Sm` on macOS, `stat -c %y` on Linux); it is the source. Never overwrite newer content with older.
2. Copy supporting files (checklists, glossaries, reference `.md`) as-is; they are dialect-neutral.
   - If the skill folder is a symlink (`npx skills` installs link into `~/.agents/skills/`), materialize it first — replace the link with a dereferenced copy (`rm` + `rsync -a target/ skill/`) so the repo never carries machine-local links.
3. Rewrite the SKILL.md frontmatter into the target dialect (table below).
4. Translate tool references in the body (table below). Leave everything else — wording, structure, language — unchanged.
5. Preserve target-side extras that have no source counterpart: `agents/openai.yaml`, 「Codex 向けメモ」 sections. Drop one only if the new body contradicts it.
6. Done when: the target SKILL.md carries target-dialect frontmatter, a grep for the source column's tool names returns nothing in the target body, and every supporting file on the source side exists on the target.
7. Commit and push the skills repo (Propagation below).

## Propagation

Both trees live in one git repo, `~/agent-skills` (github.com/Heart050323/agent-skills): `codex/` and `claude/` are linked to `~/.codex/skills` and `~/.claude/skills` (symlink on macOS, junction on Windows). Pull before editing any skill; after porting, commit and push:

```
git -C ~/agent-skills pull && git -C ~/agent-skills add -A && git -C ~/agent-skills commit -m "skills: <what changed>" && git -C ~/agent-skills push
```

Other devices pick the change up with `git -C ~/agent-skills pull`. On a merge conflict, the fresher-side rule (step 1) decides.

## Frontmatter dialects

| Claude | Codex |
|---|---|
| `name`, `description`, `argument-hint` | keep verbatim |
| `disable-model-invocation: true` | drop (no equivalent) |
| `allowed-tools: [...]` | drop |
| `model: opus` | drop |
| — | add `metadata:` → `short-description: <≤6 words>` |

Codex skills may also carry `agents/openai.yaml` (`interface:` with `display_name`, `short_description`, `default_prompt` using `$skill-name`). Create it for skills the user invokes by name; skip it for pure reference skills.

## Tool-reference translation (Codex → Claude)

| Codex | Claude |
|---|---|
| ask the user in plain text | `AskUserQuestion` |
| do it directly (`rg`, shell) | `Task` / `Agent` / `Explore` subagent |
| `rg` / `rg --files` | `Grep` / `Glob` tools |
| read/edit/write the file (plain phrasing) | `Read` / `Edit` / `Write` tools |
| update the plan | `TodoWrite` / `TaskCreate` |
| write a local HTML file and report its path | `Artifact` |
| fetch/search the web (plain phrasing) | `WebFetch` / `WebSearch` |
| `$skill-name` | `/skill-name` invocation |

Claude → Codex runs the table right-to-left, replacing named Claude tools with their Codex equivalents (e.g. `AskUserQuestion` becomes asking the user in plain text).

## Scope

Global skills only. `~/.codex/skills/.system/` is Codex-internal — never port into or out of it. Project-level skills (`.claude/skills/` inside a repo) sync only when the user asks.
