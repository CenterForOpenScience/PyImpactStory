from unittest import TestCase
from impact_product import Article
import json

__author__ = 'ericabaranski'


class TestArticle(TestCase):
    def setUp(self):
        raw_json = open("Heather_articles")
        raw_dict = json.load(raw_json)
        self.article = raw_dict.get("articles")
        self.a = Article(self.article[0])

    def test__parse_bib_info(self):
        bib = self.article[0].get("biblio", {})
        Article._parse_bib_info(self.a, bib)

        self.assertTrue(self.a._issn)
        self.assertTrue(self.a._journal)
        self.assertFalse(self.a._number)
        self.assertFalse(self.a._volume)
        self.assertFalse(self.a._first_page)
        self.assertFalse(self.a._first_author)
        self.assertTrue(self.a._is_oa_journal)
        self.assertTrue(self.a._repository)
        self.assertFalse(self.a._full_citation)
        self.assertFalse(self.a._published_date)
        self.assertFalse(self.a._day)
        self.assertFalse(self.a._month)
        self.assertFalse(self.a._full_citation_type)
        self.assertFalse(self.a._h1)
        self.assertFalse(self.a._oai_id)
        self.assertTrue(self.a._free_fulltext_url)