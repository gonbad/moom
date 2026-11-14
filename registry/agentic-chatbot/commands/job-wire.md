---
name: job-wire
description: Connect real inference providers and scoped services, verifying live tool round trips.
---

# /job-wire

Read `AGENTS.md`, the four `docs/constitution/` documents and `docs/kandoo/living/profile.md`,
`job.md`, `server.md` and `status.md`. Resolve the active Project `ID` and `VERSION` from
status; all paths are workspace-root paths. Read the installed references
`docs/kandoo/living/references/workflow.md`, `services.md`, `budgets.md` and
`infrastructure.md` (plus `messenger.md` and `payments.md` when in scope), plus
`docs/projects/ID/living/tools.md`, `capabilities.md`, `docs/projects/ID/living/prompts/` and submitted
rounds in `docs/projects/ID/versions/VERSION/`. Preserve earlier outputs and authorization.

Gate: Automated deterministic gate tests in `/job-build` pass. Transition from scripted
fixtures to the **configured runtime model and services**:
1. **Provider & Service Credentials:**
   - Read runtime model/service keys from gitignored
     `docs/projects/ID/secrets/credentials.md` (never unscoped `docs/secrets/`) and sync
     `projects/ID/.env` internally without printing secret values or referring the
     participant to non-`.md` files. Apply the configured forward proxy per process if
     needed; if a live provider or upstream API is unavailable, preserve local harness
     evidence and record that dependency as `planned` or `blocked` rather than `verified`.
2. **Bounded Live Tool Round Trips:**
   - Run real multi-turn requests using `docs/projects/ID/living/prompts/` and synthetic
     caller identities.
   - Verify structured tool calls, `[h_*]` handle preservation, reference-monitor
     interception, real/sandbox service responses, natural persona synthesis and redacted
     audit entries.
3. **Redacted Wiring Report:**
   - Record each provider/service/transport state (`planned`, `configured`,
     `authenticated`, `callable`, `effect-verified`), observed latency, token usage and
     redacted diagnostics in `docs/projects/ID/versions/VERSION/wire-report.md`, then
     route to `/job-test`.

Apply the file-review/certainty protocol on `.md` files inside `docs/` and assess updates
to the Job, shared Kandoo, active Project and write-only creator feedback. Persist what
changed, evidence, pending review and next action in `docs/projects/ID/living/status.md`
and mirror `docs/kandoo/living/status.md`. Finish every reply with the current Job's full ordered
steps localized and one exact next action (`/job-test` or the pending `.md` file).
