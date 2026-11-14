---
name: job-edge-cases
description: Specify defenses against prompt injection, token budget exhaustion, hallucination and outages.
---

# /job-edge-cases

Read `AGENTS.md`, the four `docs/constitution/` documents and `docs/kandoo/living/profile.md`,
`job.md`, `server.md` and `status.md`. Resolve the active Project `ID` and `VERSION` from
status; all paths are workspace-root paths. Read the installed references
`docs/kandoo/living/references/workflow.md`, `authority.md` and `budgets.md` (plus
`messenger.md` when a messenger channel is selected), `docs/projects/ID/living/capabilities.md`
and submitted rounds in `docs/projects/ID/versions/VERSION/`. Preserve earlier outputs
and authorization.

Gate: `docs/projects/ID/living/capabilities.md` exists and has no unsubmitted question
round pending. Author `docs/projects/ID/living/edge-cases.md`:
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

Resolve open questions via `docs/projects/ID/versions/VERSION/NN-questions.md` in
Obsidian; once submitted, hand off to `/job-prompts`.

Apply the file-review/certainty protocol on `.md` files inside `docs/` and assess updates
to the Job, shared Kandoo, active Project and write-only creator feedback. Persist what
changed, evidence, pending review and next action in `docs/projects/ID/living/status.md`
and mirror `docs/kandoo/living/status.md`. Finish every reply with the current Job's full ordered
steps localized and one exact next action (`/job-prompts` or the pending `.md` file).
