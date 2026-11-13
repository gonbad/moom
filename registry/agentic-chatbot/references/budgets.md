# Enforced budgets and deterministic fallback

Record owner-selected per-peer rate limits, one in-flight turn per peer, bounded
model/tool requests per run, timeouts, output maxima, daily per-user tokens and a
global daily token/cost breaker with explicit reset timezone and units. Enforce these
in trusted runtime code before model calls and between tool iterations, not in prompts.
Unknown or missing accounting never means unlimited usage.

Use atomic counters/reservations shared by workers, reserving a conservative allowance
and reconciling actual usage. Handle concurrent users, cancellations, provider failures,
missing usage, process restart and day rollover. Consult actual provider/model pricing
if cost accounting is selected; token and per-run caps remain an independent bound.
Bound tool resources too. On quota or outage stop inference and use a reviewed
deterministic menu/support path while preserving state, status/cancel operations and
the chosen action approval policies. Recovery never auto-executes an unapproved proposal.
Test concurrent reservations, mid-loop limits, global breaker, rollover, crash recovery,
timeouts and useful fallback with all model calls disabled.
