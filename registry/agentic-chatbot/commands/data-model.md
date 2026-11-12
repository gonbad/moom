# Agent and service data model

Write LIVING/data-model.md with PostgreSQL schema, platform-scoped caller identity,
conversation/run context, history, handles, proposals, inbox/outbox idempotency, quotas
and applicable domain state. Keep independently owned backend/bridge state separate.
Specify migrations, locks/constraints, retention, backup/restore and separate test data.
Review data meaning and service ownership before privacy and capability declarations.
