---
name: adaptive-effort
description: "Compare model or reasoning-effort options for a concrete workload when the user asks to reduce cost or latency, or evaluate a settings tradeoff. Do not use as a preflight for ordinary tasks."
metadata:
  short-description: Match effort to task difficulty
---

# Adaptive Effort

Use for a concrete cost, latency, or model/effort selection decision. Ordinary tasks do not need a preliminary tier classification or routine advice to switch models.

## Compare a real workload

Identify the quality requirement, failure cost, latency target, and available budget. Use representative tasks and a current baseline. Separate model inference cost from tool latency, repeated context, retries, and review overhead; a cheaper model can cost more end to end if it needs more attempts.

When the host exposes model or reasoning settings, check the supported values and current documentation. Compare viable settings on the same success criteria. Report observed quality, elapsed time, and usage/cost when available; label estimates and missing measurements. Do not promise a savings percentage without evidence.

## Recommendations versus configuration

Instructions to “think less” or “use the cheapest model” are not proof that the host's configured model or reasoning setting changed. Preserve the user's chosen settings unless a supported control and authorization permit a change; report a change only after confirmation from that control. Do not hardcode a permanent cheapest-model hierarchy.

Assess delegation only when it is available and useful for the requested workload, including coordination and verification costs. This skill does not require spawning agents or installing a router. Keep the current setup when no measured benefit justifies changing it.

Finish with a specific recommendation and its evidence, or the smallest comparison that would resolve the uncertainty. Avoid a per-task tier announcement.

Sources: [reasoning effort and adaptive reasoning](https://developers.openai.com/api/docs/guides/reasoning), [scoped skill guidance](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra). Recheck supported controls and prices when making a recommendation.
