from unittest import TestCase
from impact_product import Slides
import json

__author__ = 'ericabaranski'


class TestSlides(TestCase):
    def setUp(self):
        raw_json = open("./fixtures/HeatherPiwowar_070914.json")
        raw_dict = json.load(raw_json)
        slides = []
        self.product_list = raw_dict.get("products")
        for product in self.product_list:
            if '_tiid' in product:
                if product["genre"] == "slides":
                    slides.append(Slides(product))
        self.s = slides[3]

    def test__parse_bib_info(self):
        bib = self.s._bib_info
        Slides._parse_bib_info(self.s, bib)

        #Change to assertEqual unittest
        '''
        self.assertTrue(self.s._username)
        self.assertTrue(self.s._repository)
        self.assertFalse(self.s._published_date)
        '''
