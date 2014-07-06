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
        self._articles = []
        self._datasets = []
        self._figures = []
        self._slides = []
        self._software = []
        self._unknown = []
        self._videos = []
        self._webpages = []
        self._all = {'articles': self._articles,
                     'datasets': self._datasets,
                     'figures': self._figures,
                     'slides': self._slides,
                     'software': self._software,
                     'unknown': self._unknown,
                     'videos': self._videos,
                     'webpages': self._webpages
                     }

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

        url = "https://impactstory.org/profile/"
        name = "Hther Pwr"
        name = name.replace(" ", "")
        raw = requests.get(url + name + "?hide=markup,awards")

        if raw.status_code == 200:
            try:
                self._parse_raw(raw.json())
            except ValueError as exception:
                raise ImpactStoryParseException(exception.message)
        else:
            self.failUnlessRaises(ImpactStoryHTTPException(raw.status_code, raw.text))

    # User with all possible product types
    def test__parse_products(self):
        product_json = open('Heather_Products')
        product_dict = json.load(product_json)
        product_list = product_dict.get('products', None)

        for product in product_list:
            if '_tiid' in product:
                self.assertTrue('_tiid' in product)

                if product["genre"] == "article":
                    self.assertTrue(product["genre"] == "article")
                    self._articles.append(Article(product))
                    num = len(self._articles)
                    self.assertTrue(type(self._articles[num - 1]))

                elif product["genre"] == "dataset":
                    self.assertTrue(product["genre"] == "dataset")
                    self._datasets.append(Dataset(product))
                    num = len(self._datasets)
                    self.assertTrue(type(self._datasets[num - 1]))

                elif product["genre"] == "figure":
                    self.assertTrue(product["genre"] == "figure")
                    self._figures.append(Figure(product))
                    num = len(self._figures)
                    self.assertTrue(type(self._figures[num - 1]))

                elif product["genre"] == "slides":
                    self.assertTrue(product["genre"] == "slides")
                    self._slides.append(Slides(product))
                    num = len(self._slides)
                    self.assertTrue(type(self._slides[num - 1]))

                elif product["genre"] == "software":
                    self.assertTrue(product["genre"] == "software")
                    self._software.append(Software(product))
                    num = len(self._software)
                    self.assertTrue(type(self._software[num - 1]))

                elif product["genre"] == "unknown":
                    self.assertTrue(product["genre"] == "unknown")
                    self._unknown.append(Unknown(product))
                    num = len(self._unknown)
                    self.assertTrue(type(self._unknown[num - 1]))

                elif product["genre"] == "video":
                    self.assertTrue(product["genre"] == "video")
                    self._videos.append(Video(product))
                    num = len(self._videos)
                    self.assertTrue(type(self._videos[num - 1]))

                elif product["genre"] == "webpage":
                    self.assertTrue(product["genre"] == "webpage")
                    self._webpages.append(Webpage(product))
                    num = len(self._webpages)
                    self.assertTrue(type(self._webpages[num - 1]))

                else:
                    print "End of Profile"
                    self.assertTrue("End of Profile")

    # User with articles
    def test_articles(self):
        user = ImpactStory("Heather Piwowar")
        self.assertTrue(user.articles)

    # User with no articles
    def test_articles(self):
        user = ImpactStory("Saman Ehsan")
        self.assertFalse(user.datasets)

    # User with no datasets
    def test_datasets(self):
        user = ImpactStory("Saman Ehsan")
        self.assertFalse(user.datasets)

    def test_figures(self):
        pass

    def test_slides(self):
        user = ImpactStory("Erica Baranski")
        self.assertTrue(user.slides)

    def test_software(self):
        pass

    def test_unknown(self):
        pass

    def test_videos(self):
        pass

    def test_webpages(self):
        pass

    def test_all(self):
        pass