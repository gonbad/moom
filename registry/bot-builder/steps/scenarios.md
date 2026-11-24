---
name: scenarios
description: Write interactive messenger turn scenarios with synthetic identities and expected responses.
---

# /scenarios

Read the project constitution and current status. Use the following references from `docs/references/`: `workflow.md`, `quality.md`.

Gate: `docs/living/edge-cases.md` exists and has a closed review. Author `docs/living/test-scenarios.md` using **synthetic
caller IDs and synthetic test data** (never real customer phone numbers or live payment
cards):
1. **Scenario Structure:** Scenario ID/title, preconditions/seeds, turn-by-turn sequence
   (actor command/text/button/callback/media → expected bot reply and keyboard), and
   expected terminal FSM + database state.
2. **Required Coverage:** Onboarding `/start`, primary completion flow, admin/operator
   actions, duplicate update delivery, stale callback tap, invalid input, cancellation
   mid-flow, restart mid-dialog, and—**only if payments are in scope**—payment/receipt
   verification and replay (otherwise mark payment scenarios `not applicable`).

Resolve open questions via `docs/versions/VERSION/NN-analysis-scenarios.md` in
Obsidian; once review closes, hand off to `/architecture`.
