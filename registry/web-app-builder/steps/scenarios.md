---
name: scenarios
description: Specify end-to-end acceptance test scenarios with synthetic identities verified on the prototype.
---

# /scenarios

Read the project constitution and current status. Use the following references from `docs/references/`: `workflow.md`, `quality.md`.

Gate: Prototype acceptance and its exact baseline tag or immutable local snapshot are
recorded in `docs/living/status.md`. Start `./frontend/` on its
allocated local port if needed.

Author `docs/living/test-scenarios.md` as the acceptance contract for
`/build` and `/test`, using **synthetic test identities and isolated synthetic
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
prototype, update `./frontend/` and affected living docs, re-verify HTML/system
fidelity, freeze a new non-colliding prototype reference (such as
`project/prototype/VERSION-r2` or a new snapshot path/hash) after the owner accepts
the changed revision. Update the baseline and acceptance evidence in Project status,
preserve the prior baseline, and invalidate stale checks.
Resolve open questions via `docs/versions/VERSION/NN-questions.md` in
Obsidian; once review closes, route to `/architecture`.
