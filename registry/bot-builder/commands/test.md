# Verify dialogs, transactions and delivery

Use a separate test database/schema. Simulate every reviewed user/admin path and test
concurrent/conflicting buttons, duplicate updates, stale state, timeout, retry, crash
and restart. Test selected payments and revocation as the payment reference specifies.
Test optional AI failure/unknown output without changing deterministic authority.

With actual credentials, verify receive/send/button round trips for each selected
platform through the HTTPS development tunnel, then walk the complete bot with the
owner. Capture sanitized fixtures and outcomes in EVIDENCE and VERSION/test-results.md.
Missing live checks remain pending. Record human acceptance of the current dialogs
separately from automated success.
