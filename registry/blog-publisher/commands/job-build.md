---
name: job-build
description: Assemble public output, offline ZIPs and verified downloads.
---

# /job-build

Read `AGENTS.md`, the four `docs/constitution/` documents and `docs/kandoo/living/profile.md`,
`job.md`, `server.md` and `status.md`. Resolve the active Project `ID` and `VERSION` from
status; all paths are workspace-root paths. Read only the installed references
`docs/kandoo/living/references/workflow.md`, `distribution.md` and `quality.md`, plus
`docs/projects/ID/living/idea.md`, `layout.md`, `publication.md` (when present) and
submitted rounds in `docs/projects/ID/versions/VERSION/`. Preserve earlier outputs and
authorization.

Gate: `docs/projects/ID/living/layout.md` and public source under `projects/ID/` are
ready. Use or generate only needed Kandoo (`kandoo/`) or Project (`projects/ID/`) build
helpers. Stage public files strictly from the allowlisted source directory, excluding
inputs, secrets, `docs/` and version history. Unfinished unrelated drafts must never
break a build; a draft preview build remains marked preview-only and undeployable.

Imported materials are local checksum-pinned artifacts; never invoke sibling template
sources, parent maintainer tools or network fetches during a build. Produce compiled web
output, standalone offline ZIPs, SHA-256 inventories and extracted network-disabled
verification (including paths with spaces or non-Latin characters). Run browser checks
with Project-owned dependencies under `projects/ID/checks/` when available; if a browser
binary or package download is unavailable, preserve the verified static/archive output,
use the prepared local check fallback and record blocked browser evidence honestly in a
`.md` verification report under `docs/projects/ID/versions/VERSION/`. Never refer the
participant to non-`.md` files outside `docs/`. Route to `/job-deploy` with separate
technical build, source fidelity and human acceptance states.

Apply the file-review/certainty protocol on `.md` files inside `docs/` and assess updates
to the Job, shared Kandoo, active Project and write-only creator feedback. Persist what
changed, evidence, pending review and next action in `docs/projects/ID/living/status.md`
and mirror `docs/kandoo/living/status.md`. Finish every reply with the current Job's full ordered
steps localized and one exact next action (`/job-deploy` or the `.md` review file in `docs/`).
