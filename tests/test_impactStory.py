from unittest import TestCase
from impact_story_class import ImpactStory
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
        self.heather = ImpactStory("Heather Piwowar")
        self.saman = ImpactStory("Saman Ehsan")
        self.brian = ImpactStory("Brian Nosek")
        self.raw = requests.get("https://impactstory.org/profile/HthrPwr?hide=markup,awards")

    # tests making a GET request given an incorrect name
    def test_wrong_username(self):
        class ImpactStoryException(Exception):
            pass

        class ImpactStoryHTTPException(ImpactStoryException):
            def __init__(self, status_code, msg):
                self.status_code = status_code
                self.msg = msg

        class ImpactStoryParseException(ImpactStoryException):
            pass

        self.failUnlessRaises(ImpactStoryHTTPException(self.raw.status_code, self.raw.text))

    # JSON with no new attributes
    def test_updated_dict(self):
        product_json = open('Heather_Products')
        product_dict = json.load(product_json)
        product_list = product_dict.get('products', None)
        ImpactStory._updated_dict(self.heather, product_list)
        self.assertFalse(self.heather._new_attributes)


    # User with all possible product types
    def test__parse_products_all(self):
        product_json = open('Heather_Products')
        product_dict = json.load(product_json)
        product_list = product_dict.get('products', None)
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
        product_json = open('Saman_Products')
        product_dict = json.load(product_json)
        product_list = product_dict.get('products', None)
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
        product_json = open('Brian_Products')
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