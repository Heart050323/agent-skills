---
name: token-efficiency
description: Apply token-frugal tool habits — filter before reading, delegate broad exploration, transform big files with bash. Use at the start of any task that reads files, runs commands, or explores a codebase, and when the user mentions token cost.
version: 2.1.0
---

# Token Efficiency

Default to frugal unless the user explicitly asks for full contents or verbose output. Every rule below is one move: **look at the smallest slice that answers the question.**

## Writing code — the biggest lever

Your own generated code is the most expensive token stream there is. Be the **lazy senior**: for any implementation beyond a small edit, fire the `delegate-worker` skill — write the spec, let the worker CLI (Codex/Grok) write the code, and spend your tokens only on the spec and the diff review. Reading rules below trim the input side; this rule cuts the output side, which is where most of the spend lives.

## Reading

- Never read a whole file to answer a narrow question — Grep for the symbol, then Read only the relevant range (offset/limit).
- Check cheap metadata first: `wc -l`, `git status --short`, `ls`, package manifests.
- Logs: `tail -100` or `grep -i error` — never the whole file.
- Structured data (JSON/CSV): `jq '.key'`, `head -20` — extract fields, don't dump.

## Exploring

- Broad multi-file questions ("how does X work here?") → delegate to an Explore subagent and keep only its conclusion, instead of reading files into your own context.
- Codebase overview: structure first (Glob, grep for `class`/`def`/exports), then read only the sections that matter.

## Transforming

- Large data files: `sed`/`awk`/`python3 -c` — reading thousands of lines just to rewrite them wastes both directions.
- Copy/move/merge: `cp`/`mv`/`cat a b > c`, never Read+Write.
- Code files stay Read + Edit: the reviewable diff is worth the read.
- New files: Write directly.

## Output

- Quiet flags by default (`-q`, `--silent`); `head`/`tail` on anything that can be long.
- Summarize command output and directory listings; don't relay raw dumps.

## Override

Ignore all of the above when the user asks for full output, when filtered output loses needed context (e.g. missing line numbers), or when deeply learning an unfamiliar codebase — there, read a few key files fully, then return to frugal mode.

For detailed bash patterns (safe globs, macOS/Linux sed differences, notebook manipulation), see [strategies.md](strategies.md).

The `adaptive-effort` skill decides which model/effort tier runs the work; this skill decides how few tokens the work itself consumes.
