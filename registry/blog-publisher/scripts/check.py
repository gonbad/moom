#!/usr/bin/env python3
"""Verify real publication files, local references, hashes and offline archives."""
import argparse
import json
from pathlib import Path
from publisher import check_release, workspace


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workspace", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    root = workspace(args.workspace)
    print(json.dumps(check_release(args.output.resolve() if args.output else root / "dist"), indent=2))


if __name__ == "__main__":
    try:
        main()
    except (ValueError, OSError, KeyError) as error:
        raise SystemExit(str(error))
