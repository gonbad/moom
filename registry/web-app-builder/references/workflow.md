# Preserve the product across all eleven web stages

Use this as an initial method, not a mandatory framework. Expand three Project paths
consistently from the workspace root: artifact root `./`, document root
`docs/`, and selected version dossier `docs/versions/VERSION/`.
Every file the
participant is asked to open, read or write must be a `.md` file inside `docs/`, with
one explicit folder exception: pasting an existing codebase into `./existing/`
or external design HTML/assets into `./design/`.

## Authoritative eleven-stage handoff

| Command | Input artifact | Output artifact | Installed references | Exit evidence | Next |
| --- | --- | --- | --- | --- | --- |
| `idea` | Selected-version input recorded in `docs/living/status.md`, optional `./existing/` | `docs/living/idea.md`, `roadmap.md`, `external-services.md` | `workflow.md` | MVP slice, differentiator and service fallbacks resolved | `prd` |
| `prd` | `docs/living/idea.md` | `docs/living/prd.md` | `workflow.md` | Personas, capabilities and non-goals resolved | `data-model` |
| `data-model` | `docs/living/prd.md` | `docs/living/data-model.md` | `workflow.md` | Plain business entities, invariants and relationships resolved | `ux` |
| `ux` | `docs/living/data-model.md`, `prd.md` | `docs/living/ux.md` | `workflow.md`, `design.md` | Screen inventory, empty/error states and key screen resolved | `visuals` |
| `visuals` | `prd.md`, `data-model.md`, `ux.md` | `./design/`, `docs/living/design-system.md` | `workflow.md`, `design.md` | Return bundle imported; owner selected visual direction | `prototype` |
| `prototype` | `./design/`, `design-system.md` | `./frontend/`, `project/prototype/VERSION` (or local snapshot) | `workflow.md`, `design.md`, `quality.md` | HTML-to-React visual comparison accepted; local Tailwind verified | `scenarios` |
| `scenarios` | Frozen prototype, `prd.md`, `ux.md` | `docs/living/test-scenarios.md` | `workflow.md`, `quality.md` | Synthetic scenarios and edge cases walked on prototype | `architecture` |
| `architecture` | Specs, frozen prototype, `test-scenarios.md`, `server.md` | `docs/living/architecture.md`, version `checklist.md` and `handoff.md` | `workflow.md`, `infrastructure.md`, `quality.md` | DB route, API seam mapping and build checklist complete | `build` |
| `build` | `architecture.md`, `checklist.md`, `handoff.md` | `./backend/`, wired `./frontend/` | `workflow.md`, `infrastructure.md`, `quality.md` | Migrations, APIs, wired UI and automated tests pass | `test` |
| `test` | Running app, frozen prototype copy, `test-scenarios.md` | `docs/versions/VERSION/NN-test-round.md` | `workflow.md`, `design.md`, `quality.md` | Prototype-to-app comparison and owner scenario acceptance recorded | `deploy` |
| `deploy` | Owner acceptance, `docs/living/server.md` | `docs/versions/VERSION/deploy-notes.md`, `release/VERSION` | `workflow.md`, `infrastructure.md`, `quality.md` | Live HTTPS/DB restart verified, or local delivery recorded | Complete |

Specification stages (`idea`, `prd`, `data-model`, `ux`, `scenarios`, `plan`) are ready for the participant to advance after analysis converges without inventing a second approval round.
Human artifact acceptance is required separately at `visuals`, `prototype` (HTML
versus React) and `test` (frozen prototype versus integrated application). Keep
mock-data and live-data calls behind `./frontend/src/api/` so backend wiring
preserves approved pixels. If scenarios modify the prototype, freeze a new prototype
reference and revalidate affected checks.

Later comparisons use the exact accepted prototype baseline recorded in
`docs/living/status.md`, including any revised tag or snapshot created
during scenarios. Never infer the baseline from the Project version alone.
