# Worker setup

## Codex (primary)

1. Install: `brew install codex`
2. Authenticate: `codex login` (browser OAuth with the ChatGPT account that holds the subscription) — inside Claude Code, type `! codex login`. API-key alternative: `codex login --api-key <key>` (platform.openai.com, pay-per-token).
3. Verify: `codex exec --skip-git-repo-check "say ok"` prints a reply.
   - "workspace is out of credits" → logged into the wrong ChatGPT workspace/account; re-run `codex login`.

## Grok (fallback)

1. Install: `brew install --cask grok-build`
2. Authenticate: `grok login` (SuperGrok / X Premium+ OAuth) — inside Claude Code, `! grok login`. API-key alternative: `export XAI_API_KEY=xai-...` in `~/.zshrc` (console.x.ai, grok-4.5 $2/M in $6/M out).
3. Verify: `grok -p "say ok" --max-turns 1` prints a reply.
