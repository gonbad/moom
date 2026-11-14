---
name: job-deploy
description: Deliver the verified deck locally or to an authorized host.
---

# /job-deploy

Read `AGENTS.md`, the four `docs/constitution/` documents and `docs/kandoo/living/profile.md`,
`job.md`, `server.md` and `status.md`. Resolve the active Project `ID` and `VERSION` from
status; all paths are workspace-root paths. Read only the installed references
`docs/kandoo/living/references/workflow.md` and `quality.md`, plus
`docs/projects/ID/living/status.md`, `docs/kandoo/living/server.md` and the `.md` build
verification record in `docs/projects/ID/versions/VERSION/`. Preserve earlier outputs and
authorization.

There is no separate `job-review` command: resolve speaker review and requested
corrections through `.md` review notes in `docs/projects/ID/versions/VERSION/` while
keeping technical readiness and human speaker acceptance distinct. Preserve previous
delivered versions. Verify that the exact delivered HTML/ZIP/PDF outputs under
`projects/ID/dist/` open cleanly offline with all fonts and media intact.

For local delivery (or when server setup was skipped), mark server hosting as skipped/not
needed, serve the deck on `http://127.0.0.1` when requested, and record the final
delivery summary and snapshot/tag identity (`project/ID/release/VERSION`, or local
SHA-256 snapshot if Git was deferred) in `docs/projects/ID/living/status.md` and
`docs/projects/ID/versions/VERSION/deploy-notes.md`—never referring the participant to
non-`.md` files outside `docs/`. If hosting was explicitly selected and authorized,
upload only public compiled assets, verify HTTPS and navigation, and record the live URL
and rollback path; if server access fails, preserve local delivery and record hosting as
blocked rather than deployed.

Apply the file-review/certainty protocol on `.md` files inside `docs/` and assess updates
to the Job, shared Kandoo, active Project and write-only creator feedback. Persist final
state in `docs/projects/ID/living/status.md` and mirror `docs/kandoo/living/status.md`.
Finish every reply with the current Job's full ordered steps localized and one exact final action
(reading the `.md` delivery summary in `docs/` or visiting the live `http://`/`https://` URL).
