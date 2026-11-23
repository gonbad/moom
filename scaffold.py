"""Build an inert method snapshot and materialize its files in a separate Git repository."""
import argparse
import csv
import hashlib
import os
import re
import shutil
import subprocess
import sys
import tempfile
from contextlib import ExitStack, contextmanager
from pathlib import Path
from urllib.parse import quote, unquote

ROOT = Path(__file__).resolve().parent
DOCS = ROOT / 'kandoo_docs'
LIVING = DOCS / 'living'
RAW = 'docs/versions/0.1/00-user-idea-input.md'
INTERPRETATION = 'docs/versions/0.1/01-kandoo-interpretation.md'
LEGACY_STAMP = 'docs/method/stamp.md'
UTILITIES = {'issue', 'iterate', 'add-idea', 'method-note'}
POINTERS = ('AGENTS.md', 'CLAUDE.md', 'GEMINI.md')
POINTER = (b"Follow docs/constitution/general.md, docs/constitution/mission.md and "
           b"docs/constitution/workflow.md. Resume from docs/living/status.md.\n")
IDENTIFIER = r'[a-z0-9]+(?:-[a-z0-9]+)*'


def require(condition, message):
    if not condition:
        raise ValueError(message)


def version_dir(version):
    require(re.fullmatch(r'\d+\.\d+', version), 'Expected a numeric Kandoo version')
    return DOCS / 'versions' / version


def markdown_bytes(path):
    return path.read_bytes().replace(b'\r\n', b'\n')


def read_tree(root):
    """Read a reusable payload without following links or importing local state."""
    require(root.is_dir() and not root.is_symlink(), f'Missing or linked source directory: {root.name}')
    result = {}
    for path in sorted(root.rglob('*')):
        name = path.relative_to(root).as_posix()
        forbidden = {'.git', '.env', 'secrets', '.obsidian', '__pycache__', '.venv',
                     '.agents', '.claude', '.opencode', '.agent', '.gemini', 'node_modules',
                     *(p.lower() for p in POINTERS)}
        part = path.name.lower()
        require(not path.is_symlink() and part not in forbidden and
                not part.startswith(('.env', 'credentials', 'id_rsa', 'id_ed25519')) and
                not part.endswith(('.local.md', '.key', '.pem', '.p12', '.pfx')) and
                not any(c in name for c in '\n\r\t`\\|'), f'Unsafe reusable path: {name}')
        if not path.is_dir():
            require(path.is_file(), f'Expected regular file: {name}')
            result[name] = markdown_bytes(path) if path.suffix == '.md' else path.read_bytes()
    return result


def hash_bytes(data):
    return hashlib.sha256(data).hexdigest()


def fingerprint(files):
    return hash_bytes(''.join(f'{hash_bytes(data)}  {name}\n'
                              for name, data in sorted(files.items())).encode())


def atomic_write(path, data):
    with tempfile.NamedTemporaryFile(dir=path.parent, delete=False) as stream:
        temporary = Path(stream.name)
        try:
            stream.write(data)
            stream.close()
            if path.exists():
                os.chmod(temporary, path.stat().st_mode & 0o777)
            os.replace(temporary, path)
        finally:
            temporary.unlink(missing_ok=True)


@contextmanager
def writer(folder):
    lock = folder / '.scaffold.lock'
    try:
        lock.mkdir()
    except FileExistsError:
        raise ValueError('Another scaffold operation holds the lock. Check its owner before recovery.') from None
    owner = lock / 'owner'
    try:
        owner.write_text(f'{os.getpid()}\n', encoding='ascii')
        yield
    finally:
        owner.unlink(missing_ok=True)
        lock.rmdir()


def write_tree(root, files):
    for name, data in files.items():
        path = root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open('xb') as stream:
            stream.write(data)


def server_mode(workflow):
    matches = re.findall(r'^Server mode: (none|shared|dedicated)$', workflow, re.MULTILINE)
    require(len(matches) == 1, 'Declare one Server mode in workflow.md')
    return matches[0]


def field(document, name, default=''):
    match = re.search(r'^' + re.escape(name) + r':[ \t]*(.*)$', document, re.MULTILINE)
    return match[1].strip() if match else default


def set_field(document, name, value):
    line = f'{name}: {value}'
    pattern = r'^' + re.escape(name) + r':.*$'
    if re.search(pattern, document, re.MULTILINE):
        return re.sub(pattern, lambda _: line, document, count=1, flags=re.MULTILINE)
    before, sep, after = document.partition('\n## ')
    return before.rstrip() + '\n' + line + '\n' + sep + after


def pipeline(workflow):
    section = workflow.partition('## Floating commands')[0]
    stages = {}
    for line in section.splitlines():
        cells = [v.strip() for v in line.strip().strip('|').split('|')]
        if not line.startswith('|') or not (cells[0].startswith('`/') or cells[0] == '—'):
            continue
        require(len(cells) in (4, 5), f'Invalid workflow row: {line}')
        mode = 'ai' if len(cells) == 4 else cells[1]
        require(mode in ('ai', 'tool', 'api', 'human'), f'Unknown stage mode: {mode}')
        if mode == 'human':
            require(cells[0] == '—', 'Human rows use — instead of a command')
            key = cells[2]
            require(key and ',' not in key and not key.startswith('/'), 'Invalid human stage label')
        else:
            require(re.fullmatch(r'`/' + IDENTIFIER + r'`', cells[0]), 'Invalid workflow command name')
            key = cells[0][1:-1]
        require(key not in stages, f'Duplicate workflow stage: {key}')
        stages[key] = mode
    require(next(iter(stages), '') == '/idea', 'Workflow must start with /idea')
    return stages


def utility_gates(workflow, stages):
    section = workflow.partition('## Floating commands')[2].partition('\n## ')[0]
    if not section:
        # Previous four-column workflows used the built-in project utilities.
        defaults = dict.fromkeys(UTILITIES, 'always')
        if server_mode(workflow) == 'dedicated':
            defaults['server'] = 'always'
        return defaults
    gates = {}
    for line in section.splitlines():
        if not line.startswith('| `/'):
            continue
        cells = [v.strip() for v in line.strip('|').split('|')]
        require(len(cells) == 3 and re.fullmatch(r'`/' + IDENTIFIER + r'`', cells[0]), 'Invalid floating command row')
        name, gate = cells[0][2:-1], cells[1].strip('`')
        require(name not in gates and gate in {'always', 'complete', *stages}, f'Invalid prerequisite for {name}')
        gates[name] = gate
    require(gates.get('method-note') == 'always', '/method-note must be available always')
    require(server_mode(workflow) != 'dedicated' or 'server' in gates, 'Dedicated server needs /server')
    return gates


def applied_version():
    status = (LIVING / 'status.md').read_text(encoding='utf-8')
    version = field(status, 'Applied Kandoo version')
    if not version and (LIVING / 'applied.md').is_file():
        version = (LIVING / 'applied.md').read_text().strip()
    return version if version != 'none' else ''


def snapshot(*, legacy=False):
    payload = read_tree(ROOT / 'template')
    required = {RAW, INTERPRETATION, 'docs/constitution/general.md', 'docs/living/status.md',
                'docs/living/profile.md'}
    require(required <= payload.keys() and not payload[INTERPRETATION],
            'Template needs a reusable idea guide and empty interpretation, general constitution, profile and status')
    for name in ('mission', 'workflow'):
        source = markdown_bytes(LIVING / f'{name}.md')
        require(source.strip(), f'Complete the {name} first')
        payload[f'docs/constitution/{name}.md'] = source
    refs = LIVING / 'references'
    if refs.exists():
        payload.update({'docs/references/' + k: v for k, v in read_tree(refs).items()})
    workflow = payload['docs/constitution/workflow.md'].decode()
    if not legacy:
        require('## Floating commands' in workflow, 'Configure /floating-commands before sealing')
        require(re.search(r'^## Shared code\s*\n\s*\S', workflow, re.MULTILINE), 'Complete /shared-code before sealing')
    if '## Floating commands' in workflow:
        for name, choices in [('Project placement', {'sibling', 'nested', 'custom', 'ask'}),
                              ('Project Git', {'independent', 'existing'}),
                              ('Remote policy', {'none', 'ask', 'configured'}),
                              ('Secrets policy', {'none', 'shared', 'per-project'})]:
            require(field(workflow, name) in choices, f'Review {name} in /topology')
        require(field(workflow, 'Project placement') != 'custom' or field(workflow, 'Project parent'),
                'Custom placement needs Project parent')
        require(payload[RAW].strip(), 'Write the reusable project intake guide')
        if server_mode(workflow) == 'shared':
            require((LIVING / 'context/server.md').is_file(), 'Write the non-secret shared server context')
    context = LIVING / 'context'
    if context.exists():
        payload.update({'docs/context/' + k: v for k, v in read_tree(context).items()})
    stages = pipeline(workflow)
    steps = {key[1:] for key in stages if key.startswith('/')}
    gates = utility_gates(workflow, stages)
    bodies = read_tree(LIVING / 'steps')
    require(set(bodies) == {s + '.md' for s in steps}, 'Step sources must match workflow')
    policy = (DOCS / 'command-names.md').read_text(encoding='utf-8')
    native = set(re.findall(r'`([a-z0-9_-]+)`', policy.partition('## Core workspace names')[0]))
    reserved = native | {p.stem for p in (DOCS / 'commands').glob('*.md')}
    require(not steps & (reserved | set(gates) | UTILITIES | {'server'}) and not set(gates) & reserved,
            'Workflow has a reserved command name')
    if '## Floating commands' in workflow:
        custom = read_tree(LIVING / 'utilities')
        require(set(custom) == {u + '.md' for u in gates}, 'Utility sources must match declared floating commands')
        require(payload.get('docs/constitution/testing.md', b'').strip(), 'Write the Kandoo testing procedure first')
        bodies.update(custom)
    else:
        for name in gates:
            bodies[name + '.md'] = markdown_bytes(DOCS / 'project-commands' / (name + '.md'))
    for filename, data in bodies.items():
        name = Path(filename).stem
        require(re.fullmatch(IDENTIFIER, name) and len(name) <= 64 and
                not name.startswith(('moom-', 'kandoo-', 'job-')) and
                re.match(r'\A---\nname: ' + re.escape(name) +
                         r'\ndescription: [^\n]+\n---\n\s*\S', data.decode()),
                f'Invalid command body: {filename}')
    require(not {LEGACY_STAMP, 'docs/method/local.md', '.gitignore'} & payload.keys(),
            'Template contains a reserved project path')
    return {'payload/' + k: v for k, v in payload.items()} | {
        'steps/' + k: v for k, v in bodies.items()} | {
        'ignore.md': markdown_bytes(ROOT / '.gitignore'), 'pointer.md': POINTER}


def seal(version):
    dossier = version_dir(version)
    files = snapshot(legacy=(dossier / 'applied').is_dir())
    # Check the final layout before publishing a seal, including conflicts on
    # case-insensitive workstations and a file occupying a generated directory.
    validate_layout(materialize(files, version))
    digest = fingerprint(files)
    dossier.mkdir(parents=True, exist_ok=True)
    dest = dossier / 'applied'
    current = applied_version()
    if current:
        require(tuple(map(int, version.split('.'))) >= tuple(map(int, current.split('.'))),
                'Cannot replace the current template with an older version')
    if any(name.startswith('payload/tests/') and name.endswith('.py') for name in files):
        with tempfile.TemporaryDirectory() as temp:
            write_tree(Path(temp), materialize(files, version))
            subprocess.run([sys.executable, '-m', 'pytest', '-q', 'tests'], cwd=temp, check=True)
    if dest.exists():
        require(load_snapshot(dest) == files, 'Sealed version differs. Open a new Kandoo version.')
    else:
        with tempfile.TemporaryDirectory(dir=dossier) as temp:
            staged = Path(temp) / 'snapshot'
            write_tree(staged, store_snapshot(files))
            staged.rename(dest)
    seal_path = dossier / 'sha256.md'
    require(not seal_path.exists() or seal_path.read_text().strip() == digest, 'Snapshot digest changed')
    atomic_write(seal_path, (digest + '\n').encode())
    # Keep the visible template constitution usable while creation reads only sealed bytes.
    for name in ('mission', 'workflow'):
        relative = f'docs/constitution/{name}.md'
        path = ROOT / 'template' / relative
        data = files['payload/' + relative]
        if not path.exists() or path.read_bytes() != data:
            atomic_write(path, data)
    status = LIVING / 'status.md'
    atomic_write(status, set_field(status.read_text(encoding='utf-8'), 'Applied Kandoo version', version).encode())
    (LIVING / 'applied.md').unlink(missing_ok=True)


def host_paths(name):
    return (f'.claude/commands/{name}.md', f'.opencode/commands/{name}.md',
            f'.agents/skills/{name}/SKILL.md')


def store_snapshot(files):
    stored = files.copy()
    manifest = []
    blobs = ROOT / '.kandoo-blobs'
    for name, data in files.items():
        if len(data) < 65536 or name.endswith('.md'):
            continue
        digest = hash_bytes(data)
        blobs.mkdir(exist_ok=True)
        require(not blobs.is_symlink(), 'Linked blob store')
        path = blobs / digest
        require(not path.is_symlink(), 'Linked snapshot blob')
        if not path.exists():
            atomic_write(path, data)
        require(hash_bytes(path.read_bytes()) == digest, 'Damaged snapshot blob')
        manifest.append(f'{digest}  {name}')
        del stored[name]
    if manifest:
        stored['binary-assets.md'] = ('\n'.join(manifest) + '\n').encode()
    return stored


def load_snapshot(path):
    files = read_tree(path)
    for line in files.pop('binary-assets.md', b'').decode().splitlines():
        digest, _, name = line.partition('  ')
        require(re.fullmatch('[0-9a-f]{64}', digest) and name.startswith('payload/') and
                '..' not in Path(name).parts and name not in files and '\\' not in name, 'Invalid snapshot blob entry')
        blob = ROOT / '.kandoo-blobs' / digest
        require(not blob.parent.is_symlink() and not blob.is_symlink(), 'Linked snapshot blob')
        data = blob.read_bytes()
        require(hash_bytes(data) == digest, 'Damaged snapshot blob')
        files[name] = data
    return files


def project_files(version):
    dossier = version_dir(version)
    source = load_snapshot(dossier / 'applied')
    require(fingerprint(source) == (dossier / 'sha256.md').read_text().strip(), 'Damaged applied snapshot')
    return materialize(source, version)


def validate_layout(files):
    directories = set()
    paths = set()
    for name in files:
        path = Path(name)
        folded = name.casefold()
        require(folded not in paths, f'Duplicate destination path: {name}')
        paths.add(folded)
        directories.update(p.as_posix().casefold() for p in path.parents)
    require(not directories & paths, 'A payload file blocks a required directory')


def materialize(source, version):
    files = {name.removeprefix('payload/'): data for name, data in source.items()
             if name.startswith('payload/')}
    files['.gitignore'] = source['ignore.md']
    for pointer in POINTERS:
        files[pointer] = source['pointer.md']
    for name, data in source.items():
        if name.startswith('steps/'):
            files.update(dict.fromkeys(host_paths(Path(name).stem), data))
    status = 'docs/living/status.md'
    value = set_field(files[status].decode(), 'Installed Kandoo version', version)
    value = set_field(value, 'Intake guide SHA256', hash_bytes(files[RAW]))
    files[status] = value.encode()
    if 'docs/method/project-ignore.md' in files:
        files['.gitignore'] += b'\n' + files['docs/method/project-ignore.md']
    return files


def git(root, *args, check=True):
    return subprocess.run(['git', '-C', str(root), *args], check=check, capture_output=True, text=True)


def check_target(dest, nested=False):
    require(dest != ROOT and (ROOT not in dest.parents or (nested and dest.parent == ROOT / 'projects')) and dest not in ROOT.parents,
            'Choose a project location outside the method workspace')
    require('.git' not in {p.lower() for p in dest.parts}, 'Destination is inside Git metadata')
    require(dest.parent.is_dir() or (nested and dest.parent == ROOT / 'projects' and not dest.parent.exists()),
            'Create or choose the destination parent first')
    for folder in (dest, *dest.parents):
        require(not folder.is_symlink(), f'Linked destination: {folder}')
        require(folder == dest or not (folder / 'docs/constitution/general.md').exists(), 'Destination is inside another project')
    require(not dest.exists() or dest.is_dir(), 'Destination is not a directory')


def create(slug, destination, interpretation=None, shared_access=False):
    require(re.fullmatch(IDENTIFIER, slug), 'Invalid project slug')
    dest = Path(os.path.abspath(destination))
    version = applied_version()
    files = project_files(version)
    workflow = files['docs/constitution/workflow.md'].decode()
    placement = field(workflow, 'Project placement')
    check_target(dest, nested=placement == 'nested')
    reuse = field(workflow, 'Project Git') == 'existing'
    if placement == 'nested':
        require(dest.parent == ROOT / 'projects', 'Use the configured projects/ child')
        ignored = git(ROOT, 'check-ignore', '-q', '--', str(dest), check=False).returncode == 0
        require(ignored != reuse, 'Configure projects/ Git tracking for the selected ownership')
    elif placement == 'sibling':
        require(dest.parent == ROOT.parent, 'Use the configured sibling location')
    elif placement == 'custom':
        require(dest.parent == Path(field(workflow, 'Project parent')).expanduser().resolve(), 'Use the configured project parent')
    if reuse:
        owner = git(dest if dest.exists() else dest.parent, 'rev-parse', '--show-toplevel', check=False)
        require(owner.returncode == 0, 'Project policy requires an existing repository')
        if Path(owner.stdout.strip()).resolve() != dest:
            require(git(dest.parent, 'check-ignore', '-q', '--', str(dest), check=False).returncode != 0,
                    'The enclosing Git repository ignores this project')
    ledger = LIVING / 'projects.md'
    original = ledger.read_bytes()
    registered_path = quote(str(dest), safe='/:')
    for line in original.decode().splitlines():
        if line.startswith('## Note receipts'):
            break
        if not line.startswith('| ') or line.startswith(('| Slug |', '| --- |')):
            continue
        cells = [cell.strip() for cell in line.strip('|').split('|')]
        require(len(cells) == 4, 'Repair the malformed project registry row first')
        other = Path(unquote(cells[1])).resolve()
        require(cells[0] != slug and dest != other, 'Project slug or path already registered')
        require(other not in dest.parents and dest not in other.parents, 'Registered project roots overlap')
    if interpretation:
        files[INTERPRETATION] = interpretation.read_bytes()
    mode = server_mode(files['docs/constitution/workflow.md'].decode())
    require(not shared_access or field(workflow, 'Secrets policy', 'shared' if mode == 'shared' else 'none') == 'shared', 'Shared access requires the shared secrets policy')
    if mode == 'shared':
        server = files.get('docs/context/server.md')
        legacy = LIVING / 'server.md'
        files['docs/living/server.md'] = server or (legacy.read_bytes() if legacy.exists() else b'# Shared server\n')
    if mode == 'dedicated':
        files.setdefault('docs/living/server.md', b'# Project server\n\nTarget unselected. Run /server at the infrastructure stage.\n')
    secret = 'docs/secrets/credentials.md'
    if shared_access:
        source = DOCS / 'secrets/credentials.md'
        require(source.is_file() and not source.is_symlink() and not source.parent.is_symlink(),
                'Missing local shared credentials')
        require(git(ROOT, 'check-ignore', '-q', '--', 'kandoo_docs/secrets/credentials.md', check=False).returncode == 0,
                'Shared credentials must be untracked and ignored')
    # Preflight the whole plan before creating any files, including ignored files.
    paths = list(files) + ([secret] if shared_access else [])
    for name in paths:
        path = dest / name
        require(not path.is_symlink(), f'Linked file at {name}')
        for parent in path.parents:
            if parent == dest:
                break
            require(not parent.is_symlink() and (not parent.exists() or parent.is_dir()), f'Blocked parent at {name}')
        if path.exists():
            require(name == '.gitignore' and path.is_file(), f'Destination collision: {name}')
    # Hold a second lock at the destination to coordinate separate Kandoos.
    with ExitStack() as directory, ExitStack() as locks, ExitStack() as rollback:
        def mkdir(folder):
            if not folder.exists():
                mkdir(folder.parent)
                folder.mkdir()
                rollback.callback(folder.rmdir)
        if not dest.parent.exists():
            dest.parent.mkdir()
            directory.callback(dest.parent.rmdir)
        if not dest.exists():
            dest.mkdir()
            directory.callback(dest.rmdir)
        locks.enter_context(writer(dest))
        require(not (dest / '.git').is_symlink(), 'Linked .git is unsupported')
        existing_git = (dest / '.git').exists()
        if existing_git or reuse:
            require(reuse or Path(git(dest, 'rev-parse', '--show-toplevel').stdout.strip()).resolve() == dest,
                    'Destination must own its repository')
            tracked = set(git(dest, 'ls-files', '-z', '--', '.').stdout.split('\0'))
            require(not (tracked & set(paths)) - {'.gitignore'},
                    'A planned path is already owned by the destination Git index')
        else:
            git(dest, 'init', '--quiet')
            rollback.callback(shutil.rmtree, dest / '.git')
            for key in ('user.name', 'user.email'):
                if not git(dest, 'config', '--get', key, check=False).stdout.strip():
                    value = git(ROOT, 'config', '--get', key, check=False).stdout.strip()
                    if value:
                        git(dest, 'config', '--local', key, value)
        for name, data in files.items():
            path = dest / name
            if name == '.gitignore' and path.exists():
                original_ignore = path.read_bytes()
                if data not in original_ignore:
                    atomic_write(path, original_ignore + b'\n' + data)
                    rollback.callback(atomic_write, path, original_ignore)
                continue
            mkdir(path.parent)
            with path.open('xb') as stream:
                rollback.callback(path.unlink)
                stream.write(data)
        require(git(dest, 'check-ignore', '-q', '--', secret, check=False).returncode == 0,
                'Destination Git rules must ignore untracked docs/secrets/credentials.md')
        if shared_access:
            path = dest / secret
            mkdir(path.parent)
            with os.fdopen(os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600), 'wb') as stream:
                rollback.callback(path.unlink)
                if os.name == 'nt':
                    # Restrict the new empty file before any access material is written.
                    identity = subprocess.check_output(['whoami', '/user', '/fo', 'csv', '/nh'], text=True)
                    sid = next(csv.reader(identity.splitlines()))[-1]
                    require(re.fullmatch(r'S-1-[0-9-]+', sid), 'Cannot determine the Windows user SID')
                    subprocess.run(['icacls', str(path), '/inheritance:r', '/grant:r', f'*{sid}:F'],
                                   check=True, capture_output=True)
                stream.write(source.read_bytes())
        require(ledger.read_bytes() == original, 'Registry changed during creation. Retry.')
        remote = 'local' if field(workflow, 'Remote policy') == 'none' else 'pending'
        entry = f'| {slug} | {registered_path} | {remote} | {version} |\n'
        rows, sep, notes = original.partition(b'## Note receipts')
        atomic_write(ledger, rows.rstrip() + b'\n' + entry.encode() + b'\n' + sep + notes)
        rollback.pop_all()
        directory.pop_all()
    return dest


def completed_steps(status, stages):
    recorded = field(status, 'Completed steps')
    if recorded:
        return [s.strip() for s in recorded.split(',') if s.strip() in stages]
    # Read the old progress block once, including the rehearsal's emoji notation.
    legacy = re.findall(r'^- (?:✅|\[done\])\s+`?(/[-\w]+)', status, re.MULTILINE)
    return [s for s in legacy if s in stages]


def progress(project):
    workflow = (project / 'docs/constitution/workflow.md').read_text(encoding='utf-8')
    stages = pipeline(workflow)
    status = (project / 'docs/living/status.md').read_text(encoding='utf-8')
    completed = completed_steps(status, stages)
    skipped = {key.strip() for key in field(status, 'Skipped steps').split(',')}
    current = field(status, 'Current step')
    for key, mode in stages.items():
        marker = '✅' if key in completed else '⏭️' if key in skipped else '🔵' if key == current else '⬜'
        print(f'{marker} [{mode.upper()}] {key}')
    gates = utility_gates(workflow, stages)
    print('Available:', ' '.join('/' + name for name, gate in gates.items()
                                 if gate == 'always' or gate in completed or
                                 (gate == 'complete' and current == 'complete')))
    print('Next:', field(status, 'Next action'))


def owned_path(name):
    return name not in {'.gitignore', LEGACY_STAMP, 'docs/method/local.md'} and not name.startswith((
        'docs/living/', 'docs/versions/', 'docs/method-notes/', 'existing/', 'samples/', 'design/'))


def project_bytes(root, name):
    path = root / name
    for parent in path.parents:
        if parent == root:
            break
        require(not parent.is_symlink() and (not parent.exists() or parent.is_dir()), f'Blocked parent at {name}')
    require(not path.is_symlink() and (not path.exists() or path.is_file()), f'Blocked file at {name}')
    return path.read_bytes() if path.exists() else None


def migrate(args):
    ledger = LIVING / 'projects.md'
    registry = ledger.read_text(encoding='utf-8')
    rows = [line for line in registry.splitlines() if line.startswith(f'| {args.slug} | ')]
    require(len(rows) == 1, 'Expected one registered project for this slug')
    cells = [value.strip() for value in rows[0].strip('|').split('|')]
    require(len(cells) == 4, 'Invalid project registry entry')
    project = Path(unquote(cells[1]))
    require(project.is_absolute() and project.resolve() == project, 'Registered path changed')
    repo = Path(git(project, 'rev-parse', '--show-toplevel').stdout.strip()).resolve()
    prefix = project.relative_to(repo)
    status_name = 'docs/living/status.md'
    existing = project_bytes(project, status_name).decode()
    old_version = cells[3]
    installed = field(existing, 'Installed Kandoo version', old_version)
    new = project_files(args.version)
    old = project_files(old_version)
    require(repo == project or field(old['docs/constitution/workflow.md'].decode(), 'Project Git') == 'existing',
            'Unexpected Git owner for the registered project')
    if installed == args.version and installed != old_version:
        # Only reconcile an interrupted installation whose recorded migration reached HEAD.
        require(f'Migrate method {old_version} to {installed}' in git(project, 'log', '-1', '--format=%s').stdout,
                'Project and ledger versions disagree')
    else:
        require(installed == old_version, 'Project and ledger versions disagree')
    workflow_path = 'docs/constitution/workflow.md'
    local_workflow = project_bytes(project, workflow_path)
    old_stages = pipeline(local_workflow.decode())
    effective_workflow = new[workflow_path]
    if workflow_path in args.keep or old[workflow_path] == new[workflow_path]:
        effective_workflow = local_workflow
    new_stages = pipeline(effective_workflow.decode())
    require(set(args.completed) <= new_stages.keys(), 'Unrecognized completed stage')
    receipts = set(completed_steps(existing, old_stages)) | set(args.completed)
    done = [stage for stage in new_stages if stage in receipts]
    skipped = [s for s in new_stages if s in {k.strip() for k in field(existing, 'Skipped steps').split(',')} and s not in done]
    outstanding = [s for s in new_stages if s not in done and s not in skipped]
    current = args.current or field(existing, 'Current step')
    if current not in new_stages and current != 'complete':
        require(not args.current and not outstanding, 'Choose a valid --current for the removed active stage')
        current = 'complete'
    require(current in new_stages or current == 'complete', 'Invalid successor stage')
    require(current != 'complete' or not outstanding or args.current == 'complete',
            'Use --current complete to acknowledge outstanding stages')
    frozen = {path for key in done if key.startswith('/') for path in host_paths(key[1:])}
    changes = {}
    conflicts = []
    keep, take = set(args.keep), set(args.take)
    require(not keep & take, 'Choose one resolution per path')
    candidates = {n for n in old.keys() | new.keys() if owned_path(n)}
    require(keep | take <= candidates, 'Resolution names an unknown method path')
    for name in sorted(candidates):
        before, after = old.get(name), new.get(name)
        if name in keep or (name not in take and (before == after or name in frozen)):
            continue
        local = project_bytes(project, name)
        if local == after:
            continue
        if local != before and name not in take:
            conflicts.append(name)
            continue
        changes[name] = after
    require(not conflicts, 'Resolve local drift with --keep or --take: ' + ', '.join(conflicts))
    # Integrate only the managed ignore block; keep participant rules in their original order.
    ignore = project_bytes(project, '.gitignore')
    if ignore is not None and old['.gitignore'] != new['.gitignore']:
        if old['.gitignore'] in ignore:
            changes['.gitignore'] = ignore.replace(old['.gitignore'], new['.gitignore'], 1)
        elif new['.gitignore'] not in ignore:
            changes['.gitignore'] = new['.gitignore'].rstrip() + b'\n' + ignore
    retained_commands = [project_bytes(project, path) or b'' for path in frozen if path not in take]
    for name in list(changes):
        if changes[name] is not None or not name.startswith(('docs/context/', 'docs/references/')):
            continue
        if any(name.encode() in body or (b'docs/references/' in body and Path(name).name.encode() in body)
               for body in retained_commands):
            del changes[name]
    if project_bytes(project, LEGACY_STAMP) is not None:
        changes[LEGACY_STAMP] = None
    status = re.sub(r'^## Workflow Progress\s*\n.*?(?=^## |\Z)', '', existing, flags=re.MULTILINE | re.DOTALL)
    status = re.sub(r'^Version:', 'Product version:', status, count=1, flags=re.MULTILINE)
    for name, value in [('Installed Kandoo version', args.version), ('Completed steps', ', '.join(done) or 'none'),
                        ('Skipped steps', ', '.join(skipped) or 'none'), ('Current step', current)]:
        status = set_field(status, name, value)
    if args.current or current != field(existing, 'Current step'):
        status = set_field(status, 'Next action', 'Delivery complete.' if current == 'complete' else current)
    if installed != args.version:
        status = status.rstrip() + f'\n- Migrated Kandoo {old_version} → {args.version}. Resume: {current}.\n'
    if status != existing:
        changes[status_name] = status.encode()
    for name, data in changes.items():
        print(('remove ' if data is None else 'write  ') + name)
    if not args.apply:
        return
    if changes:
        require(not git(project, 'status', '--porcelain').stdout, 'Commit the reviewed project checkpoint first')
        git(project, 'symbolic-ref', '--quiet', 'HEAD')
        head = git(project, 'rev-parse', 'HEAD').stdout.strip()
        with tempfile.TemporaryDirectory() as temp:
            work = Path(temp) / 'migration'
            git(project, 'worktree', 'add', '--detach', str(work), head)
            try:
                target = work / prefix
                for name, data in changes.items():
                    path = target / name
                    require(project_bytes(project, name) == project_bytes(target, name), f'Untracked collision at {name}')
                    if data is None:
                        path.unlink(missing_ok=True)
                    else:
                        path.parent.mkdir(parents=True, exist_ok=True)
                        atomic_write(path, data)
                git(work, 'add', '-A')
                tracked = set(git(target, 'ls-files', '-z', '--', '.').stdout.split('\0'))
                require(all((name in tracked) == (data is not None) for name, data in changes.items()),
                        'Git ignore or index rules conflict with the migration. Review the target rules.')
                git(work, 'commit', '-m', f'Migrate method {old_version} to {args.version}')
                commit = git(work, 'rev-parse', 'HEAD').stdout.strip()
                require(git(project, 'rev-parse', 'HEAD').stdout.strip() == head and
                        not git(project, 'status', '--porcelain').stdout, 'Project changed during migration')
                git(project, 'update-ref', f'refs/heads/backup/migrate-{head}', head, '0' * len(head),
                    check=False)
                require(git(project, 'rev-parse', f'refs/heads/backup/migrate-{head}').stdout.strip() == head,
                        'Could not preserve checkpoint')
                git(project, 'merge', '--ff-only', '--no-overwrite-ignore', commit)
            finally:
                git(project, 'worktree', 'remove', '--force', str(work))
    require(ledger.read_text(encoding='utf-8') == registry, 'Ledger changed. Retry migration.')
    cells[3] = args.version
    atomic_write(ledger, registry.replace(rows[0], '| ' + ' | '.join(cells) + ' |').encode())


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='action', required=True)
    sub.add_parser('seal').add_argument('version')
    render = sub.add_parser('render', help='Materialize a sealed baseline for migration comparison')
    render.add_argument('version')
    render.add_argument('destination', type=Path)
    new = sub.add_parser('create')
    new.add_argument('slug')
    new.add_argument('destination', type=Path)
    new.add_argument('--interpretation', type=Path)
    new.add_argument('--shared-access', action='store_true')
    sub.add_parser('preview').add_argument('destination', type=Path)
    sub.add_parser('progress').add_argument('project', type=Path)
    migration = sub.add_parser('migrate')
    migration.add_argument('slug')
    migration.add_argument('version')
    migration.add_argument('--apply', action='store_true')
    migration.add_argument('--current')
    migration.add_argument('--completed', action='append', default=[], help='Added stage satisfied by reviewed existing evidence')
    migration.add_argument('--keep', action='append', default=[])
    migration.add_argument('--take', action='append', default=[])
    args = parser.parse_args()
    if args.action == 'progress':
        progress(args.project)
    elif args.action in ('preview', 'render'):
        files = materialize(snapshot(), 'preview') if args.action == 'preview' else project_files(args.version)
        validate_layout(files)
        dest = args.destination.absolute()
        check_target(dest)
        dest.mkdir()
        try:
            write_tree(dest, files)
        except BaseException:
            shutil.rmtree(dest)
            raise
    elif args.action == 'migrate' and not args.apply:
        migrate(args)
    else:
        with writer(LIVING):
            if args.action == 'seal':
                seal(args.version)
            elif args.action == 'migrate':
                migrate(args)
            else:
                print(create(args.slug, args.destination, args.interpretation, args.shared_access))


if __name__ == '__main__':
    try:
        main()
    except (OSError, ValueError, subprocess.SubprocessError) as error:
        sys.exit(str(error))
