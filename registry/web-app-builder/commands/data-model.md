# Data model

Derive LIVING/data-model.md from the reviewed PRD. Specify tables, ownership, typed
columns, primary/foreign keys, relationships, constraints, indexes, time zones and
transaction boundaries. Use PostgreSQL, including UUID/TIMESTAMPTZ/JSONB when useful;
no SQLite substitute. Plan repeatable migrations, backup/restore, seed data and a
separate test database/schema. Reconcile the inventory of existing data before changes.
Review data meaning and retention with the owner before proceeding to UX.
