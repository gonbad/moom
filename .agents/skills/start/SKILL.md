---
name: start
description: Set up a fresh workspace through one chat question at a time, with Git backup and an actual starter catalog.
---

# /start

Read `AGENTS.md`, all of `docs/constitution/`, and the living profile, status and Job.
All paths are relative to the workspace root. Apply the review constitution's **chat
setup exception** and the bottom progress rules. Ask one unanswered question per turn,
process and save its answer, then ask the next. Never assign a setup questionnaire file
or ask the person to submit an assistant-written setup summary.

## Resume or choose languages

1. Inspect lifecycle before changing anything. If configured, preserve the Kandoo and
   hand off to its saved next action; settings changes use `/preferences`. If
   finalizing, resume the saved finalization checklist. If setup is incomplete, reuse
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
   Explain opening `docs/` in Obsidian. No Python, Node, Docker or SSH is a universal
   local prerequisite; install only tools needed for the actual work.
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
   GitHub key or create one, provide its public key in a Markdown note inside `docs/`,
   guide adding it to the account, and verify access before changing the remote.
   Keep GitHub and server keys distinct. Working HTTPS remains usable if SSH is deferred.
9. Before an authorized backup, verify ignore rules and staged files, excluding
    credentials, caches and logs. Verify the intended participant destination and a
    real push/ref; `ls-remote` alone proves no write access. Save actual backup evidence
    in the profile. Offline, missing Git/identity or an explicit skip can continue with
    the missing capability honestly pending. Do not force-push unrelated history.

## Persist and hand off

After each answer/check, update `profile.md` and `status.md` under
`docs/kandoo/living/`, including the pending setup question and next action. Append a
non-secret assistant-written decision/check summary to
`docs/kandoo/versions/0.1/setup.md`; preserve earlier answers and their certainty.
An explicit chat answer is Confirmed; explicit delegation is Provisional; silence is
pending. Leave server state unselected unless an explicit request already supplies a choice.

Mark bootstrap start done when required preferences are answered or explicitly
delegated and intended checks are resolved or deferred. Record verified, pending,
user-skipped and not-needed checks separately. Clear the pending setup question and
make Job selection current.

## Show the available choices

Read the actual local `registry/README.md` and enumerate immediate starter directories
that have a readable `job.md`, its declared commands and references, and both
`project-input/en.md` and `project-input/fa.md`. Check that the shared Project forms
are present before offering a named install. Cross-check the
catalog against those files. Show each available identifier, a one-line description
from its Job, and the exact invocation for the current host. Never hardcode a starter
count or show a planned/missing starter as available. Report a damaged entry separately;
do not offer a command that will fail. If the whole catalog is missing in a template
checkout, report the incomplete checkout without fetching or inventing entries.

For Claude Code/OpenCode use `/job IDENTIFIER`; for Codex use `$job IDENTIFIER` or
select the job skill and send the identifier; for Antigravity select/mention the job
skill and send the identifier as its request. Do not assume every host has an argument
parser: the same ordinary request, “Use the job procedure with starter IDENTIFIER,”
must route to the fast path. Include the no-argument custom option (`/job`, `$job`,
or select the job skill without a starter) for defining/adapting a method through
file intake. Known-starter selection does not require Job-definition questions.

This actual catalog is the deliberate setup-menu exception to the single-action rule.
End with localized bootstrap progress and one action: choose one displayed starter
invocation or the custom Job option. While setup remains incomplete, the next action
instead answers its single pending chat question or unavoidable account/access step.
Explain that `/preferences` handles later settings; never name a setup-question file.
