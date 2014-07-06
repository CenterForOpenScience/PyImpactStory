from unittest import TestCase
from impact_story_class import ImpactStory
import json

__author__ = 'saman'


class TestProduct(TestCase):

    def setUp(self):
        pass

    def test__parse_aliases(self):
        aliases_json = open('Heather_aliases')
        aliases_dict = json.load(aliases_json)
        alias = aliases_dict.get('aliases', None)

        self._best_url = alias.get('best_url', None)
        self.assertTrue(self._best_url)

        self._url = alias.get('url', None)
        self.assertTrue(self._url)

        self._github = alias.get('github', None)
        self.assertFalse(self._github)

        self._altmetric_com = alias.get('altmetric_com', None)
        self.assertTrue(self._altmetric_com)

        self._doi = alias.get('doi', None)
        self.assertTrue(self._doi)

        self._pmid = alias.get('pmid', None)
        self.assertFalse(self._pmid)

        self._uuid = alias.get('uuid', None)
        self.assertFalse(self._uuid)

        self._pmc = alias.get('pmc', None)
        self.assertFalse(self._pmc)

        self._arxiv = alias.get('arxiv', None)
        self.assertFalse(self._arxiv)



    def test__parse_product_bib(self):
        pass

    def test__parse_metrics(self):
        pass

    def test_display_metrics(self):
        pass


    '''
    def test_tiid(self):
        self.fail()

    def test_awardedness_score(self):
        self.fail()

    def test_currently_updating(self):
        self.fail()

    def test_has_metrics(self):
        self.fail()

    def test_has_new_metric(self):
        self.fail()

    def test_metric_by_name(self):
        self.fail()

    def test_metrics(self):
        self.fail()

    def test_is_true_product(self):
        self.fail()

    def test_latest_diff_timestamp(self):
        self.fail()

    def test_has_percentiles(self):
        self.fail()

    def test_best_url(self):
        self.fail()

    def test_url(self):
        self.fail()

    def test_github(self):
        self.fail()

    def test_altmetric_com(self):
        self.fail()

    def test_doi(self):
        self.fail()

    def test_pmid(self):
        self.fail()

    def test_uuid(self):
        self.fail()

    def test_pmc(self):
        self.fail()

    def test_arxiv(self):
        self.fail()

    def test_genre(self):
        self.fail()

    def test_title(self):
        self.fail()

    def test_authors(self):
        self.fail()

    def test_year(self):
        self.fail()

    def test_free_fulltext_host(self):
        self.fail()
    '''