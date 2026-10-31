---
name: token-efficiency
description: Reduce unnecessary context and tool output for large files, logs, or broad exploration; compare model/effort settings when the user asks about cost or latency. Preserve correctness evidence.
version: 2.2.0
---

# Token Efficiency

Default to frugal unless the user explicitly asks for full contents or verbose output. Every rule below is one move: **look at the smallest slice that answers the question.**

## Diagnose overhead

Use available usage measurements to distinguish repeated input, generated output, tool output, cache behavior, and retries. A long session or large output is a lead to investigate, not proof of a particular cost share. Preserve needed continuity; do not promise that restarting or delegating is cheaper without a relevant comparison.

## Reading

- Never read a whole file to answer a narrow question — Grep for the symbol, then Read only the relevant range (offset/limit).
- Check cheap metadata first: `wc -l`, `git status --short`, `ls`, package manifests.
- Logs: `tail -100` or `grep -i error` — never the whole file.
- Structured data (JSON/CSV): `jq '.key'`, `head -20` — extract fields, don't dump.

## Exploring

- Broad multi-file questions ("how does X work here?") → search the relevant symbols and boundaries first. Consider authorized delegation only when its reduced context load outweighs coordination and verification costs.
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

For a requested cost, latency, or model-setting comparison, read [model/effort comparisons](references/model-effort.md). Ordinary tasks do not need a model-selection preflight.
