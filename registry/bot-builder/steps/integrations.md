---
name: integrations
description: Configure messenger platform adapters, API differences and conditional payment policies.
---

# /integrations

Read the project constitution and current status. Use the following references from `docs/references/`: `workflow.md`, `payments.md`, `messenger.md`.

Gate: `docs/living/data-model.md` exists and has a closed review. Author `docs/living/integrations.md` (always named
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
   `docs/secrets/credentials.md`—keep them out of
   non-`.md` files referred to the participant.

Resolve open questions via `docs/versions/VERSION/NN-questions.md` in
Obsidian; once review closes, hand off to `/edge-cases`.
