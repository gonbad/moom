# Usage budgets and deterministic fallback

Before exposing a public agent, specify per-peer rate limits, one in-flight model turn
per peer, bounded model/tool requests per run, timeouts, maximum outputs, daily per-user
token limits and an agent-wide daily token/cost circuit breaker. Record units, reset
time zone and owner-selected values in LIVING/budgets.md. Limits are enforced in trusted
code before model calls and before continuing multi-step reasoning; prompts cannot
change them. Disabled/unknown accounting is not unlimited free usage.

Use atomic shared counters/reservations in PostgreSQL or Redis so concurrent users,
workers and tool iterations cannot each spend the full remaining budget. Reserve a
conservative allowance before execution and reconcile measured usage afterward;
handle provider errors, cancellations, missing usage reports, restarts and day rollover.
Track actual provider/model pricing only when cost accounting is selected; keep token
caps and per-run maxima as an independent bound. A global breaker applies across all
users, not just one conversation. Also bound external-tool resource consumption.

On limits or provider outage, stop further inference and offer the reviewed deterministic
menu/support path. Preserve pending state, let safe status/cancel operations work, and
retain any selected approval policy. Recovery never automatically executes an unapproved
proposal. Test concurrent reservations, a run crossing its limit mid-loop, global quota,
reset boundary, crash/restart, provider timeout and fallback with model calls disabled.
