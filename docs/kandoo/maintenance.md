# Maintain your Kandoo

Describe the desired change in conversation; you do not need to locate configuration
files or run terminal commands. The assistant resolves the owner and preserves the
selected Project. These commands also accept a short description of the desired work.

| Intent and example | Route | Result and evidence |
| --- | --- | --- |
| Start another work item: `new-project — an astronomy article` | `new-project` | A new numeric ID, meaningful/provisional slug, idea and source intake; earlier Projects preserved. |
| Change chat or document language | `preferences` | Keep the two choices independent; use the selected chat language immediately, preserve historical answers and avoid unrelated infrastructure checks. |
| Change the workspace display name | `preferences` | Update shared display references without implying a folder, Git remote or URL rename. |
| Change this workspace's Git identity, authentication or remote | `preferences` | Reuse existing facts, inspect ownership/history, change only the requested settings and verify applicable backup evidence; never change global identity or force-push unrelated history. |
| Add a server or domain, retaining existing services | `preferences` | Create/preserve the ignored credentials file before handoff; check affected access, origin/aliases, DNS, proxy routing and trusted TLS without resetting unrelated infrastructure. |
| Change future output or workflow | `iterate`, Job/shared scope | Revise the living method and affected commands; preserve old Project evidence. |
| Fix a concrete fault | `issue` | Reproduce, repair and verify the affected scope. |
| Save an idea for later | `add-idea` | Record it in the correct roadmap without interrupting the current step. |

For example, `preferences — change chat language to Persian` already supplies the
new value; the assistant applies and records it without another answer form. Unresolved
non-obvious choices use a numbered review in the owning shared or Project version. A missing
local credentials file does not delete an existing server. After settings work, resume
the selected Project's saved step. Switch AI hosts freely; there is no host preference
to reconfigure, and every supported command copy remains installed.

## Publication removal, when the Job publishes Projects

Describe exactly which effect you want:

- **Remove from the index:** edit the authored index, keeping the post published and
  accessible by direct URL. This does not make it private.
- **Unpublish:** remove the post from release selection and remove/update incoming
  links; verify and publish the new release. Preserve local source and documentation.
- **Delete the local Project too:** identify the exact docs/artifacts and backup policy
  in the owning review record before deletion. Do not infer local deletion from an
  unpublish request. Git history and copies already held elsewhere are separate.

Use ordinary conversation or `iterate` with the target Project and shared/index
scope. The assistant operates code/configuration and provides a Markdown summary inside
`docs/`. It verifies the index and direct URL after publication. Changing a Job never
automatically removes or republishes existing Projects.

## Bringing existing work

The initial idea input links a Markdown source note and source inventory inside the
Project docs. Paste notes and links there, or point out a file you already created.
For an existing application or binary bundle, the assistant provides the exact
`projects/ID/existing/` drop location. Raw inputs remain separate from public source.
If the name is provisional, the first handoff explains when it will be resolved.

## What counts as completion

The assistant records the specific changed setting, checks actually performed and any
remaining dependency in the owning shared/Project version. Local checks, human review,
public deployment and Git backup are separate evidence. A public source repository
also exposes its committed docs/history, even when the website excludes those files;
review the intended public contents before publishing it.

## Improving the method while fixing this Project

Say, for example: “The arm rotates the whole character. Fix this Project and update
the Job so future asset reviews test limb pivots.” `/issue` can resolve Both scopes
without asking you to identify the technical cause or repeat the explicit scope.
For a planned workflow change, use `/iterate` with the same scope. The assistant
records the general method change separately from Project facts, synchronizes only
changed commands, reports downstream evidence invalidated and preserves other Projects.
An ordinary request works too; these commands are routing aids, not required syntax.

Infrastructure selection occurs when the Job needs it. Choose an identified existing target,
a new Project-specific server or local deferral. `/preferences` can handle an explicit
shared or Project access change earlier; it never moves other Projects as a side effect.
