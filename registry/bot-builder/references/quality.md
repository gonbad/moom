# Bot quality criteria

- Every product has independent specs, tokens, state and deployment configuration.
- The reviewed menu and FSM determine behavior; optional inference is a bounded leaf.
- Platform adapters normalize identities, messages, callbacks, files and delivery
  errors. Unsupported operations are explicit; mock delivery is not live evidence.
- Inbox deduplication, atomic transitions and idempotent effects survive concurrent
  clicks, repeated webhooks, timeout/retry, process crash and restart.
- Manual provisional access does not become settled payment; administrators can
  review, revoke access and ban according to the selected policy.
- The public webhook is authenticated as supported, HTTPS is trusted and renewed,
  and the same dispatch logic works through the dev tunnel and production service.
- The owner reviews key dialogs and a complete journey, including failures and
  administrative actions. Automated checks never stand in for that acceptance.
