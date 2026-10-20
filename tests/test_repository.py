"""Regression checks for duplicate campaigns and cross-business configuration drift."""
import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('validator', ROOT / 'scripts/validate_repository.py')
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


class RepositoryContractTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name) / 'repo'
        shutil.copytree(ROOT, self.root, ignore=shutil.ignore_patterns('.git', '__pycache__'))

    def tearDown(self):
        self.tmp.cleanup()

    def edit(self, path, mutate):
        p = self.root / path
        value = json.loads(p.read_text())
        mutate(value)
        p.write_text(json.dumps(value))

    def test_current_package(self):
        self.assertEqual([], mod.validate(self.root))

    def test_duplicate_campaign_rejected(self):
        self.edit('businesses/erudience/campaigns/index.json', lambda v: v['campaigns'].append(v['campaigns'][0].copy()))
        self.assertTrue(any('Duplicate campaign' in e for e in mod.validate(self.root)))

    def test_cross_business_rejected(self):
        self.edit('businesses/erudience/campaigns/au-telecom-partners/campaign.json', lambda v: v.update(business_id='other'))
        self.assertTrue(any('Cross-business' in e for e in mod.validate(self.root)))

    def test_unverified_activation_rejected(self):
        self.edit('businesses/erudience/campaigns/automation-newsletter/campaign.json', lambda v: v['activation'].update(enabled=True))
        self.assertTrue(any('Unready activation' in e for e in mod.validate(self.root)))

    def test_incorrect_audience_basis_rejected(self):
        self.edit('businesses/erudience/campaigns/automation-newsletter/campaign.json', lambda v: v['audience'].update(relationship='cold-business'))
        self.assertTrue(any('Audience basis/type mismatch' in e for e in mod.validate(self.root)))

    def test_unknown_offer_rejected(self):
        self.edit('businesses/erudience/campaigns/au-telecom-partners/campaign.json', lambda v: v.update(offer_ref='businesses/other/offers/catalog.json#invented'))
        self.assertTrue(any('Unresolved business offer' in e for e in mod.validate(self.root)))

    def test_legacy_fork_rejected(self):
        (self.root / 'erudience/agents').mkdir()
        (self.root / 'erudience/agents/duplicate.md').write_text('Duplicate procedure')
        self.assertTrue(any('Legacy erudience tree' in e for e in mod.validate(self.root)))

    def test_missing_migrated_asset_rejected(self):
        (self.root / 'core/templates/email-sequence.md').unlink()
        self.assertTrue(any('Missing canonical file' in e for e in mod.validate(self.root)))


if __name__ == '__main__':
    unittest.main()
