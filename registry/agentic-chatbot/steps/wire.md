---
name: wire
description: Connect real inference providers and scoped services, verifying live tool round trips.
---

# /wire

Read the project constitution and current status. Use the following references from `docs/references/`: `services.md`, `workflow.md`, `budgets.md`, `payments.md`, `messenger.md`, `infrastructure.md`.

Gate: Automated deterministic gate tests in `/build` pass. Transition from scripted
fixtures to the **configured runtime model and services**:
1. **Provider & Service Credentials:**
   - Read runtime model/service keys from gitignored
     `docs/secrets/credentials.md` and sync
     `./.env` internally without printing secret values or referring the
     participant to non-`.md` files. Apply the configured forward proxy per process if
     needed; if a live provider or upstream API is unavailable, preserve local harness
     evidence and record that dependency as `planned` or `blocked` rather than `verified`.
2. **Bounded Live Tool Round Trips:**
   - Run real multi-turn requests using `docs/living/prompts/` and synthetic
     caller identities.
   - Verify structured tool calls, `[h_*]` handle preservation, reference-monitor
     interception, real/sandbox service responses, natural persona synthesis and redacted
     audit entries.
3. **Redacted Wiring Report:**
   - Record each provider/service/transport state (`planned`, `configured`,
     `authenticated`, `callable`, `effect-verified`), observed latency, token usage and
     redacted diagnostics in `docs/versions/VERSION/wire-report.md`, then
     route to `/test`.
