from unittest import TestCase
from impact_product import Software
import json

__author__ = 'ericabaranski'


class TestSoftware(TestCase):
    def setUp(self):
        raw_json = open("Heather_software")
        raw_dict = json.load(raw_json)
        self.software = raw_dict.get("software")
        self.so = Software(self.software[0])

    def test__parse_bib_info(self):
        bib = self.software[0].get("biblio", {})
        Software._parse_bib_info(self.so, bib)

        self.assertTrue(self.so._create_date)
        self.assertTrue(self.so._last_push_date)
        self.assertTrue(self.so._owner)
        self.assertTrue(self.so._description)

