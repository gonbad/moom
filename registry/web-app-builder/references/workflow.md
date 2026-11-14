# Preserve the product across all eleven web stages

Use this as an initial method, not a mandatory framework. Expand three Project paths
consistently from the workspace root: artifact root `projects/ID/`, document root
`docs/projects/ID/`, and selected version dossier `docs/projects/ID/versions/VERSION/`.
Never create unscoped root `frontend/`, `backend/` or `docs/secrets/`. Every file the
participant is asked to open, read or write must be a `.md` file inside `docs/`, with
one explicit folder exception: pasting an existing codebase into `projects/ID/existing/`
or external design HTML/assets into `projects/ID/design/`.

## Authoritative eleven-stage handoff

| Command | Input artifact | Output artifact | Installed references | Exit evidence | Next |
| --- | --- | --- | --- | --- | --- |
| `job-idea` | Selected-version input recorded in `docs/projects/ID/living/status.md`, optional `projects/ID/existing/` | `docs/projects/ID/living/idea.md`, `roadmap.md`, `external-services.md` | `workflow.md` | MVP slice, differentiator and service fallbacks resolved | `job-prd` |
| `job-prd` | `docs/projects/ID/living/idea.md` | `docs/projects/ID/living/prd.md` | `workflow.md` | Personas, capabilities and non-goals resolved | `job-data-model` |
| `job-data-model` | `docs/projects/ID/living/prd.md` | `docs/projects/ID/living/data-model.md` | `workflow.md` | Plain business entities, invariants and relationships resolved | `job-ux` |
| `job-ux` | `docs/projects/ID/living/data-model.md`, `prd.md` | `docs/projects/ID/living/ux.md` | `workflow.md`, `design.md` | Screen inventory, empty/error states and key screen resolved | `job-design` |
| `job-design` | `prd.md`, `data-model.md`, `ux.md` | `projects/ID/design/`, `docs/projects/ID/living/design-system.md` | `workflow.md`, `design.md` | Return bundle imported; owner selected visual direction | `job-prototype` |
| `job-prototype` | `projects/ID/design/`, `design-system.md` | `projects/ID/frontend/`, `project/ID/prototype/VERSION` (or local snapshot) | `workflow.md`, `design.md`, `quality.md` | HTML-to-React visual comparison accepted; local Tailwind verified | `job-scenarios` |
| `job-scenarios` | Frozen prototype, `prd.md`, `ux.md` | `docs/projects/ID/living/test-scenarios.md` | `workflow.md`, `quality.md` | Synthetic scenarios and edge cases walked on prototype | `job-plan` |
| `job-plan` | Specs, frozen prototype, `test-scenarios.md`, `server.md` | `docs/projects/ID/living/architecture.md`, version `checklist.md` and `handoff.md` | `workflow.md`, `infrastructure.md`, `quality.md` | DB route, API seam mapping and build checklist complete | `job-build` |
| `job-build` | `architecture.md`, `checklist.md`, `handoff.md` | `projects/ID/backend/`, wired `projects/ID/frontend/` | `workflow.md`, `infrastructure.md`, `quality.md` | Migrations, APIs, wired UI and automated tests pass | `job-test` |
| `job-test` | Running app, frozen prototype copy, `test-scenarios.md` | `docs/projects/ID/versions/VERSION/NN-test-round.md` | `workflow.md`, `design.md`, `quality.md` | Prototype-to-app comparison and owner scenario acceptance recorded | `job-deploy` |
| `job-deploy` | Owner acceptance, `docs/kandoo/living/server.md` | `docs/projects/ID/versions/VERSION/deploy-notes.md`, `project/ID/release/VERSION` | `workflow.md`, `infrastructure.md`, `quality.md` | Live HTTPS/DB restart verified, or local delivery recorded | Complete |

Specification stages (`idea`, `prd`, `data-model`, `ux`, `scenarios`, `plan`) advance
once any open question round is submitted without inventing a second approval round.
Human artifact acceptance is required separately at `job-design`, `job-prototype` (HTML
versus React) and `job-test` (frozen prototype versus integrated application). Keep
mock-data and live-data calls behind `projects/ID/frontend/src/api/` so backend wiring
preserves approved pixels. If scenarios modify the prototype, freeze a new prototype
reference and revalidate affected checks.

Later comparisons use the exact accepted prototype baseline recorded in
`docs/projects/ID/living/status.md`, including any revised tag or snapshot created
during scenarios. Never infer the baseline from the Project version alone.
