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
STAMP = 'docs/method/stamp.md'
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


def snapshot():
    payload = read_tree(ROOT / 'template')
    required = {RAW, INTERPRETATION, 'docs/constitution/general.md', 'docs/living/status.md',
                'docs/living/profile.md'}
    require(required <= payload.keys() and not payload[RAW] and not payload[INTERPRETATION],
            'Template needs both empty idea files, general constitution, profile and status')
    for name in ('mission', 'workflow'):
        source = markdown_bytes(LIVING / f'{name}.md')
        require(source.strip(), f'Complete the {name} first')
        payload[f'docs/constitution/{name}.md'] = source
    refs = LIVING / 'references'
    if refs.exists():
        payload.update({'docs/references/' + k: v for k, v in read_tree(refs).items()})
    workflow = payload['docs/constitution/workflow.md'].decode()
    steps = re.findall(r'^\| `/([^`]+)` \|', workflow, re.MULTILINE)
    require(all(re.fullmatch(IDENTIFIER, step) for step in steps), 'Invalid workflow command name')
    bodies = read_tree(LIVING / 'steps')
    require(steps and steps[0] == 'idea' and len(set(steps)) == len(steps) and
            set(bodies) == {s + '.md' for s in steps}, 'Step sources must match workflow, beginning with /idea')
    mode = server_mode(workflow)
    utilities = UTILITIES | ({'server'} if mode == 'dedicated' else set())
    policy = (DOCS / 'command-names.md').read_text(encoding='utf-8')
    native = set(re.findall(r'`([a-z0-9_-]+)`', policy.partition('## Core workspace names')[0]))
    reserved = native | {p.stem for p in (DOCS / 'commands').glob('*.md')} | UTILITIES | {'server'}
    require(not set(steps) & reserved, 'Workflow has a reserved command name')
    for name in utilities:
        bodies[name + '.md'] = markdown_bytes(DOCS / 'project-commands' / (name + '.md'))
    for filename, data in bodies.items():
        name = Path(filename).stem
        require(re.fullmatch(IDENTIFIER, name) and len(name) <= 64 and
                not name.startswith(('moom-', 'kandoo-', 'job-')) and
                re.match(r'\A---\nname: ' + re.escape(name) +
                         r'\ndescription: [^\n]+\n---\n\s*\S', data.decode()),
                f'Invalid command body: {filename}')
    require(not {STAMP, 'docs/method/local.md', '.gitignore'} & payload.keys(),
            'Template contains a reserved project path')
    return {'payload/' + k: v for k, v in payload.items()} | {
        'steps/' + k: v for k, v in bodies.items()} | {
        'ignore.md': markdown_bytes(ROOT / '.gitignore'), 'pointer.md': POINTER}


def seal(version):
    dossier = version_dir(version)
    files = snapshot()
    # Check the final layout before publishing a seal, including conflicts on
    # case-insensitive workstations and a file occupying a generated directory.
    validate_layout(materialize(files, version))
    digest = fingerprint(files)
    dossier.mkdir(parents=True, exist_ok=True)
    dest = dossier / 'applied'
    head = LIVING / 'applied.md'
    if head.exists():
        current = head.read_text().strip()
        require(tuple(map(int, version.split('.'))) >= tuple(map(int, current.split('.'))),
                'Cannot replace the current template with an older version')
    if dest.exists():
        require(read_tree(dest) == files, 'Sealed version differs. Open a new Kandoo version.')
    else:
        with tempfile.TemporaryDirectory(dir=dossier) as temp:
            staged = Path(temp) / 'snapshot'
            write_tree(staged, files)
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
    atomic_write(head, (version + '\n').encode())


def host_paths(name):
    return (f'.claude/commands/{name}.md', f'.opencode/commands/{name}.md',
            f'.agents/skills/{name}/SKILL.md')


def project_files(version):
    dossier = version_dir(version)
    source = read_tree(dossier / 'applied')
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
    owned = {name: data for name, data in files.items() if name != '.gitignore' and not name.startswith(
        ('docs/living/', 'docs/versions/', 'docs/method-notes/', 'existing/', 'design/'))}
    stamp = f'# Installed method\n\nKandoo version: {version}\nStatus schema: 1\n\n'
    files[STAMP] = (stamp + ''.join(f'- `{name}` {hash_bytes(data)}\n'
                                    for name, data in sorted(owned.items()))).encode()
    return files


def git(root, *args, check=True):
    return subprocess.run(['git', '-C', str(root), *args], check=check, capture_output=True, text=True)


def check_target(dest):
    require(dest != ROOT and ROOT not in dest.parents and dest not in ROOT.parents,
            'Choose a project location outside the method workspace')
    require('.git' not in {p.lower() for p in dest.parts}, 'Destination is inside Git metadata')
    require(dest.parent.is_dir(), 'Create or choose the destination parent first')
    for folder in (dest, *dest.parents):
        require(not folder.is_symlink(), f'Linked destination: {folder}')
        require(folder == dest or not (folder / STAMP).exists(), 'Destination is inside another project')
    require(not dest.exists() or dest.is_dir(), 'Destination is not a directory')


def create(slug, destination, interpretation=None, shared_access=False):
    require(re.fullmatch(IDENTIFIER, slug), 'Invalid project slug')
    dest = Path(os.path.abspath(destination))
    check_target(dest)
    version = (LIVING / 'applied.md').read_text().strip()
    files = project_files(version)
    ledger = LIVING / 'projects.md'
    original = ledger.read_bytes()
    registered_path = quote(str(dest), safe='/:')
    for line in original.decode().splitlines():
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
    require(not shared_access or mode == 'shared', 'Access copy requires shared server mode')
    if mode == 'shared':
        files['docs/living/server.md'] = (LIVING / 'server.md').read_bytes()
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
        if not dest.exists():
            dest.mkdir()
            directory.callback(dest.rmdir)
        locks.enter_context(writer(dest))
        require(not (dest / '.git').is_symlink(), 'Linked .git is unsupported')
        existing_git = (dest / '.git').exists()
        if existing_git:
            require(Path(git(dest, 'rev-parse', '--show-toplevel').stdout.strip()).resolve() == dest,
                    'Destination must own its repository')
            tracked = set(git(dest, 'ls-files', '-z').stdout.split('\0'))
            require(not (tracked & set(paths)) - {'.gitignore'},
                    'A planned path is already owned by the destination Git index')
        else:
            git(dest, 'init', '--quiet')
            rollback.callback(shutil.rmtree, dest / '.git')
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
        entry = f'| {slug} | {registered_path} | pending | {version} |\n'
        atomic_write(ledger, original.rstrip(b'\n') + b'\n' + entry.encode())
        rollback.pop_all()
        directory.pop_all()
    return dest


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
    args = parser.parse_args()
    if args.action == 'render':
        files = project_files(args.version)
        dest = args.destination.absolute()
        check_target(dest)
        dest.mkdir()
        write_tree(dest, files)
    else:
        with writer(LIVING):
            if args.action == 'seal':
                seal(args.version)
            else:
                print(create(args.slug, args.destination, args.interpretation, args.shared_access))


if __name__ == '__main__':
    try:
        main()
    except (OSError, ValueError, subprocess.SubprocessError) as error:
        sys.exit(str(error))
