---
name: output-check-fix-loop
description: "Review and fix a specified artifact with output-checker, rechecking affected behavior for up to three correction rounds. Use when the user requests iterative correction; report unresolved defects and incomplete checks."
disable-model-invocation: true
model: opus
allowed-tools: ["Read", "Glob", "Grep", "Edit", "Bash", "WebSearch", "WebFetch", "Task"]
---

# Output Check Fix Loop

Use the supplied target, or the most recent relevant artifact in the conversation. This skill requests both review and correction.

Read [output-checker](../output-checker/SKILL.md) and follow its [bounded correction protocol](../output-checker/autofix.md). That protocol owns severity, fix scope, the three-round limit, stopping conditions, verification, and the final verdict. Do not start a nested second loop or reset the round count by invoking --autofix again.

Report fixes, checks, remaining defects, and unverified items. Stop when the requested scope passes, or when the shared protocol reaches a stop condition. Missing evidence is not a confirmed defect and cannot be fixed merely to obtain a clean verdict.
