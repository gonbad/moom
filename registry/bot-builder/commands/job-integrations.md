---
name: job-integrations
description: Configure messenger platform adapters, API differences and conditional payment policies.
---

# /job-integrations

Read `AGENTS.md`, the four `docs/constitution/` documents and `docs/kandoo/living/profile.md`,
`job.md`, `server.md` and `status.md`. Resolve the active Project `ID` and `VERSION` from
status; all paths are workspace-root paths. Read the installed references
`docs/kandoo/living/references/workflow.md` and `messenger.md` (plus `payments.md` only
when payments are in scope), `docs/projects/ID/living/prd.md`, `flow.md`,
`data-model.md`, `external-services.md` and submitted rounds in
`docs/projects/ID/versions/VERSION/`. Preserve earlier outputs and authorization.

Gate: `docs/projects/ID/living/data-model.md` exists and has no unsubmitted question
round pending. Author `docs/projects/ID/living/integrations.md` (always named
`integrations.md`):
1. **Messenger Adapter Normalization:** Specify only the selected platform(s) (Telegram,
   Bale, Rubika), webhook vs polling mode, button/contact capabilities, and text fallbacks
   for unsupported controls.
2. **Conditional Payment & Settlement Policy:** If payments are included, document Bale
   native wallet or transfer-receipt verification and let the owner explicitly choose
   `strict` versus bounded `optimistic` provisional fulfillment (never recording
   `optimistic` as `settled`). If payments are outside scope, mark this section `not
   applicable`.
3. **Project Secret Boundaries:** List non-secret environment variable names (such as
   `TELEGRAM_BOT_TOKEN` or `BALE_BOT_TOKEN`) here in `integrations.md`, and instruct the
   owner to place real/test token values only in gitignored
   `docs/projects/ID/secrets/credentials.md`—never in unscoped `docs/secrets/` or
   non-`.md` files referred to the participant.

Resolve open questions via `docs/projects/ID/versions/VERSION/NN-questions.md` in
Obsidian; once submitted, hand off to `/job-edge-cases`.

Apply the file-review/certainty protocol on `.md` files inside `docs/` and assess updates
to the Job, shared Kandoo, active Project and write-only creator feedback. Persist what
changed, evidence, pending review and next action in `docs/projects/ID/living/status.md`
and mirror `docs/kandoo/living/status.md`. Finish every reply with the current Job's full ordered
steps localized and one exact next action (`/job-edge-cases` or the pending `.md` file).
