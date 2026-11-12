# Verify the whole agent

Read authority, budgets and edge cases. Exercise caller/handle isolation, selected
policy combinations, hard executor/alias bypass attempts, wrong/expired/replayed
approvals and actual soft-confirmation conversations. Exercise simultaneous usage
reservations, per-run/per-user/global limits, mid-loop exhaustion, provider outage,
day rollover and restart with model calls disabled in deterministic fallback.

Test duplicate effects, unknown remote outcomes, permissions and every reviewed
end-user/admin journey using separate test data. Record sanitized machine/live-model
evidence under EVIDENCE and VERSION/test-results.md. Walk key dialogues and the
complete result with the owner; human acceptance is recorded only for the revision
they actually reviewed. Leave unavailable live checks pending.
