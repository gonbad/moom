---
name: build
description: Implement bot engine, FSM transitions, messenger adapters and self-contained simulated test harness.
---

# /build

Read the project constitution and current status. Use the following references from `docs/references/`: `fsm.md`, `workflow.md`, `payments.md`, `messenger.md`, `infrastructure.md`, `quality.md`.

Gate: `architecture.md`, `checklist.md` and `handoff.md` exist with a closed review. Implement inside `./`:
1. **Core Bot Engine (`./app/`):**
   - Implement models and migrations on the planned database route (VPS PostgreSQL over
     native OpenSSH tunnel with isolated test data, local Docker PostgreSQL on
     macOS/Linux, or the explicitly selected Windows-no-server SQLite fallback in
     `./data/`). If a live VPS tunnel is temporarily unreachable, preserve
     completed code and mark live DB verification pending rather than claiming it passed.
   - Implement the deterministic FSM dispatcher from `flow.md`, selected messenger
     adapters from `integrations.md`, and payment/receipt modules **only if payments are
     in scope**.
   - Read secret tokens only from gitignored `docs/secrets/credentials.md`
     and sync `./.env` internally without printing secrets or referring the
     participant to non-`.md` files.
2. **Self-Contained Simulated Harness (`./tests/`):**
   - Build a local in-memory messenger harness inside `./tests/` that injects
     normalized `Event` fixtures (commands, text, callbacks, media, duplicates, stale
     tokens and mid-dialog restarts) into the dispatcher against isolated test data and
     asserts outgoing replies plus database state without external repos or network calls.
3. **Verification Summary:**
   - Run the automated test suite to green and record what passed and what live checks
     remain pending in a `.md` report under `docs/versions/VERSION/`.
