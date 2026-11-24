---
name: edge-cases
description: Specify defenses against prompt injection, token budget exhaustion, hallucination and outages.
---

# /edge-cases

Read the project constitution and current status. Use the following references from `docs/references/`: `workflow.md`, `budgets.md`, `authority.md`, `messenger.md`.

Gate: `docs/living/capabilities.md` exists and has a closed review. Author `docs/living/edge-cases.md`:
1. **Prompt Injection & Stale History:** Defenses against indirect injection from
   tool/document payloads, role-switching prompts and stale chat history attempting to
   reuse expired offers or manufacture approval.
2. **Atomic Token, Cost & Concurrency Quotas:** Per-run tool/turn/token limits plus
   per-caller and global daily spend caps enforced atomically outside the prompt, with
   graceful user-facing hold messages.
3. **Malformed Tool Calls & Unknown Outcomes:** Typed schema-error feedback, bounded
   retries and querying idempotency keys rather than blindly repeating unknown-outcome
   mutations.
4. **Provider & Service Outage Fallback:** Deterministic fallback menu/message preserving
   pending state and enforcing the exact same caller scope and `confirm + hard` gates as
   normal runs, recovering only after a customer-data-free provider probe succeeds.

Resolve open questions via `docs/versions/VERSION/NN-analysis-edge-cases.md` in
Obsidian; once review closes, hand off to `/prompts`.
