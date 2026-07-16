---
name: delegate-worker
description: Delegate implementation work — writing code, refactors, test suites, multi-file migrations — to a worker CLI (Codex/GPT-5.5 first, Grok 4.5 fallback), keeping Claude (Fable) as architect and reviewer to cut Fable-tier token spend. Fire whenever a task involves substantial hands-on implementation, or when the user mentions delegation (codexにやらせて, grokに委譲, delegate to codex/grok). Skip silently when no worker is authenticated or the edit is small enough to do directly.
version: 1.3.0
---

# Delegate to a worker

Claude is the **lazy senior**: it decides what to build, writes the spec, reviews the diff — and writes no implementation code itself while a worker is available. The worker executes the spec headless. Decisions never cross that line — only well-specified execution does.

## Gate — pick the session's worker

Once per session, before first delegation:

1. Probe Codex: `codex exec --skip-git-repo-check "say ok"` — an auth or credit error disqualifies it.
2. If Codex fails, probe Grok: `grok -p "say ok" --max-turns 1`.
3. First worker that answers is the worker for the whole session. Both fail → do the work yourself, tell the user which probes failed (setup: [SETUP.md](SETUP.md)), and don't re-probe this session.

## Delegate or keep

Delegate execution: implementation from a settled design, mechanical refactors, tests against defined behavior, documented migrations across many files, first drafts Claude will review.

Keep judgment: architecture and API design, code touching security/money/data-deletion, debugging that needs conversation context, final review, and edits small enough that writing a spec costs more than doing them.

## The spec

The worker is blind to this conversation — the spec must stand alone. Write it to `<scratchpad>/worker-task-NN.md` with four sections:

- **Goal** — one paragraph of what done looks like.
- **Files** — exact paths to create or modify, and the conventions they follow.
- **Constraints** — what not to touch, dependencies not to add.
- **Acceptance** — commands that must pass (`npm test`, `tsc --noEmit`, …).

The spec is done when a stranger with no chat history could execute it.

## Run — Codex (primary)

```bash
codex exec -C <project-root> --skip-git-repo-check -s workspace-write \
  <model-flags> \
  -o <scratchpad>/worker-last.md - < <spec>
```

Pick `<model-flags>` by classifying the **delegated subtask** (not the parent task) on the `adaptive-effort` ladder:

| Tier | Model flags |
|---|---|
| Mechanical | `-m gpt-5.6-luna -c model_reasoning_effort='"low"'` |
| Routine | `-m gpt-5.6-terra -c model_reasoning_effort='"medium"'` |
| Hard | `-m gpt-5.6-sol -c model_reasoning_effort='"high"'` |

A stronger worker means fewer correction round-trips, and each round-trip costs Fable review tokens — so implementation with real correctness pressure is Hard even when the design is settled.

Escalation ladder, climbed only when a Hard delegation fails review twice on the same defect:

1. Resume the worker once at `'"xhigh"'`.
2. Still failing → take the work back and fix it directly in Fable.
3. Defect resists a single-context fix (heisenbug, cross-cutting interaction) → go **ultracode**: call the Workflow tool — independent diagnosis fan-out, fix, adversarial verify. This rung spends Fable tokens freely; it is justified exactly because two worker passes and an xhigh pass already failed. (User standing-approved this rung 2026-07-16.)

`-o` captures the worker's final message so you never re-read its full transcript. Background it (`run_in_background: true`) for anything non-trivial and keep working. Corrections after review: `codex exec resume --last "<correction>"` — don't restart from scratch. Never use `--dangerously-bypass-approvals-and-sandbox`; `workspace-write` plus review covers every legitimate case.

Grok fallback invocation and its silent-cancel gotcha: [GROK.md](GROK.md).

## Review

The delegation is not done until this passes:

1. Read the diff — `git diff --stat`, then the changed hunks, not whole files. A run that "finished" with no diff means the worker died silently — check its last message, then [GROK.md](GROK.md)/[SETUP.md](SETUP.md) for the failure modes.
2. Run the acceptance commands yourself. The worker's own "tests pass" claim counts for nothing.
3. Small fixes: apply directly. Structural misses: resume the worker's session with a correction.
4. Report what the worker changed, what Claude fixed, and the verification results — labeled as such.
