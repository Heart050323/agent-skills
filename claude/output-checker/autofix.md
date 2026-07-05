# --autofix — Self-Correction Loop (自己修正ループ)

Triggered when ARGUMENTS contain `--autofix` or the caller requests self-correction. Instead of only reporting, run this loop.

## Loop protocol

1. **Review** — run the normal Step 1–4 review. Collect all 🔴 and 🟡 findings.
2. **Fix** — for each 🔴/🟡: apply the fix directly with the **Edit** tool, and log `✏️ FIXED | {location} | {description}`.
3. **Re-review** — re-read the modified file(s) and run the review again from scratch. If new 🔴/🟡 appear (including regressions), return to step 2. Cap at **3 iterations** to prevent infinite loops.
4. **Final report**:

   ```
   ══════════════════════════════════════
   Self-Correction Loop: {N} iteration(s)
   ══════════════════════════════════════
   ✏️ FIXED     | {count} issues fixed
   🔴 REMAINING | {count} unresolved critical (if any)
   🟡 REMAINING | {count} unresolved warnings (if any)
   ✅ RESULT    | PASS / FAIL
   ══════════════════════════════════════
   ```

   - **PASS**: zero 🔴 and zero 🟡 remaining.
   - **FAIL**: at least one 🔴 or 🟡 remains after 3 iterations.

## Rules for the fix step

- Only fix what is clearly wrong. Never apply 🔵 changes — they're informational.
- Preserve the author's intent and style. Minimal diffs only.
- If a fix needs architectural change beyond a simple edit (e.g. rewriting a class), do NOT auto-fix — report it as 🔴 REMAINING with what needs to change.
- ARCHITECTURE findings (ARCH VIOLATION / ARCH RISK) are structural — always report as REMAINING, never auto-fix.
