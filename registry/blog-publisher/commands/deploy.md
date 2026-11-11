# Deploy the verified release

Use the workspace origin and hosting adapter described in ../references/distribution.md.
Run `python3 moom.py run scripts/deploy.py --dry-run` to validate the actual release
and adapter. With the user's existing authorization for that concrete origin, run the
same command without --dry-run. Transfer only compiled dist/ through the workspace
adapter; retain rollback capability. Verify the public index, every published post,
archives, and release hashes, and record the deployment receipt separately from acceptance.
