# Provision bot services and HTTPS development delivery

Read the infrastructure contract in full. Retain independent deployment identity,
ports and volumes; generate and protect database credentials before starting Compose.
Prove PostgreSQL authentication and Redis connectivity through native SSH -L forwards.
Provision a Project-unique nip.io hostname or supplied domain and trusted HTTPS at the
VPS. Route the public webhook to the retained reverse-forward port and run the unified
SSH session with -L database/cache plus -R webhook routing, using the verified key.

Use the selected platforms' authenticated webhook mechanisms and sanitized logs.
Prove delivery through the proxy/tunnel once a local handler exists. If blocked,
record the exact missing access or use supported polling with the same dispatcher on
both environments. Do not run concurrent consumers or claim a mock endpoint is live.
