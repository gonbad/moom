# Deterministic messaging product across all eleven stages

Choose a menu/button/dialog bot when flows and business rules are deterministic. Optional
narrow inference may classify a phrase or summarize text without choosing arbitrary
business tools. Keep platform transport, normalized events, the state machine and
business services separate so supporting Bale alongside Telegram or Rubika never
duplicates business logic.

Expand three Project paths consistently from the workspace root: artifact root
`projects/ID/`, document root `docs/projects/ID/`, and selected version dossier
`docs/projects/ID/versions/VERSION/`. Every file the participant is asked to open, read
or edit must be a `.md` file inside `docs/` (including gitignored
`docs/projects/ID/secrets/credentials.md` for tokens; the only folder exception outside
`docs/` is pasting an existing codebase into `projects/ID/existing/`).

## Authoritative eleven-stage handoff

| Command | Input artifact | Output artifact | Installed references | Exit evidence | Next |
| --- | --- | --- | --- | --- | --- |
| `job-idea` | Selected-version input recorded in `docs/projects/ID/living/status.md`, optional `projects/ID/existing/` | `docs/projects/ID/living/idea.md`, `roadmap.md`, `external-services.md` | `workflow.md` | Core journey, target platforms and payment applicability resolved | `job-prd` |
| `job-prd` | `docs/projects/ID/living/idea.md` | `docs/projects/ID/living/prd.md` | `workflow.md` | Personas, slash/menu commands and non-goals resolved | `job-flow` |
| `job-flow` | `docs/projects/ID/living/prd.md` | `docs/projects/ID/living/flow.md` | `workflow.md`, `fsm.md` | FSM transition table, keyboards and message templates resolved | `job-data-model` |
| `job-data-model` | `docs/projects/ID/living/flow.md` | `docs/projects/ID/living/data-model.md` | `workflow.md`, `fsm.md` | User, session, domain and optional payment entities resolved | `job-integrations` |
| `job-integrations` | `docs/projects/ID/living/data-model.md` | `docs/projects/ID/living/integrations.md` | `workflow.md`, `messenger.md`, conditional `payments.md` | Selected platform adapters, token variable names and conditional payment policy resolved | `job-edge-cases` |
| `job-edge-cases` | `docs/projects/ID/living/integrations.md`, `flow.md` | `docs/projects/ID/living/edge-cases.md` | `workflow.md`, `fsm.md`, `messenger.md` | Deduplication, stale callbacks, unexpected inputs and expiry resolved | `job-scenarios` |
| `job-scenarios` | `flow.md`, `integrations.md`, `edge-cases.md` | `docs/projects/ID/living/test-scenarios.md` | `workflow.md`, `quality.md` | Turn-by-turn synthetic scenarios and failure cases specified | `job-plan` |
| `job-plan` | Living specs, `test-scenarios.md`, `docs/kandoo/living/server.md` | `docs/projects/ID/living/architecture.md`, version `checklist.md` and `handoff.md` | `workflow.md`, `fsm.md`, `messenger.md`, `infrastructure.md`, `quality.md` | DB route, adapter interfaces and build checklist complete | `job-build` |
| `job-build` | `architecture.md`, `checklist.md`, `handoff.md` | `projects/ID/app/`, `projects/ID/tests/` | `workflow.md`, `fsm.md`, `messenger.md`, conditional `payments.md`, `infrastructure.md`, `quality.md` | Engine, adapters and local simulated harness tests pass | `job-test` |
| `job-test` | Running bot + test token, `test-scenarios.md` | `docs/projects/ID/versions/VERSION/NN-test-round.md` | `workflow.md`, `messenger.md`, `quality.md` | Live messenger rehearsal and owner acceptance recorded | `job-deploy` |
| `job-deploy` | Owner acceptance, `docs/kandoo/living/server.md` | `docs/projects/ID/versions/VERSION/deploy-notes.md`, `project/ID/release/VERSION` | `workflow.md`, `messenger.md`, `infrastructure.md`, `quality.md` | Production webhook/poller and restart verified, or local delivery recorded | Complete |

Keep living specs in `docs/projects/ID/living/` (`idea.md`, `prd.md`, `flow.md`,
`data-model.md`, `integrations.md`, `edge-cases.md`, `test-scenarios.md`,
`architecture.md`, `roadmap.md`, `external-services.md`, `status.md`). Not every bot is
a payment bot: when payments are outside scope, mark payment sections `not applicable`
in `data-model.md`, `integrations.md`, `test-scenarios.md` and `job-build` rather than
inventing invoices. Specification steps advance once open question rounds are submitted;
live messenger product acceptance at `job-test` remains an explicit human sign-off.
