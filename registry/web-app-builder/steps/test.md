---
name: test
description: Conduct side-by-side frozen-prototype comparison and human scenario acceptance testing.
---

# /test

Read the project constitution and current status. Use the following references from `docs/references/`: `design.md`, `workflow.md`, `quality.md`.

Gate: Automated build checks pass and the integrated app runs on `http://127.0.0.1:APP_PORT`.
Keep human product acceptance distinct from passing automated tests:
1. **Second Visual Fidelity Gate (Frozen Prototype vs Integrated App):**
   - Read the exact accepted prototype baseline and hashes from
     `docs/living/status.md`, including any revision frozen by scenarios.
     Verify that reference and launch it from a separate Git worktree or snapshot copy
     on a free port
     (`http://127.0.0.1:PROTO_PORT`) alongside `http://127.0.0.1:APP_PORT`—never checking
     out an old tag over active `./` files.
     Never reconstruct the baseline name from `VERSION` or silently fall back to an
     earlier tag. If it is unavailable, recover that exact baseline or record the
     comparison as blocked.
   - Compare layout, spacing, RTL typography, states and asset loading across both URLs,
     verifying zero runtime CDN calls. Record this second comparison separately from the
     `prototype` HTML-to-React comparison.
2. **Owner Scenario Walkthrough:**
   - Prepare synthetic test accounts; record any test admin credentials only in gitignored
     `docs/secrets/credentials.md` and reference that `.md` file safely—never
     printing passwords in chat or review sheets.
   - Write a pre-filled `.md` observation sheet
     `docs/versions/VERSION/NN-test-round.md` linked to
     `docs/living/test-scenarios.md` so the owner can test in the browser and
     record «چه دیدم» / «درست بود؟» (or conversation-language equivalents) in Obsidian.
3. **Defect Resolution:**
   - Fix reported visual/functional defects under `./`, rerun affected tests,
     refresh the running app and repeat impacted checks until the owner explicitly
     records acceptance in `docs/`.
