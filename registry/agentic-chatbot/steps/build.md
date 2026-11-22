---
name: build
description: Implement agent harness, reference monitor, owned services and self-contained security gate tests.
---

# /build

Read the project constitution and current status. Use the following references from `docs/references/`: `services.md`, `workflow.md`, `budgets.md`, `authority.md`, `infrastructure.md`, `quality.md`.

Gate: `architecture.md`, `checklist.md` and `handoff.md` exist with a closed review. Implement inside `./`:
1. **Harness, Monitor & Services (`./app/`, `./services/`):**
   - Implement models and migrations on the planned database route (VPS PostgreSQL over
     native OpenSSH tunnel with isolated test data, local Docker on macOS/Linux, or the
     explicitly selected Windows-no-server SQLite fallback in `./data/`). Mark
     live VPS DB verification pending if the tunnel is unreachable rather than faking a pass.
   - Implement the reference monitor enforcing the exact owner-selected `execution_mode`
     + `confirmation_policy` pairs from `capabilities.md`: `read + none`,
     `direct + none`, `direct + soft` and `confirm + hard` (never inventing a mixed
     `soft_confirm` execution mode or overriding owner-chosen `direct` policies with a
     global hard rule).
   - Implement the `[h_*]` handle vault, redacted audit logging, atomic budget accounting,
     deterministic outage fallback, and owned services/bridges loading prompts from
     `docs/living/prompts/` (or synced into `./app/prompts/`).
2. **Self-Contained Automated Gate Tests (`./tests/`):**
   - Write in-process scripted model-turn tests verifying: `confirm + hard` proposals
     cannot execute without a valid one-use approval bound to `caller + action + args_hash`
     (even if the model passes `confirmed=true`); owner-selected `direct + none` and
     `direct + soft` actions follow their chosen policy without silent global conversion;
     wrong-caller/expired `[h_*]` handles fail; durable audit logs contain zero raw
     secrets/PII; and concurrent runs respect atomic token/spend caps.
3. **Verification Summary:**
   - Run the local test suite to green and summarize results in a `.md` report under
     `docs/versions/VERSION/`, then route to `/wire`.
