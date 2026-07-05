# ARCHITECTURE checklist — Software Stability (6 Principles)

Layers on top of [`code.md`](code.md) or [`webapp.md`](webapp.md) when the target has 3+ files, project-internal imports, or DB/API interactions. These 6 determine long-term maintainability. Each has a **Check** — the grounding action (usually a grep/count); run it, don't judge from a read.

Labels: 🔴 ARCH VIOLATION · 🟡 ARCH RISK · 🔵 ARCH IMPROVE (severity scale in SKILL.md).

## P1. Schema / Types — are data shapes defined before implementation?

- Explicit type definitions exist and are shared across modules? (`types.ts`, `schema.prisma`, OpenAPI spec)
- API inputs/outputs validated at runtime? (Zod, Pydantic, JSON Schema)
- No type mismatches between modules? (e.g. age as `string` in one module, `number` in another)
- Date formats, naming conventions, required/optional fields consistent across boundaries?
- **Check**: grep for `any`, untyped params, raw `JSON.parse` without validation, inconsistent field names across files.

## P2. Normalization (DRY / SSOT) — is each fact stored in exactly one place?

- No duplicated constants, config values, or business rules across files? (magic numbers, hardcoded URLs, tax rates)
- Single Source of Truth for each config? (one `constants.ts`, one `.env`)
- A business-rule change (tax 10%→12%) requires editing only 1 file?
- **False DRY warning**: similar-looking code with different change reasons is NOT duplication — don't flag it.
- **Check**: grep for literal business numbers (`0.10`, `3000`), duplicated string literals, identical function bodies.

## P3. Coupling — are dependencies between modules minimal?

- Modifying one file doesn't force cascading changes to others?
- Modules communicate through interfaces, not internals? (no importing private helpers)
- No God file/class with multiple unrelated concerns?
- Dependency fan-out: **10+ project-internal imports in one module = red flag**.
- **Agent risk**: if a change requires understanding 15+ files at once, it exceeds the agent's effective working set — coupling is too tight.
- **Check**: count imports per file, look for cascading test failures and deep cross-module call chains.

## P4. DAG — do dependencies flow one-way without cycles?

- No circular imports? (A→B→A, directly or transitively)
- Consistent direction? (UI → Logic → Data → DB; never reverse)
- Dependency chain depth ≤5 levels?
- **Check**: trace import chains. Tools: `madge --circular`, `jscycles`, `eslint-plugin-import/no-cycle`, `dependency-cruiser`.

## P5. Idempotency — is every write operation safe to re-execute?

- Data writes use UPSERT / ON CONFLICT / unique-key pre-check?
- External API calls and webhooks carry idempotency keys?
- Batch/migration scripts have per-step "already done?" checks for safe resume?
- Financial ops and notifications guarded against duplicate execution?
- **Agent risk**: agents retry by nature (run→error→fix→re-run). Non-idempotent scripts + agent retry = compounding side effects.
- **Check**: grep for raw `INSERT` without conflict handling, API calls without idempotency headers, unguarded email/notification sends.

## P6. State Minimization — is mutable state kept to a minimum?

- No unnecessary global/module-level mutable state?
- Functions pure where possible? (same input → same output)
- Mutable state consolidated in documented, minimal locations? (one store, not scattered `let`s across files)
- **State explosion**: n boolean state vars in one component = 2ⁿ combinations to test. Flag when this becomes unmanageable.
- **Check**: grep for `let`, `var`, mutable globals. In React: many `useState` calls in one component suggest grouping into an object or switching to `useReducer`.

## Testing — validator of the 6 principles

- Are modules testable in isolation? (if not → coupling too tight)
- Do tests cover idempotency? (same operation twice → same result)
- Does one module's test failure stay isolated from unrelated modules?
- If no tests exist in a multi-file project: `🔴 ARCH VIOLATION | Testing | No automated tests — 6 principles unverifiable`.

## Summary line

End the ARCHITECTURE section with:

```
Stability: {X}/6 | Critical: {🔴 list or "None"} | At Risk: {🟡 list or "None"}
```
