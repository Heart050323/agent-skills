# Bounded correction loop

Use only when fixes or self-correction are requested. Use this protocol for output-checker --autofix or a request to review and fix.

1. Review the requested scope using SKILL.md. Separate confirmed findings from missing evidence and optional suggestions.
2. Fix supported 🔴/🟡 findings with the smallest change that preserves the intended behavior. Do not change content merely to eliminate an uncertainty. Leave optional suggestions alone unless requested.
3. Recheck each fix and affected behavior, including plausible regressions. Reuse still-valid evidence for unaffected areas. Perform a final coverage check against the original request; do not repeatedly run unrelated suites merely to make the report green.
4. Stop when required checks pass and no supported defects remain, or after **3 correction rounds**. Stop earlier on repeated failure without new evidence, oscillation, or when all remaining work is blocked. A blocked item does not stop independent fixes.

A small, verified architecture fix may be appropriate; the category name alone is not a blocker. A broad redesign or change to product intent outside the request remains a proposal. Keep a log of changes and the checks that verify them.

Final report: rounds used; fixes; evidence; unresolved defects; unverified checks; and why the loop stopped. Use PASS / ISSUES FOUND / INCOMPLETE / ISSUES FOUND + INCOMPLETE as defined in SKILL.md. Never turn missing test access into PASS, and never count lack of access itself as a proven code defect.
