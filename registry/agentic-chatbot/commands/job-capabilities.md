---
name: job-capabilities
description: Record the owner's per-action execution mode and confirmation policy after explaining tradeoffs.
---

# /job-capabilities

Read `AGENTS.md`, the four `docs/constitution/` documents and `docs/kandoo/living/profile.md`,
`job.md`, `server.md` and `status.md`. Resolve the active Project `ID` and `VERSION` from
status; all paths are workspace-root paths. Read the installed references
`docs/kandoo/living/references/workflow.md` and `authority.md` (plus `payments.md` when
payments apply), `docs/projects/ID/living/tools.md`, `privacy.md` and submitted rounds in
`docs/projects/ID/versions/VERSION/`. Preserve earlier outputs and authorization.

Gate: `docs/projects/ID/living/privacy.md` exists and has no unsubmitted question round
pending. Author `docs/projects/ID/living/capabilities.md` using one consistent two-column
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
   `docs/projects/ID/versions/VERSION/NN-questions.md` and **preserve the owner's
   explicit per-action selection**—do not impose a global rule forbidding `direct` +
   `soft` or `direct` + `none` on financial, deletion or high-privilege actions when the
   owner chooses them. Caller identity, backend business eligibility, idempotency,
   handle-sink validation, budget checks and separate payment settlement remain mandatory
   under every policy.

Once the question round is submitted, record Confirmed vs Delegated/Provisional selections
in `capabilities.md` and hand off to `/job-edge-cases`.

Apply the file-review/certainty protocol on `.md` files inside `docs/` and assess updates
to the Job, shared Kandoo, active Project and write-only creator feedback. Persist what
changed, evidence, pending review and next action in `docs/projects/ID/living/status.md`
and mirror `docs/kandoo/living/status.md`. Finish every reply with the current Job's full ordered
steps localized and one exact next action (`/job-edge-cases` or the pending `.md` file).
