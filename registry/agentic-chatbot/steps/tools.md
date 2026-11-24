---
name: tools
description: Inventory services, attenuate model-visible tools and generate Project-scoped contracts.
---

# /tools

Read the project constitution and current status. Use the following references from `docs/references/`: `services.md`, `workflow.md`, `payments.md`, `authority.md`.

Gate: `docs/living/prd.md` exists and has a closed review. Author `docs/living/tools.md` inside `docs/` so every contract
reviewed by the participant stays in Obsidian Markdown:
1. **Service Classification & Fallbacks:** Classify each dependency (`existing_api`,
   `owned_backend`, `api_bridge`), record ranked fallbacks, and mark payments `not
   applicable` when outside scope. Before authoring a platform bridge, inspect the
   optional API repository identified in the installed `services.md` reference.
   Record source/revision, capability fit, provenance/license findings, verification
   gaps and the reuse/adapt/reject decision; do not assume a gateway is production-ready.
2. **Model-Visible Tools vs Internal Service APIs:** Separate raw backend/admin APIs
   from caller-scoped tools exposed to the model (never exposing SQL, shell, generic
   HTTP or caller-override arguments).
3. **Executable Contracts (`./contracts/`):** For owned backends or bridges,
   have the assistant generate machine OpenAPI schemas under
   `./contracts/<service>/openapi.yaml` (never unscoped `docs/contracts/`, and
   never referring the participant to edit YAML files).
4. **Secret Variable Names:** List non-secret key names (model provider, service APIs,
   test bot tokens) in `tools.md` and instruct the owner to place secret values only in
   gitignored `docs/secrets/credentials.md`
   or non-`.md` files.

Resolve open questions via `docs/versions/VERSION/NN-analysis-tools.md` in
Obsidian; once review closes, hand off to `/sops`.
