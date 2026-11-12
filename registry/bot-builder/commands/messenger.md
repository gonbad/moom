# Specify and implement messenger adapters

Read [messenger contracts](../references/messenger.md). Record selected platforms,
verified current official API sources, normalized schemas, limitations and proxy
requirements in LIVING/messenger.md. Implement adapters in SOURCE/app/messenger/ and
transport fixtures under this Project's tests. Preserve platform identity and tokenize
secrets only through ignored config. Prove normalized message and callback behavior;
keep live integration verification pending until credentials and handlers are available.
