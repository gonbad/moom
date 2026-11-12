"""Exercise distributed software Jobs, Project ownership, Compose and SPA navigation."""
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
JOBS = ('web-app-builder', 'bot-builder', 'agentic-chatbot')


def module(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    value = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(value)
    return value


class SoftwareJobs(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='moom-software-jobs-')
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)

    def call(self, root, *args, fail=False):
        result = subprocess.run([sys.executable, str(root / 'moom.py'), '--workspace', str(root), *args], capture_output=True, text=True, check=False)
        self.assertEqual(result.returncode != 0, fail, result.stderr)
        return result if fail else json.loads(result.stdout)

    def test_release_zip_initializes_every_software_job_and_resumes_two_projects(self):
        archive = self.base / 'moom.zip'
        result = subprocess.run([sys.executable, str(SOURCE / 'tools/release.py'), '--check', '--output', str(archive)], capture_output=True, text=True, check=False)
        self.assertEqual(result.returncode, 0, result.stderr)
        for name in JOBS:
            with self.subTest(job=name):
                root = self.base / name
                with zipfile.ZipFile(archive) as bundle:
                    bundle.extractall(root)
                self.assertEqual(self.call(root, 'catalog', name)[0]['name'], name)
                self.call(root, 'install', name)
                first = self.call(root, 'new', 'first', '--first')['project']
                paths = self.call(root, 'run', 'scripts/project.py', 'init')
                prd = Path(paths['LIVING']) / 'prd.md'
                prd.write_text('First requirements', encoding='utf-8')
                (Path(paths['SOURCE']) / 'sentinel.txt').write_text('First source', encoding='utf-8')
                self.call(root, 'verify-job', '--smoke', 'scripts/smoke.py')
                self.call(root, 'finish-job')
                self.assertFalse((root / 'registry').exists())
                self.assertEqual(json.loads((root / 'workspace.json').read_text())['job']['status'], 'ready')
                self.call(root, 'new', 'second')
                second = self.call(root, 'run', 'scripts/project.py', 'init')
                (Path(second['LIVING']) / 'prd.md').write_text('Second requirements', encoding='utf-8')
                self.assertNotEqual(paths['LIVING'], second['LIVING'])
                self.call(root, 'switch', first)
                self.assertEqual(self.call(root, 'run', 'scripts/project.py', 'paths'), paths)
                self.assertEqual(prd.read_text(encoding='utf-8'), 'First requirements')
                self.assertEqual((Path(paths['SOURCE']) / 'sentinel.txt').read_text(), 'First source')
                for command in (root / 'job' / name / 'commands').glob('*.md'):
                    self.assertTrue(self.call(root, 'procedure', command.stem)['text'])
                self.assertTrue(self.call(root, 'check')['ok'])

    def test_release_rejects_unindexed_duplicate_and_incomplete_starters(self):
        root = self.base / 'template'
        shutil.copytree(SOURCE, root, ignore=shutil.ignore_patterns('.git', '__pycache__', 'local'))
        release = module(SOURCE / 'tools/release.py', 'release_catalog_test')
        release.validate_catalog(root)
        orphan = root / 'registry/forgotten'
        orphan.mkdir()
        with self.assertRaisesRegex(ValueError, 'unindexed'):
            release.validate_catalog(root)
        orphan.rmdir()
        index = root / 'registry/index.json'
        original = index.read_text()
        data = json.loads(original)
        data['jobs'].append(data['jobs'][0])
        index.write_text(json.dumps(data))
        with self.assertRaisesRegex(ValueError, 'Duplicate'):
            release.validate_catalog(root)
        index.write_text(original)
        (root / 'registry/bot-builder/commands/infra.md').unlink()
        with self.assertRaisesRegex(ValueError, 'Broken Job reference'):
            release.validate_catalog(root)

    def test_project_helper_rejects_foreign_dossiers_and_path_escape(self):
        helper = module(SOURCE / 'registry/web-app-builder/scripts/project.py', 'project_scope_test')
        root = self.base / 'kandoo'
        root.mkdir()
        item = {'id': '001-first', 'docs': 'docs/projects/002-other/versions/V0/V0.1'}
        state = {'active_project': '001-first', 'projects': {'001-first': item}}
        (root / 'workspace.json').write_text(json.dumps(state))
        with self.assertRaisesRegex(ValueError, 'another Project'):
            helper.initialize(root)
        item['docs'] = '../foreign'
        (root / 'workspace.json').write_text(json.dumps(state))
        with self.assertRaisesRegex(ValueError, 'relative'):
            helper.initialize(root)
        self.assertFalse((self.base / 'foreign').exists())

    @unittest.skipUnless(shutil.which('docker'), 'Docker Compose needed for configuration validation')
    def test_compose_requires_secrets_and_supports_isolation_and_container_dns(self):
        if subprocess.run(['docker', 'compose', 'version'], capture_output=True, check=False).returncode:
            self.skipTest('Docker Compose plugin unavailable')
        for name in ('compose.yaml', 'compose.app.yaml'):
            shutil.copy2(SOURCE / 'registry/web-app-builder/assets' / name, self.base / name)
        (self.base / '.env.app').write_text('')
        excluded = {'DB_NAME', 'DB_USER', 'DB_PASSWORD', 'PG_PORT', 'REDIS_PORT', 'APP_PORT'}
        env = {k: v for k, v in os.environ.items() if k not in excluded}
        command = ['docker', 'compose', '-f', str(self.base / 'compose.yaml')]
        configs = []
        for number in (1, 2):
            values = {'DB_NAME': f'app{number}', 'DB_USER': f'owner{number}', 'DB_PASSWORD': 'test-only-password', 'PG_PORT': str(15430 + number), 'REDIS_PORT': str(16370 + number), 'APP_PORT': str(18000 + number)}
            config_env = self.base / f'.env.{number}'
            config_env.write_text(''.join(f'{key}={value}\n' for key, value in values.items()))
            result = subprocess.run([*command, '-f', str(self.base / 'compose.app.yaml'), '--project-name', f'project{number}', '--env-file', str(config_env), 'config', '--format', 'json'], env=env, capture_output=True, text=True, check=False)
            self.assertEqual(result.returncode, 0, result.stderr)
            config = json.loads(result.stdout)
            app = config['services']['app']
            self.assertIn('@postgres:5432/', app['environment']['DATABASE_URL'])
            self.assertEqual(app['environment']['REDIS_URL'], 'redis://redis:6379/0')
            self.assertEqual(config['services']['postgres']['ports'][0]['host_ip'], '127.0.0.1')
            configs.append(config)
        self.assertNotEqual(configs[0]['services']['postgres']['ports'], configs[1]['services']['postgres']['ports'])
        self.assertNotEqual(configs[0]['volumes']['pgdata']['name'], configs[1]['volumes']['pgdata']['name'])
        empty = self.base / '.env.empty'
        empty.write_text('DB_NAME=app\nDB_USER=owner\nDB_PASSWORD=\nPG_PORT=15432\nREDIS_PORT=16379\n')
        result = subprocess.run([*command, '--env-file', str(empty), 'config', '--quiet'], env=env, capture_output=True, text=True, check=False)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('DB_PASSWORD', result.stderr)

    @unittest.skipUnless(importlib.util.find_spec('starlette') and importlib.util.find_spec('httpx'), 'Starlette/httpx needed for real ASGI routing checks')
    def test_spa_fallback_preserves_api_asset_and_method_errors(self):
        from starlette.applications import Starlette
        from starlette.routing import Mount
        from starlette.testclient import TestClient
        static = module(SOURCE / 'registry/web-app-builder/assets/spa.py', 'spa_test')
        (self.base / 'index.html').write_text('<html>React shell</html>')
        app = Starlette(routes=[Mount('/', app=static.SPAStaticFiles(directory=self.base, html=True))])
        with TestClient(app) as client:
            for path in ('/', '/dashboard', '/settings/profile'):
                response = client.get(path, headers={'accept': 'text/html'})
                self.assertEqual(response.status_code, 200)
                self.assertIn('React shell', response.text)
            for path in ('/api/missing', '/health', '/assets/missing', '/assets/app.js', '/missing.css'):
                response = client.get(path, headers={'accept': 'text/html'})
                self.assertEqual(response.status_code, 404, path)
                self.assertNotIn('React shell', response.text)
            self.assertEqual(client.get('/dashboard', headers={'accept': 'application/json'}).status_code, 404)
            self.assertEqual(client.post('/dashboard', headers={'accept': 'text/html'}).status_code, 405)
            response = client.head('/dashboard', headers={'accept': 'text/html'})
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.content, b'')
