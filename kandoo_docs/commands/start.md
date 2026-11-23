---
name: start
description: Set up a fresh workspace through one chat question at a time, with optional Git backup and routine intake.
---

# /start

Read `AGENTS.md`, the Kandoo constitution, living profile and status.
All paths are relative to the workspace root. Apply the review constitution's **chat
setup exception** and the bottom progress rules. Ask one unanswered question per turn,
process and save its answer, then ask the next. Never assign a setup questionnaire file
or ask the person to submit an assistant-written setup summary.

## Resume or choose languages

1. Inspect lifecycle before changing anything. If configured, preserve the applied version and
   hand off to its saved next action; apply explicit settings changes conversationally. Resume any open version at its saved step. If setup is incomplete, reuse
   saved choices and continue its pending question/check. Never restart over real work.
2. If conversation language has not already been explicitly supplied, the first and
   only question is bilingual:

   > Which language would you like to use in chat? **English (recommended)** or **Persian**?
   >
   > زبان گفت‌وگو را چه انتخاب می‌کنید؟ **انگلیسی (پیشنهادی)** یا **فارسی**؟

   English is a recommendation, not an answer inferred from a command or silence.
   Save the answer before continuing. Thereafter use that language for every question,
   explanation, progress label and next action; paths/command identifiers stay unchanged.
3. Ask document language next, unless already answered. Recommend English if the
   person can comfortably use it, and Persian if they cannot. Keep it independent of
   chat language. New participant-facing documents follow this separate preference.

## Detect local facts

4. Detect OS/shell, writable workspace, Git and the current host. Derive the workspace
   name from the folder or supplied request; ask only if a meaningful ambiguity remains.
   Never ask which AI host the participant will use. All supported host copies are
   installed; another session may use a different host and resume the same saved state.
   Explain opening `kandoo_docs/` in Obsidian. Check Python 3.9+ before building the template and Git before creating a project.
5. Server intake belongs to the installed Job at its declared infrastructure stage.
   Do not ask about servers, create a server credentials scaffold, contact a server or provision
   DNS/TLS/proxy during universal setup. Preserve any access facts already supplied
   without printing secrets. A local content Job can complete without a server.

## Git and backup

6. Inspect Git, effective identity and all fetch/push remotes. Prefer the participant's
   repository created with GitHub **Use this template** and cloned over HTTPS. Existing
   forks are valid. ZIP extraction needs local Git initialization when available; help
   connect a participant-owned remote or record remote backup pending. Preserve
   nonempty history and branches. Never push a participant workspace to `gonbad/moom`.
7. Reuse effective `user.name`/`user.email` from local or inherited configuration without
   another question. For missing fields, use trustworthy supplied or authenticated
   account facts, respecting email privacy; ask only for a value still unknown. Do not
   derive authorship from the remote owner or template history. Write necessary new
   identity settings locally; never change global identity or create one per Project.
8. Reuse working authentication. Public HTTPS cloning needs no repository login; private
   cloning and pushes need authentication. Prefer an installed credential manager or
   GitHub CLI's HTTPS/browser login, with required account consent. GitHub account
   passwords do not authenticate Git; do not put passwords/tokens in URLs, prompts or
   chat. SSH is not a prerequisite to cloning. For later SSH setup, reuse a suitable
   GitHub key or create one, provide its public key in a Markdown note inside `kandoo_docs/`,
   guide adding it to the account, and verify access before changing the remote.
   Keep GitHub and server keys distinct. Working HTTPS remains usable if SSH is deferred.
9. Before an authorized backup, verify ignore rules and staged files, excluding
    credentials, caches and logs. Verify the intended participant destination and a
    real push/ref; `ls-remote` alone proves no write access. Save actual backup evidence
    in the profile. Offline, missing Git/identity or an explicit skip can continue with
    the missing capability honestly pending. Do not force-push unrelated history.

## Persist and hand off

After each answer/check, update `profile.md` and `status.md` under
`kandoo_docs/living/`, including the pending setup question and next action. Append a
non-secret assistant-written decision/check summary to
`kandoo_docs/versions/0.1/setup.md`; preserve earlier answers and their certainty.
An explicit chat answer is Confirmed; explicit delegation is Provisional; silence is
pending. Leave server state unselected unless an explicit request already supplies a choice.

Mark bootstrap start done when required preferences are answered or explicitly
delegated and intended checks are resolved or deferred. Record verified, pending,
user-skipped and not-needed checks separately. Clear the pending setup question and
make /job current. Check ancestor Git roots and host instructions. For intentional nesting offer a local Git exclude for the Kandoo in its enclosing repository. Preserve unrelated rules.
Compare the input bytes (normalize CRLF to LF) with Job guide SHA256 in status. If they match, localize the untouched 00-job-input.md guide into the document language, preserving any participant edits. Announce the input path, samples/ for example outputs and existing/ for code, documents or assets to adopt. Create these folders if missing. Invite free-form input and end with the exact /job invocation. Save the localized guide hash in status before participant edits so an untouched guide never counts as user input.
