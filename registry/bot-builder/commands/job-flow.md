---
name: job-flow
description: Design deterministic FSM states, menu hierarchies, transitions and message templates.
---

# /job-flow

Read `AGENTS.md`, the four `docs/constitution/` documents and `docs/kandoo/living/profile.md`,
`job.md`, `server.md` and `status.md`. Resolve the active Project `ID` and `VERSION` from
status; all paths are workspace-root paths. Read only the installed references
`docs/kandoo/living/references/workflow.md` and `fsm.md`, `docs/projects/ID/living/idea.md`,
`prd.md` and submitted rounds in `docs/projects/ID/versions/VERSION/`. Preserve earlier
outputs and authorization.

Gate: `docs/projects/ID/living/prd.md` exists and has no unsubmitted question round
pending. Author `docs/projects/ID/living/flow.md` (always named `flow.md`):
1. **FSM State Transition Table:** Complete tabular mapping of every state (`idle`,
   domain draft states, confirmation, and conditional payment states only when payments
   are in scope), expected input (command, text, reply button, opaque callback token,
   contact or media), guard/validation rule, transactional mutation, outgoing reply and
   next state.
2. **Keyboards & Navigation:** Persistent reply keyboards, inline button layouts, and
   universal escape actions (`«انصراف»` / `/cancel`, `«بازگشت»`, `«منوی اصلی»`).
3. **Message Templates:** Verbatim text for greetings, prompts, validation errors,
   confirmations and help messages, written in natural Persian/chosen language suited to
   the persona.

Resolve open questions via `docs/projects/ID/versions/VERSION/NN-questions.md` in
Obsidian; once submitted, hand off to `/job-data-model`.

Apply the file-review/certainty protocol on `.md` files inside `docs/` and assess updates
to the Job, shared Kandoo, active Project and write-only creator feedback. Persist what
changed, evidence, pending review and next action in `docs/projects/ID/living/status.md`
and mirror `docs/kandoo/living/status.md`. Finish every reply with the current Job's full ordered
steps localized and one exact next action (`/job-data-model` or the pending `.md` file).
