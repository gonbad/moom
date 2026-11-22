---
name: deploy
description: Publish verified web output to the explicitly selected publication target, honoring explicit deferrals.
---

# /deploy

Read the project constitution and current status. Use the following references from `docs/references/`: `workflow.md`, `distribution.md`, `infrastructure.md`, `quality.md`.

Before hosting, resolve Project server selection and publication scope using
`docs/living/server.md` and the installed infrastructure reference. This
stage owns initial intake. Read the copied shared target instructions and local protected access, or record local deferral. An unasked server is not a skipped server. Preserve shared
origins and other Projects. If target selection changes canonical links or release
scope, rebuild/verify those outputs before publishing.

Gate: Build verification is recorded in `docs/versions/VERSION/`. If local
or private delivery is chosen (or server setup was skipped), mark server hosting as
skipped/not needed, serve a local `http://127.0.0.1` preview when requested, and record
the local preview/delivery summary in `docs/living/status.md` and
`docs/versions/VERSION/deploy-notes.md`—never requiring a server or
referring the participant to non-`.md` files outside `docs/`.

For public hosting, require explicit owner acceptance and preserved authorization for the
specific origin recorded in `docs/living/publication.md`; a Job revision supplies no new
target permission. Reject preview-only builds and upload only verified compiled files,
never source, secrets or `docs/`. Compare uploaded hashes, activate atomically, verify
HTTPS entry pages/assets on the origin and supported aliases, intentional downloads
and health checks, and roll back on failure. If SSH or
network access fails, preserve the local release and record live deployment as blocked
without claiming publication. Save an immutable Markdown deployment receipt in the
project dossier `docs/versions/VERSION/` and `deploy-notes.md`, keeping live
deployment evidence and human editorial acceptance distinct.
