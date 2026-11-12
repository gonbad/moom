# Deploy the accepted web application with HTTPS

Read [infrastructure](../references/infrastructure.md). Confirm the concrete deployment
target authorization and current acceptance evidence, retaining existing authorization.
Build SOURCE/frontend with compiled Tailwind and local assets. Inspect the built output
for runtime CDN dependencies. Deploy the same accepted code and migrations with backups.

For the default FastAPI serving path, copy assets/spa.py into the generated backend
and mount SPAStaticFiles AFTER API routes, with the resolved frontend/dist directory.
A bare StaticFiles(html=True) mount does not implement React navigation fallback.
Use browser-history routing with the supplied fallback, or explicitly configure and
test an equivalent strategy. GET/HEAD HTML navigation can receive the shell; unknown
API routes, missing assets and other methods must retain correct errors.

For containers, adapt assets/compose.app.yaml and a Project Dockerfile, merging it
with the database Compose stack under the retained identity. Verify database/cache
access inside the application container. Host systemd is also supported with the
host connection URLs. Prove startup/restart as the real service user.

Configure the participant's A record using optional Cloudflare DNS or the exact manual
record. Resolve server hostnames to IPv4; inspect conflicting records. Configure a
host Caddy site proxying to 127.0.0.1:APP_PORT, or an equivalent Nginx/Certbot setup,
without overwriting other sites. Obtain and verify a trusted certificate and hostname,
HTTP-to-HTTPS redirect, renewal, and public frontend/API access. Test nested routes
by direct entry/reload, missing assets and API errors over HTTPS after restart.

Record the deployed revision, URL, sanitized test evidence and rollback/renewal details
in VERSION/deployment.md and LIVING/status.md. A service being running or DNS resolving
alone is insufficient deployment evidence.
