# Bespoke deterministic state machine

Specify the reviewed dialog's states, normalized events, guarded transitions,
caller-scoped context, effects, visible replies and cancel/back/expiry paths. Invalid
or stale events preserve state and explain the available next action. Key identity by
platform, bot and peer; never merge same-number users across transports.

Use unique inbox keys, row locks or version checks, and a transaction covering the
transition plus outbound intent. Handle first-row creation races. Do not hold a DB
lock during a remote model/API call. Use an outbox and stable idempotency keys;
reconcile an unknown remote outcome before retrying, rather than claiming exactly-once
HTTP effects. Test duplicates, parallel buttons, stale events, cancel/expiry, restart,
send failure and retry recovery. Narrow AI classification returns constrained intent
or unknown; deterministic guards still choose the transition and effects.
