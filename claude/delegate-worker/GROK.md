# Grok fallback

Used only when the Codex probe fails (see SKILL.md Gate).

## Run

```bash
grok --cwd <project-root> --prompt-file <spec> \
  --permission-mode auto \
  --allow 'run_terminal_command' --allow 'read_file' \
  --allow 'write_file' --allow 'edit_file' \
  --reasoning-effort <effort> --check --max-turns 40
```

Grok has one model (grok-4.5), so effort is the only dial: Mechanical → `low`, Routine → `medium`, Hard → `high` (same ladder as SKILL.md).

Corrections after review: `grok -c -p "<correction>"` (continues the last session in that cwd). Parallel independent specs: add `-w <name>` per run (git worktree isolation), merge after review. Never `bypassPermissions` or `--always-approve`.

## Silent-cancel gotcha (verified 2026-07-15/16)

Headless Grok cannot answer permission prompts: a blocked tool cancels the whole run with exit 0 — one narration line, no file changes, no error. The `--allow` set above is the known-reliable minimum; `run_terminal_command` alone was not enough for tasks involving `npm install`. If a run still ends after one line with no diff, rerun with `--debug-file <path>` and grep it for `PermissionCancelled` to find which tool to `--allow`.
