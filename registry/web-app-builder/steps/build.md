---
name: build
description: Implement backend services, migrations, API endpoints and wire the approved frontend seam.
---

# /build

Read the project constitution and current status. Use the following references from `docs/references/`: `workflow.md`, `infrastructure.md`, `quality.md`.

Gate: `architecture.md`, `checklist.md` and `handoff.md` exist with a closed review. Implement inside `./`:
1. **Backend & Database (`./backend/`):**
   - Implement models, migrations, transactional ownership checks and API routes matching
     `architecture.md`.
   - Connect to the planned database route (VPS PostgreSQL over verified native OpenSSH
     tunnel with isolated test data, local Docker PostgreSQL on macOS/Linux, or the
     explicitly selected Windows-no-server SQLite fallback in `./data/`). If a
     live VPS tunnel or external API is temporarily unreachable, preserve completed code,
     run local fallback adapters and mark live database/service verification pending rather
     than claiming it passed.
   - Read secret values from gitignored `docs/secrets/credentials.md` and sync
     runtime `./backend/.env` internally; never print secrets in chat or ask the
     participant to edit `.env` or code files.
2. **Frontend Wiring (`./frontend/`):**
   - Preserve the approved screens and Tailwind classes unchanged; replace mock generators
     inside `./frontend/src/api/` with real HTTP calls.
   - Verify production frontend compilation with zero external CDN dependencies.
3. **Automated Tests & Local Stack:**
   - Write and run self-contained backend/contract/migration tests under
     `./backend/tests/` covering scenarios, authorization denials, idempotency
     and upstream failures.
   - Start the full-stack application on its allocated local port (`http://127.0.0.1:APP_PORT`),
     walk the primary flows, and record build/test evidence in a `.md` summary under
     `docs/versions/VERSION/`.
