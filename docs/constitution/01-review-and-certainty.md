# File review and certainty

The certainty and evidence rules apply to every task. File-based intake/review starts
with `/create-job` and applies to later Job steps, planned iterations, issue fixes,
shared infrastructure, ordinary requests and method changes, with the setup exception
below. Read the owning living docs and current open version before asking again;
prior answers and authorization persist.

## Initial setup uses chat

During `/start`, ask one unanswered question at a time in chat. The first is the
English/Persian conversation-language question with English recommended; once answered,
use the selected language and ask document language separately. Reuse supplied facts;
never ask for an AI-host preference. Save each answer and the next unresolved item in
the living profile/status and an assistant-written `docs/kandoo/versions/0.1/setup.md`
summary. Do not create a participant setup questionnaire or require summary submission.
Explicit answers are Confirmed; explicit delegation selects a Provisional recommendation;
silence remains pending. Credentials remain in ignored Markdown, never in chat.
Universal setup has no server question or credentials scaffold. Infrastructure
intake occurs only at the installed Job's declared stage or an explicit settings request.

`/pick-job IDENTIFIER` installs an exact prepared starter without Job-definition intake
or a question round. After preparing Project 1, show its intake locations before
restart. Invoking its first command requests reading the initial idea and sources.
Numbered rounds still require explicit submission. `/create-job` retains the
custom file workflow below. This exception removes
redundant method questions; it never implies acceptance of a produced artifact.
From Project intake onward, use the file workflow below. A direct settings request already
supplies its answer: apply and record it without another approval form. Unresolved,
non-obvious settings choices use the shared numbered review; infrastructure changes
retain their actual access, verification and authorization requirements.

## File intake and review

Resolve the owner first: a Job/shared change uses `docs/kandoo/versions/VERSION/`;
a Project change uses `docs/projects/ID/versions/VERSION/`. If ownership is unclear,
ask one concise routing question before creating the round. Job intake starts in
`docs/kandoo/versions/0.1/00-job-input.md`. Write questions and reviewable non-obvious
AI decisions into the next unused `01-questions.md`, `02-questions.md`, ... in that
same open version. Inspect every existing `NN-*` file in that dossier, including user
source files, issues and reviews. Allocate maximum occupied numeric prefix + 1, not
merely the next unused questions filename. Read relevant supplied source material
before writing questions; never ask for a duplicate paste. Preserve existing names
and submitted answers. New raw collections can use an unnumbered `sources/` folder.
Use numeric order, including `COMMENT` / `نظر`; later submitted
choices supersede earlier ones without erasing the originals.

For each item use this structure, translated to the document language:

```markdown
## 1. Which source should the article use?

**Kind:** Open question / proposed decision

**Context:** You already supplied a collection of notes in this version.

**Options:**

- **A — Reuse the supplied notes.** Keep one authoritative source.
- **B — Add another collection.** Import it separately and record its purpose.

**AI recommendation:** A, because the existing file contains the requested material.

**Your answer:**


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

## Example resolutions after submission

Keep the question and answer unchanged, then append the resolution:

| Item | Submitted answer | Selected choice | Certainty and evidence |
| --- | --- | --- | --- |
| 1 | A | Reuse supplied notes | Confirmed; explicit A in the submitted round |
| 2 | Blank | Recommended short introduction | Delegated / Provisional; file submitted with `done` |

Before submission, item 2 remains pending. These specification resolutions do not
prove that the owner accepted the finished article or authorized publication.
Use bold field labels, separate option bullets and a visible blank answer area in
every new round. Do not prefill the answer with the recommendation.
