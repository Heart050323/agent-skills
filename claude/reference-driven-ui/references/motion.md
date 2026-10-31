# Motion comparison with Takayu

Sources: [Motion Reference](https://motion-reference.takayustudio.jp/), [FLIP example](https://motion-reference.takayustudio.jp/#motion=flip-reorder), [site terms](https://takayustudio.jp/reference-network/terms.html). This is an independent reference site, not Apple documentation.

Search by purpose and feel, then inspect a candidate at normal speed and by frame stepping. Use onion-skin views to compare spatial paths and the A/B lab to vary one parameter at a time. Record the detail link, trigger, changed properties, duration/curve, and final state. Use the user's actual text where possible to expose wrapping and reading-time differences.

Treat displayed timing and generated CSS/WAAPI/GSAP/React examples as demo starting points. A schematic overall easing curve does not necessarily describe each object's velocity. Autoplay and seek controls do not establish correct behavior under repeated real input, cancellation, or focus changes.

For a reorder/FLIP implementation, use stable item identities, measure before and after the layout change, and animate the inverse displacement back to the final layout. Ensure semantic order and focus follow the intended result; do not leave the document permanently in a visually disguised order. Compare both normal and reduced-motion outcomes and test real content/resize rather than copying demo timings unchanged.

Viewing a reference or seeing a copy button is not a blanket reuse license. The site's terms, updated 2026-10-28, require checking the relevant source/content conditions for reused material. Distinguish studying an effect, independently implementing it, and copying source code; preserve notices or obtain permission where required.

Evidence: interactive FLIP controls were inspected on 2026-10-14. The public page and terms were re-read on 2026-10-31, but no fresh interactive browser session was available then. Re-open the relevant detail page during an actual implementation and mark unobserved playback accordingly.
