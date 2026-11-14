---
name: job-layout
description: Design this post for its content, language and reading modes.
---

# /job-layout

Read `AGENTS.md`, the four `docs/constitution/` documents and `docs/kandoo/living/profile.md`,
`job.md`, `server.md` and `status.md`. Resolve the active Project `ID` and `VERSION` from
status; all paths are workspace-root paths. Read only the installed references
`docs/kandoo/living/references/workflow.md`, `distribution.md` and `quality.md`, plus
`docs/projects/ID/living/idea.md`, `brief.md`, `story.md`, `content.md` and submitted
rounds in `docs/projects/ID/versions/VERSION/`. Preserve earlier outputs and authorization.

Gate: `docs/projects/ID/living/content.md` exists and open editorial questions are
resolved. Choose a layout suited to this post's format rather than copying every prior
post's theme. Use the real text from `content.md` to design typography, reading density,
diagrams, navigation and narrow-screen behavior. Set language/direction deliberately and
isolate code, paths and identifiers as LTR; preserve accessible labels, focus, contrast,
reduced motion, print and offline behavior.

Record layout decisions and public/private source boundaries in
`docs/projects/ID/living/layout.md`, and generate the public source files under
`projects/ID/src/` (or declared `site/`) with bundled local fonts/assets and license
notices (no runtime design CDN). Serve a local `http://127.0.0.1` preview if helpful for
visual inspection, and record any layout review notes in `.md` files under
`docs/projects/ID/versions/VERSION/`; never refer the participant to edit or open raw
non-`.md` files outside `docs/`. Update an authored index Project only when public
discovery is explicitly in scope. Route to `/job-build`.

Apply the file-review/certainty protocol on `.md` files inside `docs/` and assess updates
to the Job, shared Kandoo, active Project and write-only creator feedback. Persist what
changed, evidence, pending review and next action in `docs/projects/ID/living/status.md`
and mirror `docs/kandoo/living/status.md`. Finish every reply with the current Job's full ordered
steps localized and one exact next action (`/job-build` or the `.md` review file in `docs/`).
