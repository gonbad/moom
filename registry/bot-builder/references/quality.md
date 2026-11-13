# Verify the bot's transitions and real platform round trips

Derive a scenario matrix from every state transition, including invalid input, edit,
cancel, back, duplicate events, stale callbacks, timeout, restart and competing users.
Use the actual PostgreSQL schema and dispatch path with isolated test data. Prove one
mutation per idempotency key and no cross-caller state access. Verify timezone/expiry
behavior without relying on a periodic cleanup job having run.

Fixture tests establish adapter mappings; run a bounded live message/callback/reply
round trip separately on each selected platform. Exercise platform rate/auth failures
and offline recovery. Confirm that only one polling/webhook consumer is active after
cutover and that outbox retries do not repeat business effects. Payment checks cover
receipt/provisional/settled distinctions and provider event replay.

Review Persian prompts, native button labels, help/back/cancel paths and useful error
messages with the owner. Record safe transport evidence and revision IDs; redact raw
payloads, tokens, phone numbers and customer receipts. A mock response does not prove
live connectivity. Delivery readiness, payment settlement, functional checks and human
acceptance stay separate; explicit skips remain visible without blocking unrelated work.
