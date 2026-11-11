# Build the publication

Read ../references/distribution.md when configuring a new source/build boundary.
Run `python3 moom.py run scripts/build.py` from the workspace, or invoke the installed
scripts/build.py by path from any directory. It builds all published Projects, their
per-Project dist/ and offline ZIPs, and a clean aggregate dist/release.json.
For a local draft preview add `--preview ID`; it cannot be deployed.
Keep the index authored explicitly and verify its cards before building.
