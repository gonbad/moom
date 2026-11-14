# Model-directed actions across all fourteen stages

Compare a deterministic bot or ordinary web app first. An agent is justified when
variable user intent requires selecting among scoped tools or composing multi-source
context; it adds latency, recurring inference cost, semantic error modes and prompt
injection risk. Explain those tradeoffs upfront. The runtime model never inherits the
coding assistant's shell, filesystem, credentials or deployment authority.

Expand three Project paths consistently from the workspace root: artifact root
`projects/ID/`, document root `docs/projects/ID/`, and selected version dossier
`docs/projects/ID/versions/VERSION/`. Never write into unscoped `docs/prompts/`,
`docs/contracts/` or `docs/secrets/`. Every file the participant is asked to open, read
or edit must be a `.md` file inside `docs/` (including reviewed prompts under
`docs/projects/ID/living/prompts/` and gitignored credentials in
`docs/projects/ID/secrets/credentials.md`; the only folder exception outside `docs/` is
pasting an existing codebase into `projects/ID/existing/`). Executable code and OpenAPI
schemas belong under `projects/ID/`.

## Authoritative fourteen-stage handoff

| Command | Input artifact | Output artifact | Installed references | Exit evidence | Next |
| --- | --- | --- | --- | --- | --- |
| `job-idea` | Selected-version input recorded in `docs/projects/ID/living/status.md`, optional `projects/ID/existing/` | `docs/projects/ID/living/idea.md`, `roadmap.md` | `workflow.md` | Suitability gate passed; narrow `0.1` domain scoped | `job-prd` |
| `job-prd` | `docs/projects/ID/living/idea.md` | `docs/projects/ID/living/prd.md` | `workflow.md`, conditional `messenger.md` | Personas, agent role, channels and refusal boundaries resolved | `job-tools` |
| `job-tools` | `docs/projects/ID/living/prd.md` | `docs/projects/ID/living/tools.md`, `projects/ID/contracts/` | `workflow.md`, `services.md`, `authority.md`, conditional `payments.md` | Service classes, attenuated tool contracts and secret keys resolved | `job-sops` |
| `job-sops` | `docs/projects/ID/living/tools.md`, `prd.md` | `docs/projects/ID/living/sops.md` | `workflow.md` | Multi-step procedures, parameter checks and recovery rules resolved | `job-data-model` |
| `job-data-model` | `docs/projects/ID/living/sops.md`, `tools.md` | `docs/projects/ID/living/data-model.md` | `workflow.md`, `authority.md` | Domain entities, session memory and redacted audit metadata resolved | `job-privacy` |
| `job-privacy` | `docs/projects/ID/living/data-model.md` | `docs/projects/ID/living/privacy.md` | `workflow.md`, `authority.md` | `[h_*]` handle masking, audit retention and sink rules resolved | `job-capabilities` |
| `job-capabilities` | `docs/projects/ID/living/tools.md`, `privacy.md` | `docs/projects/ID/living/capabilities.md` | `workflow.md`, `authority.md`, conditional `payments.md` | Per-action owner confirmation policy (`read+none`, `direct+none`, `direct+soft`, `confirm+hard`) resolved | `job-edge-cases` |
| `job-edge-cases` | `docs/projects/ID/living/capabilities.md` | `docs/projects/ID/living/edge-cases.md` | `workflow.md`, `authority.md`, `budgets.md`, conditional `messenger.md` | Injection defense, token/spend quotas and outage fallback resolved | `job-prompts` |
| `job-prompts` | `prd.md`, `sops.md`, `privacy.md`, `capabilities.md`, `edge-cases.md` | `docs/projects/ID/living/prompts/system.md`, `persona.md`, `examples.md` | `workflow.md`, `authority.md` | Reviewed prompts aligned with capability vocabulary and handles | `job-plan` |
| `job-plan` | All living specs and `docs/kandoo/living/server.md` | `docs/projects/ID/living/architecture.md`, version `checklist.md` and `handoff.md` | `workflow.md`, `authority.md`, `budgets.md`, `services.md`, `infrastructure.md`, `quality.md` | Reference monitor, DB route and checklist complete | `job-build` |
| `job-build` | `architecture.md`, `checklist.md`, `handoff.md` | `projects/ID/app/`, `projects/ID/services/`, `projects/ID/tests/` | `workflow.md`, `authority.md`, `budgets.md`, `services.md`, `infrastructure.md`, `quality.md` | Harness, services and deterministic security/gate tests pass | `job-wire` |
| `job-wire` | Built harness, `docs/projects/ID/living/prompts/`, `secrets/credentials.md` | `docs/projects/ID/versions/VERSION/wire-report.md` | `workflow.md`, `services.md`, `budgets.md`, conditional `messenger.md`, `infrastructure.md` | Real configured model and service round trips verified | `job-test` |
| `job-test` | Wired agent, `capabilities.md`, `edge-cases.md` | `docs/projects/ID/versions/VERSION/adversarial-report.md`, `NN-test-round.md` | `workflow.md`, `authority.md`, `budgets.md`, `quality.md` | Adversarial boundary probes and owner acceptance recorded | `job-deploy` |
| `job-deploy` | Owner acceptance, `docs/kandoo/living/server.md` | `docs/projects/ID/versions/VERSION/deploy-notes.md`, `project/ID/release/VERSION` | `workflow.md`, `budgets.md`, `infrastructure.md`, `quality.md` | VPS daemon, HTTPS/poller and budget caps verified, or local delivery recorded | Complete |

Specification stages advance once open question rounds are submitted without adding
redundant approval ceremonies; structural harness tests, live model dialogues, owner
acceptance and live deployment remain separate evidence columns. Not every agent uses a
messenger or processes payments—mark unused channels or payment sections `not applicable`.
