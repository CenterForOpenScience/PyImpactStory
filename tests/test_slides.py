from unittest import TestCase
from impact_product import Slides
import json

__author__ = 'ericabaranski'


class TestSlides(TestCase):
    def setUp(self):
        raw_json = open("Heather_slides")
        raw_dict = json.load(raw_json)
        self.slide = raw_dict.get("slides")
        self.s = Slides(self.slide[0])

    def test__parse_bib_info(self):
        bib = self.slide[0].get("biblio", {})
        Slides._parse_bib_info(self.s, bib)

        self.assertTrue(self.s._username)
        self.assertTrue(self.s._repository)
        self.assertFalse(self.s._published_date)

