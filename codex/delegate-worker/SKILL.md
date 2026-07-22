---
name: delegate-worker
description: Delegate implementation or research from Codex to an isolated worker CLI when the user explicitly asks to delegate the current task, or when a cheaper worker, parallel execution, or context isolation gives a concrete benefit. Do not fire merely because delegation is discussed, for tiny edits, or for work requiring host-only tools.
metadata:
  short-description: Delegate work to a CLI
---

# Delegate to a worker

The host is the **lazy senior**: decide what to build, write the spec, review the result, and retain judgment. The worker executes a bounded task headlessly.

## 1. Pass the benefit gate

From a Codex host, delegate only when at least one condition is true:

- The user explicitly asks to delegate the current task.
- A cheaper worker tier can do the task without losing needed context.
- Independent context protects the host session from a broad implementation or investigation.
- Disjoint work can run usefully in parallel.

Keep the task in the host when delegation itself is only being discussed, the work is a tiny edit (roughly 10 changed lines or fewer with no new logic), the worker would use the same tier for a simple task, or the task needs host-only MCP tools or artifacts. Architecture, security/money/data-deletion decisions, conversation-dependent debugging, and final review always stay with the host; a worker may implement an exact decision.

The gate is complete when either one concrete delegation benefit is identified or the host keeps the task locally.

## 2. Select the session worker

Only after the benefit gate passes, follow [SETUP.md](SETUP.md) once for the session. Prefer Codex when its login check succeeds; let the first real delegated task test credits and model availability instead of spending a separate model call on `say ok`.

An authentication, credit, or unavailable-model failure disqualifies that worker. A host safety, permission, or data-transfer denial blocks delegation for that task; do not switch workers to evade it. If no worker is usable, do the work locally, report the failed check or denial once, and do not re-check this session.

## 3. Choose a lane

- **Express** — one bounded change or investigation: one spec, one worker.
- **Fan-out** — independent subtasks with disjoint file sets: one spec per subtask, launched together. Overlapping file sets run serially.

## 4. Write the spec

The worker is blind to the conversation. Write `<scratchpad>/worker-task-NN.md` with:

- **Goal** — what done looks like.
- **Files** — exact paths and conventions.
- **Constraints** — boundaries and forbidden changes.
- **Acceptance** — commands or evidence that must pass.

The spec is complete when a stranger with no chat history can execute it without making product or architecture decisions.

## 5. Run the worker

For implementation:

```bash
codex exec -C <project-root> --skip-git-repo-check -s workspace-write --json \
  <model-flags> -o <scratchpad>/worker-last-NN.md - < <spec> \
  > <scratchpad>/worker-run-NN.jsonl
```

Record the writer's `thread_id` from the `thread.started` JSON event in `<scratchpad>/worker-session-NN.txt` before launching another Codex run. Never correct a worker with `resume --last`; resume the recorded writer ID explicitly.

Choose the delegated subtask's tier, not the parent task's tier:

| Tier | Model flags |
|---|---|
| Mechanical | `-m gpt-5.6-luna -c model_reasoning_effort='"low"'` |
| Routine | `-m gpt-5.6-terra -c model_reasoning_effort='"medium"'` |
| Hard | `-m gpt-5.6-sol -c model_reasoning_effort='"high"'` |

Run non-trivial work in the background. Never use `--dangerously-bypass-approvals-and-sandbox`.

For web research with no edits, keep the default read-only sandbox and enable search:

```bash
codex exec --skip-git-repo-check -c tools.web_search=true --json \
  <model-flags> -o <scratchpad>/worker-last-NN.md - < <spec> \
  > <scratchpad>/worker-run-NN.jsonl
```

Require facts and inference to be separated and every load-bearing claim to carry a source URL. If the work needs host-session tools or artifacts, keep that part in the host. For Grok fallback details, read [GROK.md](GROK.md) only when Codex fails its login check or first real task for authentication, credit, or model availability.

## 6. Review

1. For diffs over roughly 150 changed lines, run a low-effort pre-review using a different model line from the writer. Record it as a separate session; it never replaces host review.
2. Read `git diff --stat`, then every changed hunk. For UI work, inspect the rendered screen.
3. Run the acceptance commands in the host. Worker claims and reviewer `CLEAN` are not evidence.
4. Apply tiny corrections directly. Send structural defects to the recorded writer:

   ```bash
   codex exec resume <writer-session-id> "<correction>"
   ```

5. Report worker changes, host corrections, and verification results separately.

The review is complete only when every changed hunk has been inspected and every acceptance item has passed or is reported as blocked.

If the same defect survives two Hard worker corrections, resume that writer once at `xhigh`; if it still fails, take the work back into the host. Use independent diagnosis fan-out only for a defect that resists a single-context fix.
