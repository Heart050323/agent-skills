---
name: output-checker
description: "Review a specified artifact or change for correctness and quality when a second opinion or quality check is needed. Report evidence-backed findings and unverified checks; edit only when fixes are requested."
metadata:
  short-description: Review generated outputs critically
---

# Output Checker

Review the requested artifact against its intended use. Preserve the distinction between a demonstrated defect, an unanswered question, and a style preference.

## Scope and evidence

Use the supplied target; otherwise identify the most recent relevant artifact in the conversation. State the target and intended outcome briefly. For a diff review, start with changed behavior and follow dependencies only as needed to assess it. Expand to a full audit when requested or when evidence shows a wider problem.

Every finding needs a location, concrete impact, evidence, and a fix or next step. Evidence can be an executed check, a reproducible calculation, a code/data trace, or an authoritative source. Label static traces as traces; do not present them as runtime tests. A grep match, import count, missing test suite, or personal preference alone does not establish a defect.

For disputed external facts, consult relevant primary sources. Prefer supplied/local evidence for claims about this project. If a material claim cannot be resolved, report it as **not verified**, with the missing evidence, rather than inventing a correction. Do not impose a quota of searches or findings.

## Select relevant checks

Read only the checklists needed by this review. A small copy edit does not require a code or architecture audit.

- Code behavior → [code](checklists/code.md).
- Argument, accuracy, or prose quality → [writing](checklists/writing.md).
- Document, deck, spreadsheet, or PDF structure and appearance → [file](checklists/file.md).
- Derivations or quantitative claims → [math](checklists/math.md).
- Browser interactions or rendered UI → [webapp](checklists/webapp.md), plus relevant code checks.
- Changes to service boundaries, shared contracts, dependency direction, persistent state, or retry behavior; or an explicit architecture review → [architecture](checklists/architecture.md). File count and ordinary internal imports do not trigger it by themselves.

Check applicable risks with representative cases. Distinguish checked, not applicable, and not checked; summarize only material coverage limits in the report. Use existing test results for unchanged behavior when still applicable. Re-run affected checks after changes; broaden when failures or new evidence justify it.

## Findings and verdict

- 🔴 **Must fix**: demonstrated failure that blocks the intended outcome or creates material harm.
- 🟡 **Should fix**: evidence-backed defect or concrete risk with a stated triggering condition and impact.
- 🔵 **Optional**: preference or polish; never a prerequisite for passing and never automatically fixed.
- **Not verified**: evidence or access is missing. Keep this separate from defect severity; do not auto-fix an uncertainty.

Use: `{severity} | {location} | {impact and trigger} | {evidence} | {fix}`. Order actual findings by impact; avoid a section for every irrelevant category.

Report what was reviewed, findings, checks performed, and material limits. Say “no issues found in the checked scope” when appropriate; do not imply exhaustive correctness. Use **PASS** only when required checks are complete and no 🔴/🟡 findings remain. Use **ISSUES FOUND** for unresolved defects, **INCOMPLETE** for material checks blocked by missing evidence, or **ISSUES FOUND + INCOMPLETE** when both apply. Keep optional suggestions separate. Respond in the user's language unless they request another.

## Requested fixes

Review alone does not imply edits. When the user requests fixes or `--autofix`, follow [autofix.md](autofix.md). The separate output-check-fix-loop skill uses the same protocol.
