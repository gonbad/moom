---
name: job-prd
description: Author agent requirements, persona profiles, interaction boundaries and operational goals.
---

# /job-prd

Read `AGENTS.md`, the four `docs/constitution/` documents and `docs/kandoo/living/profile.md`,
`job.md`, `server.md` and `status.md`. Resolve the active Project `ID` and `VERSION` from
status; all paths are workspace-root paths. Read the installed reference
`docs/kandoo/living/references/workflow.md` (plus `messenger.md` when a messenger channel
is selected), `docs/projects/ID/living/idea.md`, `roadmap.md` and submitted rounds in
`docs/projects/ID/versions/VERSION/`. Preserve earlier outputs and authorization.

Gate: `docs/projects/ID/living/idea.md` exists and has no unsubmitted question round
pending. Author `docs/projects/ID/living/prd.md`:
1. **Caller Personas & Trusted Context:** Profiles for human callers or scheduled run
   principals, language habits, expectations and authentication boundaries.
2. **Agent Persona & Refusal Boundaries:** Role, linguistic tone, domain limits and
   explicit out-of-scope refusal rules.
3. **Core Workflows:** Primary goals the agent fulfills through scoped tools (without
   forcing a chat UI on a scheduled task).
4. **Non-Goals:** Actions or integrations excluded from this version.

Resolve open questions via `docs/projects/ID/versions/VERSION/NN-questions.md` in
Obsidian; once submitted, hand off to `/job-tools`.

Apply the file-review/certainty protocol on `.md` files inside `docs/` and assess updates
to the Job, shared Kandoo, active Project and write-only creator feedback. Persist what
changed, evidence, pending review and next action in `docs/projects/ID/living/status.md`
and mirror `docs/kandoo/living/status.md`. Finish every reply with the current Job's full ordered
steps localized and one exact next action (`/job-tools` or the pending `.md` file).
