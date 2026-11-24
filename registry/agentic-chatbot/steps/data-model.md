---
name: data-model
description: Define agent business entities, session memory and redacted audit metadata persistence.
---

# /data-model

Read the project constitution and current status. Use the following references from `docs/references/`: `workflow.md`, `authority.md`.

Gate: `docs/living/sops.md` exists and has a closed review. Author `docs/living/data-model.md` in plain business terms without
raw SQL:
1. **Business Entities:** Domain nouns read or mutated by owned services (marking payment
   entities `not applicable` if payments are outside scope).
2. **Session, Proposal & Budget State:** Session IDs, authenticated caller context, SOP
   progress, pending `direct + soft` offers or `confirm + hard` proposals with expiry,
   and per-caller/global budget counters.
3. **Redacted Audit Metadata (Never Unredacted Raw Payloads):** Specify durable audit
   records using **redacted metadata only**—run ID, timestamp, caller ID, tool name,
   opaque handle IDs (`[h_*]`), outcome status, latency and token/cost counts. Never
   persist raw secrets, tokens, unmasked PII or dereferenced handle values in audit logs;
   exact permitted fields, access limits and retention windows are finalized in
   `docs/living/privacy.md`.

Resolve open questions via `docs/versions/VERSION/NN-analysis-data-model.md` in
Obsidian; once review closes, hand off to `/privacy`.
