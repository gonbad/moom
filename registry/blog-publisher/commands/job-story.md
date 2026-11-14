---
name: job-story
description: Outline narrative structure, section headings, evidence sequence and transitions.
---

# /job-story

Read `AGENTS.md`, the four `docs/constitution/` documents and `docs/kandoo/living/profile.md`,
`job.md`, `server.md` and `status.md`. Resolve the active Project `ID` and `VERSION` from
status; all paths are workspace-root paths. Read only the installed references
`docs/kandoo/living/references/workflow.md` and `quality.md`, `docs/projects/ID/living/idea.md`,
`docs/projects/ID/living/brief.md`, and submitted rounds in `docs/projects/ID/versions/VERSION/`.
Preserve earlier outputs and authorization.

Gate: `docs/projects/ID/living/brief.md` exists and has no unsubmitted question round
pending. Author `docs/projects/ID/living/story.md`:
1. **Narrative Arc & Actor Sequence:** Progression from concrete reader hook/problem
   through worked steps or evidence to actionable takeaway, explicitly preserving who
   performs each step (reader vs assistant vs system).
2. **Ordered Section Hierarchy:** Complete heading sequence (H1, H2, H3), the single
   claim or task of each section, estimated weight, and transition bridges between sections.
3. **Evidence & Example Map:** Map every claim in `brief.md` and creator correction in
   the open version to a specific section, naming the exact source fact, worked example,
   diagram, table or code listing that supports it, and flagging any missing source fact.

Use `docs/projects/ID/versions/VERSION/NN-questions.md` for non-obvious structural
choices, ordering tradeoffs or missing prerequisites. Invite the owner to inspect
`docs/projects/ID/living/story.md` in Obsidian; once submitted choices/edits are
resolved, hand off to `/job-content`.

Apply the file-review/certainty protocol on `.md` files inside `docs/` and assess updates
to the Job, shared Kandoo, active Project and write-only creator feedback. Persist what
changed, evidence, pending review and next action in `docs/projects/ID/living/status.md`
and mirror `docs/kandoo/living/status.md`. Finish every reply with the current Job's full ordered
steps localized and one exact next action (`/job-content` or the pending `.md` file in `docs/`).
