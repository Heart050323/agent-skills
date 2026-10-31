---
name: output-check-fix-loop
description: "Review and fix a specified artifact with output-checker, rechecking affected behavior for up to three correction rounds. Use when the user requests iterative correction; report unresolved defects and incomplete checks."
argument-hint: "[対象の出力 / ファイルパス / 直前の成果物]"
metadata:
  short-description: Iterate on output-check findings
---

# Output Check Fix Loop

Use the supplied target, or the most recent relevant artifact in the conversation. This skill requests both review and correction.

Read [output-checker](../output-checker/SKILL.md) and follow its [bounded correction protocol](../output-checker/autofix.md). That protocol owns severity, fix scope, the three-round limit, stopping conditions, verification, and the final verdict. Do not start a nested second loop or reset the round count by invoking --autofix again.

Report fixes, checks, remaining defects, and unverified items. Stop when the requested scope passes, or when the shared protocol reaches a stop condition. Missing evidence is not a confirmed defect and cannot be fixed merely to obtain a clean verdict.

## Codex 向けメモ


- `$output-checker` を最後の一回だけ使うのではなく、各修正ラウンドの判定役として使う
- 反復の途中では、短く進捗を共有しつつ実作業を止めない
- 問題が消えたら、最後に「何を直したか」「何で確認したか」「残件があるか」だけを簡潔に報告する
