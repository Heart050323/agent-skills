---
name: find-skills
description: Discover and install agent skills from the npx skills / skills.sh registry. Use when the user explicitly wants to find, search for, browse, or install a skill — e.g. "find a skill for X", "is there a skill that does X", "install a skill to …". Do NOT fire on general "how do I / can you do X" questions unless they ask for a skill.
---

# Find Skills

Find a reusable skill when the user asks to discover or install one. Start with installed skills and the host's standard installer; avoid duplicating an existing capability.

Search the requested registry or original author's repository. Read the candidate's SKILL.md and relevant scripts before recommending it. Assess whether its scope, permissions, dependencies, maintenance, license, and concrete workflow fit the user's task. Stars and install counts can help discovery but do not establish correctness or safety.

Present a small set of relevant options with source URLs and meaningful tradeoffs. Distinguish search results from content actually inspected. If no candidate adds useful specialized knowledge, complete the task with the existing tools instead of adding a generic prompt.

When installation is requested, use the available installer or verify the current registry CLI instructions. An `npx` command can download and execute code; browsing a registry does not authorize that execution. Follow the environment's approval requirements, inspect the exact source/version, preserve existing local edits, and validate the resulting installation. Do not bulk-update unrelated skills or suppress required approval with convenience flags.

Registry for discovery: https://skills.sh/. Prefer the original repository as the source for inspection.
