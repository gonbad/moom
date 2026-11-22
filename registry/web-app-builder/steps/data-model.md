---
name: data-model
description: Specify what the product must remember using plain conceptual business nouns without SQL.
---

# /data-model

Read the project constitution and current status. Use the following references from `docs/references/`: `workflow.md`.

Gate: `docs/living/prd.md` exists and has a closed review. Author `docs/living/data-model.md` as a plain-language business
domain specification—strictly forbidding SQL, table names, foreign keys, indexes or ERD
syntax (those belong later in `architecture.md`):
1. **Entity Inventory:** Every business thing («چیز») the product remembers, one line each.
2. **Entity Details:** Plain explanation plus a table of field name · business meaning ·
   required? · unique («یکتا»)?
3. **Relationships:** Plain sentences using one-to-many («یک‌به‌چند»), many-to-many
   («چند‌به‌چند») or one-to-one («یک‌به‌یک»).
4. **Data Integrity Invariants:** Domain rules that must always hold (such as non-negative
   balances or immutable settled orders).
5. **Intentionally Omitted Data:** Nouns or fields excluded from this version.

`/ux` may refine this document in place if screen design exposes missing fields.
Resolve open questions via `docs/versions/VERSION/NN-questions.md` in
Obsidian; once review closes, hand off to `/ux`.
