#!/usr/bin/env python3
"""Deterministic workspace mechanics. The coding assistant follows Markdown.

Python 3.10+, standard library only. One writer per workspace.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import uuid
import zipfile
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PACKAGE_ROOTS = {
    "SKILL.md",
    "LICENSE",
    "LICENSE.md",
    "LICENSE.txt",
    "commands",
    "references",
    "scripts",
    "assets",
}


def now():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def read(path):
    return json.loads(path.read_text(encoding="utf-8"))


def write(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        mode="w", encoding="utf-8", dir=path.parent, delete=False
    ) as stream:
        temporary = Path(stream.name)
        try:
            json.dump(value, stream, ensure_ascii=False, indent=2)
            stream.write("\n")
        except BaseException:
            temporary.unlink(missing_ok=True)
            raise
    temporary.replace(path)


def within(root, name):
    path = (root / name).resolve()
    if not path.is_relative_to(root.resolve()):
        raise ValueError(f"Path leaves workspace: {name}")
    return path


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest() if path.is_file() else None


def files(folder):
    result = {}
    for path in sorted(folder.rglob("*")):
        if path.is_symlink():
            raise ValueError(f"Symlinks are not portable package files: {path}")
        if path.is_file() and "__pycache__" not in path.parts and path.suffix != ".pyc":
            result[path.relative_to(folder).as_posix()] = sha(path)
    return result


def tree_sha(folder):
    return hashlib.sha256(
        json.dumps(files(folder), sort_keys=True).encode()
    ).hexdigest()


def config(root):
    value = read(root / "workspace.json")
    if value.get("schema") != 1:
        raise ValueError(
            "Unsupported workspace schema; preserve state and arrange a schema migration"
        )
    return value


def validate_state(state):
    """Reject incomplete imports before checks or state-changing operations."""
    if not isinstance(state.get("projects"), dict) or not isinstance(state.get("profile"), dict):
        raise ValueError("Workspace needs profile and projects objects; migrate the complete state")
    job = state.get("job")
    if job and (job.get("status") not in ("initializing", "ready") or not job.get("version")):
        raise ValueError("Job state needs its status and version; complete the workspace migration")
    for identifier, item in state["projects"].items():
        if (item.get("id") != identifier or not isinstance(item.get("milestones"), dict)
                or not item.get("job_observed") or not item.get("docs") or not item.get("version")):
            raise ValueError(f"Incomplete Project state: {identifier}; migrate id, milestones, job_observed, docs and version")
    for key in ("active_project", "first_project"):
        if state.get(key) is not None and state[key] not in state["projects"]:
            raise ValueError(f"Unknown {key} in workspace state")


def slug(value):
    if len(value) > 64 or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", value):
        raise ValueError(
            "Use a name of at most 64 lowercase letters, digits and single hyphens"
        )
    return value


def version(value):
    value = value.lstrip("Vv")
    if not re.fullmatch(r"\d+\.\d+(?:\.\d+)?", value):
        raise ValueError("Use a numeric major.minor or major.minor.patch version")
    return value


def version_key(value):
    parts = tuple(map(int, version(value).split(".")))
    return parts + (0,) * (3 - len(parts))


def version_path(base, number):
    number = version(number)
    major, minor, *patch = number.split(".")
    path = base / "versions" / f"V{major}" / f"V{major}.{minor}"
    return path / f"V{number}" if patch and patch[0] != "0" else path


def skill_info(folder):
    text = (folder / "SKILL.md").read_text(encoding="utf-8")
    match = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)", text, re.DOTALL)
    if not match:
        raise ValueError("SKILL.md needs YAML frontmatter with name and description")
    header = match[1]

    def scalar(key):
        item = re.search(r"^" + re.escape(key) + r":\s*(.+)$", header, re.MULTILINE)
        if not item:
            raise ValueError(f"Missing Skill field: {key}")
        raw = item[1].strip()
        if raw.startswith('"'):
            return json.loads(raw)
        if raw.startswith("'") and raw.endswith("'"):
            return raw[1:-1].replace("''", "'")
        if raw in ("|", ">", "|-", ">-"):
            tail = header[item.end() :]
            lines = []
            for line in tail.splitlines()[1:]:
                if line and not line.startswith((" ", "\t")):
                    break
                lines.append(line.strip())
            return " ".join(lines).strip()
        return raw

    name, description = scalar("name"), scalar("description")
    if slug(name) != folder.name or not 0 < len(description) <= 1024:
        raise ValueError(
            "Skill name must match its directory and description must have 1–1024 characters"
        )
    revision = re.search(
        r"^  version:\s*[\"']?([0-9]+\.[0-9]+(?:\.[0-9]+)?)[\"']?\s*$",
        header,
        re.MULTILINE,
    )
    return {
        "name": name,
        "description": description,
        "version": revision[1] if revision else "0.1.0",
    }


def validate_package(folder):
    info = skill_info(folder)
    entries = files(folder)
    if not any(name in entries for name in ("LICENSE", "LICENSE.md", "LICENSE.txt")):
        raise ValueError("A reusable Job must retain its license")
    for name in entries:
        parts = Path(name).parts
        if parts[0] not in PACKAGE_ROOTS or any(
            p.startswith(".env") or p in ("secrets", ".git", "node_modules", ".venv")
            for p in parts
        ):
            raise ValueError(f"Not a reusable recipe file: {name}")
        path = within(folder, name)
        if path.suffix in (".md", ".py", ".json", ".html", ".css", ".js"):
            text = path.read_text(encoding="utf-8")
            if re.search(r"(?<![\w-])(?:\./)?registry/", text):
                raise ValueError(
                    f"Active Job must be independent of the starter catalog: {name}"
                )
        if path.suffix == ".md":
            for target in re.findall(r"\[[^\]]*\]\(([^\s)]+)\)", text):
                if target.startswith(("#", "/")) or re.match(
                    r"[a-zA-Z][\w+.-]*:", target
                ):
                    continue
                destination = target.split("#", 1)[0]
                if (
                    destination
                    and not within(
                        folder, (path.parent / destination).relative_to(folder)
                    ).exists()
                ):
                    raise ValueError(f"Broken Job reference in {name}: {target}")
    for command in (folder / "commands").glob("*.md"):
        slug(command.stem)
        if command.stem.startswith("moom-"):
            raise ValueError("Jobs cannot declare the reserved moom- command namespace")
    return info


def job_folder(root, state):
    if not state.get("job"):
        raise ValueError("Configure a Job with moom-job first")
    folder = within(root, "job/" + slug(state["job"]["name"]))
    others = [p for p in (root / "job").iterdir() if p.is_dir() and p != folder]
    if others:
        raise ValueError("A Kandoo has exactly one Job")
    return folder


def command_sources(root, state):
    sources = {
        p.stem: p for p in sorted((root / ".moom/core/commands").glob("moom-*.md"))
    }
    if state.get("job"):
        folder = job_folder(root, state)
        validate_package(folder)
        for path in sorted((folder / "commands").glob("*.md")):
            # Namespacing also avoids host builtins such as status and export.
            name = f"job-{folder.name}-{path.stem}"
            slug(name)
            if name in sources:
                raise ValueError(f"Command collision: {name}")
            sources[name] = path
    return sources


def wrappers(root, state):
    output = {}
    for name, source in command_sources(root, state).items():
        relative = source.relative_to(root).as_posix()
        description = source.read_text(encoding="utf-8").splitlines()[0].lstrip("# ")
        body = (
            "<!-- Generated by Moom. Edit the canonical procedure, then run sync. -->\n"
            f"Read AGENTS.md and `{relative}` in full, then follow that procedure.\n"
            "Use the current workspace.json selection and current Job. Preserve the user's supplied context.\n"
        )
        front = (
            "---\n"
            + f"description: {json.dumps(description, ensure_ascii=False)}\n---\n\n"
        )
        output[f".claude/commands/{name}.md"] = front + body
        output[f".opencode/commands/{name}.md"] = front + body
        output[f".agents/skills/{name}/SKILL.md"] = (
            "---\n"
            + f"name: {name}\ndescription: {json.dumps(description, ensure_ascii=False)}\n---\n\n"
            + body
        )
    return output


def sync(root, check=False):
    state = config(root)
    output = wrappers(root, state)
    record = root / ".moom/generated.json"
    old = read(record) if record.exists() else {}
    conflicts = []
    for name in sorted(set(old) | set(output)):
        path = within(root, name)
        current = sha(path)
        desired = (
            hashlib.sha256(output[name].encode()).hexdigest()
            if name in output
            else None
        )
        if current is not None and current != desired and current != old.get(name):
            conflicts.append(name)
    if conflicts:
        raise ValueError(
            "Preserve and reconcile edited or colliding host commands: "
            + ", ".join(conflicts)
        )
    hashes = {
        name: hashlib.sha256(text.encode()).hexdigest() for name, text in output.items()
    }
    if check:
        if (
            old != hashes
            or any(
                sha(within(root, name)) != checksum for name, checksum in hashes.items()
            )
            or any(within(root, name).exists() for name in set(old) - set(output))
        ):
            raise ValueError("Host commands need synchronization")
    else:
        for name in set(old) - set(output):
            within(root, name).unlink(missing_ok=True)
        for name, text in output.items():
            path = within(root, name)
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding="utf-8", newline="\n")
        write(record, hashes)
    return {"commands": len(output) // 3, "files": len(output), "checked": check}


def dashboard(root, state):
    lines = [
        "# Moom / Kandoo",
        "",
        "[Guide](moom/guide.md) · [Review protocol](moom/review.md)",
        "",
    ]
    job = state.get("job")
    if job:
        lines += [
            f"Job: **{job['name']}**, revision {job['version']}, {job['status']}.",
            "",
            "[Job discussions](job/) · [Workspace discussions](workspace/)",
        ]
    elif (root / "registry/index.json").exists():
        lines += [
            "No Job yet. Ask for **moom-job** to describe the repeated task and first real Project."
        ]
    lines += [
        "",
        "| Project | Version | Progress | Documents |",
        "| --- | --- | --- | --- |",
    ]
    for identifier, item in state["projects"].items():
        marks = item.get("milestones", {})
        progress = f"{sum(m['state'] == 'ready' for m in marks.values())} ready / {sum(m['state'] == 'accepted' for m in marks.values())} accepted"
        review = item.get("pending_review")
        if review:
            progress += f"; [review]({review['file'].removeprefix('docs/')})"
        lines.append(
            f"| {identifier}{' (selected)' if identifier == state['active_project'] else ''} | V{item['version']} | {progress} | [current]({item['docs'].removeprefix('docs/')}/) |"
        )
        living = root / "docs/projects" / identifier / "living/status.md"
        living.parent.mkdir(parents=True, exist_ok=True)
        living.write_text(
            f"# {item['title']}\n\nVersion: V{item['version']}\n\n{progress}\n\n[Current documents]({Path(os.path.relpath(root / item['docs'], living.parent)).as_posix()}/)\n",
            encoding="utf-8",
        )
    (root / "docs/index.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def save(root, state):
    validate_state(state)
    write(root / "workspace.json", state)
    dashboard(root, state)


def install(root, name, source=None):
    state = config(root)
    original = read(root / "workspace.json")
    if state.get("job"):
        if state["job"]["name"] != name:
            raise ValueError(
                "A Job already exists; resume it instead of replacing its improvements"
            )
        folder = job_folder(root, state)
        validate_package(folder)
        if state["job"]["status"] == "initializing":
            sync(root)
            resume_job_documents(root, state["job"])
            save(root, state)
        return {"job": state["job"], "resumed": True}
    slug(name)
    origin = Path(source).resolve() if source else within(root, f"registry/{name}")
    info = validate_package(origin)
    if info["name"] != name:
        raise ValueError("Source Skill name does not match requested Job")
    destination = within(root, f"job/{name}")
    journal = root / ".moom/local/install.json"
    pending = read(journal) if journal.exists() else None
    existing = [p for p in (root / "job").iterdir() if p.is_dir()]
    recovered = False
    if existing:
        if existing != [destination] or not pending or pending["name"] != name:
            raise ValueError(
                "Existing Job files need recovery; refusing to overwrite them"
            )
        info = validate_package(destination)
        recovered = True
    before = (
        read(root / ".moom/generated.json")
        if (root / ".moom/generated.json").exists()
        else {}
    )
    state["job"] = {
        "name": name,
        "version": info["version"],
        "status": "initializing",
        "origin": {
            "kind": "local" if source else "embedded",
            "name": name,
            "version": info["version"],
            "sha256": tree_sha(origin),
        },
    }
    if recovered:
        state["job"]["origin"] = pending["origin"]
    else:
        write(journal, {"name": name, "origin": state["job"]["origin"]})
        # Same-filesystem rename makes package placement atomic. The journal
        # identifies a placed package if execution stops before state is saved.
        with tempfile.TemporaryDirectory(
            prefix="install-", dir=journal.parent
        ) as temporary:
            staged = Path(temporary) / name
            shutil.copytree(
                origin, staged, ignore=shutil.ignore_patterns("__pycache__", "*.pyc")
            )
            validate_package(staged)
            staged.replace(destination)
    generated_before = {
        key: within(root, key).read_bytes() if within(root, key).is_file() else None
        for key in set(before) | set(wrappers(root, state)) | {".moom/generated.json"}
    }
    try:
        # sync checks collisions before writing; keep originals for failed writes too.
        write(root / "workspace.json", state)
        sync(root)
        resume_job_documents(root, state["job"])
        write(root / "workspace.json", state)
        dashboard(root, state)
    except BaseException:
        for generated, content in generated_before.items():
            path = within(root, generated)
            if content is None:
                path.unlink(missing_ok=True)
            else:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(content)
        if not recovered:
            shutil.rmtree(destination)
        write(root / "workspace.json", original)
        raise
    journal.unlink(missing_ok=True)
    return {
        "job": state["job"],
        "next": "Adapt the recipe, create the first Project, verify-job, then finish-job. Catalog retained.",
    }


def resume_job_documents(root, job):
    if job.get("docs"):
        return
    destination = version_path(root / "docs/job", job["version"])
    if (destination / "version.json").exists():
        entry = read(destination / "version.json")
        if entry["version"] != job["version"]:
            raise ValueError(
                "Job setup documents have a different version; preserve and reconcile them"
            )
        job["docs"] = destination.relative_to(root).as_posix()
    else:
        open_version(
            root,
            job,
            root / "docs/job",
            job["version"],
            "Adapt this reusable Job through the first actual Project.",
        )


def verify_job(root, script):
    state = config(root)
    folder = job_folder(root, state)
    validate_package(folder)
    helper = within(folder, script)
    if (
        not helper.is_file()
        or helper.suffix != ".py"
        or not helper.is_relative_to(folder / "scripts")
    ):
        raise ValueError(
            "Use a reviewed Python smoke operation under the active Job's scripts/"
        )
    before = tree_sha(folder)
    result = subprocess.run(
        [sys.executable, str(helper)],
        cwd=root,
        env={
            **os.environ,
            "MOOM_WORKSPACE": str(root),
            "MOOM_JOB": str(folder),
            "MOOM_PROJECT": state.get("active_project") or "",
        },
        capture_output=True,
        text=True,
        timeout=120,
        check=False,
    )
    if result.returncode or tree_sha(folder) != before:
        raise ValueError(
            f"Representative operation failed or changed the recipe: {result.stderr[-2000:]}"
        )
    sync(root, check=True)
    state["job"]["verified_digest"] = before
    write(
        root / ".moom/local/setup-check.json",
        {
            "job_sha256": before,
            "script": script,
            "stdout": result.stdout,
            "checked_at": now(),
        },
    )
    save(root, state)
    return {"verified": before, "output": result.stdout.strip()}


def finish_job(root):
    state = config(root)
    folder = job_folder(root, state)
    validate_package(folder)
    if state["job"]["status"] != "ready" and state["job"].get(
        "verified_digest"
    ) != tree_sha(folder):
        raise ValueError(
            "Verify the adapted Job's representative operation before catalog cleanup"
        )
    if not state.get("first_project"):
        raise ValueError("Create the first real Project before finishing Job setup")
    sync(root, check=True)
    state["job"]["status"] = "ready"
    # Persist usable setup before cleanup. A failed deletion is resumable.
    save(root, state)
    catalog = root / "registry"
    if catalog.exists():
        if catalog.is_symlink():
            raise ValueError("Refusing to clean up a symlinked catalog")
        shutil.rmtree(catalog)
    state["catalog_removed"] = True
    save(root, state)
    return {"job": state["job"]["name"], "catalog_removed": True}


def target_entity(root, state, target, identifier=None):
    if target == "project":
        identifier = identifier or state.get("active_project")
        if identifier not in state["projects"]:
            raise ValueError("Choose an existing Project")
        return state["projects"][identifier], root / "docs/projects" / identifier
    if target == "job":
        job_folder(root, state)
        return state["job"], root / "docs/job"
    if target == "workspace":
        return state["workspace"], root / "docs/workspace"
    raise ValueError(
        "Select project, job or workspace; unknown scope must be asked in chat first"
    )


def open_version(root, entity, base, number, note, primary=None):
    number = version(number)
    destination = version_path(base, number)
    if (destination / "version.json").exists():
        raise ValueError("Version already initialized; preserve its history")
    if primary:
        source = within(root, primary)
        if (
            source.parent != destination
            or not re.fullmatch(r"01-[\w-]+\.md", source.name)
            or not source.is_file()
            or len(list(destination.glob("01-*.md"))) != 1
        ):
            raise ValueError(
                "Adopt exactly one owner-prepared 01-*.md in the target version folder"
            )
    else:
        if destination.exists() and any(destination.iterdir()):
            raise ValueError(
                "Prepared input exists; adopt its primary file with --input"
            )
        destination.mkdir(parents=True, exist_ok=True)
        source = destination / "01-request.md"
        source.write_text(f"# Requested change\n\n{note}\n", encoding="utf-8")
    change = {
        "file": source.relative_to(root).as_posix(),
        "sha256": sha(source),
        "entry_mode": "owner-prepared" if primary else "agent-assisted",
    }
    write(
        destination / "version.json",
        {
            "version": number,
            "status": "draft",
            "change_input": change,
            "created_at": now(),
        },
    )
    entity["version"] = number
    entity["docs"] = destination.relative_to(root).as_posix()
    entity["milestones"] = {}
    entity.pop("pending_review", None)
    entity.pop("review_history", None)
    return {"version": number, "docs": entity["docs"], "change_input": change}


def new_project(root, name, title=None, first=False):
    state = config(root)
    job_folder(root, state)
    if first and state.get("first_project"):
        state["active_project"] = state["first_project"]
        save(root, state)
        return {"project": state["first_project"], "resumed": True}
    slug(name)
    count = max([int(p.split("-", 1)[0]) for p in state["projects"]] + [0]) + 1
    identifier = f"{count:03d}-{name}"
    physical = within(root, f"projects/{identifier}")
    if physical.exists():
        raise ValueError("Project already exists; refusing to overwrite its files")
    for directory in ("inputs", "src", "dist"):
        (physical / directory).mkdir(parents=True)
    item = {
        "id": identifier,
        "title": title or identifier,
        "created_at": now(),
        "job_observed": tree_sha(job_folder(root, state)),
    }
    open_version(
        root,
        item,
        root / "docs/projects" / identifier,
        "0.1.0",
        "First real result: record the intended outcome and input here.",
    )
    (physical / "README.md").write_text(
        f"# {item['title']}\n\nInputs: inputs/ · editable source: src/ · generated output: dist/\n\n[Discussions](../../docs/projects/{identifier}/)\n",
        encoding="utf-8",
    )
    (physical / "roadmap.md").write_text(
        "# Roadmap\n\nRecord later candidates here. A roadmap entry does not authorize implementation.\n",
        encoding="utf-8",
    )
    state["projects"][identifier] = item
    state["active_project"] = identifier
    if not state.get("first_project"):
        state["first_project"] = identifier
    save(root, state)
    return {"project": identifier, "docs": item["docs"], "job": state["job"]["name"]}


def iterate(root, target, number, note, identifier=None, primary=None):
    state = config(root)
    entity, base = target_entity(root, state, target, identifier)
    if version_key(number) <= version_key(entity["version"]):
        raise ValueError("The new version must be greater than the current version")
    previous = dict(entity)
    if target == "project":
        snapshot = version_path(root / "projects" / entity["id"], previous["version"])
        if snapshot.exists():
            raise ValueError(
                "Previous source snapshot already exists; preserve history"
            )
    result = open_version(root, entity, base, number, note, primary)
    if target == "project":
        physical = root / "projects" / entity["id"]
        snapshot = version_path(physical, previous["version"])
        snapshot.mkdir(parents=True)
        for path in physical.iterdir():
            if path.name in (
                "versions",
                "dist",
                ".git",
                "secrets",
                "node_modules",
                ".venv",
                "__pycache__",
            ) or path.name.startswith(".env"):
                continue
            if path.is_symlink():
                raise ValueError(
                    "Resolve source symlinks before snapshotting a Project"
                )
            if path.is_dir():
                shutil.copytree(
                    path,
                    snapshot / path.name,
                    ignore=shutil.ignore_patterns(
                        ".git",
                        "secrets",
                        "node_modules",
                        ".venv",
                        "__pycache__",
                        ".env",
                        ".env.*",
                    ),
                )
            elif path.is_file():
                shutil.copy2(path, snapshot / path.name)
        result["previous_source"] = snapshot.relative_to(root).as_posix()
    if target == "job":
        # Opening discussions does not publish or relabel the working recipe.
        entity["candidate_version"] = entity["version"]
        entity["version"] = previous["version"]
    if previous.get("docs"):
        write(root / previous["docs"] / "state-at-close.json", previous)
    save(root, state)
    return result


def review_round(root, target, title, before, identifier=None):
    state = config(root)
    entity, _ = target_entity(root, state, target, identifier)
    if not entity.get("docs"):
        raise ValueError("Open an entity version before creating a review")
    if entity.get("pending_review"):
        raise ValueError("Resolve the submitted round before opening another")
    folder = within(root, entity["docs"])
    number = (
        max(
            [int(p.name.split("-", 1)[0]) for p in folder.glob("[0-9]*-review.md")]
            + [0]
        )
        + 1
    )
    path = folder / f"{number:03d}-review.md"
    path.write_text(
        f"# {title}\n\nDependent step: {before}\n\n## Questions\n\nAdd only material unresolved choices; give 2–3 options with one Recommended and an empty Answer field.\n\n## Uncertain decisions\n\nState the proposal, uncertainty, and an empty Confirmation / override field.\n\n## Result to inspect\n\nLink the actual revision and explain changed decisions; keep full documents available.\n",
        encoding="utf-8",
    )
    entity["pending_review"] = {
        "file": path.relative_to(root).as_posix(),
        "state": "waiting",
        "before": before,
    }
    save(root, state)
    return entity["pending_review"]


def issue(root, target, title, identifier=None):
    state = config(root)
    if target in ("moom", "intake"):
        folder = (
            root
            / "docs/workspace"
            / ("moom-feedback" if target == "moom" else "intake")
        )
    else:
        entity, _ = target_entity(root, state, target, identifier)
        if not entity.get("docs"):
            _, base = target_entity(root, state, target, identifier)
            open_version(
                root,
                entity,
                base,
                entity["version"],
                "Track the current entity's changes and defects.",
            )
            save(root, state)
        folder = within(root, entity["docs"])
    folder.mkdir(parents=True, exist_ok=True)
    number = (
        max(
            [int(p.name.split("-", 1)[0]) for p in folder.glob("[0-9]*-issue.md")] + [0]
        )
        + 1
    )
    path = folder / f"{number:03d}-issue.md"
    path.write_text(
        f"# {title}\n\nOwner: {target}\n\n## Observed result and expected outcome\n\n## Diagnosis and related fixes\n\nKeep the correction with its owner; link related Job or engine changes.\n\n## Verification\n",
        encoding="utf-8",
    )
    return {"file": path.relative_to(root).as_posix(), "target": target}


def record(root, step, artifact, accepted=False, evidence=None):
    state = config(root)
    entity, _ = target_entity(root, state, "project")
    path = within(root, artifact)
    if not path.is_file():
        raise ValueError("Record a concrete artifact file")
    if accepted and not evidence:
        raise ValueError(
            "Human acceptance requires evidence of approval of this revision"
        )
    entity["milestones"][slug(step)] = {
        "artifact": path.relative_to(root).as_posix(),
        "sha256": sha(path),
        "state": "accepted" if accepted else "ready",
        "evidence": evidence,
        "job_revision": tree_sha(job_folder(root, state)),
        "at": now(),
    }
    save(root, state)
    return entity["milestones"][step]


def engine_path(name):
    path = Path(name)
    if path.is_absolute() or ".." in path.parts:
        return False
    return name in {
        "VERSION",
        "moom.py",
        "AGENTS.md",
        "CLAUDE.md",
        "GEMINI.md",
        "README.md",
        ".gitignore",
        ".gitattributes",
        "LICENSE",
        "tools/release.py",
    } or name.startswith((".moom/core/", "docs/moom/"))


def release_manifest(source):
    value = read(source / ".moom/release.json")
    if value.get("schema") != 1:
        raise ValueError("Unsupported release schema")
    version(value["version"])
    for name, checksum in value["engine"].items():
        if not engine_path(name) or sha(within(source, name)) != checksum:
            raise ValueError(f"Invalid engine release path or hash: {name}")
    for name, checksum in value["bootstrap"].items():
        if not name.startswith("registry/") or sha(within(source, name)) != checksum:
            raise ValueError(f"Invalid bootstrap release path or hash: {name}")
    return value


def update(root, source, apply=False, resolutions=None):
    source = Path(source).resolve()
    incoming = release_manifest(source)
    baseline = read(root / ".moom/managed.json")
    state = config(root)
    if incoming["workspace_schema"] != state["schema"]:
        raise ValueError("This release needs a structured workspace schema migration")
    if version_key(incoming["version"]) <= version_key(baseline["version"]):
        raise ValueError("Choose a newer, pinned Moom release")
    changes, conflicts, selected = [], [], {}
    groups = ["engine"] + (
        [] if state.get("job") or state.get("catalog_removed") else ["bootstrap"]
    )
    for group in groups:
        old = baseline[group]
        new = incoming[group]
        for name in sorted(set(old) | set(new)):
            if not (
                engine_path(name) if group == "engine" else name.startswith("registry/")
            ):
                raise ValueError(f"Invalid installed baseline ownership: {name}")
            local = sha(within(root, name))
            if local == new.get(name):
                continue
            # Local modifications survive when upstream has not changed this file.
            if old.get(name) == new.get(name):
                continue
            if local != old.get(name):
                resolution = (
                    within(Path(resolutions).resolve(), name) if resolutions else None
                )
                if resolution and resolution.is_file() and name in new:
                    selected[name] = resolution
                else:
                    conflicts.append(
                        {
                            "file": name,
                            "baseline": old.get(name),
                            "local": local,
                            "upstream": new.get(name),
                        }
                    )
                    continue
            else:
                selected[name] = within(source, name) if name in new else None
            changes.append(name)
    plan = {
        "from": baseline["version"],
        "to": incoming["version"],
        "files": changes,
        "conflicts": conflicts,
        "catalog_skipped": "bootstrap" not in groups,
    }
    if not apply:
        return plan
    if conflicts:
        raise ValueError(
            "Semantic reconciliation required; no update applied: "
            + ", ".join(c["file"] for c in conflicts)
        )
    sync(root, check=True)
    checkpoint = root / ".moom/local/updates" / uuid.uuid4().hex
    affected = set(changes) | {
        ".moom/release.json",
        ".moom/managed.json",
        ".moom/generated.json",
    }
    affected.update(read(root / ".moom/generated.json"))
    affected.update(wrappers(root, state))
    restore = {}
    for name in affected:
        path = within(root, name)
        restore[name] = sha(path)
        if path.is_file():
            backup = within(checkpoint / "files", name)
            backup.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(path, backup)
    write(
        checkpoint / "checkpoint.json",
        {"before": restore, "plan": plan, "status": "prepared"},
    )
    try:
        for name, item in selected.items():
            destination = within(root, name)
            if item is None:
                destination.unlink(missing_ok=True)
            else:
                destination.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(item, destination)
        write(root / ".moom/release.json", incoming)
        write(root / ".moom/managed.json", incoming)
        # Execute the NEW helper so changed adapter generation is checked too.
        subprocess.run(
            [sys.executable, str(root / "moom.py"), "--workspace", str(root), "sync"],
            capture_output=True,
            text=True,
            check=True,
            timeout=60,
        )
        subprocess.run(
            [sys.executable, str(root / "moom.py"), "--workspace", str(root), "check"],
            capture_output=True,
            text=True,
            check=True,
            timeout=60,
        )
    except BaseException:
        for name, checksum in restore.items():
            target = within(root, name)
            if checksum is None:
                target.unlink(missing_ok=True)
            else:
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(within(checkpoint / "files", name), target)
        write(
            checkpoint / "checkpoint.json",
            {"before": restore, "plan": plan, "status": "rolled-back"},
        )
        raise
    write(
        checkpoint / "checkpoint.json",
        {
            "before": restore,
            "plan": plan,
            "status": "applied",
            "after": {name: sha(within(root, name)) for name in affected},
        },
    )
    return {
        **plan,
        "applied": True,
        "checkpoint": checkpoint.relative_to(root).as_posix(),
    }


def check(root):
    state = config(root)
    validate_state(state)
    sync(root, check=True)
    stale = []
    if state.get("job"):
        validate_package(job_folder(root, state))
    if state.get("catalog_removed") and (root / "registry").exists():
        raise ValueError(
            "A completed Kandoo must not have its bootstrap catalog restored"
        )
    for identifier, item in state["projects"].items():
        within(root, f"projects/{identifier}")
        entry = read(within(root, item["docs"]) / "version.json")
        if entry["version"] != item["version"]:
            raise ValueError(
                "Version records disagree; use iterate instead of relabeling state"
            )
        primary = entry["change_input"]
        if sha(within(root, primary["file"])) != primary["sha256"]:
            raise ValueError(
                "Primary input changed; reread it and explicitly refresh its recorded hash"
            )
        for step, mark in item.get("milestones", {}).items():
            if sha(within(root, mark["artifact"])) != mark["sha256"]:
                stale.append(f"{identifier}/{step}")
    if stale:
        raise ValueError(
            "Artifact receipts are stale; review the changed revision: "
            + ", ".join(stale)
        )
    return {"ok": True, "projects": len(state["projects"]), "job": state.get("job")}


def export_job(root, output):
    state = config(root)
    folder = job_folder(root, state)
    info = validate_package(folder)
    destination = Path(output).resolve()
    if destination.is_relative_to(folder):
        raise ValueError("Export outside the reusable Job directory")
    destination.parent.mkdir(parents=True, exist_ok=True)
    entries = files(folder)
    with zipfile.ZipFile(destination, "w", zipfile.ZIP_DEFLATED) as archive:
        for name in entries:
            archive.write(folder / name, f"{folder.name}/{name}")
        archive.writestr(
            "manifest.json",
            json.dumps(
                {**info, "origin": state["job"]["origin"], "sha256": entries},
                ensure_ascii=False,
                indent=2,
            ),
        )
    return {
        "archive": str(destination),
        "sha256": sha(destination),
        "files": len(entries),
        "publication": "Submit for owner review; this does not publish to the catalog.",
    }


def acknowledge_input(root, target, identifier=None):
    state = config(root)
    entity, _ = target_entity(root, state, target, identifier)
    path = within(root, entity["docs"]) / "version.json"
    entry = read(path)
    entry["change_input"]["sha256"] = sha(within(root, entry["change_input"]["file"]))
    if not entry["change_input"]["sha256"]:
        raise ValueError("Primary input is missing")
    entry["input_reread_at"] = now()
    write(path, entry)
    return entry["change_input"]


def adopt_job(root, note):
    state = config(root)
    entity, _ = target_entity(root, state, "project")
    entity["job_observed"] = tree_sha(job_folder(root, state))
    entity.setdefault("job_adaptations", []).append(
        {"note": note, "sha256": entity["job_observed"], "at": now()}
    )
    save(root, state)
    return {"project": entity["id"], "job_sha256": entity["job_observed"], "note": note}


def job_revision(root, note):
    state = config(root)
    folder = job_folder(root, state)
    info = validate_package(folder)
    job = state["job"]
    if version_key(info["version"]) <= version_key(job["version"]):
        raise ValueError(
            "Update the Skill metadata.version after verifying the changed recipe"
        )
    if job.get("candidate_version") != info["version"]:
        raise ValueError(
            "Open the matching Job iteration before recording its revision"
        )
    if job.get("verified_digest") != tree_sha(folder):
        raise ValueError("Verify the current recipe's representative operation first")
    entry = read(within(root, job["docs"]) / "version.json")
    entry.update(status="recorded", note=note, job_sha256=tree_sha(folder))
    write(within(root, job["docs"]) / "version.json", entry)
    job["version"] = info["version"]
    job.pop("candidate_version", None)
    save(root, state)
    return {"job": info["name"], "version": info["version"], "note": note}


def parser():
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("--workspace", type=Path, default=ROOT)
    commands = cli.add_subparsers(dest="command", required=True)
    commands.add_parser("status")
    commands.add_parser("check")
    p = commands.add_parser("sync")
    p.add_argument("--check", action="store_true")
    p = commands.add_parser("catalog")
    p.add_argument("query", nargs="?", default="")
    p = commands.add_parser("install")
    p.add_argument("name")
    p.add_argument("--source")
    p = commands.add_parser("verify-job")
    p.add_argument("--smoke", required=True)
    commands.add_parser("finish-job")
    p = commands.add_parser("new")
    p.add_argument("slug")
    p.add_argument("--title")
    p.add_argument("--first", action="store_true")
    p = commands.add_parser("switch")
    p.add_argument("project")
    p = commands.add_parser("procedure")
    p.add_argument("step")
    p = commands.add_parser("run")
    p.add_argument("helper")
    p.add_argument("arguments", nargs=argparse.REMAINDER)
    p = commands.add_parser("iterate")
    p.add_argument("--target", choices=["project", "job", "workspace"], required=True)
    p.add_argument("--project")
    p.add_argument("--version", required=True)
    p.add_argument("--note", required=True)
    p.add_argument("--input")
    p = commands.add_parser("review-round")
    p.add_argument("--target", choices=["project", "job", "workspace"], required=True)
    p.add_argument("--project")
    p.add_argument("--title", required=True)
    p.add_argument("--before", required=True)
    p = commands.add_parser("resolve-review")
    p.add_argument("--target", choices=["project", "job", "workspace"], required=True)
    p.add_argument("--project")
    p.add_argument("--note", required=True)
    p = commands.add_parser("issue")
    p.add_argument("title")
    p.add_argument(
        "--target",
        choices=["project", "job", "workspace", "moom", "intake"],
        required=True,
    )
    p.add_argument("--project")
    p = commands.add_parser("record")
    p.add_argument("step")
    p.add_argument("--artifact", required=True)
    p.add_argument("--accepted", action="store_true")
    p.add_argument("--evidence")
    p = commands.add_parser("update")
    p.add_argument("--source", required=True)
    p.add_argument("--apply", action="store_true")
    p.add_argument("--resolution-dir")
    p = commands.add_parser("export-job")
    p.add_argument("--output", required=True)
    p = commands.add_parser("acknowledge-input")
    p.add_argument("--target", choices=["project", "job", "workspace"], required=True)
    p.add_argument("--project")
    p = commands.add_parser("adopt-job")
    p.add_argument("--note", required=True)
    p = commands.add_parser("job-revision")
    p.add_argument("--note", required=True)
    return cli


def main():
    args = parser().parse_args()
    root = args.workspace.resolve()
    try:
        if args.command == "status":
            state = config(root)
            result = {
                "engine": (root / "VERSION").read_text().strip(),
                "workspace": state,
            }
            if state.get("job"):
                result["current_job_sha256"] = tree_sha(job_folder(root, state))
                result["projects_needing_job_adaptation_check"] = [
                    name
                    for name, item in state["projects"].items()
                    if item.get("job_observed") != result["current_job_sha256"]
                ]
        elif args.command == "check":
            result = check(root)
        elif args.command == "sync":
            result = sync(root, args.check)
        elif args.command == "catalog":
            index = root / "registry/index.json"
            result = (
                [
                    p
                    for p in read(index)["jobs"]
                    if args.query.lower()
                    in (p["name"] + " " + p["description"]).lower()
                ]
                if index.exists()
                else []
            )
        elif args.command == "install":
            result = install(root, args.name, args.source)
        elif args.command == "verify-job":
            result = verify_job(root, args.smoke)
        elif args.command == "finish-job":
            result = finish_job(root)
        elif args.command == "new":
            result = new_project(root, args.slug, args.title, args.first)
        elif args.command == "switch":
            state = config(root)
            if args.project not in state["projects"]:
                raise ValueError("Unknown Project")
            state["active_project"] = args.project
            save(root, state)
            result = {
                "project": args.project,
                "job": state["job"],
                "adaptation_check_required": state["projects"][args.project][
                    "job_observed"
                ]
                != tree_sha(job_folder(root, state)),
            }
        elif args.command == "procedure":
            folder = job_folder(root, config(root))
            target = within(folder, f"commands/{slug(args.step)}.md")
            if not target.is_file():
                raise ValueError("Unknown Job procedure")
            result = {
                "procedure": target.relative_to(root).as_posix(),
                "text": target.read_text(encoding="utf-8"),
                "job_sha256": tree_sha(folder),
            }
        elif args.command == "run":
            state = config(root)
            folder = job_folder(root, state)
            path = within(folder, args.helper)
            if (
                not path.is_file()
                or path.suffix != ".py"
                or not path.is_relative_to(folder / "scripts")
            ):
                raise ValueError(
                    "Choose a reviewed active Job Python helper under scripts/"
                )
            result = subprocess.run(
                [sys.executable, str(path), *args.arguments],
                cwd=root,
                env={
                    **os.environ,
                    "MOOM_WORKSPACE": str(root),
                    "MOOM_JOB": str(folder),
                    "MOOM_PROJECT": state.get("active_project") or "",
                },
                check=False,
            )
            return result.returncode
        elif args.command == "iterate":
            result = iterate(
                root, args.target, args.version, args.note, args.project, args.input
            )
        elif args.command == "review-round":
            result = review_round(
                root, args.target, args.title, args.before, args.project
            )
        elif args.command == "resolve-review":
            state = config(root)
            entity, _ = target_entity(root, state, args.target, args.project)
            pending = entity.pop("pending_review", None)
            if not pending:
                raise ValueError("No pending review")
            entity.setdefault("review_history", []).append(
                {**pending, "state": "answered", "note": args.note, "at": now()}
            )
            save(root, state)
            result = {
                "answered": pending["file"],
                "acceptance": "Recorded separately for the actual artifact revision",
            }
        elif args.command == "issue":
            result = issue(root, args.target, args.title, args.project)
        elif args.command == "record":
            result = record(
                root, args.step, args.artifact, args.accepted, args.evidence
            )
        elif args.command == "update":
            result = update(root, args.source, args.apply, args.resolution_dir)
        elif args.command == "export-job":
            result = export_job(root, args.output)
        elif args.command == "acknowledge-input":
            result = acknowledge_input(root, args.target, args.project)
        elif args.command == "adopt-job":
            result = adopt_job(root, args.note)
        elif args.command == "job-revision":
            result = job_revision(root, args.note)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except (ValueError, OSError, KeyError, subprocess.SubprocessError) as error:
        print(f"Moom: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
