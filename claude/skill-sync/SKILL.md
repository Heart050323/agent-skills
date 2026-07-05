---
name: skill-sync
description: Port skills between Claude (~/.claude/skills) and Codex (~/.codex/skills) so both agents share one skill set. Use after creating, editing, or installing any skill, and when the user asks to sync or share skills across agents.
version: 1.0.0
---

# Skill Sync

Every skill lives in both `~/.claude/skills/<name>/` and `~/.codex/skills/<name>/`. The two copies are **ports, not mirrors**: same behavior, each phrased in its host's dialect. After any skill is created, edited, or installed on one side, port it to the other before finishing the task.

## Porting procedure

1. Identify the fresher side by SKILL.md modification time (`stat -f %Sm` on macOS, `stat -c %y` on Linux); it is the source. Never overwrite newer content with older.
2. Copy supporting files (checklists, glossaries, reference `.md`) as-is; they are dialect-neutral.
3. Rewrite the SKILL.md frontmatter into the target dialect (table below).
4. Translate tool references in the body (table below). Leave everything else — wording, structure, language — unchanged.
5. Preserve target-side extras that have no source counterpart: `agents/openai.yaml`, 「Codex 向けメモ」 sections. Drop one only if the new body contradicts it.
6. Done when: the target SKILL.md carries target-dialect frontmatter, a grep for the source column's tool names returns nothing in the target body, and every supporting file on the source side exists on the target.
7. Commit and push the skills repo (Propagation below).

## Propagation

Both trees live in one git repo, `~/agent-skills` (github.com/Heart050323/agent-skills): `claude/` and `codex/` are linked to `~/.claude/skills` and `~/.codex/skills` (symlink on macOS, junction on Windows). Pull before editing any skill; after porting, commit and push:

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

## Tool-reference translation (Claude → Codex)

| Claude | Codex |
|---|---|
| `AskUserQuestion` | ask the user in plain text |
| `Task` / `Agent` / `Explore` subagent | do it directly (`rg`, shell) |
| `Grep` / `Glob` tools | `rg` / `rg --files` |
| `Read` / `Edit` / `Write` tools | read/edit/write the file (plain phrasing) |
| `TodoWrite` / `TaskCreate` | update the plan |
| `Artifact` | write a local HTML file and report its path |
| `WebFetch` / `WebSearch` | fetch/search the web (plain phrasing) |
| `/skill-name` invocation | `$skill-name` |

Codex → Claude runs the table right-to-left, restoring a named Claude tool only where the behavior genuinely needs it (e.g. a required user prompt becomes `AskUserQuestion`).

## Scope

Global skills only. `~/.codex/skills/.system/` is Codex-internal — never port into or out of it. Project-level skills (`.claude/skills/` inside a repo) sync only when the user asks.
