#!/usr/bin/env python3
"""Resolve and initialize only the selected Moom Project's directories."""
from __future__ import annotations

import argparse
import json
import os
import re
from pathlib import Path


def confined(root, relative):
    relative = Path(relative)
    if relative.is_absolute() or ".." in relative.parts:
        raise ValueError("Project paths must stay relative to the workspace")
    target = (root / relative).resolve()
    if not target.is_relative_to(root):
        raise ValueError("Project path escapes the workspace")
    if target != root / relative:
        raise ValueError("Project paths must not traverse symlinks")
    return target


def context(workspace):
    root = Path(workspace).resolve()
    state = json.loads((root / "workspace.json").read_text(encoding="utf-8"))
    identifier = state.get("active_project")
    if not isinstance(identifier, str) or not re.fullmatch(r"[0-9]{3,}-[a-z0-9-]+", identifier):
        raise ValueError("Select a real Moom Project first")
    item = state.get("projects", {}).get(identifier)
    if not item or item.get("id") != identifier:
        raise ValueError("Selected Project is absent from workspace state")
    project = confined(root, f"projects/{identifier}")
    doc_root = confined(root, f"docs/projects/{identifier}")
    version = confined(root, item["docs"])
    if not version.is_relative_to(doc_root / "versions"):
        raise ValueError("Version dossier belongs to another Project")
    values = {
        "PROJECT_ID": identifier,
        "PROJECT": project,
        "SOURCE": confined(root, f"projects/{identifier}/src"),
        "LIVING": confined(root, f"docs/projects/{identifier}/living"),
        "VERSION": version,
        "EXISTING": confined(root, f"projects/{identifier}/existing_product"),
        "DESIGN": confined(root, f"projects/{identifier}/design"),
        "EVIDENCE": confined(root, f"projects/{identifier}/evidence"),
        "DEPLOY": confined(root, f"projects/{identifier}/src/deploy"),
    }
    return values


def initialize(workspace):
    values = context(workspace)
    for key, path in values.items():
        if key != "PROJECT_ID":
            path.mkdir(parents=True, exist_ok=True)
    return values


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=("paths", "init"), nargs="?", default="paths")
    parser.add_argument("--workspace", type=Path, default=Path(os.environ.get("MOOM_WORKSPACE", Path(__file__).resolve().parents[3])))
    args = parser.parse_args()
    values = initialize(args.workspace) if args.action == "init" else context(args.workspace)
    print(json.dumps({key: str(value) for key, value in values.items()}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    try:
        main()
    except (ValueError, KeyError, OSError) as error:
        raise SystemExit(str(error))
