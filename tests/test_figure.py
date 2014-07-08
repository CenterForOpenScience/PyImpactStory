from unittest import TestCase
from impact_product import Figure
import json

__author__ = 'ericabaranski'


class TestFigure(TestCase):
    def setUp(self):
        raw_json = open("Heather_figures")
        raw_dict = json.load(raw_json)
        self.figure = raw_dict.get("figures")
        self.f = Figure(self.figure[0])

    def test__parse_bib_info(self):
        bib = self.figure[0].get("biblio", {})
        Figure._parse_bib_info(self.f, bib)

        self.assertFalse(self.f._is_oa_journal)
        self.assertTrue(self.f._repository)
        self.assertTrue(self.f._published_date)
