# Optional motion patterns

Use only for a brief that benefits from scroll choreography. Select the project's existing animation stack where possible and check its current API before implementing a pattern.

- **Sticky stack:** cards accumulate in a pinned region. Derive distances from measured card and container sizes; recompute when fonts or images load and on relevant resize. Provide a readable linear layout on narrow screens and under reduced motion.
- **Horizontal pan:** vertical scroll reveals a wide sequence. Derive travel from actual overflow; keep keyboard focus and reading order usable. Avoid trapping scroll. A normal horizontally scrollable list may serve the task better.
- **Entry sequence:** briefly introduce related content with small staggered offsets. Avoid delaying the primary message or hiding content before JavaScript initializes. Reduced-motion mode should show the final content without waiting.

Keep element ownership clear when combining tools; avoid multiple systems writing the same transform. Release timelines, observers, and listeners when the component unmounts. Test interruption, navigation away/back, viewport changes, and the static fallback. Prefer transforms and opacity when suitable, but validate actual performance rather than assuming a property guarantees smoothness.
