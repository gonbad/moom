# Bespoke FSM contract

The assistant generates a small FSM for this bot's reviewed dialog graph; there is no
universal application runtime to adopt blindly. Specify `state`, normalized `event`,
allowed `transitions`, caller-scoped `context_data`, guards and effects. Each transition
names its expected current state, required inputs, next state, cancel/back/expiry paths,
and visible response. Invalid or stale events leave state unchanged and return a
useful deterministic explanation. Keep user state keyed by platform, bot identity and
peer ID; do not merge same-number users across platforms.

For each incoming platform update, insert a unique inbox key, lock the relevant state
row (or use a version-checked update), validate guards and commit the transition with
outbound intent in one PostgreSQL transaction. Handle first-row creation races too.
Do not hold a database lock while awaiting an external API/model. Use an outbox and
stable idempotency keys for effects. If a remote timeout leaves an outcome unknown,
reconcile status before retry; exactly-once HTTP delivery is not generally available.

AI classifiers return a constrained intent or unknown; deterministic guards still
control transitions. Bounded Q&A sees only permitted context and returns an answer,
never an executable plan. Include tests of duplicate updates, parallel conflicting
buttons, stale state/version, abort/timeout, restart, failed send and retry recovery.
