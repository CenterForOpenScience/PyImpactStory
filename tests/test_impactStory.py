from unittest import TestCase
from impact_story_class import ImpactStory
from impact_story_class import ImpactStoryException
from impact_story_class import ImpactStoryHTTPException
from impact_story_class import ImpactStoryParseException

from impact_product import Article
from impact_product import Dataset
from impact_product import Figure
from impact_product import Slides
from impact_product import Software
from impact_product import Unknown
from impact_product import Video
from impact_product import Webpage
import requests
import json

__author__ = 'saman'


class TestImpactStory(TestCase):

    def setUp(self):
        self.heather = ImpactStory.from_id("Heather Piwowar")
        self.saman = ImpactStory.from_id("Saman Ehsan")
        self.brian = ImpactStory.from_id("Brian Nosek")

    # test for valid username
    def test_from_id_valid(self):
        impact_story_obj = ImpactStory.from_id("Heather Piwowar")
        self.assertIsInstance(impact_story_obj, ImpactStory)

    # test for invalid username
    def test_from_id_invalid(self):
        with self.assertRaises(ImpactStoryHTTPException) as cm:
            ImpactStory.from_id("Htr Pwr")
        exception = cm.exception
        self.failUnlessRaises(exception)

    # test getting JSON data from file
    def test_from_file_json(self):
        json_file = "./fixtures/HeatherPiwowar_070814.json"
        impact_story_obj = ImpactStory.from_file(json_file)
        self.assertIsInstance(impact_story_obj, ImpactStory)

    # test corrupted JSON file
    def test_from_file_corrupted(self):
        corrupted_json = "./fixtures/Corrupted_JSON.json"
        with self.assertRaises(ImpactStoryParseException) as cm:
            ImpactStory.from_file(corrupted_json)
        exception = cm.exception
        self.failUnlessRaises(exception)

    # test wrong file type
    def test_from_file_csv(self):
        csv_file = "./fixtures/HeatherPiwowar_070814.csv"
        ImpactStory.from_file(csv_file)
        self.assertTrue("File type is not JSON")


    # JSON with no new attributes
    def test_updated_dict(self):
        heather_raw = "./fixtures/HeatherPiwowar_070814.json"
        heather_json = open(heather_raw)
        raw_dict = json.load(heather_json)
        product_list = raw_dict.get('products', [])
        ImpactStory._updated_dict(self.heather, product_list)
        self.assertFalse(self.heather._new_attributes)

    # User with all possible product types
    def test__parse_products_all(self):
        heather_raw = "./fixtures/HeatherPiwowar_070814.json"
        heather_json = open(heather_raw)
        raw_dict = json.load(heather_json)
        product_list = raw_dict.get('products', [])
        ImpactStory._parse_products(self.heather, product_list)

        self.assertTrue(self.heather.articles)
        self.assertTrue(self.heather.datasets)
        self.assertTrue(self.heather.figures)
        self.assertTrue(self.heather.slides)
        self.assertTrue(self.heather.software)
        self.assertTrue(self.heather.unknown)
        self.assertTrue(self.heather.videos)
        self.assertTrue(self.heather.webpages)

    # User with no products
    def test__parse_products_none(self):
        saman_raw = "./fixtures/SamanEhsan_070814.json"
        product_json = open(saman_raw)
        product_dict = json.load(product_json)
        product_list = product_dict.get('products', [])
        ImpactStory._parse_products(self.saman, product_list)

        self.assertFalse(self.saman.articles)
        self.assertFalse(self.saman.datasets)
        self.assertFalse(self.saman.figures)
        self.assertFalse(self.saman.slides)
        self.assertFalse(self.saman.software)
        self.assertFalse(self.saman.unknown)
        self.assertFalse(self.saman.videos)
        self.assertFalse(self.saman.webpages)

    # Typical user
    def test__parse_products(self):
        brian_raw = "./fixtures/BrianNosek_070814.json"
        product_json = open(brian_raw)
        product_dict = json.load(product_json)
        product_list = product_dict.get('products', None)
        ImpactStory._parse_products(self.brian, product_list)

        self.assertTrue(self.brian.articles)
        self.assertFalse(self.brian.datasets)
        self.assertFalse(self.brian.figures)
        self.assertFalse(self.brian.slides)
        self.assertTrue(self.brian.software)
        self.assertTrue(self.brian.unknown)
        self.assertFalse(self.brian.videos)
        self.assertTrue(self.brian.webpages)