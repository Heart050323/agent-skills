---
name: token-efficiency
description: Apply token-frugal tool habits — filter before reading, delegate broad exploration, transform big files with bash. Use at the start of any task that reads files, runs commands, or explores a codebase, and when the user mentions token cost.
metadata:
  short-description: Minimize tokens reading/writing files
---

# Token Efficiency

Default to frugal unless the user explicitly asks for full contents or verbose output. Every rule below is one move: **look at the smallest slice that answers the question.**

## Reading

- Never read a whole file to answer a narrow question — search for the symbol with `rg`, then read only the relevant range (specific line numbers or sections).
- Check cheap metadata first: `wc -l`, `git status --short`, `ls`, package manifests.
- Logs: `tail -100` or `grep -i error` — never the whole file.
- Structured data (JSON/CSV): `jq '.key'`, `head -20` — extract fields, don't dump.

## Exploring

- Broad multi-file questions ("how does X work here?") → search directly with `rg` and read only matching sections, instead of reading files wholesale into context.
- Codebase overview: structure first (`rg --files`, `rg 'class|def|exports'`), then read only the sections that matter.

## Transforming

- Large data files: `sed`/`awk`/`python3 -c` — reading thousands of lines just to rewrite them wastes both directions.
- Copy/move/merge: `cp`/`mv`/`cat a b > c`, never read+write.
- Code files stay read + edit: the reviewable diff is worth the read.
- New files: write directly.

## Output

- Quiet flags by default (`-q`, `--silent`); `head`/`tail` on anything that can be long.
- Summarize command output and directory listings; don't relay raw dumps.

## Override

Ignore all of the above when the user asks for full output, when filtered output loses needed context (e.g. missing line numbers), or when deeply learning an unfamiliar codebase — there, read a few key files fully, then return to frugal mode.

For detailed bash patterns (safe globs, macOS/Linux sed differences, notebook manipulation), see [strategies.md](strategies.md).

The `$adaptive-effort` skill decides which model/effort tier runs the work; this skill decides how few tokens the work itself consumes.

## Codex 向けメモ

claude側 v2.1.0 (2026-07-16) の「Writing code — the biggest lever」節(実装を delegate-worker 経由で Codex/Grok に委譲する lazy senior 規則)は、Fable=オーケストレーター構成の専用規則のため、このポートには意図的に含めない — その構成では Codex 自身がワーカー側。
