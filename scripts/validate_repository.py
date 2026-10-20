"""Check canonical layout, campaign references, tenancy and local links. No network."""
from pathlib import Path
import json
import re
import sys


def validate(root):
    root = Path(root)
    errors = []
    def read(path):
        try:
            return json.loads((root / path).read_text())
        except (OSError, ValueError) as exc:
            errors.append(f'{path}: {exc}')
            return {}
    def exists(path):
        if not isinstance(path, str) or not (root / path.split('#')[0]).is_file():
            errors.append(f'Missing canonical file: {path}')
    registry = read('businesses/registry.json').get('businesses', [])
    types = {v['id']: v for v in read('core/campaigns/types.json').get('types', [])}
    uses = {v['id'] for v in read('core/use-cases/catalog.json').get('use_cases', [])}
    ids, businesses, registered = set(), set(), set()
    for b in registry:
        bid = b['id']
        if bid in businesses:
            errors.append(f'Duplicate business: {bid}')
        businesses.add(bid)
        bp = b['path']
        if bp != f'businesses/{bid}':
            errors.append(f'Business path mismatch: {bid}')
        control = read(f'{bp}/config/run-control.json')
        if control.get('business_id') != bid:
            errors.append(f'Run control business mismatch: {bid}')
        offers = read(f'{bp}/offers/catalog.json')
        if offers.get('business_id') != bid:
            errors.append(f'Offer catalogue business mismatch: {bid}')
        offer_ids = {o['id'] for o in offers.get('offers', [])}
        index = read(f'{bp}/campaigns/index.json')
        if index.get('business_id') != bid:
            errors.append(f'Campaign registry business mismatch: {bid}')
        for e in index.get('campaigns', []):
            path = e['path'] + '/campaign.json'
            registered.add(path)
            c = read(path)
            if not c:
                continue
            cid = c.get('campaign_id')
            if cid in ids:
                errors.append(f'Duplicate campaign: {cid}')
            ids.add(cid)
            if c.get('business_id') != bid or not e['path'].startswith(bp + '/campaigns/'):
                errors.append(f'Cross-business campaign: {cid}')
            if cid != e.get('campaign_id') or c.get('status') != e.get('status') or c.get('type_id') != e.get('type_id'):
                errors.append(f'Campaign registry drift: {cid}')
            typ = types.get(c.get('type_id'))
            if not typ:
                errors.append(f'Unknown campaign type: {cid}')
            elif c.get('audience', {}).get('relationship') != typ['audience_class']:
                errors.append(f'Audience basis/type mismatch: {cid}')
            required = ['schema_version', 'audience', 'offer_ref', 'use_case_ids', 'agent_roles', 'sender_account_ref', 'private_audience_ref', 'sequence', 'metrics', 'activation', 'blockers']
            for field in required:
                if field not in c:
                    errors.append(f'{cid}: missing {field}')
            for field in ['core_workflow', 'business_workflow', 'strategy_path']:
                exists(c.get(field))
            ref = c.get('offer_ref', '')
            if ref != f'{bp}/offers/catalog.json#' + ref.split('#')[-1] or ref.split('#')[-1] not in offer_ids:
                errors.append(f'Unresolved business offer: {cid}')
            for use in c.get('use_case_ids', []):
                if use not in uses:
                    errors.append(f'Unknown use case: {cid}/{use}')
            for role in c.get('agent_roles', []):
                exists(f'core/agents/{role}.md')
            for field in ['countries','industries','company_types','decision_roles','relationship','inclusion','exclusion','eligibility_evidence']:
                if field not in c.get('audience', {}):
                    errors.append(f'{cid}: missing audience field {field}')
            a = c.get('activation', {})
            if a.get('enabled'):
                if not control.get('outreach', {}).get('enabled') or not c.get('sender_account_ref') or not c.get('private_audience_ref') or c.get('blockers'):
                    errors.append(f'Unready activation: {cid}')
                if c.get('status') not in ('approved','active'):
                    errors.append(f'Unapproved campaign activation: {cid}')
            if not a.get('approval_required', True):
                errors.append(f'Approval bypass: {cid}')
    for p in (root / 'businesses').glob('*/campaigns/*/campaign.json'):
        if str(p.relative_to(root)) not in registered:
            errors.append(f'Unregistered campaign: {p.relative_to(root)}')
    for p in root.rglob('*.json'):
        if '.git' not in p.parts:
            try:
                json.loads(p.read_text())
            except ValueError as exc:
                errors.append(f'Invalid JSON {p}: {exc}')
    for p in root.rglob('*.md'):
        if '.git' in p.parts:
            continue
        for target in re.findall(r'\]\(([^)]+)\)', p.read_text()):
            if '://' not in target and not target.startswith('#') and '<' not in target:
                if not (p.parent / target.split('#')[0]).exists():
                    errors.append(f'Broken link {p.relative_to(root)}: {target}')
    duplicates = list((root / 'core').glob('skills/*/references/*'))
    if duplicates:
        errors.append('Editable core skill reference copies reintroduced')
    legacy = root / 'erudience'
    if legacy.exists() and any(p.is_file() and p.name != 'README.md' for p in legacy.rglob('*')):
        errors.append('Legacy erudience tree reintroduced; use businesses/erudience')
    migration = read('governance/migration-2026-10-20.json')
    for old, new in migration.get('path_map', {}).items():
        exists(new)
    return errors


if __name__ == '__main__':
    root = Path(__file__).resolve().parents[1]
    errors = validate(root)
    if errors:
        print('\n'.join(errors))
        sys.exit(1)
    print('PASS: canonical layout, links, JSON, registered campaigns, business isolation and migration destinations.')
