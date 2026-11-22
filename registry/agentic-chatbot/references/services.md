# Independently usable services, Project-scoped contracts and live wiring

Inventory every integration in `docs/living/tools.md`:

| Class | Responsibility | Required evidence |
| --- | --- | --- |
| `existing_api` | Authoritative third-party API via scoped client | Authenticated call and scope/error handling |
| `owned_backend` | Project domain state, transactions and REST API | Real service, migrations and contract tests |
| `api_bridge` | Scoped adapter over a non-API system | Real integration, session restore and supported controls |

## Inspect existing bridges before building one

For a messaging/personal-account integration, inspect
[gonbad/api](https://github.com/gonbad/api) for a suitable existing gateway or client;
its Eitaa project is a candidate example. Inspect the repository at the time of use,
not an assumed deployment or a sibling checkout. Record in the consumer Project's
`docs/living/tools.md`: source URL and selected commit/tag, required versus supported actions,
authentication/session/event capabilities, provenance/license terms for adopted code,
verification gaps, and the reuse/adapt/reject decision with its reason. Do not assume
a root license describes every imported component or that a handshake proves readiness.
If unavailable or unsuitable, record that finding and evaluate the next alternative.

Adopt only the needed client/service, with recorded provenance, under this Project's
artifact root. When the agent needs its own gateway, deploy an isolated service
alongside it, using participant-owned credentials, volumes and ports. Do not use the
author's accounts or assume a public endpoint is a participant service. Never clone
another Kandoo over this workspace, add an API starter merely for this dependency, or
require the Moom template/source at runtime. This optional product reference may remain
in the installed Job after detachment. Its code is generated or imported only into a
real Project, never bundled inside the Markdown-only starter.

Verify the adopted revision's required calls, inbound events/webhooks, authorization,
session restoration and restart behavior through the agent's scoped tool boundary.
Saved upstream claims and a URL alone are not deployment or acceptance evidence.

## Project ownership and wiring

Generate all code and machine schemas inside the Project's artifact root `./`
(never unscoped `docs/contracts/`):

```text
./app/                  agent harness, reference monitor, handle vault
./services/<name>/      owned business API, migrations and transactions
./services/bridge/      optional bridge and restricted session state
./contracts/<name>/     generated openapi.yaml schemas matching docs/living/tools.md
```

Keep human-reviewed tool and API specifications in `docs/living/tools.md`
so everything the participant reads or edits stays Markdown inside `docs/`. The backend
owns prices, capacity, deadlines and settlement; the agent harness owns session runs,
handle vaults and pending proposals. Call services through scoped HTTP/client seams
rather than importing domain tables directly into model loops.

For personal-account or browser bridges, verify that the target interface supports the
needed actions. Collect credentials only via gitignored
`docs/secrets/credentials.md` or interactive local terminal login—never
chat, logs or question files. Ignore session profiles before creation, restrict file
permissions, and test restart restoration.

Record the runtime inference provider/model/account separately from the coding host in
`docs/living/tools.md` and `architecture.md`. Track each dependency honestly
as `planned`, `configured`, `authenticated`, `callable` or `effect-verified` in
`docs/versions/VERSION/wire-report.md`, using synthetic callers and
authorized sandbox actions rather than messaging real customers.
