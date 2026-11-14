---
name: job-idea
description: Scope the product, benchmark competitors, identify unfair advantage and external fallbacks.
---

# /job-idea

Read `AGENTS.md`, the four `docs/constitution/` documents and `docs/kandoo/living/profile.md`,
`job.md`, `server.md` and `status.md`. Resolve the active Project `ID` and `VERSION` from
status; all paths are workspace-root paths. Read only the installed reference
`docs/kandoo/living/references/workflow.md`, the selected-version input recorded in `docs/projects/ID/living/status.md`,
and submitted rounds in that version. Preserve earlier outputs and authorization.

If the participant has an existing codebase, they may paste it into
`projects/ID/existing/` (one of the permitted non-`docs/` drop folders); inspect models,
schemas, routes and business rules thoroughly before proposing changes. Contrast the
product with 2–3 realistic alternatives (competitors, domestic platforms such as Divar,
Bale or Snapp, or manual Excel/paper habits) and isolate the decisive unfair advantage.

Cut version `0.1` to one demonstrable vertical slice and bank deferred features in
`docs/projects/ID/living/roadmap.md`. For every external service dependency, document a
ranked fallback chain (primary, secondary and zero-dependency local fallback) plus
non-secret credential variable names in `docs/projects/ID/living/external-services.md`
(recording domestic versus foreign network constraints and instructing the owner to
store actual keys only in gitignored `docs/projects/ID/secrets/credentials.md`).

Always write and maintain `docs/projects/ID/living/idea.md` with actors, problem,
differentiator, fallbacks and the `0.1` boundary—never use an alternative version-only
filename instead of `living/idea.md`. Resolve open choices via
`docs/projects/ID/versions/VERSION/NN-questions.md` in Obsidian; once submitted, hand
off directly to `/job-prd`.

Apply the file-review/certainty protocol on `.md` files inside `docs/` and assess updates
to the Job, shared Kandoo, active Project and write-only creator feedback. Persist what
changed, evidence, pending review and next action in `docs/projects/ID/living/status.md`
and mirror `docs/kandoo/living/status.md`. Finish every reply with the current Job's full ordered
steps localized and one exact next action (`/job-prd` or the pending `.md` question file).
