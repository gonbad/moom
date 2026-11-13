# Payments, receipt evidence and fulfillment

Ask whether payments are needed; skip this reference otherwise. For native Bale
payments verify current invoice, checkout, inquiry and successful-payment contracts,
currency/amount units (Rials versus Tomans), credentials and exact order correlation.
An invoice or approved pre-checkout is not settlement. Trust authenticated provider
data, enforce unique transaction IDs and idempotent fulfillment under duplicates.

For uploaded card-transfer receipts, distinguish claimed evidence from verified
settlement. OCR/AI can extract and flag; it cannot prove money arrived. Explain and
record the owner's policy: strict verification before fulfillment, or optimistic
provisional access followed by authenticated admin review, rejection and revocation.
Keep payment status separate from fulfillment status; provisional access is never
represented as verified payment. Bound review actions to admin identity, order,
current version and one-use decisions, preserving audit history.

A ban restricts owned product entitlements, not a person's ability to open a messenger
chat. Test forged/reused receipts, wrong amount/unit/order, duplicates, unauthorized
admins, repeated decisions, cancellation races and revocation. Preserve the selected
policy in failures and restarts. The participant may revise the Job to fit their work.
