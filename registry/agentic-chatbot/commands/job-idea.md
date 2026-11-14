---
name: job-idea
description: Assess agent suitability, explain cost/security risks, scope core capability and boundaries.
---

# /job-idea

Read `AGENTS.md`, the four `docs/constitution/` documents and `docs/kandoo/living/profile.md`,
`job.md`, `server.md` and `status.md`. Resolve the active Project `ID` and `VERSION` from
status; all paths are workspace-root paths. Read only the installed reference
`docs/kandoo/living/references/workflow.md`, the selected-version input recorded in `docs/projects/ID/living/status.md`,
and submitted rounds in that version. Preserve earlier outputs and authorization.

Inspect `projects/ID/existing/` if the participant pasted an existing codebase (a
permitted drop folder outside `docs/`). **Suitability Gate:** Explain the tradeoffs of
model-directed tool loops versus a deterministic bot (`bot-builder`) or ordinary web app
(`web-app-builder`): latency, recurring token cost, semantic mistakes and prompt
injection risk. Confirm with the owner via `NN-questions.md` that autonomous tool
selection genuinely adds value here.

Identify the narrow version `0.1` capability, caller personas, channel (messenger, web
or scheduled job), whether payments apply or are `not applicable`, and external systems.
Bank secondary tools and future scope in `docs/projects/ID/living/roadmap.md`.

Always write and maintain `docs/projects/ID/living/idea.md`—never substitute a
version-only filename. Resolve open questions via
`docs/projects/ID/versions/VERSION/NN-questions.md` in Obsidian; once submitted, hand
off directly to `/job-prd`.

Apply the file-review/certainty protocol on `.md` files inside `docs/` and assess updates
to the Job, shared Kandoo, active Project and write-only creator feedback. Persist what
changed, evidence, pending review and next action in `docs/projects/ID/living/status.md`
and mirror `docs/kandoo/living/status.md`. Finish every reply with the current Job's full ordered
steps localized and one exact next action (`/job-prd` or the pending `.md` question file).
