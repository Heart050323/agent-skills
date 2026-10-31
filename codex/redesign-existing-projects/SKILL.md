---
name: redesign-existing-projects
description: Improve an existing website or app through targeted, evidence-based UI changes while preserving its brand, real content, stack, and working behavior.
metadata:
  short-description: Upgrade existing sites to premium
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

When a requested upgrade benefits from an existing interactive example, identify the exact insertion point or component being replaced before porting it. Preserve that component's actions, data, and states while changing its presentation.

- Inspect the example's working HTML/CSS/JS and the host framework, styling, and theme setup. Port it into the host's component lifecycle; standalone script initialization is not automatically suitable for a framework component.
- Map reference color tokens to the project's semantic theme variables instead of adding a second palette. Keep selectors scoped to the component and verify it in every supported theme.
- Exercise pointer, touch, keyboard, visible focus, and reduced-motion behavior in the integrated component. A source library's accessibility claim is a starting point, not a substitute for checking the port.
- Record the source element URL, relevant source revision when available, and retained license notices. Report what changed and what could not be verified.

[Lucian UX/UI Prompt](https://github.com/Seokwoooo/lucian-uxui-prompt) is one optional source of interactive examples. Its README documents per-element links, scoped selectors, and mapping `--ux-*` tokens into a host theme. The [MIT license](https://github.com/Seokwoooo/lucian-uxui-prompt/blob/main/LICENSE) requires preservation of the copyright and permission notice when copying covered code; retain the gallery's source credit as well. Reviewed 2026-10-14 at repository revision `42396145b375a17712fd738ca0e1d977556c0b73`. Use only a component that serves the brief; this reference does not require installing its separate skill or executing its build scripts.

Finish with the user-visible changes, the evidence used to check them, and material limitations. Do not call a design better solely because it has more animation or a different font.
