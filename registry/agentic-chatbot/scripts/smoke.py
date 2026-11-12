#!/usr/bin/env python3
"""Exercise Project ownership and resume mechanics without external services."""
import json
import tempfile
from pathlib import Path

from project import initialize

with tempfile.TemporaryDirectory(prefix="software-job-smoke-") as temporary:
    root = Path(temporary)
    state = {"active_project": "001-first", "projects": {}}
    for identifier in ("001-first", "002-second"):
        state["projects"][identifier] = {"id": identifier, "docs": f"docs/projects/{identifier}/versions/V0/V0.1"}
    def select(identifier):
        state["active_project"] = identifier
        (root / "workspace.json").write_text(json.dumps(state), encoding="utf-8")
        return initialize(root)
    first = select("001-first")
    (first["LIVING"] / "prd.md").write_text("First product", encoding="utf-8")
    (first["SOURCE"] / "example.txt").write_text("First artifact", encoding="utf-8")
    second = select("002-second")
    (second["LIVING"] / "prd.md").write_text("Second product", encoding="utf-8")
    assert first["PROJECT"] != second["PROJECT"]
    assert (select("001-first")["LIVING"] / "prd.md").read_text(encoding="utf-8") == "First product"
    assert (first["SOURCE"] / "example.txt").read_text(encoding="utf-8") == "First artifact"
    state["projects"]["001-first"]["docs"] = state["projects"]["002-second"]["docs"]
    (root / "workspace.json").write_text(json.dumps(state), encoding="utf-8")
    try:
        initialize(root)
    except ValueError:
        pass
    else:
        raise AssertionError("Cross-Project dossier was accepted")
    print(json.dumps({"ok": True, "operation": "initialize two Projects, preserve first on resume, reject foreign dossier", "external_services": "not exercised"}))
