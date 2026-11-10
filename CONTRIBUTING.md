# Contributing

Develop and test the generic template in temporary copies. Leave workspace.json empty
of user configuration and keep job/ and projects/ empty in a template release.

For a starter Job, add registry/NAME/SKILL.md with the standard name and description,
an independent version under metadata, its origin and a retained license. Include only
reusable commands/, references/, scripts/ and assets/. Add a concise entry to
registry/index.json so discovery can read descriptions before complete recipes.
Provide a representative, self-contained Python smoke operation under scripts/.
Do not add project inputs, reviews, secrets, built output or installed environments.

Participants can use moom-export to prepare a Job contribution. Only the repository
owner includes recipes in official releases after review. AI-assisted review is not a
claim of manual audit or proof of safety; keep origins and meaningful changes explicit.

Canonical base commands live in .moom/core/commands/. Generated copies must be
rebuilt rather than edited. Job commands cannot use the moom- namespace; their
host aliases use job-NAME-STEP to avoid host builtins and base commands.

```sh
python3 moom.py sync
python3 -m unittest discover -s tests -v
python3 tools/release.py
python3 tools/release.py --check
```

The release tool builds a path-and-hash manifest from an explicit allowlist and verifies
the pristine template. Commit the compiled files, tag the Moom version from VERSION,
and push the reviewed commit and tag. Workshop's private authoring discussions stay
outside this repository. A configured Kandoo exports its Job; it does not publish itself
as a generic Moom template.
