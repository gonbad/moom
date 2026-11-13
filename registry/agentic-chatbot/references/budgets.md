# Bounded model runs, concurrency and outage recovery

Define per-run tool calls, wall time, input/output tokens and retry limits, plus
per-user and global daily spend/usage quotas. Enforce them outside the prompt with
atomic reservation/accounting so concurrent callers cannot all pass a stale budget
check. Include operational probes and scheduled jobs in the global budget. Release
unused reservations; preserve actual usage after partial failure or restart.

Bound active runs per caller and globally. Persist run identity, cancellation and
idempotency; stop on repeated tool failure and return a useful partial result. A retry
never grants new authority or repeats an unknown-outcome mutation automatically.
Tool errors should be typed and actionable without exposing private response bodies.

Specify deterministic outage behavior: preserve state, explain unavailability, and
provide retry/support or a verified menu/alternate interface when selected. That
fallback invokes the same business service and respects the same scope and hard
approval. It is not a secret unlimited bypass for blocked users.

Recovery is proven by a bounded configured-provider check, not by elapsed time. Share
one tool-free, customer-data-free probe with persisted backoff; do not notify idle
customers automatically. At their next input preserve a pending wizard answer,
contact, payment or confirmation event before switching modes. Provide authoritative
current business/expiry state alongside sanitized history. Switch back to chat only
after a usable model reply is delivered; failed inference/delivery keeps fallback state.
Test provider timeout, quota exhaustion, parallel runs, duplicate scheduling, restart,
probe storms and partial delivery. Record real dialogue behavior separately from these
deterministic accounting and recovery checks.
