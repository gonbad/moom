# Verify the complete product

Run proportionate backend/API/integration checks against a separate test database;
never reset the live production database. Exercise the reviewed acceptance scenarios,
permissions, validation, async failures and migration/restart behavior. Test the built
frontend using the actual production serving path, including direct route entry,
refresh, missing assets and unknown API errors.

Save machine outcomes in EVIDENCE and summarize them in VERSION/test-results.md.
Walk the complete product with the owner in manageable journeys, fix reported defects,
and record their actual acceptance separately from the checks. Carry any unresolved
behavior, external dependency or visual mismatch as a blocker, not an implicit pass.
