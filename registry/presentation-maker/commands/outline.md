---
name: outline
description: Develop the argument, slide beats, examples and speaker timing.
---

# /outline

Read `AGENTS.md`, the four `docs/constitution/` documents and `docs/kandoo/living/profile.md`,
`job.md`, `server.md` and `status.md`. Resolve the active Project `ID` and `VERSION` from
status; all paths are workspace-root paths. Read only the installed references
`docs/kandoo/living/references/workflow.md`, `slides.md` and `visuals.md`, `docs/projects/ID/living/idea.md`,
and submitted rounds in `docs/projects/ID/versions/VERSION/`. Preserve earlier outputs
and authorization.

Gate: `docs/projects/ID/living/idea.md` exists and has a closed review. Build an argument from recognizable problem through worked example, model,
counterexample and audience action. Write `docs/projects/ID/living/outline.md` with
sections, assertion beat/claim, source, visual treatment, speaker notes (kept separate
from audience text) and realistic time budget including exercises and questions. Flag
claims needing source verification instead of inventing statistics or dropping them.

Write `docs/projects/ID/living/assets.md` mapping every required visual to slide
beats, purpose, variants/transitions, source/format, provenance and review criteria.
Use the visual reference to plan SVG-first design and image-generation/supplied-image
fallbacks. Assets are planned here and reviewed before full deck assembly in build.

Write `docs/projects/ID/living/design.md` specifying typography, palette, diagram
vocabulary, RTL/LTR rules and navigation controls. Check the whole arc for duplicated
setup, missing transitions and unsupported conclusions. Record non-obvious format or
narrative tradeoffs in `docs/projects/ID/versions/VERSION/NN-questions.md`; once review closes, route to `/build`.

Apply the file-review/certainty protocol on `.md` files inside `docs/` and assess updates
to the Job, shared Kandoo, active Project and write-only creator feedback. Persist what
changed, evidence, pending review and next action in `docs/projects/ID/living/status.md`
and mirror `docs/kandoo/living/status.md`. Finish every reply with the current Job's full ordered
steps localized and one exact next action (`/build` or the pending `.md` file in `docs/`).
