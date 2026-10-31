---
name: redesign-existing-projects
description: Improve an existing website or app through targeted, evidence-based UI changes while preserving its brand, real content, stack, and working behavior.
---

# Improve an existing interface

Use for a requested redesign or targeted UI improvement. Start with the affected pages, current stack, design tokens, real content, and the user's intended outcome. Preserve working navigation, data contracts, brand assets, and interactions.

Identify concrete problems before choosing visual changes: unclear hierarchy, difficult reading, broken responsive layout, missing states, inaccessible controls, or inconsistent components. A familiar font, equal-column grid, or flat surface is not a defect by itself. Prioritize problems that block the user's task, then coherence and polish.

## Change and check

- Reuse the current framework, styling conventions, and available components. Make focused changes; do not migrate the stack for a visual refresh.
- Keep names, prices, metrics, dates, claims, and testimonials faithful to their sources. Use clearly identified fictional data only for an explicitly fictional demo; never randomize real values to look authentic.
- Choose typography, spacing, density, and color for the content and brand. Treat decorative depth, asymmetry, alternate fonts, and motion as optional techniques, not quality gates.
- Check responsive reading order, text wrapping, contrast, focus, keyboard interaction, and relevant loading, empty, error, and success states. Decorative images may have empty alt text; meaningful images need an appropriate description.
- Preserve supported themes. Add another theme, legal pages, or new flows only when within the request. Existing content should remain usable without decorative animation; respect reduced motion.
- Confirm imports and installed versions before adding a dependency. Validate changed behavior and inspect representative rendered sizes when browser access is available; report static-only review as such.

## Adapting a reference component

For a supplied example or a request to find an interactive pattern, use [reference-driven-ui](../reference-driven-ui/SKILL.md). Its source-specific guides cover Lucian catalogue lookup, motion comparison, code inspection, theme mapping, lifecycle adaptation, attribution, and integration checks. Keep the redesign's original scope and real application behavior.

Finish with the user-visible changes, the evidence used to check them, and material limitations. Do not call a design better solely because it has more animation or a different font.
