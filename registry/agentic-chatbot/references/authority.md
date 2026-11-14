# Tool contracts and owner-selected per-action confirmation

Bind caller identity strictly from authenticated transport/session context—never from a
model-supplied `user_id` argument. Use one consistent capability schema across
`capabilities.md`, `prompts/`, reference-monitor code and tests:

| Execution Mode | Confirmation Policy | Meaning and runtime enforcement |
| --- | --- | --- |
| `read` | `none` | Caller-scoped read-only query executed directly within budget |
| `direct` | `none` | Caller-scoped mutation executed directly with eligibility and idempotency checks |
| `direct` | `soft` | Conversational confirmation: offer delivered first, caller reply interpreted in context, deterministic provenance/caller/expiry/one-use checks enforced |
| `confirm` | `hard` | Proposal-only to the model: raw executor excluded from model tools; independent trusted UI/callback/token approval bound to `caller + action + args_hash` required before execution |

Never mix `soft_confirm` as a separate execution mode. Explain the concrete security and
usability tradeoffs for each action and **preserve the owner's explicit per-action
selection**—there is no global rule forbidding `direct + soft` or `direct + none` on
financial, deletion or high-privilege actions when the owner deliberately chooses it.
Conversely, never describe `direct + soft` as an independent security boundary, and
whenever the owner selects `confirm + hard`, model text or `confirmed=true` arguments
can never satisfy or bypass that gate.

Regardless of confirmation policy, every tool enforces authenticated caller scope,
backend transactional eligibility, idempotency keys and atomic budget caps. Receipt OCR
or image interpretation never marks an order settled.

For `direct + soft`, persist the offered action only after its prompt is delivered;
check caller, expiry, bound resource and one-use execution in deterministic code while
using the configured model (not brittle keyword regexes) for natural replies.

For `confirm + hard`, expose only `propose_<action>` to the model; render bound
arguments via trusted code and require authenticated, expiring, one-use approval.
Changed arguments require a fresh proposal. Keep raw executors, shell/HTTP sinks and
admin endpoints unreachable from model tool registries, fallbacks and retries.

Store sensitive user attributes in a handle vault as typed opaque handles (`[h_card_1]`,
`[h_national_id_2]`), resolving them only inside reviewed backend sinks after caller,
type, ownership and expiry checks. Durable audit logs store redacted metadata and handle
IDs, never raw secrets or unmasked PII. Reference library support such as
[Pydantic AI deferred tools](https://ai.pydantic.dev/deferred-tools/) is an
implementation aid, not a substitute for verifying this boundary.
