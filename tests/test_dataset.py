from unittest import TestCase
from impact_product import Dataset
import json

__author__ = 'ericabaranski'


class TestDataset(TestCase):
    def setUp(self):
        raw_json = open("./fixtures/HeatherPiwowar_070914.json")
        raw_dict = json.load(raw_json)
        dataset = []
        self.product_list = raw_dict.get("products")
        for product in self.product_list:
            if '_tiid' in product:
                if product["genre"] == "dataset":
                    dataset.append(Dataset(product))
        self.d = dataset[1]

    def test__parse_bib_info(self):
        bib = self.d._bib_info
        Dataset._parse_bib_info(self.d, bib)

        #Change to assertEqual unittest
        '''
        self.assertFalse(self.d._is_oa_journal)
        self.assertTrue(self.d._repository)
        self.assertTrue(self.d._published_date)
        '''