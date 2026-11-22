---
name: deploy
description: Deliver the verified deck locally or to an authorized host.
---

# /deploy

Read the project constitution and current status. Use the following references from `docs/references/`: `workflow.md`, `quality.md`.

Deliver the verified downloadable offline artifact as the primary output; hosting
is secondary unless explicitly overridden. There is no separate review command: resolve speaker review and requested
corrections through `.md` review notes in `docs/versions/VERSION/` while
keeping technical readiness and human speaker acceptance distinct. Preserve previous
delivered versions. Verify that the exact delivered HTML/ZIP/PDF outputs under
`./dist/` open cleanly offline with all fonts and media intact.

For local delivery (or when server setup was skipped), mark server hosting as skipped/not
needed, serve the deck on `http://127.0.0.1` when requested, and record the final
delivery summary and snapshot/tag identity (`release/VERSION`, or local
SHA-256 snapshot if Git was deferred) in `docs/living/status.md` and
`docs/versions/VERSION/deploy-notes.md`—never referring the participant to
non-`.md` files outside `docs/`. If hosting was explicitly selected, resolve
`docs/living/server.md` using the infrastructure Constitution: use /server for dedicated hosting or record local deferral. Universal
setup leaves the target unselected, which is not a hosting skip. With the selected
target and existing authorization, upload only public compiled assets, verify HTTPS and navigation, and record the live URL
and rollback path; if server access fails, preserve local delivery and record hosting as
blocked rather than deployed.
