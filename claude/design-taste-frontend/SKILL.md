---
name: design-taste-frontend
description: Design landing pages and portfolios with a deliberate visual direction, coherent implementation, verified content, and checks appropriate to the brief.
---

# Design a distinctive landing page

Use for landing pages and portfolios where the brief calls for a deliberate visual direction. For an existing product interface, start with its tasks, brand, and constraints; use the narrower redesign workflow when appropriate.

## Establish the direction

Infer audience, primary action, content, assets, tone, and technical constraints from the brief. Clarify only choices that materially change the result and cannot be inferred. Explain the chosen direction briefly, then implement it. Do not turn the design process into a questionnaire or assign arbitrary style scores.

Choose visual density, amount of motion, and layout variation to suit the content. A service information page may benefit from a conventional grid; an expressive portfolio may benefit from an editorial composition. Existing fonts, icons, centered headings, and simple layouts are valid choices.

## Build within the project

- Preserve the requested stack, brand identity, meaningful content, and working interactions. Inspect installed packages and conventions before adding dependencies.
- Use a coherent type scale, spacing, and semantic color tokens. Confirm fonts support the languages in the content. Support the themes actually requested; a dark-mode toggle is not mandatory for every page.
- Structure the page around a real message and next action. Use supplied or verified names, prices, metrics, dates, and testimonials. Clearly mark fictional demo data and keep it separate from production facts.
- Choose imagery for its informational role. Avoid unrelated placeholders standing in for actual products, people, or properties. Keep source/license information needed for reuse.
- Implement meaningful focus, hover, pressed, loading, empty, and error states where relevant. Keep controls usable by keyboard and touch. Prefer semantic HTML and a logical reading order.
- Select viewport sizing for the behavior required, then test browser chrome and narrow screens. Do not prescribe a single viewport unit or layout primitive for all cases.
- Use motion to explain changes or support the chosen expression. Keep essential content visible when animation fails or is reduced. Reuse the installed animation approach and clean up observers, listeners, and timelines on unmount.

## Conditional references

- Selecting a concrete UI/motion example or implementing a supplied reference: use [reference-driven-ui](../reference-driven-ui/SKILL.md), then return to this page-level brief.

- Choosing a named design system or checking an API: use [official sources](references/official-sources.md), then read the current documentation for the selected system. Do not load or install every system in the list.
- A brief that needs scroll-linked choreography: read [motion patterns](references/motion-patterns.md). Choose a pattern because it serves the page, not to satisfy an animation quota.

## Finish

Inspect representative narrow and wide layouts and relevant interaction states. Check overflow, text wrapping, image loading, contrast, visible focus, reduced motion, and the primary action. Use actual render/interaction evidence when available and distinguish it from static review. Complete the requested artifact and report material limits; do not require a deployment, a new component library, or a new theme outside the task.
