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
A request to finish the reviewed work or proceed to the next step also closes a numbered round under the rules below. `/create-job` retains the
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

## Closing a review

At handoff, link the living document and its numbered review. Invite the participant to answer questions, confirm or override proposed assumptions, edit the document directly, or leave an inline `COMMENT` or `نظر`. They may use any combination and submit in chat, including a request to process the comments alone.

On every submission or resumption, reread the current living document(s) under review together with the open round and the participant's latest message. Preserve direct edits. Record each submitted comment with its location, wording and disposition in the numbered dossier. Apply clear corrections wherever they affect the current work. Remove a marker from the living text only after incorporating its resolution and preserving the feedback. If its meaning conflicts with another instruction or remains unclear, retain the marker and ask the specific outstanding question.

When processing a submission, a request to finish, or a request to advance, append resolutions without filling in the participant’s answer fields. Record the selected choice, its certainty and the evidence for each item. An explicit selection of the recommendation, a different answer, an override, or “accept all listed recommendations” is **Explicit confirmation**. When an answer or confirmation is absent, adopt the stated recommendation and record **Soft confirmation**. A bare `done` submits the work with soft defaults. A later explicit choice supersedes the default. For a new review, write a concrete recommended choice that can actually be adopted.

Apply the same distinction to the reviewed revision. Record explicit acceptance only when the participant actually accepts that revision. Otherwise record soft confirmation for continuing the work. A direction to proceed authorizes the handoff while preserving this distinction. Keep the participant’s words, comments and direct edits ahead of conflicting defaults. Follow up on unresolved comments or missing facts that a recommendation cannot supply. Close the review once each item has a recorded resolution and the reviewed living documents have no unresolved comment markers. Keep technical evidence and authorization for external actions separate from review certainty.

| Review input | Decision record |
| --- | --- |
| “Use A” when A is recommended | A, explicit confirmation, participant selected A |
| Blank when A is recommended | A, soft confirmation, recommendation applied |
| “Continue” without endorsing the revision | Revision soft-confirmed for the next step |
| Inline correction | Participant’s words, the applied change and the affected revision, or an open question if clarification is needed |
