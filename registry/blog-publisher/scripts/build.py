#!/usr/bin/env python3
"""Build the configured publication and standalone offline archives."""
import argparse
import json
from pathlib import Path
from publisher import build, workspace


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workspace", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--preview", help="Include this draft in a local-only release")
    args = parser.parse_args()
    print(json.dumps(build(workspace(args.workspace), args.output, args.preview), indent=2))


if __name__ == "__main__":
    try:
        main()
    except (ValueError, OSError, KeyError) as error:
        raise SystemExit(str(error))
