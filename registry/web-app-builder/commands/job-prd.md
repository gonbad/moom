---
name: job-prd
description: Author the product requirement document with detailed user personas and boundaries.
---

# /job-prd

Read `AGENTS.md`, the four `docs/constitution/` documents and `docs/kandoo/living/profile.md`,
`job.md`, `server.md` and `status.md`. Resolve the active Project `ID` and `VERSION` from
status; all paths are workspace-root paths. Read only the installed reference
`docs/kandoo/living/references/workflow.md`, `docs/projects/ID/living/idea.md`, `roadmap.md`,
`external-services.md` and submitted rounds in `docs/projects/ID/versions/VERSION/`.
Preserve earlier outputs and authorization.

Gate: `docs/projects/ID/living/idea.md` exists and has no unsubmitted question round
pending. Author `docs/projects/ID/living/prd.md`:
1. **User Personas:** For each actor (visitor, customer, administrator, operator), write
   a concrete persona covering context, digital literacy, primary viewport (mobile vs
   desktop), Persian/Latin language habits, what success looks like in two minutes,
   anxieties (payment/privacy trust), and expected tone.
2. **Core Capabilities:** Primary journeys in this version mapped directly to the vertical
   slice in `idea.md`.
3. **Boundaries and Non-Goals:** Explicit exclusions for this version so later design and
   build stages do not drift.

Put open product questions and non-obvious tradeoffs in
`docs/projects/ID/versions/VERSION/NN-questions.md` in Obsidian. Once any open round is
submitted (Confirmed or Delegated/Provisional), record decisions without adding a
duplicate approval round, commit if local Git is active (or record Git deferred), and
hand off to `/job-data-model`.

Apply the file-review/certainty protocol on `.md` files inside `docs/` and assess updates
to the Job, shared Kandoo, active Project and write-only creator feedback. Persist what
changed, evidence, pending review and next action in `docs/projects/ID/living/status.md`
and mirror `docs/kandoo/living/status.md`. Finish every reply with the current Job's full ordered
steps localized and one exact next action (`/job-data-model` or the pending `.md` file).
