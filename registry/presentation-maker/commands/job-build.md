---
name: job-build
description: Build and verify the selected presentation with local assets.
---

# /job-build

Read `AGENTS.md`, the four `docs/constitution/` documents and `docs/kandoo/living/profile.md`,
`job.md`, `server.md` and `status.md`. Resolve the active Project `ID` and `VERSION` from
status; all paths are workspace-root paths. Read only the installed references
`docs/kandoo/living/references/workflow.md`, `slides.md` and `quality.md`, plus
`docs/projects/ID/living/idea.md`, `outline.md`, `design.md` and submitted rounds in
`docs/projects/ID/versions/VERSION/`. Preserve earlier outputs and authorization.

Gate: `docs/projects/ID/living/outline.md` and `design.md` exist with no unsubmitted
question round pending. Generate editable source under `projects/ID/src/` and deliverable
output under `projects/ID/dist/` for the chosen format; author genuine layouts and
diagrams rather than forcing every beat into one bullet template. Bundle fonts, media
and licenses locally under `projects/ID/` with zero runtime CDN dependency. If a font or
package download is blocked, use the configured proxy or a clean local system fallback
font and record the fallback honestly.

For HTML, implement stable slide IDs, keyboard/touch navigation, focus restoration,
overview/deep links and browser history without marking skipped slides visited or
trapping keys inside inputs. Check mixed Persian/LTR text, reduced motion, desktop/mobile
overflow, notes, print/PDF export and network-disabled opening from a path with spaces.
Serve a local `http://127.0.0.1` preview for the speaker and record technical check
results, artifact hashes and review prompts in a `.md` file under
`docs/projects/ID/versions/VERSION/`; never refer the participant to open or edit raw
non-`.md` files outside `docs/`. Keep speaker acceptance pending until given for this
revision, and route to `/job-deploy`.

Apply the file-review/certainty protocol on `.md` files inside `docs/` and assess updates
to the Job, shared Kandoo, active Project and write-only creator feedback. Persist what
changed, evidence, pending review and next action in `docs/projects/ID/living/status.md`
and mirror `docs/kandoo/living/status.md`. Finish every reply with the current Job's full ordered
steps localized and one exact next action (`/job-deploy` or the `.md` review file in `docs/`).
