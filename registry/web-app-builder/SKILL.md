---
name: web-app-builder
description: Build and deploy a document-driven FastAPI and React web app from a core idea and optional existing product. Use external HTML designs, preserve their appearance, and deploy to the participant's VPS with HTTPS.
license: MIT
metadata:
  version: "0.1.1"
  author: gonbad
  origin: https://github.com/gonbad/moom
---

# Web app builder

Use for repeated creation of independent full-stack web products. Read the
[Project contract](references/project.md) first, then the [workflow](references/workflow.md).
Run only the current step's command using the active Project's resolved paths.

1. [start](commands/start.md): first input, server identity and product-owned configuration.
2. [infra](commands/infra.md): PostgreSQL/Redis in VPS Compose and native SSH forwarding.
3. [idea-core](commands/idea-core.md): V0.1 core idea and optional existing-product inventory.
4. [prd](commands/prd.md): requirements and acceptance criteria.
5. [data-model](commands/data-model.md): PostgreSQL schema and migrations.
6. [ux](commands/ux.md): routes, journeys, screen states and primary view.
7. [design](commands/design.md): one external-design prompt plus three specifications.
8. [prototype](commands/prototype.md): supervised React conversion with screenshot fidelity.
9. [scenarios](commands/scenarios.md): reviewable acceptance journeys on the prototype.
10. [plan](commands/plan.md): architecture, integrations and implementation handoff.
11. [backend](commands/backend.md): build the API and connect the approved frontend.
12. [test](commands/test.md): functional checks and the complete owner walkthrough.
13. [deploy](commands/deploy.md): production service, SPA routing, domain and trusted HTTPS.

Use [infrastructure](references/infrastructure.md) during infra/deploy and the
[quality criteria](references/quality.md) throughout. The supplied Project helper and
scripts/smoke.py support Moom initialization; application code is generated for each
Project. External conversion tools are allowed under AI supervision.
