# Deploy: sync static distribution to VPS

Transfer the minimized `dist/` tree to the configured static hosting origin.
Only transfer compiled assets; keep working documents, git history, and secrets local.
Verify public HTTPS accessibility and checksum integrity after sync.
