# Payment authority, receipts and provisional fulfillment

The business service owns order, amount/currency, reservation expiry, invoice identity
and settlement. Messenger adapters normalize payment events; neither a screenshot nor
an AI classification establishes payment. Retain server-side eligibility checks even
when the dialog has already shown a confirmation button.

For native Bale payments verify current `sendInvoice`, pre-checkout and successful
payment structures against its official documentation. Bind an opaque order reference
to the caller and expected amount; verify the provider result and unique charge ID.
Support timeouts, duplicated events, cancellation and reconciliation. A resend must
reuse a valid invoice without extending its original expiry or creating another charge.
Never copy Telegram field assumptions into Bale without a real verified fixture.

For transfer receipts, explain the tradeoff and let the owner choose:

| Policy | Fulfillment | Settlement record |
| --- | --- | --- |
| strict | Wait for authenticated settlement or reviewed reconciliation | verified only after real evidence |
| optimistic | Limited reversible provisional fulfillment after receipt intake | pending/unverified until reconciled |

Record the choice, provisional limits, expiry, reviewer and reversal/support behavior.
Store receipts privately with restricted retention; public logs show opaque references.
Separate `receipt_received`, `provisional`, `settled`, `rejected` and `refunded` states.
An optimistic acceptance must never write a settled flag. Use idempotency keys and a
transaction for provider events and reservation release. Test amount/currency mismatch,
wrong order/caller, duplicate settlement, expired invoice, late settlement and a failed
reply after successful payment. Report real money effects only when explicitly authorized.
Source: [Bale payment methods and objects](https://docs.bale.ai/).
