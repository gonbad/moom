# Deterministic messaging product across all eleven stages

Choose a menu/button/dialog bot when flows and business rules are deterministic. Optional
narrow inference may classify a phrase or summarize text without choosing arbitrary
business tools. Keep platform transport, normalized events, the state machine and
business services separate so supporting Bale alongside Telegram or Rubika never
duplicates business logic.

Expand three Project paths consistently from the workspace root: artifact root
`./`, document root `docs/`, and selected version dossier
`docs/versions/VERSION/`. Every file the participant is asked to open, read
or edit must be a `.md` file inside `docs/` (including gitignored
`docs/secrets/credentials.md` for tokens; the only folder exception outside
`docs/` is pasting an existing codebase into `./existing/`).

## Authoritative eleven-stage handoff

| Command | Input artifact | Output artifact | Installed references | Exit evidence | Next |
| --- | --- | --- | --- | --- | --- |
| `idea` | Selected-version input recorded in `docs/living/status.md`, optional `./existing/` | `docs/living/idea.md`, `roadmap.md`, `external-services.md` | `workflow.md` | Core journey, target platforms and payment applicability resolved | `prd` |
| `prd` | `docs/living/idea.md` | `docs/living/prd.md` | `workflow.md` | Personas, slash/menu commands and non-goals resolved | `flow` |
| `flow` | `docs/living/prd.md` | `docs/living/flow.md` | `workflow.md`, `fsm.md` | FSM transition table, keyboards and message templates resolved | `data-model` |
| `data-model` | `docs/living/flow.md` | `docs/living/data-model.md` | `workflow.md`, `fsm.md` | User, session, domain and optional payment entities resolved | `integrations` |
| `integrations` | `docs/living/data-model.md` | `docs/living/integrations.md` | `workflow.md`, `messenger.md`, conditional `payments.md` | Selected platform adapters, token variable names and conditional payment policy resolved | `edge-cases` |
| `edge-cases` | `docs/living/integrations.md`, `flow.md` | `docs/living/edge-cases.md` | `workflow.md`, `fsm.md`, `messenger.md` | Deduplication, stale callbacks, unexpected inputs and expiry resolved | `scenarios` |
| `scenarios` | `flow.md`, `integrations.md`, `edge-cases.md` | `docs/living/test-scenarios.md` | `workflow.md`, `quality.md` | Turn-by-turn synthetic scenarios and failure cases specified | `architecture` |
| `architecture` | Living specs, `test-scenarios.md`, `docs/living/server.md` | `docs/living/architecture.md`, version `checklist.md` and `handoff.md` | `workflow.md`, `fsm.md`, `messenger.md`, `infrastructure.md`, `quality.md` | DB route, adapter interfaces and build checklist complete | `build` |
| `build` | `architecture.md`, `checklist.md`, `handoff.md` | `./app/`, `./tests/` | `workflow.md`, `fsm.md`, `messenger.md`, conditional `payments.md`, `infrastructure.md`, `quality.md` | Engine, adapters and local simulated harness tests pass | `test` |
| `test` | Running bot + test token, `test-scenarios.md` | `docs/versions/VERSION/NN-test-round.md` | `workflow.md`, `messenger.md`, `quality.md` | Live messenger rehearsal and owner acceptance recorded | `deploy` |
| `deploy` | Owner acceptance, `docs/living/server.md` | `docs/versions/VERSION/deploy-notes.md`, `release/VERSION` | `workflow.md`, `messenger.md`, `infrastructure.md`, `quality.md` | Production webhook/poller and restart verified, or local delivery recorded | Complete |

Keep living specs in `docs/living/` (`idea.md`, `prd.md`, `flow.md`,
`data-model.md`, `integrations.md`, `edge-cases.md`, `test-scenarios.md`,
`architecture.md`, `roadmap.md`, `external-services.md`, `status.md`). Not every bot is
a payment bot: when payments are outside scope, mark payment sections `not applicable`
in `data-model.md`, `integrations.md`, `test-scenarios.md` and `build` rather than
inventing invoices. Specification steps are ready for the participant to advance after analysis converges;
live messenger product acceptance at `test` remains an explicit human sign-off.
