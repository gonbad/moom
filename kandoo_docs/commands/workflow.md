---
name: workflow
description: Write the ordered project steps, gates and method-specific infrastructure policy.
---

# /workflow

Start from the reviewed mission and open version. In kandoo_docs/living/workflow.md declare exactly one line `Server mode: none`, `Server mode: dedicated` or `Server mode: shared`. Specify the responsible stage and local deferral for methods needing infrastructure. Dedicated methods receive a project /server helper. Shared methods hand down connection instructions when creating a project; the project owns all port/domain/volume allocation and verification.

Write a Markdown pipeline table like a registry workflow: begin each stage row with "| `/idea` |" (substitute its command for later rows), followed by English and document-language labels and its exit condition. The first stage is always /idea. Define inputs, outputs, handoff and gates for each stage, including a representative pilot before full production when relevant. Put each complete command in kandoo_docs/living/steps/NAME.md with YAML name and description on separate lines. Add needed standalone references in living/references/ and cite their eventual project paths under docs/references/. Validate names against command-names.md and installed commands. Make paths relative to the project root. Plan reusable code and regression checks in template/ when the method requires them. Record review, step mapping and next action /apply.
