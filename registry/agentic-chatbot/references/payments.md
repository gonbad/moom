# Agent payment tools and settlement boundaries

The agent explains order status and permitted next actions. The business service owns
invoice issuance, reservation expiry, provider verification and settlement; no prompt,
image interpretation or conversation cache can settle an order. Model-visible tools
return typed current status and opaque invoice/order handles scoped to the caller.

Owner-selected direct/soft/hard confirmation applies to eligible payment-related
actions as recorded in the tool policy. Preserve the selected gate when handing off
to a messenger, hosted checkout or deterministic fallback. Checkout approval and a
successful payment are separate facts. A status read must not issue/reissue invoices.

For Bale native payment, implement and verify its current invoice/pre-checkout/
successful-payment events through the service adapter using the official
[Bale documentation](https://docs.bale.ai/). Check amount/currency, order ownership,
provider charge uniqueness and transaction eligibility. Do not infer field parity
with Telegram. Deduplicate webhooks and reconcile uncertain results by request key.

For receipt upload let the owner choose strict reconciliation or bounded optimistic
fulfillment. In optimistic mode record `provisional` separately from `settled`, with
limits, expiry and a reversal/support path. Keep receipts and extracted sensitive
values private; the model sees only the reviewed minimum context/handles.

Supply absolute expiry and current eligibility independently of old chat history.
Resending an invoice does not restart its TTL. An expired item needs an explicit,
valid reopening operation that rechecks deadline/capacity and selected approval;
a thank-you or an old affirmative reply is not a reopening request. Test stale-history
replay, unswept expiry, another caller's handle, duplicate provider events, late payment
and a reply failure after settlement. Separate deterministic settlement checks from
observed configured-model explanations and never test real money without authority.
