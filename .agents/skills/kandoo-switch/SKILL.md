---
name: kandoo-switch
description: Resume a chosen existing Project with its own version, progress and current Job adaptation.
---

# /kandoo-switch

Read `AGENTS.md`, all of `docs/constitution/`, living profile, shared status/server and
the installed Job. Require configured state. Use workspace-root paths throughout.

Use the requested exact Project ID; if ambiguous, list existing IDs with living titles
and ask one selection question. Never choose whichever directory sorts last. Verify
both the target dossier and artifact directory exist; diagnose a mismatch instead of
creating a new Project to conceal it. Save the former Project's status first.

Read the target's `living/idea.md` and `living/status.md`, then only its selected open
version's inputs and submitted rounds needed for the resumed step. Restore that
Project's version, progress, pending questions/review and next action into shared
status. Do not scan historical versions, rebuild outputs, republish or reset progress.

Compare the Project's recorded Job revision with the current Job. Record the impact
and adaptation check in its open version; use the review protocol for non-obvious
changes. Preserve confirmed product decisions and accepted outputs. Evolving the Job
is allowed, but a method change does not authorize a deployment. Assess the Job,
shared docs/code, this Project and append-only feedback as appropriate.

End with the restored Project's localized progress and one exact pending file action
or current `job-*` command. Switching alone does not require a host restart.
