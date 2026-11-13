# Tool contracts and participant-selected confirmation

Bind caller identity from authenticated transport/session context, never a model's
`user_id` argument. Each tool contract should state:

| Field | Example |
| --- | --- |
| Purpose and parameters | `reserve_slot(slot_handle)`; no caller/price override |
| Resource scope | Only this caller's eligible appointments |
| Return schema | Typed success, unavailable, expired, denied, retryable |
| Eligibility and idempotency | Capacity/deadline inside service transaction; request key |
| Sensitive values | Opaque typed handle, expiry, permitted resolver/sink |
| Action policy | read, direct, soft confirmation or hard confirmation |
| Audit/failure | Safe event ID, timeout/unknown-outcome behavior |

Explain policy tradeoffs per action and preserve the owner's selection. Direct and
soft confirmation both grant execution authority; soft adds conversational behavior,
not an independent security boundary. Do not impose hard approval universally from
an older research framework. All policies retain caller scope and business validation.

For soft confirmation, persist the exact offered action only after its question was
successfully delivered. Consume a later caller reply with full context, including
refusal, correction and ambiguity. The model interprets language; deterministic code
checks provenance, caller, expiry, exact bound resource and one-use execution. Avoid
keyword regexes for nuanced names/consent or pretending that fixture strings prove
semantic quality. Exercise real configured-model multi-turn conversations when available.

For hard confirmation, the model sees proposal tools only. Trusted UI/code renders
bound arguments and verifies authenticated, expiring, one-use approval for that
caller/action/argument hash. Changed arguments require a new proposal. Raw executors,
aliases, generic HTTP/shell dispatch and bypasses stay outside the model registry.
Model text and `confirmed=true` cannot manufacture approval. Keep gates on fallback,
callbacks, retries and bridges. A text-only channel requires a real trusted code flow
if hard approval is selected; do not advertise unsupported buttons.

Resolve sensitive handles only at reviewed sinks after caller/type/ownership/expiry
checks. Redact traces and history. Test wrong-caller handles, replay, altered arguments,
expired proposals and direct executor reachability; assert no protected mutation.
Library deferred-tool support is an implementation option, not proof of this full
boundary: [Pydantic AI deferred tools](https://ai.pydantic.dev/deferred-tools/).
