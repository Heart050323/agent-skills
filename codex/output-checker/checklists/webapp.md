# WEBAPP checklist

Layers on top of [`code.md`](code.md) — run that first. These checks simulate real user behavior to catch bugs static code review misses. The spine applies hard here: **trace**, don't eyeball — write out concrete values at every step.

Labels: 🔴 SCENARIO FAIL · 🟡 EDGE CASE · 🔵 UX (severity scale in SKILL.md).

## 1. Scenario-based functional testing

Trace each user flow with **concrete data**. For each scenario, write the exact values at each step:

```
Scenario: [user action]
Input:    [concrete values]
Expected: [what should happen]
Actual:   [trace through the code — what DOES happen?]
Verdict:  ✅ PASS / 🔴 FAIL (explain discrepancy)
```

Minimum scenarios:

- **Happy path** — normal usage with typical data
- **First-use / empty state** — zero data, first interaction
- **Day-one edge case** — actions on the start / creation date
- **Boundary values** — 0, 1, max, exactly-at-limit
- **Time-sensitive logic** — midnight, timezone boundaries, date rollover
- **Negative / impossible inputs** — NaN, negative, absurdly large

## 2. Data flow & state consistency

- Does data written to storage (IndexedDB, localStorage, API) match what's read back?
- Race conditions between concurrent reads/writes?
- After an import/export roundtrip, is data identical?
- Do computed (derived) values stay consistent with source data?

## 3. Calculation verification

For any formula in the app, **plug in 3+ concrete examples** and verify the output:

```
Example 1: calc(100, 5, "2026-01-01", "2026-12-31") → expected X, actual Y
Example 2: calc(1, 1, "2026-02-26", "2026-02-26")   → expected X, actual Y
Example 3: calc(50, 50, "2026-01-01", "2026-06-30") → expected X, actual Y
```

## 4. Cross-component consistency

- Do different screens showing the same data agree? (home card vs. detail page)
- If a value updates on one screen, does it reflect everywhere?
- Are loading / error states handled on all screens?

## 5. Mobile & PWA

- Touch targets at least 44×44px?
- Layout works at 320px width? Any horizontal scroll?
- PWA manifest: do icon paths resolve with the base path?
- Offline: does the service worker cache critical assets?

## 6. Timezone & locale

- All date operations on the same timezone (local vs. UTC)?
- String-based date comparisons (`"2026-01-01" >= "2025-12-31"`) correct?
- Correct behavior at midnight local time?
