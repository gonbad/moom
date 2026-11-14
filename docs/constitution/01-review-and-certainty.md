# File review and certainty

This protocol applies to bootstrap, every Job step, planned iterations, issue fixes,
shared infrastructure, ordinary requests and method changes. Read the owning living
docs and current open version before asking again; prior authorization persists.

Resolve the owner first: a Job/shared change uses `docs/kandoo/versions/VERSION/`;
a Project change uses `docs/projects/ID/versions/VERSION/`. If ownership is unclear,
ask one concise routing question before creating the round. Job intake starts in
`docs/kandoo/versions/0.1/00-job-input.md`. Write questions and reviewable non-obvious
AI decisions into the next unused `01-questions.md`, `02-questions.md`, ... in that
same open version. Use numeric order, including `COMMENT` / `نظر`; later submitted
choices supersede earlier ones without erasing the originals.

For each item use this structure, translated to the document language:

```markdown
## 1. A concrete question or non-obvious proposed decision
Kind: open question / AI decision
Context: the relevant facts and tradeoff.
Options: A. concrete alternative; B. concrete alternative.
AI Recommendation: A, with a brief reason.
Your answer:
```

Include choices the user might reasonably disagree with even if the assistant has
already made a working decision. State its effect and allow confirmation or override.
Do not bury choices in a finished deliverable. Keep rounds manageable and let the
person write or voice-transcribe in Obsidian, save, then say `done` / `نوشتم` or an
equivalent explicit submission. Continue unrelated authorized work while awaiting it.

After a submitted round, append a resolution section without changing the questions
or user answers. For each item record selected choice, evidence of submission,
certainty and reason:

| User response on submission | Certainty | Behavior |
| --- | --- | --- |
| Explicit answer or explicit endorsement of the recommendation | Confirmed (`قطعی`) | Treat as settled unless the participant changes it |
| Answer left blank | Delegated / Provisional (`پیش‌فرض موقت`) | Apply the recommendation immediately; revisit if later facts improve it |
| No submission yet | Pending | Do not interpret silence as delegation or approval |

A blanket `done` submits the file; it does not explicitly confirm every blank.
An explicit “accept all recommendations” confirms them. If facts contradict a
confirmed choice, explain the conflict and request the specific change; do not
silently downgrade it. When revising a delegated choice, record the new facts and
explain the change in the next relevant round and living decision summary.

Delegation lets specification work proceed. When a procedure gates on a specification
document being "approved", that specification is ready to advance once its open question
round (if any) has been submitted—producing Confirmed or Delegated/Provisional decisions
in the living document—with no unsubmitted round pending; do not invent a redundant
second approval ceremony for every specification stage. By contrast, visual designs,
interactive prototypes, authored narratives, presentations and integrated products
require explicit human artifact acceptance on the reviewed revision. Delegation never
supplies missing credentials, account consent, spending authority, deployment permission
or human artifact acceptance. Respect explicit authorization already given; avoid
repeated approvals for reversible implementation work. A recommendation cannot authorize
an otherwise unauthorized external operation. Every review sheet, question round and
status summary presented to the participant is a `.md` file inside `docs/`. Record
functional checks, fidelity, human acceptance and public deployment separately, with
their actual evidence. A passing test is never an invented human approval.
