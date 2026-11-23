---
name: topology
description: Set project placement, Git, remote and environment policy.
---

# /topology

Review a proposed policy once per Kandoo in living/workflow.md. Use the stable field names below. Leave local content jobs free of server questions.

    Project placement: sibling
    Project Git: independent
    Remote policy: none
    Secrets policy: none

Placement options are sibling (../SLUG), nested (projects/SLUG, excluded from the parent Git tree), custom (record the parent directory), and ask. Record which inputs /new-project must request each time. For nested paths inspect ancestor host instructions and Git ownership and explain their effect. Independent initializes or reuses a destination-root repository. Existing uses a project-root or enclosing repository. In an enclosing repository keep the new project directory tracked and stage only scoped paths. Use either main or master as configured. Remote options are none, ask, or configured. For configured remotes record the provider/namespace (default to Kandoo’s provider), private/public choice, manual URL or authorized CLI/API creation, verified destination and backup cadence. Default to local commits at closed steps and pushes at agreed milestones when enabled.

For deployment choose shared connection plus per-project allocation, or dedicated server intake at the relevant stage. For API jobs independently choose shared or per-project credentials. Record non-secret details in living/context/ and credentials only in ignored kandoo_docs/secrets/. Confirm the policy and continue to /shared-code.
