#!/usr/bin/env python3
"""Build and aggregate blog posts into a static dist directory."""

import argparse
import json
import shutil
from pathlib import Path


def build_post(project_dir, dist_dir):
    site_dir = project_dir / "site"
    if not site_dir.exists():
        site_dir = project_dir
    dist_dir.mkdir(parents=True, exist_ok=True)
    for item in site_dir.iterdir():
        if item.name.startswith(".") or item.name in ("dist", "__pycache__"):
            continue
        dest = dist_dir / item.name
        if item.is_dir():
            if dest.exists():
                shutil.rmtree(dest)
            shutil.copytree(item, dest)
        else:
            shutil.copy2(item, dest)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", type=Path, help="Specific project directory to build")
    parser.add_argument("--output", type=Path, default=Path("dist"), help="Output directory")
    args = parser.parse_args()

    root = Path.cwd()
    output_dir = args.output.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    if args.project:
        pdir = args.project.resolve()
        pname = pdir.name
        build_post(pdir, output_dir / pname)
        print(f"Built project {pname} to {output_dir / pname}")
    else:
        projects_dir = root / "projects"
        if projects_dir.is_dir():
            for pdir in sorted(projects_dir.iterdir()):
                if pdir.is_dir() and not pdir.name.startswith("."):
                    target = output_dir if pdir.name == "000-index" else output_dir / pdir.name
                    build_post(pdir, target)
        print(f"Built blog to {output_dir}")


if __name__ == "__main__":
    main()
