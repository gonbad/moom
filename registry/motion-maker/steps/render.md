---
name: render
description: Render the explicitly requested accepted HTML revision to a verified silent video.
---

# /render

Read the project constitution and current status. Use the following references from `docs/references/`: `workflow.md`, `animation.md`, `quality.md`.

Read `docs/living/animation.md`, the accepted preview identity and requested output.
Require explicit rendering intent plus acceptance of the current revision. `/render`
supplies intent, but cannot accept a new/unseen preview; route unresolved review back
to `/animate`. Do not install a renderer or launch frame capture before this gate.

Verify fonts/assets and deterministic frame seeking. Make a short sample, compare
encoded frames to the accepted HTML, then encode the whole silent video using the
animation reference's bounded-resource/error-handling procedure. Preserve earlier
exports; exclude controls, teleprompter and other non-content UI from capture. Probe
and view the actual output, checking aspect ratio, frame rate, duration, cuts and final
hold. Record source/output hashes, settings, elapsed capture/encode, verification and
limits in `docs/living/render.md` and the current dossier. Failed or partial
files remain unaccepted. Hand off to `/dubb` for voice or final silent delivery.
