# Architecture review

Use for the boundaries and state transitions identified in SKILL.md. Trace the relevant contracts and failure paths; a search match is a lead, not a verdict. Apply the severity and uncertainty rules in SKILL.md.

## Data contracts

Check the actual shapes crossing module, service, or trust boundaries. Trace a representative value from producer to consumer; examine runtime validation where untrusted input enters. Flag a concrete mismatch or reachable unsafe input, not the mere presence of `any` or `JSON.parse`.

## Ownership and coupling

Identify who owns shared facts and business rules. Check whether a change could leave competing values inconsistent. Similar code with different reasons to change need not be merged. Import counts and dependency depth are investigation hints, not failure thresholds; report the actual unwanted dependency or change propagation.

## Dependency direction

Trace suspected cycles and show their consequence, such as initialization failure or broken layering required by the project. Do not impose one universal layering pattern. Use an existing dependency tool when helpful; a new analyzer is not required for every review.

## Retries and persistent effects

Inspect operations that can be delivered or executed more than once. Trace retries, concurrent requests, partial failure, and recovery. Determine where deduplication or transactional protection belongs; inserts are not universally wrong and an UPSERT is not universally sufficient. Verify protection against duplicated effects with disposable fixtures or a static trace, not live charges or messages.

## Mutable state

Look for conflicting owners, stale derived values, races, and reachable invalid states. Report a concrete inconsistent transition. Counts of boolean fields, `let`, or `useState` are not defects by themselves.

## Verification

Use tests, contract checks, or concrete traces for the boundaries at risk. Missing automated tests are a coverage limitation unless a stated requirement mandates them or a specific defect is demonstrated. Do not assign a universal numeric stability score. Summarize the boundaries checked, findings, and remaining uncertainty.
