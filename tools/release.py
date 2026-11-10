#!/usr/bin/env python3
"""Compile and verify a pristine public Moom template using an explicit allowlist."""

import argparse
import importlib.util
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("moom_core", ROOT / ".moom/core/moom.py")
core = importlib.util.module_from_spec(spec)
spec.loader.exec_module(core)

ENGINE_FILES = [
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
]
ENGINE_TREES = [".moom/core", "docs/moom"]
SOURCE_FILES = [
    "CONTRIBUTING.md",
    "workspace.json",
    "job/.gitkeep",
    "projects/.gitkeep",
    "shared/.gitkeep",
    "docs/index.md",
    "docs/job/living/README.md",
    "docs/workspace/living/README.md",
    ".moom/release.json",
    ".moom/managed.json",
    ".moom/generated.json",
    ".github/workflows/check.yml",
]


def manifest():
    engine = {name: core.sha(ROOT / name) for name in ENGINE_FILES}
    for tree in ENGINE_TREES:
        engine.update(
            {
                f"{tree}/{name}": checksum
                for name, checksum in core.files(ROOT / tree).items()
            }
        )
    bootstrap = {
        f"registry/{name}": checksum
        for name, checksum in core.files(ROOT / "registry").items()
    }
    return {
        "schema": 1,
        "workspace_schema": 1,
        "version": core.version((ROOT / "VERSION").read_text().strip()),
        "repository": "https://github.com/gonbad/moom",
        "engine": engine,
        "bootstrap": bootstrap,
        "bootstrap_policy": "omit after a Job exists; never restore a removed catalog",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    state = core.config(ROOT)
    if (
        state["job"]
        or state["projects"]
        or state["profile"]
        or state["catalog_removed"]
    ):
        raise ValueError("Publish the pristine template, not a configured Kandoo")
    if any(p.is_dir() for p in (ROOT / "job").iterdir()) or any(
        p.is_dir() for p in (ROOT / "projects").iterdir()
    ):
        raise ValueError(
            "Public template must not contain installed Jobs or Project data"
        )
    catalog = core.read(ROOT / "registry/index.json")
    for entry in catalog["jobs"]:
        info = core.validate_package(ROOT / "registry" / entry["name"])
        if info["version"] != entry["version"]:
            raise ValueError("Catalog and recipe versions disagree")
    core.sync(ROOT, check=args.check)
    value = manifest()
    if any(checksum is None for checksum in value["engine"].values()):
        raise ValueError("Missing required engine source")
    if args.check:
        if value != core.read(ROOT / ".moom/release.json") or value != core.read(
            ROOT / ".moom/managed.json"
        ):
            raise ValueError("Release manifest is stale; compile before publishing")
    else:
        core.dashboard(ROOT, state)
        core.write(ROOT / ".moom/release.json", value)
        core.write(ROOT / ".moom/managed.json", value)
    core.release_manifest(ROOT)
    core.check(ROOT)
    if args.output:
        allowed = (
            set(value["engine"])
            | set(value["bootstrap"])
            | set(SOURCE_FILES)
            | set(core.read(ROOT / ".moom/generated.json"))
        )
        allowed.update("tests/" + name for name in core.files(ROOT / "tests"))
        args.output.parent.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(args.output, "w", zipfile.ZIP_DEFLATED) as archive:
            for name in sorted(allowed):
                path = core.within(ROOT, name)
                if not path.is_file():
                    raise ValueError(f"Missing allowlisted public file: {name}")
                archive.write(path, name)
    print(
        f"Moom {value['version']}: compiled commands, pristine state and release hashes verified."
    )


if __name__ == "__main__":
    try:
        main()
    except (ValueError, OSError) as error:
        print(error, file=sys.stderr)
        raise SystemExit(1)
