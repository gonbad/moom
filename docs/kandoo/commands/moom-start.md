---
name: moom-start
description: Set up a fresh workspace through one chat question at a time, with Git backup and optional server access.
---

# /moom-start

Read `AGENTS.md`, all of `docs/constitution/`, and the living profile, status and Job.
All paths are relative to the workspace root. Apply the review constitution's **chat
setup exception** and the bottom progress rules. Ask one unanswered question per turn,
process and save its answer, then ask the next. Never assign a setup questionnaire file
or ask the person to submit an assistant-written setup summary.

## Resume or choose languages

1. Inspect lifecycle before changing anything. If configured, preserve the Kandoo and
   hand off to its saved next action; settings changes use `/kandoo-settings`. If
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

## Detect facts and handle the optional server

4. Detect OS/shell, writable workspace, Git and the current host. Derive the workspace
   name from the folder or supplied request; ask only if a meaningful ambiguity remains.
   Never ask which AI host the participant will use. All supported host copies are
   installed; another session may use a different host and resume the same saved state.
   Explain opening `docs/` in Obsidian. No Python, Node, Docker or SSH is a universal
   local prerequisite; install only tools needed for the actual work.
5. Address the server before Job selection. **Create or preserve** the ignored Markdown
   file `docs/kandoo/secrets/credentials.md` using the infrastructure constitution's
   scaffold before referring the participant to it. Verify ignore coverage and local
   permissions first. Ask only for server availability in chat; credentials go in the
   file. Explain that continuing with the fresh scaffold empty and no server supplied
   means no server for now: record `none`/deferred without a file-submission gate or
   repeated prompts. Do not infer an answer merely because you just created a blank
   file; a request to continue without filling it is sufficient. If a server has
   been promised or partly supplied, record pending access rather than no server or a
   successful check. Never erase existing server facts because a local file is empty.
6. With access supplied, follow `docs/constitution/03-infrastructure-and-secrets.md`:
   SSH fingerprint/login and dedicated key, existing-service inventory, domain or free
   `nip.io` name, DNS, publicly trusted HTTPS/renewal and authenticated forward proxy.
   Ask any remaining domain preference in its own turn. Reuse working keys, proxy and
   services; record non-secret evidence in `docs/kandoo/living/server.md`. Honor skips
   and defer dependent checks without blocking unrelated local work.

## Git and backup

7. Inspect Git, effective identity and all fetch/push remotes. Prefer the participant's
   repository created with GitHub **Use this template** and cloned over HTTPS. Existing
   forks are valid. ZIP extraction needs local Git initialization when available; help
   connect a participant-owned remote or record remote backup pending. Preserve
   nonempty history and branches. Never push a participant workspace to `gonbad/moom`.
8. Reuse effective `user.name`/`user.email` from local or inherited configuration without
   another question. For missing fields, use trustworthy supplied or authenticated
   account facts, respecting email privacy; ask only for a value still unknown. Do not
   derive authorship from the remote owner or template history. Write necessary new
   identity settings locally; never change global identity or create one per Project.
9. Reuse working authentication. Public HTTPS cloning needs no repository login; private
   cloning and pushes need authentication. Prefer an installed credential manager or
   GitHub CLI's HTTPS/browser login, with required account consent. GitHub account
   passwords do not authenticate Git; do not put passwords/tokens in URLs, prompts or
   chat. SSH is not a prerequisite to cloning. For later SSH setup, reuse a suitable
   GitHub key or create one, provide its public key in a Markdown note inside `docs/`,
   guide adding it to the account, and verify access before changing the remote.
   Keep GitHub and server keys distinct. Working HTTPS remains usable if SSH is deferred.
10. Before an authorized backup, verify ignore rules and staged files, excluding
    credentials, caches and logs. Verify the intended participant destination and a
    real push/ref; `ls-remote` alone proves no write access. Save actual backup evidence
    in the profile. Offline, missing Git/identity or an explicit skip can continue with
    the missing capability honestly pending. Do not force-push unrelated history.

## Persist and hand off

After each answer/check, update `profile.md`, `server.md` and `status.md` under
`docs/kandoo/living/`, including the pending setup question and next action. Append a
non-secret assistant-written decision/check summary to
`docs/kandoo/versions/0.1/setup.md`; preserve earlier answers and their certainty.
An explicit chat answer is Confirmed; explicit delegation is Provisional; silence is
pending. The empty optional server scaffold has only the narrow meaning above.

Mark bootstrap start done when required preferences are answered or explicitly
delegated and intended checks are resolved or deferred. Record verified, pending,
user-skipped and not-needed checks separately. Clear the pending setup question and
make Job definition current. Explain that `/moom-job` starts **file-based** intake and
that `/kandoo-settings` changes settings later.

End with the localized bootstrap progress (start, Job definition, first Project
workflow) and one next action: answer the single pending chat question, complete an
unavoidable account/access action, or invoke `/moom-job` using the current host's
invocation style. Never name a setup-question file as the next action.
