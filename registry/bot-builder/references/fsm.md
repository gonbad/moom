# Dialog state, transactions and idempotent delivery

Write a transition table before handlers. Example for an event-registration bot:

| Current state | Event | Guard | Mutation and next state | Reply |
| --- | --- | --- | --- | --- |
| idle | register | registration open | Create draft → name_needed | Ask name |
| name_needed | text | domain validation | Save name → contact_needed | Ask contact |
| contact_needed | contact/text | belongs to caller or explicitly validated | Save → review | Show summary |
| review | edit | draft owned by caller | Return to selected field | Ask corrected value |
| review | confirm | capacity/deadline inside transaction | Reserve once → payment_pending | Show payment choice |
| payment_pending | provider event | amount/order/provider verified | Settle once → complete | Receipt |
| any draft | cancel | draft still cancelable | Release reservation → idle | Confirm cancellation |

Adapt names and guards to the real product. Store conversation state by platform,
bot identity and caller, with durable version/expiry. Keep private-chat identity
separate from a group chat ID. Callback data should be a short opaque action token
bound to caller, flow revision, action and expiry, not raw trusted price/user fields.
A stale button gets a safe current-state reply; it must not replay a mutation.

Example internal interface (generate code in the Project, not the template):

```python
async def dispatch(event, context):
    # context carries trusted platform/bot/caller and repository clients
    # transaction: deduplicate update, lock flow, validate guard, persist/outbox
    return [SendText(...), ShowMenu(...)]
```

Use a unique event key and DB transaction for deduplication, row locking or optimistic
version checks for competing updates, and an outbox for replies that can retry after
a committed mutation. Do not retry a non-idempotent business action after an unknown
network outcome; query by idempotency key first. Delivery failure and business failure
are different states. Derive expiry at read time even if a cleanup scheduler is late.
Test duplicate/out-of-order updates, rapid taps, cancellation racing with payment,
restart midway through a dialog and another caller presenting the same token.
