#!/usr/bin/env python3
"""Run the bundled Moom helper; no package installation is required."""

import runpy
from pathlib import Path

if __name__ == "__main__":
    runpy.run_path(
        str(Path(__file__).resolve().parent / ".moom/core/moom.py"), run_name="__main__"
    )
