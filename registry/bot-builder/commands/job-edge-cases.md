---
name: job-edge-cases
description: Define failure recovery, stale callback handling, debounce and transport resilience.
---

# /job-edge-cases

Read `AGENTS.md`, the four `docs/constitution/` documents and `docs/kandoo/living/profile.md`,
`job.md`, `server.md` and `status.md`. Resolve the active Project `ID` and `VERSION` from
status; all paths are workspace-root paths. Read only the installed references
`docs/kandoo/living/references/workflow.md`, `fsm.md` and `messenger.md`, plus
`docs/projects/ID/living/flow.md`, `data-model.md`, `integrations.md` and submitted
rounds in `docs/projects/ID/versions/VERSION/`. Preserve earlier outputs and authorization.

Gate: `docs/projects/ID/living/integrations.md` exists and has no unsubmitted question
round pending. Author `docs/projects/ID/living/edge-cases.md`:
1. **Transport & Outbox Failures:** Polling timeout backoff, duplicate webhook delivery
   deduplication (`update_key`), send-timeout unknown outcomes without blind mutation
   replay, and invalid-token circuit breaking without logging secret values.
2. **Stale, Duplicate & Cross-Caller Actions:** Graceful answers for expired or old
   callback queries, rapid double-tap idempotency, and rejecting another caller's token.
3. **Unexpected Inputs & Mid-Flow `/start`:** Freeform text when buttons were expected,
   unsupported media/large files, and `/start` mid-flow behavior.
4. **Expiry & Cancellation:** Read-time draft/reservation expiry without relying on a
   background cron having run, plus explicit `«انصراف»` cleanup.

Resolve open questions via `docs/projects/ID/versions/VERSION/NN-questions.md` in
Obsidian; once submitted, hand off to `/job-scenarios`.

Apply the file-review/certainty protocol on `.md` files inside `docs/` and assess updates
to the Job, shared Kandoo, active Project and write-only creator feedback. Persist what
changed, evidence, pending review and next action in `docs/projects/ID/living/status.md`
and mirror `docs/kandoo/living/status.md`. Finish every reply with the current Job's full ordered
steps localized and one exact next action (`/job-scenarios` or the pending `.md` file).
