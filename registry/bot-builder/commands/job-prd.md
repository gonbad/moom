---
name: job-prd
description: Author bot requirements, command lists, user personas and interaction rules.
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
1. **User Personas:** Detailed profiles for actors (visitor, customer, administrator,
   support operator), their mobile messenger habits, language preferences and expected
   turnaround times.
2. **Commands & Menu System:** Supported slash commands (`/start`, `/help`, `/cancel`,
   `/status`), persistent reply keyboards, inline action buttons and back/home navigation.
3. **Operational Policies:** Notification triggers, administrative rules, session timeout
   windows, support/operator handoff, and whether payments apply to this version.
4. **Non-Goals:** Capabilities explicitly excluded from this version.

Resolve open questions via `docs/projects/ID/versions/VERSION/NN-questions.md` in
Obsidian; once submitted, hand off to `/job-flow`.

Apply the file-review/certainty protocol on `.md` files inside `docs/` and assess updates
to the Job, shared Kandoo, active Project and write-only creator feedback. Persist what
changed, evidence, pending review and next action in `docs/projects/ID/living/status.md`
and mirror `docs/kandoo/living/status.md`. Finish every reply with the current Job's full ordered
steps localized and one exact next action (`/job-flow` or the pending `.md` file).
