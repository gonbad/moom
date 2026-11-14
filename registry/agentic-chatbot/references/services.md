# Independently usable services, Project-scoped contracts and live wiring

Inventory every integration in `docs/projects/ID/living/tools.md`:

| Class | Responsibility | Required evidence |
| --- | --- | --- |
| `existing_api` | Authoritative third-party API via scoped client | Authenticated call and scope/error handling |
| `owned_backend` | Project domain state, transactions and REST API | Real service, migrations and contract tests |
| `api_bridge` | Scoped adapter over a non-API system | Real integration, session restore and supported controls |

Generate all code and machine schemas inside the Project's artifact root `projects/ID/`
(never unscoped `docs/contracts/`):

```text
projects/ID/app/                  agent harness, reference monitor, handle vault
projects/ID/services/<name>/      owned business API, migrations and transactions
projects/ID/services/bridge/      optional bridge and restricted session state
projects/ID/contracts/<name>/     generated openapi.yaml schemas matching living/tools.md
```

Keep human-reviewed tool and API specifications in `docs/projects/ID/living/tools.md`
so everything the participant reads or edits stays Markdown inside `docs/`. The backend
owns prices, capacity, deadlines and settlement; the agent harness owns session runs,
handle vaults and pending proposals. Call services through scoped HTTP/client seams
rather than importing domain tables directly into model loops.

For personal-account or browser bridges, verify that the target interface supports the
needed actions. Collect credentials only via gitignored
`docs/projects/ID/secrets/credentials.md` or interactive local terminal login—never
chat, logs or question files. Ignore session profiles before creation, restrict file
permissions, and test restart restoration.

Record the runtime inference provider/model/account separately from the coding host in
`docs/projects/ID/living/tools.md` and `architecture.md`. Track each dependency honestly
as `planned`, `configured`, `authenticated`, `callable` or `effect-verified` in
`docs/projects/ID/versions/VERSION/wire-report.md`, using synthetic callers and
authorized sandbox actions rather than messaging real customers.
