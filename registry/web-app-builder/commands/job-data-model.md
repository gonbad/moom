---
name: job-data-model
description: Specify what the product must remember using plain conceptual business nouns without SQL.
---

# /job-data-model

Read `AGENTS.md`, the four `docs/constitution/` documents and `docs/kandoo/living/profile.md`,
`job.md`, `server.md` and `status.md`. Resolve the active Project `ID` and `VERSION` from
status; all paths are workspace-root paths. Read only the installed reference
`docs/kandoo/living/references/workflow.md`, `docs/projects/ID/living/idea.md`, `prd.md`
and submitted rounds in `docs/projects/ID/versions/VERSION/`. Preserve earlier outputs
and authorization.

Gate: `docs/projects/ID/living/prd.md` exists and has no unsubmitted question round
pending. Author `docs/projects/ID/living/data-model.md` as a plain-language business
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

`/job-ux` may refine this document in place if screen design exposes missing fields.
Resolve open questions via `docs/projects/ID/versions/VERSION/NN-questions.md` in
Obsidian; once submitted, hand off to `/job-ux`.

Apply the file-review/certainty protocol on `.md` files inside `docs/` and assess updates
to the Job, shared Kandoo, active Project and write-only creator feedback. Persist what
changed, evidence, pending review and next action in `docs/projects/ID/living/status.md`
and mirror `docs/kandoo/living/status.md`. Finish every reply with the current Job's full ordered
steps localized and one exact next action (`/job-ux` or the pending `.md` question file).
