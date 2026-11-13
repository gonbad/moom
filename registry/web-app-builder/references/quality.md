# Evidence and handoff

Derive checks from the real inputs and agreed output. Test the actual artifact and
its important interactions, error cases and operating environment, not merely folder
existence. Preserve input-to-output fidelity separately from functional success.
Keep test/review evidence in the current Project version without exposing private data.

Show the complete result to the person. Record acceptance only when they explicitly
accept that revision. If review is pending say so. A submitted question round or a
successful automated check cannot manufacture acceptance.

For offline delivery, test from an extracted path containing spaces and non-Latin
characters with networking disabled. Verify every runtime dependency is local, file
links work, and private input/history/secrets are excluded from exports. For live
delivery, verify the actual public URL, runtime restart, routing and relevant state
recovery. Retain a working previous release and an applicable rollback method.
Only publish with existing or explicit authorization for that actual target.
