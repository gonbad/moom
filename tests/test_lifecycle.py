"""Behavioral checks in isolated workspaces; no claims of human or UI approval."""

import importlib.util
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

SOURCE = Path(__file__).resolve().parents[1]
TEMPLATE_VERSION = (SOURCE / "VERSION").read_text(encoding="utf-8").strip()
spec = importlib.util.spec_from_file_location(
    "moom_test_core", SOURCE / ".moom/core/moom.py"
)
core = importlib.util.module_from_spec(spec)
spec.loader.exec_module(core)


class Lifecycle(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="moom-lifecycle-")
        self.addCleanup(self.temporary.cleanup)
        self.base = Path(self.temporary.name)
        self.root = self.base / "kandoo"
        self.copy_template(self.root)

    def copy_template(self, destination):
        shutil.copytree(
            SOURCE,
            destination,
            ignore=shutil.ignore_patterns(
                ".git", "__pycache__", "local", "*.pyc", "dist"
            ),
        )

    def call(self, *args, root=None, fail=False):
        target = root or self.root
        result = subprocess.run(
            [
                sys.executable,
                str(target / "moom.py"),
                "--workspace",
                str(target),
                *args,
            ],
            capture_output=True,
            text=True,
            env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"},
            check=False,
        )
        if fail:
            self.assertNotEqual(result.returncode, 0, result.stdout)
            return result
        self.assertEqual(result.returncode, 0, result.stderr)
        return json.loads(result.stdout)

    def state(self):
        return json.loads((self.root / "workspace.json").read_text())

    def setup_job(self, finish=True):
        self.call("install", "presentation-maker")
        self.call("new", "first", "--first")
        self.call("verify-job", "--smoke", "scripts/check.py")
        if finish:
            self.call("finish-job")

    def next_release(self, number="0.3.0", broken=False):
        target = self.base / "upstream"
        self.copy_template(target)
        (target / "VERSION").write_text(number + "\n")
        readme = target / "README.md"
        readme.write_text(readme.read_text() + "\nUpstream release change.\n")
        if broken:
            path = target / ".moom/core/moom.py"
            path.write_text(
                path.read_text().replace(
                    "def check(root):\n",
                    'def check(root):\n    raise ValueError("Synthetic post-update failure")\n',
                )
            )
        result = subprocess.run(
            [sys.executable, str(target / "tools/release.py")],
            capture_output=True,
            text=True,
            check=False,
        )
        # A deliberately broken release needs only the manifest for rollback tests.
        if not broken:
            self.assertEqual(result.returncode, 0, result.stderr)
        return target

    def test_setup_adaptation_cleanup_resume_and_current_job_dispatch(self):
        self.setup_job(finish=False)
        recipe = self.root / "job/presentation-maker/references/quality.md"
        recipe.write_text(
            recipe.read_text()
            + "\nLearned from Project 001: check the actual intended audience action.\n"
        )
        self.call("finish-job", fail=True)
        self.assertTrue((self.root / "registry").is_dir())
        self.call("verify-job", "--smoke", "scripts/check.py")
        self.call("finish-job")
        learned = recipe.read_bytes()
        self.assertFalse((self.root / "registry").exists())
        self.assertTrue(self.call("install", "presentation-maker")["resumed"])
        self.assertEqual(recipe.read_bytes(), learned)
        self.assertTrue(self.call("new", "other", "--first")["resumed"])
        self.assertEqual(len(self.state()["projects"]), 1)
        second = self.call("new", "second")
        self.assertEqual(second["project"], "002-second")
        helper = self.root / "job/presentation-maker/scripts/current.py"
        helper.write_text(
            'import json, os\nprint(json.dumps({"revision": "improved", "project": os.environ["MOOM_PROJECT"]}))\n'
        )
        self.call("switch", "001-first")
        result = self.call("run", "scripts/current.py")
        self.assertEqual(result, {"revision": "improved", "project": "001-first"})
        pending = self.call("status")["projects_needing_job_adaptation_check"]
        self.assertIn("001-first", pending)
        self.call(
            "adopt-job", "--note", "Checked changed helper; preserved previous outputs"
        )
        self.assertNotIn(
            "001-first", self.call("status")["projects_needing_job_adaptation_check"]
        )
        self.assertTrue(self.call("check")["ok"])

    def test_interrupted_setup_retains_catalog_and_local_improvements(self):
        self.setup_job(finish=False)
        smoke = self.root / "job/presentation-maker/scripts/check.py"
        working = smoke.read_bytes()
        smoke.write_text('raise SystemExit("Synthetic interrupted setup")\n')
        self.call("verify-job", "--smoke", "scripts/check.py", fail=True)
        self.call("finish-job", fail=True)
        self.assertTrue((self.root / "registry/index.json").exists())
        self.assertTrue(self.call("install", "presentation-maker")["resumed"])
        self.assertIn("Synthetic", smoke.read_text())
        smoke.write_bytes(working)
        self.call("verify-job", "--smoke", "scripts/check.py")
        self.call("finish-job")
        self.assertFalse((self.root / "registry").exists())

    def test_install_recovers_atomic_placement_before_state_and_missing_documents_pointer(
        self,
    ):
        source = self.root / "registry/presentation-maker"
        destination = self.root / "job/presentation-maker"
        shutil.copytree(source, destination)
        note = destination / "references/quality.md"
        note.write_text(
            note.read_text() + "\nPreserve work done before state recovery.\n"
        )
        core.write(
            self.root / ".moom/local/install.json",
            {
                "name": "presentation-maker",
                "origin": {
                    "kind": "embedded",
                    "name": "presentation-maker",
                    "version": "0.1.0",
                    "sha256": core.tree_sha(source),
                },
            },
        )
        self.call("install", "presentation-maker")
        self.assertIn("Preserve work", note.read_text())
        self.assertIsNotNone(self.state()["job"]["docs"])
        state = self.state()
        state["job"].pop("docs")
        core.write(self.root / "workspace.json", state)
        self.assertTrue(self.call("install", "presentation-maker")["resumed"])
        self.assertIn("docs/job/versions/", self.state()["job"]["docs"])
        self.assertTrue((self.root / "registry").exists())

    def test_no_matching_recipe_can_install_a_new_local_skill(self):
        self.assertEqual(self.call("catalog", "no-such-task-family"), [])
        source = self.base / "field-notes"
        (source / "scripts").mkdir(parents=True)
        (source / "SKILL.md").write_text(
            '---\nname: field-notes\ndescription: Write bounded field notes from actual observations.\nmetadata:\n  version: "0.1.0"\n---\n\nUse the actual observation and check the final notes.\n'
        )
        shutil.copy2(SOURCE / "LICENSE", source / "LICENSE")
        (source / "scripts/check.py").write_text(
            'print("Representative field-note operation")\n'
        )
        self.call("install", "field-notes", "--source", str(source))
        self.call("verify-job", "--smoke", "scripts/check.py")
        self.call("finish-job", fail=True)
        self.call("new", "observation", "--first")
        self.call("finish-job")
        self.assertEqual(self.state()["job"]["origin"]["kind"], "local")

    def test_scoping_issues_before_projects_and_independent_job_revisions(self):
        before = core.files(self.root / "docs")
        self.call("issue", "Unknown scope", fail=True)
        self.assertEqual(before, core.files(self.root / "docs"))
        self.call("install", "presentation-maker")
        report = self.call(
            "issue", "Recipe defect before any Project", "--target", "job"
        )
        self.assertIn("docs/job/versions/V0/V0.1/", report["file"])
        self.assertFalse(self.state()["projects"])
        draft = self.call(
            "iterate",
            "--target",
            "job",
            "--version",
            "0.2.0",
            "--note",
            "Improve the method",
        )
        self.assertEqual(draft["version"], "0.2.0")
        self.assertEqual(self.state()["job"]["version"], "0.1.0")
        skill = self.root / "job/presentation-maker/SKILL.md"
        skill.write_text(
            skill.read_text().replace('version: "0.1.0"', 'version: "0.2.0"')
        )
        self.call("job-revision", "--note", "Not verified", fail=True)
        self.call("verify-job", "--smoke", "scripts/check.py")
        self.call("job-revision", "--note", "Verified revised recipe")
        self.assertEqual(self.state()["job"]["version"], "0.2.0")
        shared = self.call("issue", "Shared code defect", "--target", "workspace")
        self.assertIn("docs/workspace/versions/V0/V0.1/", shared["file"])

    def test_nested_versions_adopt_owner_input_preserve_source_and_review_rounds(self):
        self.setup_job()
        artifact = self.root / "projects/001-first/src/output.txt"
        artifact.write_text("Previous working result")
        first = self.call(
            "review-round",
            "--target",
            "project",
            "--title",
            "First actual review",
            "--before",
            "render",
        )
        self.call(
            "review-round",
            "--target",
            "project",
            "--title",
            "Cannot overwrite waiting round",
            "--before",
            "render",
            fail=True,
        )
        (self.root / first["file"]).write_text("Owner's submitted answers\n")
        self.call(
            "resolve-review",
            "--target",
            "project",
            "--note",
            "Read submitted answers; blank choices delegated locally",
        )
        second = self.call(
            "review-round",
            "--target",
            "project",
            "--title",
            "Next unresolved choice",
            "--before",
            "render",
        )
        self.assertNotEqual(first["file"], second["file"])
        self.assertEqual(
            (self.root / first["file"]).read_text(), "Owner's submitted answers\n"
        )
        folder = self.root / "docs/projects/001-first/versions/V1/V1.2"
        folder.mkdir(parents=True)
        primary = folder / "01-transcription.md"
        primary.write_text("Owner-prepared change: preserve this exact input.\n")
        self.call(
            "iterate",
            "--target",
            "project",
            "--version",
            "1.2",
            "--note",
            "Must adopt",
            fail=True,
        )
        self.assertFalse((self.root / "projects/001-first/versions").exists())
        result = self.call(
            "iterate",
            "--target",
            "project",
            "--version",
            "1.2",
            "--note",
            "Adopt prepared input",
            "--input",
            str(primary),
        )
        self.assertEqual(
            primary.read_text(), "Owner-prepared change: preserve this exact input.\n"
        )
        self.assertEqual(result["change_input"]["entry_mode"], "owner-prepared")
        self.assertEqual(
            (self.root / result["previous_source"] / "src/output.txt").read_text(),
            "Previous working result",
        )
        patch = self.call(
            "iterate", "--target", "project", "--version", "1.2.1", "--note", "Patch"
        )
        self.assertTrue(patch["docs"].endswith("versions/V1/V1.2/V1.2.1"))

    def test_receipts_distinguish_readiness_acceptance_and_changed_artifacts(self):
        self.setup_job()
        path = self.root / "projects/001-first/src/output.txt"
        path.write_text("Candidate result")
        name = path.relative_to(self.root).as_posix()
        self.call("record", "draft", "--artifact", name, "--accepted", fail=True)
        mark = self.call("record", "draft", "--artifact", name)
        self.assertEqual(mark["state"], "ready")
        self.assertIsNone(mark["evidence"])
        path.write_text("Changed candidate")
        self.assertIn("stale", self.call("check", fail=True).stderr)
        self.call("record", "draft", "--artifact", name)
        self.assertTrue(self.call("check")["ok"])

    def test_primary_input_edits_require_explicit_reread_record(self):
        self.setup_job()
        project = self.state()["projects"]["001-first"]
        request = self.root / project["docs"] / "01-request.md"
        request.write_text("The actual input has changed.\n")
        self.assertIn("reread", self.call("check", fail=True).stderr)
        self.call("acknowledge-input", "--target", "project")
        self.assertTrue(self.call("check")["ok"])

    def test_update_keeps_improved_job_projects_state_and_removed_catalog(self):
        self.setup_job()
        local = self.root / "job/presentation-maker/references/quality.md"
        local.write_text(local.read_text() + "\nLocal improvement retained.\n")
        before = local.read_bytes()
        state = (self.root / "workspace.json").read_bytes()
        (self.root / "shared/local.txt").write_text("Local integration")
        upstream = self.next_release()
        plan = self.call("update", "--source", str(upstream))
        self.assertTrue(plan["catalog_skipped"])
        self.assertEqual((self.root / "VERSION").read_text().strip(), TEMPLATE_VERSION)
        self.call("update", "--source", str(upstream), "--apply")
        self.assertEqual((self.root / "VERSION").read_text().strip(), "0.3.0")
        self.assertEqual(local.read_bytes(), before)
        self.assertEqual((self.root / "workspace.json").read_bytes(), state)
        self.assertEqual(
            (self.root / "shared/local.txt").read_text(), "Local integration"
        )
        self.assertFalse((self.root / "registry").exists())
        self.call("verify-job", "--smoke", "scripts/check.py")

    def test_update_semantic_conflict_has_no_partial_writes_and_accepts_resolution(
        self,
    ):
        local = self.root / "README.md"
        local.write_text(local.read_text() + "\nUser's local instructions.\n")
        original = local.read_bytes()
        upstream = self.next_release()
        plan = self.call("update", "--source", str(upstream))
        self.assertIn("README.md", [item["file"] for item in plan["conflicts"]])
        self.call("update", "--source", str(upstream), "--apply", fail=True)
        self.assertEqual(local.read_bytes(), original)
        self.assertEqual((self.root / "VERSION").read_text().strip(), TEMPLATE_VERSION)
        resolution = self.base / "resolved"
        resolution.mkdir()
        (resolution / "README.md").write_bytes(
            original + b"\nUpstream release change.\n"
        )
        self.call(
            "update",
            "--source",
            str(upstream),
            "--resolution-dir",
            str(resolution),
            "--apply",
        )
        self.assertIn("User's local instructions.", local.read_text())
        self.assertIn("Upstream release change.", local.read_text())

    def test_failed_update_restores_engine_and_retains_recovery_checkpoint(self):
        self.setup_job()
        original = core.files(self.root / ".moom/core")
        readme = (self.root / "README.md").read_bytes()
        state = (self.root / "workspace.json").read_bytes()
        upstream = self.next_release(broken=True)
        self.call("update", "--source", str(upstream), "--apply", fail=True)
        self.assertEqual(core.files(self.root / ".moom/core"), original)
        self.assertEqual((self.root / "README.md").read_bytes(), readme)
        self.assertEqual((self.root / "workspace.json").read_bytes(), state)
        self.assertEqual((self.root / "VERSION").read_text().strip(), TEMPLATE_VERSION)
        checkpoints = list(
            (self.root / ".moom/local/updates").glob("*/checkpoint.json")
        )
        self.assertEqual(len(checkpoints), 1)
        self.assertEqual(
            json.loads(checkpoints[0].read_text())["status"], "rolled-back"
        )
        self.assertTrue(self.call("check")["ok"])

    def test_edited_generated_commands_and_collisions_are_preserved(self):
        wrapper = self.root / ".claude/commands/moom-job.md"
        wrapper.write_text(wrapper.read_text() + "\nUser customization\n")
        original = wrapper.read_bytes()
        self.call("sync", fail=True)
        self.assertEqual(wrapper.read_bytes(), original)
        collision = self.root / ".claude/commands/job-presentation-maker-render.md"
        collision.write_text("User's installed extension; do not delete\n")
        self.call("install", "presentation-maker", fail=True)
        self.assertEqual(
            collision.read_text(), "User's installed extension; do not delete\n"
        )
        self.assertIsNone(self.state()["job"])
        self.assertFalse((self.root / "job/presentation-maker").exists())

    def test_job_export_excludes_private_state_and_retains_license_origin_and_hashes(
        self,
    ):
        self.setup_job()
        (self.root / "docs/workspace/living/private.md").write_text(
            "PRIVATE_WORKSPACE_SENTINEL"
        )
        (self.root / "projects/001-first/inputs/client.txt").write_text(
            "PRIVATE_PROJECT_SENTINEL"
        )
        archive = self.base / "job.zip"
        self.call("export-job", "--output", str(archive))
        with zipfile.ZipFile(archive) as package:
            names = package.namelist()
            content = b"".join(package.read(name) for name in names)
            self.assertNotIn(b"PRIVATE_WORKSPACE_SENTINEL", content)
            self.assertNotIn(b"PRIVATE_PROJECT_SENTINEL", content)
            self.assertIn("presentation-maker/LICENSE", names)
            manifest = json.loads(package.read("manifest.json"))
            self.assertEqual(manifest["origin"]["kind"], "embedded")
            for name, checksum in manifest["sha256"].items():
                import hashlib

                self.assertEqual(
                    hashlib.sha256(
                        package.read("presentation-maker/" + name)
                    ).hexdigest(),
                    checksum,
                )
        forbidden = self.root / "job/presentation-maker/.env"
        forbidden.write_text("SECRET_SENTINEL")
        self.call("export-job", "--output", str(self.base / "unsafe.zip"), fail=True)
        self.assertFalse((self.base / "unsafe.zip").exists())

    def test_package_escape_and_malicious_release_ownership_are_rejected(self):
        source = self.root / "registry/presentation-maker"
        (source / "references/quality.md").write_text(
            "[outside](../../../workspace.json)\n"
        )
        self.call("install", "presentation-maker", fail=True)
        self.assertIsNone(self.state()["job"])
        upstream = self.next_release()
        manifest_path = upstream / ".moom/release.json"
        manifest = json.loads(manifest_path.read_text())
        manifest["engine"]["projects/escape.txt"] = "pretend"
        manifest_path.write_text(json.dumps(manifest))
        self.call("update", "--source", str(upstream), "--apply", fail=True)
        self.assertFalse((self.root / "projects/escape.txt").exists())

    def test_secrets_are_ignored_at_any_depth(self):
        subprocess.run(
            ["git", "init", "-q", str(self.root)], check=True, capture_output=True
        )
        names = [
            ".env",
            "nested/.env.production",
            "docs/secrets/token.txt",
            "docs/projects/001/secrets/token.txt",
            "nested/docs/job/living/secrets/token.txt",
            ".env.example",
        ]
        result = subprocess.run(
            ["git", "check-ignore", "--stdin", "-z"],
            cwd=self.root,
            input=("\0".join(names) + "\0").encode("utf-8"),
            capture_output=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(
            set(result.stdout.decode("utf-8").split("\0")) - {""}, set(names[:-1])
        )


if __name__ == "__main__":
    unittest.main()
