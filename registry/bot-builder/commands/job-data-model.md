---
name: job-data-model
description: Define persistent bot data entities, user profiles, session states and optional transaction records.
---

# /job-data-model

Read `AGENTS.md`, the four `docs/constitution/` documents and `docs/kandoo/living/profile.md`,
`job.md`, `server.md` and `status.md`. Resolve the active Project `ID` and `VERSION` from
status; all paths are workspace-root paths. Read only the installed references
`docs/kandoo/living/references/workflow.md` and `fsm.md`, `docs/projects/ID/living/prd.md`,
`flow.md` and submitted rounds in `docs/projects/ID/versions/VERSION/`. Preserve earlier
outputs and authorization.

Gate: `docs/projects/ID/living/flow.md` exists and has no unsubmitted question round
pending. Author `docs/projects/ID/living/data-model.md` in plain business terms without
raw SQL:
1. **Users & Identities:** Caller keys (`platform`, `bot_id`, `caller_id`, private vs
   group `chat_id`), contact/profile fields and timestamps.
2. **Session & Callback State:** Current FSM state, version/expiry, draft payload and
   opaque one-use/expiring callback action tokens.
3. **Business Entities:** Domain objects created or updated by the bot's core flow.
4. **Transactions & Invoices (Conditional):** Include order, currency, expiry and
   `receipt_received` / `provisional` / `settled` / `rejected` / `refunded` records
   **only when payments are in scope**; otherwise explicitly mark this section `not
   applicable`.
5. **Deduplication & Redacted Audit Metadata:** Inbound `update_key` deduplication,
   outbox delivery status and redacted operator/event metadata (never storing raw tokens).

Resolve open questions via `docs/projects/ID/versions/VERSION/NN-questions.md` in
Obsidian; once submitted, hand off to `/job-integrations`.

Apply the file-review/certainty protocol on `.md` files inside `docs/` and assess updates
to the Job, shared Kandoo, active Project and write-only creator feedback. Persist what
changed, evidence, pending review and next action in `docs/projects/ID/living/status.md`
and mirror `docs/kandoo/living/status.md`. Finish every reply with the current Job's full ordered
steps localized and one exact next action (`/job-integrations` or the pending `.md` file).
