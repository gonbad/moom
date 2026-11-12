# Provision the agent's server services

Read the infrastructure contract in full. Retain unique deployment identity, ports,
Compose volumes and generated protected DB credentials. Start PostgreSQL/Redis on the
VPS and prove authenticated access through native SSH -L forwards. For messenger
webhooks add -R in the same SSH session, use a verified project-specific nip.io/domain
HTTPS endpoint and the same local/production handler. Record identity, allocations
and redacted checks in LIVING/infrastructure.md. Do not claim live delivery before a
handler and actual platform registration have been exercised.
