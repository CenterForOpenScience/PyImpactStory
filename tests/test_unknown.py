from unittest import TestCase
from impact_product import Unknown
import json

__author__ = 'ericabaranski'


class TestUnknown(TestCase):
    def setUp(self):
        raw_json = open("./fixtures/HeatherPiwowar_070914.json")
        raw_dict = json.load(raw_json)
        unknown = []
        self.product_list = raw_dict.get("products")
        for product in self.product_list:
            if '_tiid' in product:
                if product["genre"] == "unknown":
                    unknown.append(Unknown(product))
        self.u = unknown[0]

    def test__parse_bib_info(self):
        bib = self.u._bib_info
        Unknown._parse_bib_info(self.u, bib)

        #Change to assertEqual unittest
        '''
        self.assertTrue(self.u._free_fulltext_host)
        self.assertTrue(self.u._free_fulltext_url)
        self.assertTrue(self.u._first_page)
        self.assertTrue(self.u._first_author)
        self.assertTrue(self.u._journal)
        self.assertTrue(self.u._number)
        self.assertTrue(self.u._volume)
        '''