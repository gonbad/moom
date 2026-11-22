---
name: assets
description: Build and review the integrated gallery using the exact accepted visual sources.
---

# /assets

Read the project constitution and current status. Use the following references from `docs/references/`: `workflow.md`, `visuals.md`, `quality.md`.

Read the accepted visual inventory and source identities. Build a local gallery
under `./` by importing the accepted SVG paths, group hierarchy, IDs, CSS
classes and animations. Preserve originals and record any necessary namespacing or
clock-adapter mapping in `docs/living/assets.md`. Provide buttons for all
planned states and transitions plus play/pause/replay/seek, with original-source
comparison at the same viewport/pose/time.

Exercise every required transition, its reset and relevant reverse/interrupted path.
Specifically check limb pivots, stable body/head, duplicate IDs/selectors, scaling,
clipping and reduced-motion fallback. Raster fallbacks keep their declared limitations.
Fix geometry/rig defects here; do not postpone them to full-scene assembly. Record
technical evidence and explicit gallery acceptance, then freeze a Project-qualified
baseline tag or immutable snapshot/hashes. Hand off to `/animate` only after the
required asset baseline is accepted.
