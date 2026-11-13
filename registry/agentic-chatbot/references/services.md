# Independently usable services and complete runtime wiring

Inventory every component in a Project-owned service table:

| Class | Responsibility | Required evidence |
| --- | --- | --- |
| existing API | Use its authoritative contract and scoped client | Authenticated operation and scope denial |
| owned backend | Implement domain state, validation and API | Real service, persistence and API tests |
| API bridge | Expose needed operations over a non-API system | Real integration, session restoration and supported controls |

A placeholder URL or SDK stub is not a completed bridge. New services belong to the
build, not a list of unexplained external prerequisites. Example Project structure:

```text
app/                  model loop, scoped tools, sanitized conversation state
services/booking/     business API, migrations, capacity/payment transactions
services/bridge/      optional connection/session state
contracts/            reviewed service request/response/error specifications
```

The backend owns prices, availability, deadlines and settlement. The agent owns
conversation/run state and pending proposals; a bridge owns login/session state.
Call APIs through scoped clients instead of importing business engines or touching
their domain tables. Service contracts describe auth, resource scope, idempotency,
errors, timeouts and events, independently of attenuated model-visible tools.

For a personal-account/browser bridge verify that the chosen interface supports the
required operations. Use a dedicated account/profile; enter phone/OTP/password through
protected local input, never chat/question files. Ignore session artifacts before
creation, restrict permissions, reuse valid sessions and prove restart restoration.
Record re-login/expiry behavior. A broadcast token or an open browser does not prove
personal messaging or bot buttons.

Choose and record runtime model/provider/account separately from the coding host and
commercial plan. Use the application's actual provider/prompt/tool path for bounded
checks; a standalone SDK demo does not prove integration. Date official provider facts.
Record planned/configured/authenticated/callable/effect-verified separately for every
model/service/transport, then repeat relevant checks from the deployment service user.
Use read-only or explicitly permitted sandbox effects; never message real customers
to prove connectivity without authorization.
