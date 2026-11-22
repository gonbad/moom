---
name: animate
description: Compose reviewed assets into a deterministic local HTML movie for acceptance.
---

# /animate

Read the project constitution and current status. Use the following references from `docs/references/`: `workflow.md`, `visuals.md`, `animation.md`, `quality.md`.

Read the accepted story and asset baseline. Build one representative short scene
first, using the exact accepted SVG/CSS and animation behaviors. Compare its visual
states with the source/gallery at matched scale and time. Obtain feedback/acceptance
of that scene before expanding the full timeline; reuse it in the finished composition.

Use the animation reference's single-clock/seek contract. Author purposeful motion and
still holds, with controls and recording guidance outside the clean frame. Serve the
full HTML locally; check boundaries, pause/restart/backward seek, typography and source
fidelity. Write `docs/living/animation.md` with source baseline, scene
mapping, timing, viewport and technical evidence. Provide a numbered Markdown review
linking the preview and record explicit acceptance of that revision. A functional
preview is not permission to encode. Stop at the accepted preview and hand off to
`/render` when the person requests video, or to `/dubb` for HTML-only final delivery.
