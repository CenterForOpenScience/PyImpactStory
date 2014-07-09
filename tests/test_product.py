from unittest import TestCase
import json
from impact_product import Product

__author__ = 'ericabaranski'


class TestProduct(TestCase):
    def setUp(self):
        raw_json = open("./fixtures/HeatherPiwowar_070814.json")
        raw_dict = json.load(raw_json)
        product_list = raw_dict.get("products")
        self.p = Product(product_list[0])

        #Change to assertEqual unittest
        '''
        self.assertFalse(self.p._currently_updating)
        self.assertTrue(self.p._is_true_product)
        self.assertTrue(self.p._latest_diff_timestamp)
        '''

    def test__parse_aliases(self):
        aliases = self.p.aliases
        Product._parse_aliases(self.p, aliases)

        #Change to assertEqual unittest
        '''
        self.assertTrue(self.p._best_url)
        self.assertTrue(self.p._url)
        self.assertFalse(self.p._github)
        self.assertFalse(self.p._altmetric_com)
        self.assertTrue(self.p._doi)
        self.assertTrue(self.p._pmid)
        self.assertFalse(self.p._uuid)
        self.assertFalse(self.p._arxiv)
        '''
    def test__parse_product_bib(self):
        bib = self.p._bib_info
        Product._parse_product_bib(self.p, bib)

        #Change to assertEqual unittest
        '''
        self.assertFalse(self.p._genre)
        self.assertTrue(self.p._title)
        self.assertTrue(self.p._authors)
        self.assertTrue(self.p._year)
        self.assertTrue(self.p._free_fulltext_host)
        '''