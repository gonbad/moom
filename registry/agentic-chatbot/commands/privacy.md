# Review sensitive data handling

Write LIVING/privacy.md identifying captured personal/secret data, model-visible forms,
trusted stores, processors, recipients, retention/deletion and approved output sinks.
Specify typed caller-bound opaque handles where required, without encrypting trivial
public strings merely to imitate a harness. Review the data flow and tradeoffs with
the owner. Keep actual credentials/session material out of prompts, logs and docs.
