---
name: delegate-worker
description: Delegate code writing and research to a worker CLI (Codex/GPT-5.6 first, Grok 4.5 fallback); the host stays architect and reviewer. Fire whenever code is about to be written or changed, at any size, whenever a research/web-investigation task is about to be dispatched, or when the user mentions delegation (codexにやらせて, delegate to codex/grok). Skip silently only when no worker is authenticated or the change falls under the tiny-edit exemption.
metadata:
  short-description: Delegate coding to a worker CLI
---

# Delegate to a worker

The host is the **lazy senior**: it decides what to build, writes the spec, reviews the diff — and writes no implementation code itself while a worker is available. The worker executes the spec headless. Decisions never cross that line — only well-specified execution does.

## Gate — pick the session's worker

Once per session, before first delegation:

1. Probe Codex: `codex exec --skip-git-repo-check "say ok"` — an auth or credit error disqualifies it.
2. If Codex fails, probe Grok: `grok -p "say ok" --max-turns 1`.
3. First worker that answers is the worker for the whole session. Both fail → do the work yourself, tell the user which probes failed (setup: [SETUP.md](SETUP.md)), and don't re-probe this session.

## Delegate or keep

Every edit goes to the worker — do not weigh "is this substantial enough". So does every research/web investigation (user directive 2026-07-18): running one in the host's own context burns host-tier tokens and defeats the skill's purpose.

The one exemption — **tiny edits**: roughly ≤10 changed lines in files already read into context, introducing no new logic (typo, rename, config value, one-guard fix). There the spec would restate more context than the diff itself contains; edit directly.

Keep judgment, always: architecture and API design, deciding *what* to change in code touching security/money/data-deletion (the worker may still type the change from an exact spec), debugging that needs conversation context, and final review.

## Lanes

Pick a lane by one test — not size or file count, but whether the request's essence completes as **one change**:

- **Express** — one change → one spec, one worker. Most delegations.
- **Fan-out** — the request decomposes into independent subtasks → one spec per subtask, all workers launched together in the background. Fan out only specs whose file sets are disjoint; specs that overlap run serially instead. Each worker's output is reviewed on its own.

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

`-o` captures the worker's final message so you never re-read its full transcript. Run it in the background for anything non-trivial and keep working. Never use `--dangerously-bypass-approvals-and-sandbox`; `workspace-write` plus review covers every legitimate case.

Pick `<model-flags>` by classifying the **delegated subtask** (not the parent task) on the `adaptive-effort` ladder:

| Tier | Model flags |
|---|---|
| Mechanical | `-m gpt-5.6-luna -c model_reasoning_effort='"low"'` |
| Routine | `-m gpt-5.6-terra -c model_reasoning_effort='"medium"'` |
| Hard | `-m gpt-5.6-sol -c model_reasoning_effort='"high"'` |

A stronger worker means fewer correction round-trips, and each round-trip costs host review tokens — so implementation with real correctness pressure is Hard even when the design is settled.

Grok fallback invocation and its silent-cancel gotcha: [GROK.md](GROK.md).

## Run — research (web)

Investigation with no file edits runs the same pipeline with web search on and the default read-only sandbox (no `-s workspace-write`):

```bash
codex exec --skip-git-repo-check -c tools.web_search=true \
  <model-flags> -o <scratchpad>/worker-last.md - < <spec>
```

`--search` fails to parse under `exec`; the config key is the working form (verified 2026-07-18).

The research spec still stands alone: the question, sources to prioritize, and what "answered" looks like — facts separated from inference, each claim with a source URL. Review = spot-check the load-bearing claims, not every line.

Fallback when the task genuinely needs the host session's own tools (MCP servers, artifact access): do that part yourself.

## Review

The delegation is not done until this passes:

1. **Pre-review** — diffs over ~150 changed lines get a cheap cross-model pass before the host reads anything. A second worker from a *different model line* than the writer (Luna wrote → Sol reviews; Sol wrote → Luna reviews), low effort, default read-only sandbox:

   ```bash
   codex exec -C <project-root> --skip-git-repo-check \
     -m <other-line> -c model_reasoning_effort='"low"' \
     -o <scratchpad>/review-NN.md \
     "Run git diff and review it against the spec at <spec>. List concrete defects only — file:line and what breaks. Reply CLEAN if none."
   ```

   Defects → resume the writer with the list, re-review. Two rounds max, then the host takes over regardless. Pre-review filters correction round-trips; it never replaces the steps below.
2. Read the diff — `git diff --stat`, then the changed hunks, not whole files. A run that "finished" with no diff means the worker died silently — check its last message, then [GROK.md](GROK.md)/[SETUP.md](SETUP.md) for the failure modes. UI changes: judge the rendered screen too, not the diff alone.
3. Run the acceptance commands yourself. Neither the worker's "tests pass" nor the pre-reviewer's CLEAN counts for anything.
4. Small fixes: apply directly. Structural misses: resume the worker's session with a correction (`codex exec resume --last "<correction>"`) — don't restart from scratch.
5. Report what the worker changed, what the host fixed, and the verification results — labeled as such.

Escalation ladder, climbed only when a Hard delegation fails review twice on the same defect:

1. Resume the worker once at `'"xhigh"'`.
2. Still failing → take the work back and fix it directly in the host session.
3. Defect resists a single-context fix (heisenbug, cross-cutting interaction) → fan out independent diagnosis runs yourself, fix, then adversarially verify. This rung spends host tokens freely; it is justified exactly because two worker passes and an xhigh pass already failed. (User standing-approved this rung 2026-07-16.)
