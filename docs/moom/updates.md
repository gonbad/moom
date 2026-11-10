# Engine updates

The participant asks for moom-update; the assistant handles Git, fetching and checks.
Select a specific upstream release tag and resolve its immutable commit. Fetch from
https://github.com/gonbad/moom into temporary storage without changing the Kandoo's
remotes or merging the template over user files. Record that commit in the workspace
version notes. Check .moom/release.json against the downloaded tree.

The manifest explicitly lists engine files and hashes, plus a bootstrap-only catalog.
.moom/managed.json retains the installed upstream baseline. Ownership is specific
paths, not the whole .moom/ directory. Local records under .moom/local/ are ignored.

Compare installed baseline → local files → requested release:

1. Replace unchanged managed files. Preserve local changes if upstream did not touch
   that file. Reconcile true conflicts semantically using both upstream versions and
   the local copy. Review contradictory instructions rather than appending text.
2. Keep customized job/, projects/, shared/, workspace.json, profile and human review
   histories intact. Entry-point local additions require the same semantic comparison.
   A schema change needs an explicit structured migration; never merge JSON as prose.
3. Once a Job exists, skip registry/ entirely, even if installation is incomplete.
   Never restore the catalog to a configured Kandoo. Before setup, bootstrap files can
   update with the same local-edit protections. A requested catalog refresh is a
   separate temporary fetch; it cannot overwrite the installed Job.
4. Plan with `update --source PATH`. Put reconciled conflicted files in a separate
   directory preserving relative paths, then use --resolution-dir PATH --apply.
   Unresolved conflicts prevent application. The helper keeps a recovery checkpoint,
   applies only selected paths, regenerates adapters and runs checks using the new
   helper. A failed check restores affected files; the checkpoint retains originals.
5. Read the check results and inspect the resulting diff. Commit only the update's
   files, using existing Git authorization; preserve unrelated staged and unstaged
   work. Do not claim remote synchronization unless a push succeeded.

The helper handles hashes and file mechanics. The assistant handles semantic merges,
schema/Job compatibility and unavoidable choices. No package-manager installation
of Moom or participant-run terminal command is required.
