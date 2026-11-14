---
name: job-sops
description: Specify Standard Operating Procedures, stage-by-stage conversational workflows and validation rules.
---

# /job-sops

Read `AGENTS.md`, the four `docs/constitution/` documents and `docs/kandoo/living/profile.md`,
`job.md`, `server.md` and `status.md`. Resolve the active Project `ID` and `VERSION` from
status; all paths are workspace-root paths. Read only the installed reference
`docs/kandoo/living/references/workflow.md`, `docs/projects/ID/living/prd.md`, `tools.md`
and submitted rounds in `docs/projects/ID/versions/VERSION/`. Preserve earlier outputs
and authorization.

Gate: `docs/projects/ID/living/tools.md` exists and has no unsubmitted question round
pending. Author `docs/projects/ID/living/sops.md`:
1. **Stage Progression:** For each multi-step capability, define ordered stages
   (discovery → slot collection → parameter validation → policy-gated tool invocation →
   outcome summary).
2. **Information Gathering & Deterministic Validation:** Specify required facts and
   deterministic format/domain checks before any tool call.
3. **Conversational Recovery:** Rules for disambiguating vague requests, handling
   corrections or topic switches, and canceling an in-progress workflow cleanly.

Resolve open questions via `docs/projects/ID/versions/VERSION/NN-questions.md` in
Obsidian; once submitted, hand off to `/job-data-model`.

Apply the file-review/certainty protocol on `.md` files inside `docs/` and assess updates
to the Job, shared Kandoo, active Project and write-only creator feedback. Persist what
changed, evidence, pending review and next action in `docs/projects/ID/living/status.md`
and mirror `docs/kandoo/living/status.md`. Finish every reply with the current Job's full ordered
steps localized and one exact next action (`/job-data-model` or the pending `.md` file).
