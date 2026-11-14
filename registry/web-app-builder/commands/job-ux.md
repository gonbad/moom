---
name: job-ux
description: Define screens, empty/error states, user flows, theme keywords and primary key screen.
---

# /job-ux

Read `AGENTS.md`, the four `docs/constitution/` documents and `docs/kandoo/living/profile.md`,
`job.md`, `server.md` and `status.md`. Resolve the active Project `ID` and `VERSION` from
status; all paths are workspace-root paths. Read only the installed references
`docs/kandoo/living/references/workflow.md` and `design.md`, `docs/projects/ID/living/prd.md`,
`data-model.md` and submitted rounds in `docs/projects/ID/versions/VERSION/`. Preserve
earlier outputs and authorization.

Gate: `docs/projects/ID/living/data-model.md` exists and has no unsubmitted question
round pending. Author `docs/projects/ID/living/ux.md`:
1. **Screens Inventory:** Name every screen explicitly (reused across design, prototype
   and scenarios), stating its content plus its **loading**, **empty** and **error** states.
2. **Primary Key Screen:** Identify the single screen that best expresses the product's
   value; `/job-design` will explore three distinct directions on this screen first.
3. **User Flows:** Step-by-step paths for each persona goal, including back navigation
   and cancellation.
4. **Theme & Viewport:** 3–4 tone keywords, mobile-first vs desktop viewport, RTL/LTR
   typography expectations and light/dark preference.

If walking screens reveals missing fields or PRD gaps, update `data-model.md` and
`prd.md` in place and note the change. Resolve open questions via
`docs/projects/ID/versions/VERSION/NN-questions.md` in Obsidian; once submitted, hand
off to `/job-design`.

Apply the file-review/certainty protocol on `.md` files inside `docs/` and assess updates
to the Job, shared Kandoo, active Project and write-only creator feedback. Persist what
changed, evidence, pending review and next action in `docs/projects/ID/living/status.md`
and mirror `docs/kandoo/living/status.md`. Finish every reply with the current Job's full ordered
steps localized and one exact next action (`/job-design` or the pending `.md` file).
