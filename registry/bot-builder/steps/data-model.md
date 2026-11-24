---
name: data-model
description: Define persistent bot data entities, user profiles, session states and optional transaction records.
---

# /data-model

Read the project constitution and current status. Use the following references from `docs/references/`: `fsm.md`, `workflow.md`.

Gate: `docs/living/flow.md` exists and has a closed review. Author `docs/living/data-model.md` in plain business terms without
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

Resolve open questions via `docs/versions/VERSION/NN-analysis-data-model.md` in
Obsidian; once review closes, hand off to `/integrations`.
