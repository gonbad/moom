---
name: privacy
description: Classify sensitive data, define handle-envelope masking and specify audit redaction and retention.
---

# /privacy

Read the project constitution and current status. Use the following references from `docs/references/`: `workflow.md`, `authority.md`.

Gate: `docs/living/data-model.md` exists and has a closed review. Author `docs/living/privacy.md`:
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

Resolve open questions via `docs/versions/VERSION/NN-analysis-privacy.md` in
Obsidian; once review closes, hand off to `/capabilities`.
