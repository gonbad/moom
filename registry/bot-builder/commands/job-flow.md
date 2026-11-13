---
name: job-flow
description: Design dialog transitions, adapter contracts and idempotent effects.
---

# /job-flow

Read `AGENTS.md`, the four `docs/constitution/` documents and the living profile,
Job, server and status. Resolve the active Project/version from status; all paths here
are workspace-root paths. Read only the installed references named below and current
Project inputs/answers. Preserve earlier outputs and authorization.

Read PRD/data plus installed fsm/messenger/payments references as applicable. Write
`living/flows.md` with current state, event, guard, transactional mutation/next state and
reply for every transition. Include back/edit/cancel, invalid input, stale buttons,
expiry and restart. Bind callback tokens to trusted caller/action/state/expiry.

Write `platforms.md` mapping each selected API payload to the normalized internal event
and outbound delivery interface. Check actual capabilities rather than assuming Telegram
compatibility. Specify deduplication, concurrency, outbox and unknown-outcome behavior.
Review the full journey and failure matrix, then route to `job-build`.

Apply the file-review/certainty protocol and assess updates to the Job, shared Kandoo,
active Project and write-only creator feedback. Persist this step's outcome, pending
review and next action in Project status and mirror shared status. Finish every reply
with all ordered steps localized and one exact next action; never invent acceptance.
