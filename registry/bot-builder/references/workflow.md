# Deterministic messaging product

Choose a menu/dialog bot when flows and business rules are known. Optional inference
can classify a phrase or summarize text; it does not choose arbitrary business tools.
Keep platform transport, a normalized event model, the state machine and business
services separate. Adding Bale beside Telegram should not duplicate registration or
payment logic. Rubika capabilities require its own verified mapping.

The combined workshop steps retain idea, PRD/scenarios, data model, dialog flow,
implementation, real platform checks and deployment. Keep `prd.md`, `flows.md`,
`data-model.md`, `platforms.md`, `payments.md` when needed, and `status.md` in Project
living docs. For each user journey define valid transitions, cancellations, retries,
timeouts and a support route before drawing keyboards.

Use synthetic identities and sandbox effects during development. A callback is input,
not authorization: validate the caller, current state and business eligibility inside
the transaction. Preserve old Projects, allocated bot identities and DB volumes.
Later versions identify affected transitions/platforms and recheck regressions rather
than replacing the whole application. Keep optional payment policy a participant
choice; it does not become an unreviewed global rule for every bot.
