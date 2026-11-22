---
name: test
description: Conduct live messenger rehearsal with isolated test credentials and owner acceptance rounds.
---

# /test

Read the project constitution and current status. Use the following references from `docs/references/`: `workflow.md`, `messenger.md`, `infrastructure.md`, `quality.md`.

Gate: Automated simulated harness tests in `/build` pass. Fixture tests never prove
live messenger connectivity:
1. **Isolated Live Test Connection:**
   - Load isolated test bot credentials from gitignored
     `docs/secrets/credentials.md` (never
     printing token values in chat or logs). Start the bot locally via polling or the
     verified reverse SSH webhook tunnel. If messenger network access or a test token is
     unavailable, apply the configured forward proxy or mark live messenger rehearsal
     blocked/pending without fabricating acceptance.
2. **Owner Rehearsal Rounds:**
   - Share the non-secret test bot handle and prepare a pre-filled `.md` observation
     sheet `docs/versions/VERSION/NN-test-round.md` referencing
     `docs/living/test-scenarios.md` so the owner can test real turns,
     buttons, cancellations, restarts and conditional payment cases, recording results in
     Obsidian.
3. **Defect Resolution:**
   - Fix reported transport, keyboard, RTL formatting or state defects in `./`,
     rerun harness regressions and repeat affected live turns until the owner records
     explicit acceptance in `docs/`.
