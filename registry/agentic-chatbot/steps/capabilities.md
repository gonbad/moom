---
name: capabilities
description: Record the owner's per-action execution mode and confirmation policy after explaining tradeoffs.
---

# /capabilities

Read the project constitution and current status. Use the following references from `docs/references/`: `workflow.md`, `payments.md`, `authority.md`.

Gate: `docs/living/privacy.md` exists and has a closed review. Author `docs/living/capabilities.md` using one consistent two-column
capability schema shared across specification, prompts, harness and tests:
1. **Capability Partition Table:**
   | Action | Execution Mode | Confirmation Policy | Plain Parameters | Envelope Parameters | Outage / Fallback |
   | --- | --- | --- | --- | --- | --- |
   | (tool name) | `read` / `direct` / `confirm` | `none` / `soft` / `hard` | (public args) | (`HandleRef[Kind]`) | (outage behavior) |
2. **Valid Policy Combinations & Tradeoffs:**
   - `read` + `none`: Caller-scoped read-only lookup executed directly within budget.
   - `direct` + `none`: Caller-scoped mutation executed directly without extra turn delay.
   - `direct` + `soft`: Conversational confirmation—offer delivered first, caller reply
     interpreted in context, deterministic provenance/caller/expiry/one-use checks
     enforced; explain clearly that `soft` improves UX safety against misunderstandings
     but is not an independent security barrier against prompt injection.
   - `confirm` + `hard`: Proposal-only to the model (`propose_<action>`); raw executor
     excluded from model tools; independent out-of-band/trusted-UI one-use approval
     bound to `caller + action + args_hash` required before execution (never satisfied by
     model dialogue or `confirmed=true`).
3. **Owner Per-Action Choice (No Blanket Global Override):**
   Explain the concrete security and UX consequences for each action in
   `docs/versions/VERSION/NN-questions.md` and **preserve the owner's
   explicit per-action selection**—do not impose a global rule forbidding `direct` +
   `soft` or `direct` + `none` on financial, deletion or high-privilege actions when the
   owner chooses them. Caller identity, backend business eligibility, idempotency,
   handle-sink validation, budget checks and separate payment settlement remain mandatory
   under every policy.

Once review closes, record confirmed selections
in `capabilities.md` and hand off to `/edge-cases`.
