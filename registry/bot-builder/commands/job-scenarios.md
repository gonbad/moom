---
name: job-scenarios
description: Write interactive messenger turn scenarios with synthetic identities and expected responses.
---

# /job-scenarios

Read `AGENTS.md`, the four `docs/constitution/` documents and `docs/kandoo/living/profile.md`,
`job.md`, `server.md` and `status.md`. Resolve the active Project `ID` and `VERSION` from
status; all paths are workspace-root paths. Read only the installed references
`docs/kandoo/living/references/workflow.md` and `quality.md`, plus
`docs/projects/ID/living/prd.md`, `flow.md`, `data-model.md`, `integrations.md`,
`edge-cases.md` and submitted rounds in `docs/projects/ID/versions/VERSION/`. Preserve
earlier outputs and authorization.

Gate: `docs/projects/ID/living/edge-cases.md` exists and has no unsubmitted question
round pending. Author `docs/projects/ID/living/test-scenarios.md` using **synthetic
caller IDs and synthetic test data** (never real customer phone numbers or live payment
cards):
1. **Scenario Structure:** Scenario ID/title, preconditions/seeds, turn-by-turn sequence
   (actor command/text/button/callback/media → expected bot reply and keyboard), and
   expected terminal FSM + database state.
2. **Required Coverage:** Onboarding `/start`, primary completion flow, admin/operator
   actions, duplicate update delivery, stale callback tap, invalid input, cancellation
   mid-flow, restart mid-dialog, and—**only if payments are in scope**—payment/receipt
   verification and replay (otherwise mark payment scenarios `not applicable`).

Resolve open questions via `docs/projects/ID/versions/VERSION/NN-questions.md` in
Obsidian; once submitted, hand off to `/job-plan`.

Apply the file-review/certainty protocol on `.md` files inside `docs/` and assess updates
to the Job, shared Kandoo, active Project and write-only creator feedback. Persist what
changed, evidence, pending review and next action in `docs/projects/ID/living/status.md`
and mirror `docs/kandoo/living/status.md`. Finish every reply with the current Job's full ordered
steps localized and one exact next action (`/job-plan` or the pending `.md` file).
