---
name: job-data-model
description: Define agent business entities, session memory and redacted audit metadata persistence.
---

# /job-data-model

Read `AGENTS.md`, the four `docs/constitution/` documents and `docs/kandoo/living/profile.md`,
`job.md`, `server.md` and `status.md`. Resolve the active Project `ID` and `VERSION` from
status; all paths are workspace-root paths. Read only the installed references
`docs/kandoo/living/references/workflow.md` and `authority.md`, plus
`docs/projects/ID/living/prd.md`, `tools.md`, `sops.md` and submitted rounds in
`docs/projects/ID/versions/VERSION/`. Preserve earlier outputs and authorization.

Gate: `docs/projects/ID/living/sops.md` exists and has no unsubmitted question round
pending. Author `docs/projects/ID/living/data-model.md` in plain business terms without
raw SQL:
1. **Business Entities:** Domain nouns read or mutated by owned services (marking payment
   entities `not applicable` if payments are outside scope).
2. **Session, Proposal & Budget State:** Session IDs, authenticated caller context, SOP
   progress, pending `direct + soft` offers or `confirm + hard` proposals with expiry,
   and per-caller/global budget counters.
3. **Redacted Audit Metadata (Never Unredacted Raw Payloads):** Specify durable audit
   records using **redacted metadata only**—run ID, timestamp, caller ID, tool name,
   opaque handle IDs (`[h_*]`), outcome status, latency and token/cost counts. Never
   persist raw secrets, tokens, unmasked PII or dereferenced handle values in audit logs;
   exact permitted fields, access limits and retention windows are finalized in
   `docs/projects/ID/living/privacy.md`.

Resolve open questions via `docs/projects/ID/versions/VERSION/NN-questions.md` in
Obsidian; once submitted, hand off to `/job-privacy`.

Apply the file-review/certainty protocol on `.md` files inside `docs/` and assess updates
to the Job, shared Kandoo, active Project and write-only creator feedback. Persist what
changed, evidence, pending review and next action in `docs/projects/ID/living/status.md`
and mirror `docs/kandoo/living/status.md`. Finish every reply with the current Job's full ordered
steps localized and one exact next action (`/job-privacy` or the pending `.md` file).
