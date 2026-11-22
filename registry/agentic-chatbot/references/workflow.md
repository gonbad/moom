# Model-directed actions across all fourteen stages

Compare a deterministic bot or ordinary web app first. An agent is justified when
variable user intent requires selecting among scoped tools or composing multi-source
context; it adds latency, recurring inference cost, semantic error modes and prompt
injection risk. Explain those tradeoffs upfront. The runtime model never inherits the
coding assistant's shell, filesystem, credentials or deployment authority.

Expand three Project paths consistently from the workspace root: artifact root
`./`, document root `docs/`, and selected version dossier
`docs/versions/VERSION/`. Every file the participant is asked to open, read
or edit must be a `.md` file inside `docs/` (including reviewed prompts under
`docs/living/prompts/` and gitignored credentials in
`docs/secrets/credentials.md`; the only folder exception outside `docs/` is
pasting an existing codebase into `./existing/`). Executable code and OpenAPI
schemas belong under `./`.

## Authoritative fourteen-stage handoff

| Command | Input artifact | Output artifact | Installed references | Exit evidence | Next |
| --- | --- | --- | --- | --- | --- |
| `idea` | Selected-version input recorded in `docs/living/status.md`, optional `./existing/` | `docs/living/idea.md`, `roadmap.md` | `workflow.md` | Suitability gate passed; narrow `0.1` domain scoped | `prd` |
| `prd` | `docs/living/idea.md` | `docs/living/prd.md` | `workflow.md`, conditional `messenger.md` | Personas, agent role, channels and refusal boundaries resolved | `tools` |
| `tools` | `docs/living/prd.md` | `docs/living/tools.md`, `./contracts/` | `workflow.md`, `services.md`, `authority.md`, conditional `payments.md` | Service classes, attenuated tool contracts and secret keys resolved | `sops` |
| `sops` | `docs/living/tools.md`, `prd.md` | `docs/living/sops.md` | `workflow.md` | Multi-step procedures, parameter checks and recovery rules resolved | `data-model` |
| `data-model` | `docs/living/sops.md`, `tools.md` | `docs/living/data-model.md` | `workflow.md`, `authority.md` | Domain entities, session memory and redacted audit metadata resolved | `privacy` |
| `privacy` | `docs/living/data-model.md` | `docs/living/privacy.md` | `workflow.md`, `authority.md` | `[h_*]` handle masking, audit retention and sink rules resolved | `capabilities` |
| `capabilities` | `docs/living/tools.md`, `privacy.md` | `docs/living/capabilities.md` | `workflow.md`, `authority.md`, conditional `payments.md` | Per-action owner confirmation policy (`read+none`, `direct+none`, `direct+soft`, `confirm+hard`) resolved | `edge-cases` |
| `edge-cases` | `docs/living/capabilities.md` | `docs/living/edge-cases.md` | `workflow.md`, `authority.md`, `budgets.md`, conditional `messenger.md` | Injection defense, token/spend quotas and outage fallback resolved | `prompts` |
| `prompts` | `prd.md`, `sops.md`, `privacy.md`, `capabilities.md`, `edge-cases.md` | `docs/living/prompts/system.md`, `persona.md`, `examples.md` | `workflow.md`, `authority.md` | Reviewed prompts aligned with capability vocabulary and handles | `architecture` |
| `architecture` | All living specs and `docs/living/server.md` | `docs/living/architecture.md`, version `checklist.md` and `handoff.md` | `workflow.md`, `authority.md`, `budgets.md`, `services.md`, `infrastructure.md`, `quality.md` | Reference monitor, DB route and checklist complete | `build` |
| `build` | `architecture.md`, `checklist.md`, `handoff.md` | `./app/`, `./services/`, `./tests/` | `workflow.md`, `authority.md`, `budgets.md`, `services.md`, `infrastructure.md`, `quality.md` | Harness, services and deterministic security/gate tests pass | `wire` |
| `wire` | Built harness, `docs/living/prompts/`, `secrets/credentials.md` | `docs/versions/VERSION/wire-report.md` | `workflow.md`, `services.md`, `budgets.md`, conditional `messenger.md`, `infrastructure.md` | Real configured model and service round trips verified | `test` |
| `test` | Wired agent, `capabilities.md`, `edge-cases.md` | `docs/versions/VERSION/adversarial-report.md`, `NN-test-round.md` | `workflow.md`, `authority.md`, `budgets.md`, `quality.md` | Adversarial boundary probes and owner acceptance recorded | `deploy` |
| `deploy` | Owner acceptance, `docs/living/server.md` | `docs/versions/VERSION/deploy-notes.md`, `release/VERSION` | `workflow.md`, `budgets.md`, `infrastructure.md`, `quality.md` | VPS daemon, HTTPS/poller and budget caps verified, or local delivery recorded | Complete |

Specification stages advance once review closes without adding
redundant approval ceremonies; structural harness tests, live model dialogues, owner
acceptance and live deployment remain separate evidence columns. Not every agent uses a
messenger or processes payments—mark unused channels or payment sections `not applicable`.
