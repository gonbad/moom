---
name: render
description: Render the explicitly requested accepted HTML revision to a verified silent video.
---

# /render

Read `AGENTS.md`, all four `docs/constitution/` documents and the living profile,
Job and status under `docs/kandoo/living/`. Resolve active `ID` and `VERSION` from
status. Read the Project's living status, recorded Current input and relevant submitted
rounds. Read installed references `workflow.md`, `quality.md`, `animation.md` under
`docs/kandoo/living/references/`. All paths are workspace-root paths.

Read `living/animation.md`, the accepted preview identity and requested output.
Require explicit rendering intent plus acceptance of the current revision. `/render`
supplies intent, but cannot accept a new/unseen preview; route unresolved review back
to `/animate`. Do not install a renderer or launch frame capture before this gate.

Verify fonts/assets and deterministic frame seeking. Make a short sample, compare
encoded frames to the accepted HTML, then encode the whole silent video using the
animation reference's bounded-resource/error-handling procedure. Preserve earlier
exports; exclude controls, teleprompter and other non-content UI from capture. Probe
and view the actual output, checking aspect ratio, frame rate, duration, cuts and final
hold. Record source/output hashes, settings, elapsed capture/encode, verification and
limits in `docs/projects/ID/living/render.md` and the current dossier. Failed or partial
files remain unaccepted. Hand off to `/dubb` for voice or final silent delivery.

Apply file-review/certainty rules and the four-domain check: Job, shared Kandoo,
active Project and write-only feedback. Preserve explicit authorization and accepted
outputs. Save evidence, current step, pending review and next action in Project
`living/status.md` and mirror shared status. Finish every reply with the full localized
Job pipeline and one exact next action, using a Markdown review/summary inside `docs/`
or the next actual command. Human acceptance is never inferred from passing checks.
