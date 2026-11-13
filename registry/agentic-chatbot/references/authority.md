# Caller scope and owner-selected action policies

Bind caller identity from trusted transport/session context, never a model argument
or textual identity claim. Every tool declares parameters, outcomes, resource scope,
eligibility, idempotency, failures and action policy. Keep sensitive credentials/data
in typed opaque handles; resolve only in approved sinks after caller/type/ownership/
expiry checks. Wrong-caller and wrong-kind handles fail; redact traces and history.

Explain and let the owner choose per action: read, direct, soft confirmation or hard
confirmation. Direct and soft both grant execution authority; soft adds conversational
behavior, not an independent security boundary. Soft confirmation must handle a real
subsequent caller reply, refusals, corrections, ambiguity, expiry and duplicates.
Do not force hard confirmation for every category or call soft behavior its equivalent.
All policies retain caller binding, business validation and auditing.

When hard is selected, expose proposal tools only; raw executors, aliases and generic
dispatchers that reach them are absent from the model's registry. Trusted code renders
the bound action/arguments and verifies authenticated, one-use, expiring approval
bound to action, arguments and caller. Changed arguments require a fresh proposal.
Model text or a confirmed flag cannot mint approval. Preserve that gate across callback,
fallback and recovery paths. Test cross-caller handles, replay, expiry, altered arguments
and execution bypass attempts; assert no protected mutation. Report structural tests
separately from observed model conversations. Current implementation libraries are
choices, not proof of a complete boundary; see [deferred tools](https://ai.pydantic.dev/deferred-tools/).
