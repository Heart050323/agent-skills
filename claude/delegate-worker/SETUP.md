# Worker setup

Read this file only after `SKILL.md` chooses delegation.

## Codex (primary)

1. Install: `brew install codex`
2. Authenticate: `codex login` with the ChatGPT account that holds the subscription; inside Claude Code, run `! codex login`. Use `codex login --with-api-key` for API billing.
3. Check authentication once per host session without invoking a model:

   ```bash
   codex login status
   ```

Let the first real delegated task test credits and model availability; do not spend a separate model call on `say ok`. An authentication, credit, or unavailable-model error disqualifies Codex. A host safety, permission, or data-transfer denial blocks delegation for the task; do not use another worker to bypass it.

## Grok (fallback)

1. Install: `brew install --cask grok-build`
2. Authenticate: `grok login`; inside Claude Code, run `! grok login`. Alternatively set `XAI_API_KEY` for API billing.
3. Probe: `grok -p "say ok" --max-turns 1`.

Use Grok only when the Codex check or first real task fails for authentication, credit, or model availability. Invocation and permission details are in [GROK.md](GROK.md).
