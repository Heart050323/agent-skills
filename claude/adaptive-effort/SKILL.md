---
name: adaptive-effort
description: Calibrate reasoning depth and model tier to task difficulty instead of running everything at maximum. Use when starting any task, when spawning subagents or workflows, and when the user mentions speed, cost, or overthinking.
version: 1.1.0
---

# Adaptive Effort

Effort is a budget, not a virtue. Before working, classify the task on the ladder and spend accordingly. Misclassifying down produces wrong answers, so when genuinely unsure go one tier up — but classify first; "unsure" is not the default.

## The ladder

| Tier | Signals | Spend |
|---|---|---|
| **Mechanical** | rename, reformat, copy edits, boilerplate, single-fact lookup, running a known command | Act directly. No extended deliberation, no exploratory reading beyond the target. |
| **Routine** | standard feature, bugfix with a clear repro, refactor within one module, docs | Brief plan, normal reasoning. Think through edge cases only where the code shows they exist. |
| **Hard** | architecture decisions, concurrency, security, debugging without a repro, perf work, anything where a wrong answer is expensive | Full reasoning depth. Verify conclusions before reporting; consider adversarial checks. |

Classify once per task, not per message. Re-classify only when the task changes shape — a routine bugfix that reveals a design flaw becomes hard.

## Delegation tiers

The caller's tier does not transfer to subtasks — a hard task is usually mostly mechanical subtasks. Decompose so the expensive tier only touches the genuinely hard part.

- **Agent tool**: `model: "haiku"` for mechanical fan-out (formatting sweeps, mass lookups), `"sonnet"` for routine implementation, omit (inherit) for hard work.
- **Workflow `agent()`**: `effort: 'low'` for mechanical stages (extraction, classification, formatting), omit for routine, `'high'` only for verify/judge stages where the run's correctness rides on it.
- **Worker CLI (`delegate-worker`)**: the delegated subtask's tier picks the worker model — the tier→model table lives in that skill's Run section.

## Session-level

When a long stretch of upcoming work is uniformly mechanical (mass renames, data cleanup), tell the user once that a lower model or effort setting would do it at a fraction of the cost — then continue at the current setting unless they switch.

The `token-efficiency` skill governs how few tokens the work consumes; this skill governs which tier does the thinking.
