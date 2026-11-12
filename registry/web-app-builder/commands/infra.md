# Provision this Project's infrastructure

Read [the infrastructure contract](../references/infrastructure.md) in full. Allocate
and retain this Project's VPS and local ports and unique Compose identity. Copy the
supplied assets/compose.yaml to DEPLOY. Generate DB credentials before provisioning;
create and transfer the protected `.env.infra` explicitly. Validate required variables,
then start PostgreSQL and Redis with that retained Compose project name and volume set.

Establish the native OpenSSH session using the verified key, local forwards and
fail-fast options. Set this Project's local application environment to the forwarded
ports. Prove an authenticated database query and Redis PING. Record redacted outcomes
and tunnel ownership in LIVING/infrastructure.md; leave missing access as a concrete
blocker. The assistant handles commands on Windows, macOS and Linux.
