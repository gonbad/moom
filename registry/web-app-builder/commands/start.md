# Start the web Project

Follow the Project contract. Reuse the active first Project or create a real Project
through Moom, then run scripts/project.py init. Ask missing language/profile questions
first. Capture the actual idea and any existing product supplied by the participant.
Collect server IP/hostname, SSH user and private-key path early; verify the exact
identity as described in the infrastructure reference. Reuse known facts and collect
secrets through ignored local files, not public documents.

Record public product configuration under LIVING/profile.md. Secrets belong in this
Project's ignored environment. Record deployment identity and port allocations under
LIVING/infrastructure.md. Do not overwrite another Project's configuration or assume
PROJECT_NAME is a globally unique VPS deployment name.
