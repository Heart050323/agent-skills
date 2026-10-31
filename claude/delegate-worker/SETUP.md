# Check the existing worker

Check whether the requested CLI is installed, then read its local `--help` and authentication-status command (for Codex: `codex exec --help` and `codex login status`). Do not run a paid model probe merely to test availability; the first authorized task can establish model access.

If installation or login is needed, follow the host's supported installation/secure-login flow and approval requirements. Never request API keys or passwords in ordinary chat. Do not install a fallback provider automatically or change security settings to make headless execution work.

Use supported controls from the installed version. Preserve the user's configured model unless a model change is requested or otherwise authorized. An unavailable worker does not prevent independent local work. Report blocked action, target, reason, and whether its outcome is known or uncertain; inspect an uncertain result before retrying.
