# PostgreSQL bot state

Write LIVING/data-model.md with platform-scoped user identity, dialog state/version,
context, deduplicated inbox, outbox/effect idempotency, domain records and applicable
payment/review records. Define transaction boundaries, unique constraints, retention,
migrations, backup/restore and separate test data. Use server PostgreSQL in development
and production. Review the data meaning and concurrency rules before FSM implementation.
