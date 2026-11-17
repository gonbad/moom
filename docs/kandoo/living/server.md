# Shared server

- Shared server choice: unselected
- Host / public IPv4 / SSH user and port: unset
- SSH fingerprint and dedicated key login: unverified
- Domain choice / DNS evidence: unset
- Public HTTPS URL / TLS verification / renewal: unverified
- HTTP forward proxy / authentication checks / tunnel readiness: unverified
- Ignored secret file references: none
- Verification evidence and pending work: none yet

Universal setup leaves this record unselected. A Job owns the stage that asks about
infrastructure. Each Project records its choice in `docs/projects/ID/living/server.md`:
reuse an identified existing server, configure a server for this Project, or none/deferred.
Unselected is not a refusal. Empty/missing credentials are not a choice or a verified
connection. A local Project never clears shared facts. `/preferences` can change an
explicitly selected shared or Project scope later.

## Deployment and port ledger

| Server identity | Owner | Deployment ID | Purpose | Remote address/port | Local forwarding port | Volume/site | Evidence |
| --- | --- | --- | --- | --- | --- | --- | --- |

Inventory before allocation. Record shared services and allocations for Projects that
explicitly select this server. Project-owned servers maintain their own facts/ledger;
check local forwarding ports across active targets too. Keep credentials ignored and
preserve other Projects' deployments and explicit target choices.
