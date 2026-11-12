# Capability and confirmation contract

Bind caller identity from the trusted transport/session context, never a model-supplied
peer ID or a text claim. Every tool declares its purpose, parameter/output schema,
resource scope, eligibility, idempotency, failure outcomes and confirmation policy.
Sensitive credentials and applicable personal data become typed opaque handles before
model exposure. Resolve them only in approved sinks after caller, type, ownership and
expiry checks; cross-caller or wrong-kind handles fail. Redact diagnostics and history.

| Policy | Runtime declaration | Model authority |
|---|---|---|
| read | mode=read, confirmation=none | Read through an attenuated context |
| direct | mode=direct, confirmation=none | Execute caller-scoped action |
| soft_confirm | mode=direct, confirmation=soft | Execute, with conversational confirmation behavior |
| confirm | mode=confirm, confirmation=hard | Propose; independent trusted approval executes |

Reject unknown policy combinations. Explain injection, irreversibility, financial or
permission effects and the limits of soft confirmation. Recommend a suitable policy,
but record the owner's explicit selection rather than forcing hard confirmation on
an entire risk category. All policies retain normal caller binding, business validation
and audit. Selecting direct authority is not permission to access another caller's data.

For soft, show exact intended parameters, wait for a real subsequent caller reply,
handle refusal/correction/expiry/duplicate responses, then execute the ordinary direct
tool. The model still has execution authority; observed conversational compliance does
not constitute an independent enforcement guarantee.

For hard, expose only proposal tools to the model. Raw executors, generic dispatchers
and aliases that can reach them must be absent from its tool registry. Persist an inert
proposal, render its bound parameters through trusted code, and ratify only with the
authenticated person's one-use, expiring, action/argument/caller-bound approval. Changed
arguments require a fresh proposal. Model text, a confirmed flag or a quoted yes cannot
mint approval. Keep the chosen gate on callbacks, fallback and recovery paths.

Test caller isolation and handle rejection for every policy. For hard, attempt bypass
through direct names, aliases, generic dispatch, replay, expiry and altered arguments;
assert no protected mutation. For soft, exercise configured model conversations over
assent, refusal, correction, ambiguity, quoted input, failed delivery, timeout and retry.
Report structural tests and observed model behavior separately. See the current
[Pydantic AI deferred-tool guidance](https://ai.pydantic.dev/deferred-tools/) when
selecting an implementation; a library feature alone does not prove the whole boundary.
