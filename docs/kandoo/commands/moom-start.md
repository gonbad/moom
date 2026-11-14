---
name: moom-start
description: Set up a fresh template with languages, participant Git backup and optional shared server.
---

# /moom-start

Read `AGENTS.md`, all of `docs/constitution/`, and the living profile, status and Job.
All paths are relative to the workspace root. Follow the file review/certainty and
bottom progress rules on every reply, including setup questions.

1. Inspect existing state before changing it. If already configured, preserve the
   Kandoo and route to its current next action. Never restart bootstrap over real work.
   If resuming setup, reuse completed facts and verify only unresolved/changed checks.
2. Collect workspace name, conversation language, document language and AI host.
   Detect OS/shell, writable workspace and Git. Explain opening `docs/` in Obsidian.
   Put open setup questions and non-obvious decisions in the first unused numbered
   round under `docs/kandoo/versions/0.1/`, including the server question upfront.
   Apply the same context/options/recommendation/answer and submission protocol as
   later steps. Until a conversation language is chosen, use the current conversation's
   language. Adapt participant-facing inputs and new docs to the document language.
   Local-only work needs no Python, Node, Docker or SSH unless the chosen work needs
   them. Install missing necessary tools natively where authorized and feasible.
3. Ask **upfront** whether the participant has a server; do not wait for Job selection.
   Record `none` cleanly for no server, DNS, TLS and proxy and continue without a
   server purchase. With one, have the participant write initial credentials only in
   gitignored `docs/kandoo/secrets/credentials.md` (never chat or question files) and
   perform the complete shared procedure in `docs/constitution/03-infrastructure-and-secrets.md`:
   verified SSH fingerprint/login, dedicated key, existing-service inventory, domain
   question, DNS A-record correction or free unique `nip.io` name, publicly trusted
   HTTPS and renewal, and authenticated HTTP forward proxy with ignored credentials.
   Verify authenticated HTTP/CONNECT downloads and anonymous denial. Reuse a tunnel-bound
   proxy for later package/API commands. Record non-secret evidence in
   `docs/kandoo/living/server.md`.
4. Inspect Git and remotes. ZIP extraction needs `git init`; missing identity needs
   repository-local `user.name` and `user.email` from the participant. Never change
   global identity. Strongly recommend a **participant-owned remote**, regardless of
   server choice. A fork already cloned is valid after ownership/write verification;
   otherwise guide creating a participant repository, or an owned bare repo over SSH.
   When connected, help an upstream-only clone acquire a participant remote. Remove/repoint template
   upstream remotes without losing participant branches; never push to `gonbad/moom`.
   Avoid remote URLs containing credentials. Preserve nonempty remote history; inspect
   and reconcile without force-pushing or overwriting work. Ask only for unavoidable
   account/OS consent. When available, verify a real first backup and its remote ref.
   Offline/local-only participants may continue with local Git and remote setup pending.
   If Git or identity is unavailable, or the user insists on skipping any setup step
   (including server verification), record the skip and consequence and continue.
5. Before committing/backing up, verify `.gitignore` protects local secrets and inspect
   the staged files. Never add credentials, caches or logs. Store backup evidence in
   `docs/kandoo/living/profile.md`. Missing repository access remains pending; `ls-remote`
   alone is not write verification. Record questions/non-obvious setup choices in
   numbered `.md` files under `docs/kandoo/versions/0.1/`, applying submitted-blank
   delegation correctly; never refer the participant to non-`.md` files or paths outside `docs/`.
6. Mark bootstrap start done when the intended setup is resolved, including explicit
   skips or offline deferrals. Record each actual check separately as verified,
   pending, user-skipped or not needed; a pending backup never blocks Job definition.
   Pending account/network setup does not become a success claim.
   Persist profile, server and status; the next active stage is Job definition.

End with one exact action: invoke `/moom-job` when setup can proceed (Codex CLI
`$moom-job`; desktop slash/dollar picker; Antigravity select/mention the skill).
If an unanswered essential preference remains, name its file; honor explicit skips.
Finish with the localized bootstrap
progress bar showing start, Job definition and first Project workflow.
