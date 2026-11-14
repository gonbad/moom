---
name: job-tools
description: Inventory services, attenuate model-visible tools and generate Project-scoped contracts.
---

# /job-tools

Read `AGENTS.md`, the four `docs/constitution/` documents and `docs/kandoo/living/profile.md`,
`job.md`, `server.md` and `status.md`. Resolve the active Project `ID` and `VERSION` from
status; all paths are workspace-root paths. Read the installed references
`docs/kandoo/living/references/workflow.md`, `services.md` and `authority.md` (plus
`payments.md` only when payments are in scope), `docs/projects/ID/living/idea.md`,
`prd.md` and submitted rounds in `docs/projects/ID/versions/VERSION/`. Preserve earlier
outputs and authorization.

Gate: `docs/projects/ID/living/prd.md` exists and has no unsubmitted question round
pending. Author `docs/projects/ID/living/tools.md` inside `docs/` so every contract
reviewed by the participant stays in Obsidian Markdown:
1. **Service Classification & Fallbacks:** Classify each dependency (`existing_api`,
   `owned_backend`, `api_bridge`), record ranked fallbacks, and mark payments `not
   applicable` when outside scope.
2. **Model-Visible Tools vs Internal Service APIs:** Separate raw backend/admin APIs
   from caller-scoped tools exposed to the model (never exposing SQL, shell, generic
   HTTP or caller-override arguments).
3. **Executable Contracts (`projects/ID/contracts/`):** For owned backends or bridges,
   have the assistant generate machine OpenAPI schemas under
   `projects/ID/contracts/<service>/openapi.yaml` (never unscoped `docs/contracts/`, and
   never referring the participant to edit YAML files).
4. **Secret Variable Names:** List non-secret key names (model provider, service APIs,
   test bot tokens) in `tools.md` and instruct the owner to place secret values only in
   gitignored `docs/projects/ID/secrets/credentials.md`—never unscoped `docs/secrets/`
   or non-`.md` files.

Resolve open questions via `docs/projects/ID/versions/VERSION/NN-questions.md` in
Obsidian; once submitted, hand off to `/job-sops`.

Apply the file-review/certainty protocol on `.md` files inside `docs/` and assess updates
to the Job, shared Kandoo, active Project and write-only creator feedback. Persist what
changed, evidence, pending review and next action in `docs/projects/ID/living/status.md`
and mirror `docs/kandoo/living/status.md`. Finish every reply with the current Job's full ordered
steps localized and one exact next action (`/job-sops` or the pending `.md` file).
