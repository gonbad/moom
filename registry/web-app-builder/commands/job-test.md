---
name: job-test
description: Conduct side-by-side frozen-prototype comparison and human scenario acceptance testing.
---

# /job-test

Read `AGENTS.md`, the four `docs/constitution/` documents and `docs/kandoo/living/profile.md`,
`job.md`, `server.md` and `status.md`. Resolve the active Project `ID` and `VERSION` from
status; all paths are workspace-root paths. Read only the installed references
`docs/kandoo/living/references/workflow.md`, `design.md` and `quality.md`, plus
`docs/projects/ID/living/test-scenarios.md`, `architecture.md` and submitted rounds in
`docs/projects/ID/versions/VERSION/`. Preserve earlier outputs and authorization.

Gate: Automated build checks pass and the integrated app runs on `http://127.0.0.1:APP_PORT`.
Keep human product acceptance distinct from passing automated tests:
1. **Second Visual Fidelity Gate (Frozen Prototype vs Integrated App):**
   - Read the exact accepted prototype baseline and hashes from
     `docs/projects/ID/living/status.md`, including any revision frozen by scenarios.
     Verify that reference and launch it from a separate Git worktree or snapshot copy
     on a free port
     (`http://127.0.0.1:PROTO_PORT`) alongside `http://127.0.0.1:APP_PORT`—never checking
     out an old tag over active `projects/ID/` files.
     Never reconstruct the baseline name from `VERSION` or silently fall back to an
     earlier tag. If it is unavailable, recover that exact baseline or record the
     comparison as blocked.
   - Compare layout, spacing, RTL typography, states and asset loading across both URLs,
     verifying zero runtime CDN calls. Record this second comparison separately from the
     `job-prototype` HTML-to-React comparison.
2. **Owner Scenario Walkthrough:**
   - Prepare synthetic test accounts; record any test admin credentials only in gitignored
     `docs/projects/ID/secrets/credentials.md` and reference that `.md` file safely—never
     printing passwords in chat or review sheets.
   - Write a pre-filled `.md` observation sheet
     `docs/projects/ID/versions/VERSION/NN-test-round.md` linked to
     `docs/projects/ID/living/test-scenarios.md` so the owner can test in the browser and
     record «چه دیدم» / «درست بود؟» (or conversation-language equivalents) in Obsidian.
3. **Defect Resolution:**
   - Fix reported visual/functional defects under `projects/ID/`, rerun affected tests,
     refresh the running app and repeat impacted checks until the owner explicitly
     records acceptance in `docs/`.

Apply the file-review/certainty protocol on `.md` files inside `docs/` and assess updates
to the Job, shared Kandoo, active Project and write-only creator feedback. Persist owner
acceptance, evidence and next action in `docs/projects/ID/living/status.md` and mirror
`docs/kandoo/living/status.md`. Finish every reply with the current Job's full ordered steps localized
and one exact next action (`/job-deploy` or the `.md` test-round file in `docs/`).
