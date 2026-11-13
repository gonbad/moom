---
name: job-build
description: Implement adapters, persistent dialog state and business services.
---

# /job-build

Read `AGENTS.md`, the four `docs/constitution/` documents and the living profile,
Job, server and status. Resolve the active Project/version from status; all paths here
are workspace-root paths. Read only the installed references named below and current
Project inputs/answers. Preserve earlier outputs and authorization.

Read reviewed flows, installed fsm/messenger/infrastructure references and payments
when selected. Generate Project code with separate transport adapters, normalized
dispatcher, transactional business service and durable outbox. Enforce caller scope,
idempotency and expiry in the real database path, not only button rendering.

Use allocated PostgreSQL/Redis services and native SSH forwarding for local development.
Keep credentials ignored and reuse them safely on resume. Implement platform-specific
payload/error mappings, acknowledgment and bounded retries. Test one vertical journey
with fixtures, then affected persistence/concurrency checks; fixture success is not
live platform evidence. Record results and next action `job-test`.

Apply the file-review/certainty protocol and assess updates to the Job, shared Kandoo,
active Project and write-only creator feedback. Persist this step's outcome, pending
review and next action in Project status and mirror shared status. Finish every reply
with all ordered steps localized and one exact next action; never invent acceptance.
