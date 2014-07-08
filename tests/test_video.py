from unittest import TestCase
from impact_product import Video
import json

__author__ = 'ericabaranski'


class TestVideo(TestCase):
    def setUp(self):
        raw_json = open("Heather_video")
        raw_dict = json.load(raw_json)
        self.video = raw_dict.get("video")
        self.v = Video(self.video[0])

    def test__parse_bib_info(self):
        bib = self.video[0].get("biblio", {})

        self.assertTrue(self.v._published_date)
        self.assertTrue(self.v._repository)
        self.assertFalse(self.v._channel_title)
