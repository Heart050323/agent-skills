---
name: delegate-worker
description: Delegate a bounded implementation, investigation, or review when authorized and useful; keep work needing host-only tools in the current session.
metadata:
  short-description: Delegate work to a CLI
---

# Delegate a bounded task

Use a worker only when delegation is authorized and has a concrete benefit, such as independent review, useful parallelism, or context isolation. Ordinary small edits and work requiring this session's browser, account, or tools usually belong in the host.

Read [SETUP.md](SETUP.md) to check an existing CLI and its supported options. Keep the user's configured model by default. For an explicit model or effort comparison, check current supported controls and measure a representative workload; do not hardcode a cheapest-model ladder.

Give the worker a goal, the minimum necessary context, exact permitted files, constraints, and observable acceptance criteria. Keep concurrent writers on disjoint files or isolated worktrees. Permission and data-access limits carry over to workers.

For an installed Codex CLI whose help confirms these options:

```bash
codex exec -C <project-root> -s workspace-write --json \
  -o <scratchpad>/worker-result.md - < <spec-file> \
  > <scratchpad>/worker-events.jsonl
```

Use `-s read-only` for inspection. Add model, search, or repository-check options only when needed and supported by the installed version. Never bypass approval or sandbox controls. A worker's unavailable model, login, or credit failure is not a reason to install or switch providers automatically; keep independent work local and report the blocker. Do not route a denied operation through another worker.

Record the session ID returned by the CLI before starting another run. Resume that ID for corrections, never an ambiguous last session. If the worker ends without the expected artifact or diff, inspect the failure; an exit code alone does not prove completion.

Review the actual diff and acceptance evidence. Run checks proportional to the changed behavior, and inspect rendered UI when appearance matters. Request another independent review when the risk warrants it, not because a line-count threshold was crossed. Do not reset an unproductive loop by switching models: after two failed corrections without new evidence, diagnose in the host or report the specific blocker. Report what changed, what was verified, and what remains uncertain.
