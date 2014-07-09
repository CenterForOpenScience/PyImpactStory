from unittest import TestCase
from impact_product import Figure
import json

__author__ = 'ericabaranski'


class TestFigure(TestCase):
    def setUp(self):
        raw_json = open("./fixtures/HeatherPiwowar_070914.json")
        raw_dict = json.load(raw_json)
        figure = []
        self.product_list = raw_dict.get("products")
        for product in self.product_list:
            if '_tiid' in product:
                if product["genre"] == "figure":
                    figure.append(Figure(product))
        self.f = figure[1]

    def test__parse_bib_info(self):
        bib = self.f._bib_info
        Figure._parse_bib_info(self.f, bib)

        #Change to assertEqual unittest
        '''
        self.assertFalse(self.f._is_oa_journal)
        self.assertTrue(self.f._repository)
        self.assertTrue(self.f._published_date)
        '''