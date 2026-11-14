---
name: job-privacy
description: Classify sensitive data, define handle-envelope masking and specify audit redaction and retention.
---

# /job-privacy

Read `AGENTS.md`, the four `docs/constitution/` documents and `docs/kandoo/living/profile.md`,
`job.md`, `server.md` and `status.md`. Resolve the active Project `ID` and `VERSION` from
status; all paths are workspace-root paths. Read only the installed references
`docs/kandoo/living/references/workflow.md` and `authority.md`, plus
`docs/projects/ID/living/tools.md`, `data-model.md` and submitted rounds in
`docs/projects/ID/versions/VERSION/`. Preserve earlier outputs and authorization.

Gate: `docs/projects/ID/living/data-model.md` exists and has no unsubmitted question
round pending. Author `docs/projects/ID/living/privacy.md`:
1. **Sensitive Data Classification:** Enumerate every sensitive attribute (national IDs,
   phone numbers, card/IBAN numbers, passwords, API/session tokens, customer receipts).
2. **Handle Envelope Architecture (`[h_*]`):** Specify how the harness intercepts
   sensitive values, stores them in an isolated caller-scoped vault with expiry, and
   replaces them with typed opaque handles (`HandleRef[Kind]`, such as `[h_card_1]` or
   `[h_national_id_2]`) before model context assembly.
3. **Sink De-Referencing Rules:** Specify which reviewed backend sinks may resolve each
   handle type after checking caller, ownership and expiry.
4. **Audit Redaction, Access & Retention:** Define exact permitted fields in durable
   audit logs vs short-lived protected diagnostics, who can access them, redaction rules
   for prompts/tool payloads, and retention/purge schedules.

Resolve open questions via `docs/projects/ID/versions/VERSION/NN-questions.md` in
Obsidian; once submitted, hand off to `/job-capabilities`.

Apply the file-review/certainty protocol on `.md` files inside `docs/` and assess updates
to the Job, shared Kandoo, active Project and write-only creator feedback. Persist what
changed, evidence, pending review and next action in `docs/projects/ID/living/status.md`
and mirror `docs/kandoo/living/status.md`. Finish every reply with the current Job's full ordered
steps localized and one exact next action (`/job-capabilities` or the pending `.md` file).
