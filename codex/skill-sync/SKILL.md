---
name: skill-sync
description: Synchronize requested personal skills between Codex and Claude while preserving host-specific controls and unrelated edits; publish only when GitHub updates are authorized.
metadata:
  short-description: Sync skills between Codex and Claude
---

# Skill Sync

Maintain the requested skills in the existing `~/agent-skills` repository: `codex/` and `claude/` are host-specific ports. Resolve the actual repository and install links before writing; do not assume another machine has this layout.

## Reconcile a bounded change

1. Read repository instructions, `git status`, the requested source and destination, and their diff. Record or back up the exact starting content. Preserve unrelated staged, unstaged, and untracked work.
2. Determine the source from the requested change, Git history, and content. Modification time is not evidence that one side is correct. If both contain unique changes, merge those changes; ask only about a substantive unresolved conflict.
3. Port the workflow and referenced resources. Preserve host-specific invocation policy, model/tool controls, and UI metadata. Tool-name substitution must preserve behavior: direct execution does not become mandatory delegation. Do not copy `.system/` or modify the host's bundled creator.
4. Check callers before merging or removing a skill. Update references and discovery descriptions, validate both ports, and inspect the resulting diff. Keep recoverable copies outside discovery paths when removing duplicate local installations. Inspect symlink targets before replacing anything.

## Publication

Local editing and cross-host synchronization do not themselves authorize publication. Use authorization already present in the conversation; do not ask again when GitHub updates are already requested.

Before an authorized push, fetch and compare the remote branch. Fast-forward only if it preserves local work. Resolve divergence from content and history, never timestamps or a force push. Stage explicit reviewed paths, including intended deletions, and inspect the staged diff so unrelated changes cannot enter the commit. Commit and push to the intended remote and branch; verify the remote commit before reporting success.

## Discovery and portability

Check `~/.agents/skills` and the configured personal skill directory for duplicate names. Keep a single maintained installation for each name; do not leave an obsolete copy discoverable. Preserve project-specific skills unless the request includes them.

For Codex, read the installed standard creator and its metadata reference before changing `agents/openai.yaml`. Keep existing automatic-selection policy unless the user requests a change. For Claude, preserve its supported frontmatter and use current host documentation when behavior differs. Do not assume a field in one host has an identical effect in the other.
