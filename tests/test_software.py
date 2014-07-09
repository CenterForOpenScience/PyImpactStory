from unittest import TestCase
from impact_product import Software
import json

__author__ = 'ericabaranski'


class TestSoftware(TestCase):
    def setUp(self):
        raw_json = open("./fixtures/HeatherPiwowar_070814.json")
        raw_dict = json.load(raw_json)
        software = []
        self.product_list = raw_dict.get("products")
        for product in self.product_list:
            if '_tiid' in product:
                if product["genre"] == "software":
                    software.append(Software(product))
        self.so = software[0]

    def test__parse_bib_info(self):
        bib = self.so._bib_info
        Software._parse_bib_info(self.so, bib)

        #Change to assertEqual unittest
        '''
        self.assertTrue(self.so._create_date)
        self.assertTrue(self.so._last_push_date)
        self.assertTrue(self.so._owner)
        self.assertTrue(self.so._description)
        '''
