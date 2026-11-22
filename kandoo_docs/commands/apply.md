---
name: apply
description: Verify a method and seal the template for subsequent projects.
---

# /apply

Require a reviewed mission and workflow in kandoo_docs/living/, including complete steps, or an exact /pick-job selection. Reconcile pending COMMENTs. Work only on the template and method dossier. Generate reusable code, local tooling and their tests inside template/ where needed. Keep participant data and credentials out. Seed only the selected chat/document languages in template/docs/living/profile.md. Localize participant-facing seed documents and labels in the chosen document language; retain the two zero-byte idea files, stable paths, the Server mode field and the command column syntax. Keep the general constitution shared across methods. Include the version change summary and old→new step map at template/docs/method/CHANGELOG.md for subsequent versions.

Verify cross-references, all procedure inputs/outputs, command collisions, conditional stages, tests for generated code, and the toolchain on a representative input. Reject runtime links into a Kandoo, sibling or registry, including paths embedded in generated code. Keep technical results separate from participant acceptance. Compare the selected starter installation against its source for an exact pick.

The assistant runs `python3 scaffold.py seal VERSION` from the Kandoo root (use the available Python 3.9+ launcher). This updates the built template constitution and joins the template, mission, workflow, references and step sources in an immutable inert snapshot, checks the step set and publishes the applied version only after verification. Repeat with identical inputs to finish an interrupted seal; a changed sealed method needs a new version. Render a throwaway copy with `python3 scaffold.py render VERSION NEW_TEMP_PATH` to verify the actual host copies, local links and project-only command inventory. Record the digest and check results in the dossier and mark the method configured. Offer /new-project. Existing projects receive changes only through /migrate.
