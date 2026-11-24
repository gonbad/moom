---
name: topology
description: Set project placement, Git, remote and environment policy.
---

# /topology

Analyze topology choices before writing the agreed policy in living/workflow.md. Use the stable field names below. Leave local content jobs free of server questions.

    Project placement: sibling
    Project Git: independent
    Remote policy: none
    Secrets policy: none

Here none describes an offline job. Select shared when authorized projects use a common API credential and per-project when each has its own.

Placement options are sibling (../SLUG), nested (projects/SLUG, excluded from the parent Git tree), custom (record the parent directory), and ask. Record which inputs /new-project must request each time. For nested paths inspect ancestor host instructions and Git ownership and explain their effect. Independent initializes or reuses a destination-root repository. Existing uses a project-root or enclosing repository. In an enclosing repository keep the new project directory tracked and stage only scoped paths. Use either main or master as configured. Remote options are none, ask, or configured. For configured remotes record the provider/namespace (default to Kandoo’s provider), private/public choice, manual URL or authorized CLI/API creation, verified destination and backup cadence. Default to scoped local commits before assistant edits and at each handoff and pushes at agreed milestones when enabled.

For deployment choose shared connection plus per-project allocation, or dedicated server intake at the relevant stage. For API jobs independently choose shared or per-project credentials. Record non-secret details in living/context/ and credentials only in ignored kandoo_docs/secrets/. Confirm the policy and offer /shared-code.

Where several projects use the same authorized API key, recommend shared as the default for that case. Store the key in ignored kandoo_docs/secrets/credentials.md and use the protected ignored copy in each authorized project on creation. Offline work with no credentials uses none.
