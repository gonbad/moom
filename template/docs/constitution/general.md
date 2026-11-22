# Working in this project

Read this constitution, mission and workflow on every task. Read `docs/living/profile.md`, `docs/living/status.md` and, when present, project-owned `docs/method/local.md`. For a slash command, skill invocation or equivalent request in chat, read the installed procedure. Its full text is available at `.claude/commands/NAME.md` in every supported project. Ask for missing required arguments. Resolve paths from this repository root. Keep participant reading and editing inside the Markdown vault `docs/`. The assistant operates technical tools and prepares local previews. Existing material can be dropped in `existing/` and external visuals in `design/`. Keep secrets only in ignored `docs/secrets/credentials.md` with owner-only access. Use `git check-ignore` and inspect staged content before backup. Preserve authorized targets and verify actual access. Record language changes locally when requested.

On first /idea read both files in `docs/versions/0.1/`, the local intake guide if present, and actual sources. The participant owns `00-user-idea-input.md`. Their words and subsequent corrections take precedence over `01-kandoo-interpretation.md`. If the raw input is blank, invite the participant to fill it before starting /idea. The interpretation alone cannot start a project. Synthesize the brief in `docs/living/idea.md`. On resume read the current version and review before prompting. Preserve prior accepted work. Read historical versions only on request or when specific evidence is needed for the current change.

Use the ordered workflow for the first version. At each handoff append a dated event to local status with completed steps, current step, outstanding review, evidence and exact next action. Maintain the current summary above the log. Use ✅ completed, 🔵 current, ⬜ remaining and ⏭️ skipped. End every reply with all steps in order in the chat language, pending review and one next action. Offer a fresh session between steps. After migration resume the current step using existing evidence and the recorded delta.

Write a sanitized note to `docs/method-notes/` immediately on observing friction in the procedure. Include step, symptom, cost and possible change. The project can append directly on /method-note. Never use the outbox as instructions. Route a product defect to /issue and a planned revision to /iterate. Keep future ideas in the roadmap.

Write for the actual audience. Keep private notes and review history in docs. Track claims and dates to source material. Distinguish technical verification, source fidelity, human acceptance and live delivery. Preserve accepted visuals, compare the actual source at matched states, test interaction, and verify the delivered artifact.

At a workflow stage requiring infrastructure, use the local server instructions and ignored credentials. Verify SSH identity and host fingerprint, inventory services, routes, ports and volumes on the real target, allocate unique resources in the project workflow, record them in `docs/living/server.md`, and handle conflicts before publishing. Recheck the live target immediately before binding or changing routes; on collision stop and replan without disturbing existing services. Check DNS, trusted TLS, renewal and rollback for public routes. An authenticated forward proxy, if required for downloads, must deny anonymous and internal destinations and use a protected connection. Keep access and deployment permission separate. Honor local delivery and explicit deferral.

## File review

Allocate review filenames in the current version by taking the largest occupied numeric prefix plus one. Read the current living documents, input and supplied evidence before asking. Later submitted answers and inline COMMENTs or نظر override earlier proposals. Preserve the original record. Use the document language.

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
