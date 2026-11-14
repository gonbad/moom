---
name: job-scenarios
description: Specify end-to-end acceptance test scenarios with synthetic identities verified on the prototype.
---

# /job-scenarios

Read `AGENTS.md`, the four `docs/constitution/` documents and `docs/kandoo/living/profile.md`,
`job.md`, `server.md` and `status.md`. Resolve the active Project `ID` and `VERSION` from
status; all paths are workspace-root paths. Read only the installed references
`docs/kandoo/living/references/workflow.md` and `quality.md`, plus
`docs/projects/ID/living/prd.md`, `data-model.md`, `ux.md` and submitted rounds in
`docs/projects/ID/versions/VERSION/`. Preserve earlier outputs and authorization.

Gate: Prototype acceptance and its exact baseline tag or immutable local snapshot are
recorded in `docs/projects/ID/living/status.md`. Start `projects/ID/frontend/` on its
allocated local port if needed.

Author `docs/projects/ID/living/test-scenarios.md` as the acceptance contract for
`/job-build` and `/job-test`, using **synthetic test identities and isolated synthetic
test credentials** (for example `09000000001` and synthetic test accounts—never real
personal phone numbers, real customer data or live passwords):
1. **End-User Primary Flows:** Complete journeys from entry to verified outcome.
2. **Admin & Operator Flows:** Back-office review, approvals and state management.
3. **Combined Multi-Actor Flows:** End-user actions triggering admin updates that reflect
   back on the user's screen.
4. **Edge Cases & Failure Recovery:** Empty/boundary inputs, Persian/Arabic numerals,
   duplicate entries, upstream 503/timeout fallbacks, rapid double-click idempotency,
   empty states, unauthenticated/cross-user denial and session-expiry recovery.

Walk every scenario against the running prototype. If a scenario requires changing the
prototype, update `projects/ID/frontend/` and affected living docs, re-verify HTML/system
fidelity, freeze a new non-colliding prototype reference (such as
`project/ID/prototype/VERSION-r2` or a new snapshot path/hash) after the owner accepts
the changed revision. Update the baseline and acceptance evidence in Project status,
preserve the prior baseline, and invalidate stale checks.
Resolve open questions via `docs/projects/ID/versions/VERSION/NN-questions.md` in
Obsidian; once submitted, route to `/job-plan`.

Apply the file-review/certainty protocol on `.md` files inside `docs/` and assess updates
to the Job, shared Kandoo, active Project and write-only creator feedback. Persist what
changed, evidence, pending review and next action in `docs/projects/ID/living/status.md`
and mirror `docs/kandoo/living/status.md`. Finish every reply with the current Job's full ordered
steps localized and one exact next action (`/job-plan` or the pending `.md` file).
