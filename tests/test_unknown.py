from unittest import TestCase
from impact_product import Unknown
import json

__author__ = 'ericabaranski'


class TestUnknown(TestCase):
    def setUp(self):
        raw_json = open("Heather_unknown")
        raw_dict = json.load(raw_json)
        self.unknown = raw_dict.get("unknown")
        self.u = Unknown(self.unknown[0])

    def test__parse_bib_info(self):
        bib = self.unknown[0].get("biblio", {})
        Unknown._parse_bib_info(self.u, bib)

        self.assertTrue(self.u._free_fulltext_host)
        self.assertTrue(self.u._free_fulltext_url)
        self.assertFalse(self.u._first_page)
        self.assertTrue(self.u._first_author)
        self.assertFalse(self.u._journal)
        self.assertFalse(self.u._number)
        self.assertFalse(self.u._volume)