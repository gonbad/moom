# Shared server

- Server choice: unasked
- Host / public IPv4 / SSH user and port: unset
- SSH fingerprint and dedicated key login: unverified
- Domain choice / DNS evidence: unset
- Public HTTPS URL / TLS verification / renewal: unverified
- HTTP forward proxy / authentication checks / tunnel readiness: unverified
- Ignored secret file references: none
- Verification evidence and pending work: none yet

`none` is a completed, valid answer for local-only work: set server, DNS, TLS and proxy
to `none` together. Later additions reuse the shared infrastructure procedure.

## Deployment and port ledger

| Owner | Deployment ID | Purpose | Remote address/port | Local forwarding port | Volume/site | Evidence |
| --- | --- | --- | --- | --- | --- | --- |

Do not guess free ports or reuse another Project's deployment. Record the proxy and
shared web service here, followed by each Project allocation. Credentials stay ignored.
