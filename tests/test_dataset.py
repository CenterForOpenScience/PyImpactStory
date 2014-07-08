from unittest import TestCase
from impact_product import Dataset
import json

__author__ = 'ericabaranski'


class TestDataset(TestCase):
    def setUp(self):
        raw_json = open("Heather_datasets")
        raw_dict = json.load(raw_json)
        self.dataset = raw_dict.get("datasets")
        self.d = Dataset(self.dataset[0])

    def test__parse_bib_info(self):
        bib = self.dataset[0].get("biblio", {})
        Dataset._parse_bib_info(self.d, bib)

        self.assertFalse(self.d._is_oa_journal)
        self.assertTrue(self.d._repository)
        self.assertFalse(self.d._published_date)