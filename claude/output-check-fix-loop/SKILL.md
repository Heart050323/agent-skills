---
name: output-check-fix-loop
description: "Run output-checker in a fix loop — reviewing the target, editing every issue, and re-reviewing until it comes back green (zero 🔴/🟡)."
disable-model-invocation: true
model: opus
allowed-tools: ["Read", "Glob", "Grep", "Edit", "Bash", "WebSearch", "WebFetch", "Task"]
---

Drive `output-checker` in a loop until its review comes back **green** — zero 🔴 and zero 🟡 — then stop.

Target: $ARGUMENTS. If none, the target is the **most recent output in this conversation** (same default as output-checker).

This skill owns only the **loop**. The classification, checklists, severity scale, fix rules, and the Verify-don't-assume protocol all live in output-checker — [`SKILL.md`](../output-checker/SKILL.md) and [`autofix.md`](../output-checker/autofix.md). Follow those; do not restate them here.

## The loop

Repeat until **green** or a stop condition below fires:

1. **Check** — run a full output-checker review of the target (Step 1–4: classify → load the matching checklists → work every item). Collect every 🔴 and 🟡.
2. **Green?** — zero 🔴 and zero 🟡 → done; go to Report. Otherwise continue.
3. **Fix** — apply output-checker's fix rules (`autofix.md`): Edit each 🔴/🟡 with a minimal diff, never touch 🔵, and log `✏️ FIXED | {location} | {what}`. A finding that cannot be safely auto-fixed (needs an architectural change, or is an ARCH VIOLATION/RISK) is not forced — mark it **BLOCKED** and leave it.
4. **Loop** — return to step 1 with a **fresh full review**, not a re-check of only the edited lines. Regressions and new breakage count against green.

## Stop conditions (besides green)

- **Cap** — 5 iterations maximum.
- **Oscillation** — a finding reappears after being fixed, or the open-finding count stops dropping across two consecutive rounds → further looping won't converge.
- **All-blocked** — every remaining finding is BLOCKED.

On any non-green stop, report exactly what remains and why. Never declare green when it isn't.

## Report

```
══════════════════════════════════════
output-check-fix-loop: {N} iteration(s)
Stopped on: green / cap / oscillation / all-blocked
══════════════════════════════════════
✏️ FIXED    | {count}
🔴 REMAINING | {count}  {one-line each, with why unfixed}
🟡 REMAINING | {count}
✅ RESULT    | GREEN / NOT GREEN
══════════════════════════════════════
```

GREEN only when a fresh full review finds zero 🔴 and zero 🟡.
