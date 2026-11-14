---
name: job-prompts
description: Author Project-scoped runtime prompts, persona rules and synthetic dialogue examples.
---

# /job-prompts

Read `AGENTS.md`, the four `docs/constitution/` documents and `docs/kandoo/living/profile.md`,
`job.md`, `server.md` and `status.md`. Resolve the active Project `ID` and `VERSION` from
status; all paths are workspace-root paths. Read only the installed references
`docs/kandoo/living/references/workflow.md` and `authority.md`, plus
`docs/projects/ID/living/prd.md`, `tools.md`, `sops.md`, `privacy.md`, `capabilities.md`,
`edge-cases.md` and submitted rounds in `docs/projects/ID/versions/VERSION/`. Preserve
earlier outputs and authorization.

Gate: `docs/projects/ID/living/edge-cases.md` exists and has no unsubmitted question
round pending. Author the reviewed prompt specifications as Markdown inside the Project's
document root `docs/projects/ID/living/prompts/` (never unscoped `docs/prompts/`):
1. **System Prompt (`docs/projects/ID/living/prompts/system.md`):** Role identity, SOP
   enforcement, tool invocation boundaries, `[h_*]` opaque handle rules (never guessing
   or requesting raw vaulted secrets), and untrusted-data boundaries.
2. **Persona & Linguistic Tone (`docs/projects/ID/living/prompts/persona.md`):** Natural,
   clear Persian/chosen language guidelines, conciseness and polite out-of-scope refusals.
3. **Synthetic Dialogue Examples (`docs/projects/ID/living/prompts/examples.md`):**
   Multi-turn examples matching the exact policies chosen in `capabilities.md`:
   - `read` + `none` and `direct` + `none` tool calls.
   - `direct` + `soft` conversational offer, refusal/correction and confirmed execution.
   - `confirm` + `hard` proposal emission (`propose_<action>`) awaiting independent
     out-of-band/UI approval.
   - Refusal of prompt injection and out-of-scope requests.

Invite review or non-obvious question resolution via
`docs/projects/ID/versions/VERSION/NN-questions.md` in Obsidian; once submitted, hand
off to `/job-plan`.

Apply the file-review/certainty protocol on `.md` files inside `docs/` and assess updates
to the Job, shared Kandoo, active Project and write-only creator feedback. Persist what
changed, evidence, pending review and next action in `docs/projects/ID/living/status.md`
and mirror `docs/kandoo/living/status.md`. Finish every reply with the current Job's full ordered
steps localized and one exact next action (`/job-plan` or the pending `.md` file).
