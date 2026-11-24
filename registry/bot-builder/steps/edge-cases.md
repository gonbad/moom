---
name: edge-cases
description: Define failure recovery, stale callback handling, debounce and transport resilience.
---

# /edge-cases

Read the project constitution and current status. Use the following references from `docs/references/`: `fsm.md`, `workflow.md`, `messenger.md`.

Gate: `docs/living/integrations.md` exists and has a closed review. Author `docs/living/edge-cases.md`:
1. **Transport & Outbox Failures:** Polling timeout backoff, duplicate webhook delivery
   deduplication (`update_key`), send-timeout unknown outcomes without blind mutation
   replay, and invalid-token circuit breaking without logging secret values.
2. **Stale, Duplicate & Cross-Caller Actions:** Graceful answers for expired or old
   callback queries, rapid double-tap idempotency, and rejecting another caller's token.
3. **Unexpected Inputs & Mid-Flow `/start`:** Freeform text when buttons were expected,
   unsupported media/large files, and `/start` mid-flow behavior.
4. **Expiry & Cancellation:** Read-time draft/reservation expiry without relying on a
   background cron having run, plus explicit `«انصراف»` cleanup.

Resolve open questions via `docs/versions/VERSION/NN-analysis-edge-cases.md` in
Obsidian; once review closes, hand off to `/scenarios`.
