from unittest import TestCase
from impact_product import Article
import json
from datetime import datetime

__author__ = 'ericabaranski'


class TestArticle(TestCase):
    def setUp(self):
        raw_json = open("./fixtures/HeatherPiwowar_070814.json")
        raw_dict = json.load(raw_json)
        article = []
        self.product_list = raw_dict.get("products")

        for product in self.product_list:
            if '_tiid' in product:
                if product["genre"] == "article" and product['_tiid'] == "rgp7ctxzzsg8prl42s9qu77z":
                    self.a = Article(product)

    def test__parse_bib_info(self):
        bib = self.a._bib_info
        Article._parse_bib_info(self.a, bib)

        self.assertEquals(self.a.issn, "17511577")
        self.assertEquals(self.a._journal, unicode("Journal of Informetrics"))
        self.assertEquals(self.a._number, "")
        self.assertEquals(self.a._volume, "")
        self.assertEquals(self.a._first_page, "")
        self.assertEquals(self.a._first_author, "")
        self.assertEquals(self.a._is_oa_journal, 'False')
        self.assertEquals(self.a._repository, "Elsevier BV")
        self.assertEquals(self.a._full_citation, "")
        self.assertEquals(self.a._published_date, None)
        self.assertNotIsInstance(self.a._published_date, datetime)

        self.assertEquals(self.a._day, 0)
        self.assertEquals(self.a._month,"Apr")
        self.assertEquals(self.a._full_citation_type, "")
        self.assertEquals(self.a._h1, "")
        self.assertEquals(self.a._oai_id, "")
        self.assertEquals(self.a._free_fulltext_url,"http://europepmc.org/abstract/MED/21339841")
