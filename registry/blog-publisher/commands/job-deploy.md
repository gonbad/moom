---
name: job-deploy
description: Deliver locally or publish only the verified release inventory.
---

# /job-deploy

Read `AGENTS.md`, the four `docs/constitution/` documents and `docs/kandoo/living/profile.md`,
`job.md`, `server.md` and `status.md`. Resolve the active Project `ID` and `VERSION` from
status; all paths are workspace-root paths. Read only the installed references
`docs/kandoo/living/references/workflow.md`, `distribution.md`, `infrastructure.md` and
`quality.md`, plus `docs/projects/ID/living/status.md`, `publication.md` (when present)
and `docs/kandoo/living/server.md`. Preserve earlier outputs and authorization.

Gate: Build verification is recorded in `docs/projects/ID/versions/VERSION/`. If local
or private delivery is chosen (or server setup was skipped), mark server hosting as
skipped/not needed, serve a local `http://127.0.0.1` preview when requested, and record
the complete local/offline delivery summary in `docs/projects/ID/living/status.md` and
`docs/projects/ID/versions/VERSION/deploy-notes.md`—never requiring a server or
referring the participant to non-`.md` files outside `docs/`.

For public hosting, require explicit owner acceptance and preserved authorization for the
specific origin (`docs/kandoo/living/publication.md`); a Job revision supplies no new
target permission. Reject preview-only builds and upload only verified compiled files,
never source, secrets or `docs/`. Compare uploaded hashes, activate atomically, verify
HTTPS entry pages, downloads and health checks, and roll back on failure. If SSH or
network access fails, preserve the local release and record live deployment as blocked
without claiming publication. Save an immutable Markdown deployment receipt in the
current shared version (`docs/kandoo/versions/`) and `deploy-notes.md`, keeping live
deployment evidence and human editorial acceptance distinct.

Apply the file-review/certainty protocol on `.md` files inside `docs/` and assess updates
to the Job, shared Kandoo, active Project and write-only creator feedback. Persist final
delivery state in `docs/projects/ID/living/status.md` and mirror
`docs/kandoo/living/status.md`. Finish every reply with the current Job's full ordered steps localized
and one exact final action (reading the `.md` delivery summary in `docs/` or visiting the
verified `http://`/`https://` URL).
