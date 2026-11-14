# Simulated harness checks, turn scenarios and live platform round trips

Build a self-contained in-process test harness inside `projects/ID/tests/` that feeds
normalized `Event` fixtures (slash commands, text, opaque callback tokens, contact/media
payloads and optional payment events) into the FSM dispatcher against isolated test
database transactions while capturing outgoing `SendText`, `ShowMenu` and
`answer_callback` calls in memory—requiring zero external repositories or live network
calls.

## Concrete turn-scenario mini-example

- **Scenario B-04 (Stale button tap after cancellation):** Precondition: synthetic caller
  `tg:900011` is in `review` with callback token `cb_8f2a`. Turn 1: caller taps
  `«انصراف»` → bot releases draft reservation, transitions to `idle` and shows main menu.
  Turn 2: caller taps the old inline button carrying `cb_8f2a` from message history →
  bot answers callback gracefully without crash or 500 error, performs zero state or DB
  mutation, and replies that the previous draft was already canceled.

Verify every state transition, invalid input, edit/back/cancel path, duplicate
`update_key` replay, stale/wrong-caller callback token, expiry derived at read time,
simulated process restart mid-dialog and competing users. Include payment state
(`receipt_received`, `provisional`, `settled`, `rejected`) and duplicate provider-event
checks **only when payments are part of the chosen bot**; otherwise mark payment checks
`not applicable`.

Fixture harness tests prove deterministic engine rules; run a bounded live rehearsal
separately in `/job-test` on each selected messenger using an isolated test bot token
from `docs/projects/ID/secrets/credentials.md`. Redact raw tokens, phone numbers and
receipts in all logs and `.md` reports. Keep automated test results, live messenger
evidence and human owner acceptance separate.
