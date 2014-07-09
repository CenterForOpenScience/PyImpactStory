from unittest import TestCase
from impact_product import Video
import json

__author__ = 'ericabaranski'


class TestVideo(TestCase):
    def setUp(self):
        raw_json = open("./fixtures/HeatherPiwowar_070914.json")
        raw_dict = json.load(raw_json)
        video = []
        self.product_list = raw_dict.get("products")
        for product in self.product_list:
            if '_tiid' in product:
                if product["genre"] == "video":
                    video.append(Video(product))
        self.v = video[0]

    def test__parse_bib_info(self):
        bib = self.v._bib_info
        Video._parse_bib_info(self.v, bib)

        #Change to assertEqual unittest
        '''
        self.assertTrue(self.v._published_date)
        self.assertTrue(self.v._repository)
        self.assertTrue(self.v._channel_title)
        '''