# Web app review

Apply relevant code checks alongside browser-specific checks. Use available browser tools for actual interaction and rendering when needed. A code trace can support a logic finding, but does not verify the rendered UI.

## Scenarios

For changed flows, choose representative user actions and state the input, expected behavior, observed behavior, and evidence method. Include normal use plus applicable failure or boundary cases. Date rollover belongs to date-dependent features; negative numbers belong to numeric inputs. Do not force every scenario onto every app.

## State and calculations

- Follow relevant writes and reads across component state, storage, and APIs; check races and round trips where those operations exist.
- Compare screens that show the same changed data and exercise applicable loading, empty, and error states.
- Independently recompute meaningful calculation cases, choosing boundaries that could reveal a defect rather than filling a fixed example quota.

## Rendering and access

- Inspect affected layouts at relevant narrow and wide widths; check overflow, focus visibility, keyboard use, and touch interaction where supported.
- Check motion preferences for animated changes and ensure content and actions remain available with reduced motion.
- Check PWA manifests, caches, and offline behavior only if the app implements or requires them.
- Verify timezone and locale behavior where the feature depends on dates, times, numbers, or translation.

Report unavailable browser or device checks as unverified. Do not claim visual correctness from source inspection alone.
