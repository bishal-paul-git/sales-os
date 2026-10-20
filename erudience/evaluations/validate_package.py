"""Validate package structure and standalone skill reference parity; no live actions."""
from pathlib import Path
import json
import re

base = Path(__file__).resolve().parents[1]
skill = base / 'skills' / 'erudience-sales-os'
refs = skill / 'references'
errors = []
canonical = [base / 'AGENTS.md', base / 'ROADMAP.md']
for part in ['agents', 'workflows', 'operations', 'knowledge', 'config', 'memory', 'integrations']:
    canonical.extend(p for p in (base / part).glob('*') if p.is_file())
by_name = {p.name: p for p in canonical}
for p in refs.glob('*'):
    if p.name not in by_name or p.read_bytes() != by_name[p.name].read_bytes():
        errors.append(f'Reference drift: {p.name}')
for p in base.rglob('*.md'):
    text = p.read_text()
    if 'TODO' in text:
        errors.append(f'Unresolved template: {p}')
    for target in re.findall(r'\]\(([^)]+)\)', text):
        if '://' not in target and not target.startswith('#'):
            if not (p.parent / target.split('#')[0]).exists():
                errors.append(f'Broken link: {p.name} -> {target}')
for target in re.findall(r'references/[\w.-]+', (skill / 'SKILL.md').read_text()):
    target = target.rstrip('.')
    if not (skill / target).is_file():
        errors.append(f'Missing skill reference: {target}')
for p in base.rglob('*.json'):
    json.loads(p.read_text())
control = json.loads((base / 'config' / 'run-control.json').read_text())
if control['outreach']['enabled'] or control['outreach']['daily_send_cap'] != 0:
    errors.append('Draft package unexpectedly enables sending')
if control['schedule']['enabled'] or control['research']['paid_run_cap'] != 0:
    errors.append('Draft package unexpectedly enables scheduling or spending')
scenarios = json.loads((base / 'evaluations' / 'scenarios.json').read_text())
assert len({s['id'] for s in scenarios}) == len(scenarios)
if errors:
    raise SystemExit('\n'.join(errors))
print(f'PASS: links, JSON, {len(list(refs.glob("*")))} portable references and disabled execution defaults.')
print(f'{len(scenarios)} behavioural scenarios available; live integration tests not executed.')
