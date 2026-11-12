# Payments and fulfillment

Ask whether payment is needed. If so, record the selected mechanisms and who reviews
receipts in LIVING/payments.md. For Bale, use the current official invoice, checkout,
transaction inquiry and successful-payment contracts. Explicitly document Rials vs
Tomans, expected currency/amount, order correlation, provider requirements and tokens.
Validate successful settlement against trusted provider data and the exact order;
issuing an invoice or approving pre-checkout does not settle a payment. Enforce unique
transaction IDs and idempotent fulfillment under duplicate notifications.

For card-to-card receipts, keep the uploaded evidence and claimed reference separate
from verified settlement. OCR/AI may extract or flag data; it cannot manufacture
settlement truth. Explain both policies and retain the owner's choice:

- Strict: administrative verification is needed before granting access.
- Optimistic: allow provisional registration/access immediately, queue the receipt for
  administrative review, and expose an authenticated admin action to reject/revoke
  and ban a fraudulent account under the product's terms.

Separate `payment_status` from `fulfillment_status`. Track pending review, verified,
rejected and provisional states explicitly. A ban is a product-level restriction;
do not imply a bot can prevent someone from opening a private messenger chat. Revoke
owned entitlements and prevent future application use according to the reviewed policy.
Administrative approval/ban requires authenticated admin identity, the correct target
and one-use/version-bound actions. Audit decisions and explain their user-visible result.
Test forged/reused receipts, amount/unit mismatch, duplicate notifications, wrong admin,
repeat approval/rejection, access revocation and a review racing with user cancellation.
