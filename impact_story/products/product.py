from datetime import datetime
from metric import Metric

"""
Generic object type for all impactstory products
extended by Article, Dataset, Figure, Slides,
Software, Video, Website & Unknown.
"""


class Product:
    def __init__(self, raw_product):
        self._tiid = str(raw_product.get('_tiid', ''))
        self._awardedness_score = int(raw_product.get('awardedness_score', 0))
        self._profile_id = int(raw_product.get('profile_id', 0))

        # parsed aliases
        self._aliases = dict(raw_product.get('aliases', {}))
        self._parse_aliases(self._aliases)

        # parsed bibliographic information
        self._bib_info = dict(raw_product.get('biblio', {}))
        self._parse_product_bib(self._bib_info)

        # parsed metrics
        self._is_true_product = bool(raw_product.get('is_true_product', False))
        self._latest_diff_timestamp = raw_product.get('latest_diff_timestamp', None)
        if self._latest_diff_timestamp:
            datetime.strptime(str(self._latest_diff_timestamp), "%Y-%m-%dT%H:%M:%S.%f")

        self._metric_by_name = dict(raw_product.get('metric_by_name', {}))
        self._metrics = []
        self._has_metrics = bool(raw_product.get('has_metrics', False))
        self._metrics_raw_sum = int(raw_product.get('metrics_raw_sum', 0))

        if self._has_metrics is True:
            self._parse_metrics(raw_product.get('metrics', []))

        self._display_metrics = []
        self.display_metrics()

    def _parse_aliases(self, alias):
        self._best_url = str(alias.get('best_url', ""))
        self._url = alias.get('url', [])
        self._github = alias.get('github', [])
        self._altmetric_com = alias.get('altmetric_com', [])
        self._doi = alias.get('doi', [])
        self._pmid = alias.get('pmid', [])
        self._uuid = alias.get('uuid', [])
        self._pmc = alias.get('pmc', [])
        self._arxiv = alias.get('arxiv',[])

    def _parse_product_bib(self, bib_info):
        self._genre = str(bib_info.get('genre', ""))
        self._title = bib_info.get('title', "")
        self._authors = bib_info.get('authors', None)
        self._year = str(bib_info.get('year', ""))
        self._free_fulltext_host = bib_info.get('free_fulltext_host', None)

    def _parse_metrics(self, metrics):
        for metric in metrics:
            self._metrics.append(Metric(metric))
    '''
    Creates a list of metrics represented as strings
    Used in Project subclasses to display metric info
    '''
    def display_metrics(self):
        display_metrics = []
        for metric in self._metrics:
            display_metrics.append(str(metric))

        display_metrics = "\n".join(self._display_metrics)
        self._display_metrics = display_metrics

    @property
    def bib_info(self):
        return self._bib_info

    @property
    def tiid(self):
        return self._tiid

    @property
    def awardedness_score(self):
        return self._awardedness_score

    @property
    def aliases(self):
        return self._aliases

    @property
    def has_metrics(self):
        return self._has_metrics

    @property
    def metric_by_name(self):
        return self._metric_by_name

    @property
    def metrics(self):
        return self._metrics

    @property
    def is_true_product(self):
        return self._is_true_product

    @property
    def latest_diff_timestamp(self):
        return self._latest_diff_timestamp

    @property
    def best_url(self):
        return self._best_url

    @property
    def url(self):
        return self._url

    @property
    def github(self):
        return self._github

    @property
    def altmetric_com(self):
        return self._altmetric_com

    @property
    def doi(self):
        return self._doi

    @property
    def pmid(self):
        return self._pmid

    @property
    def uuid(self):
        return self._uuid

    @property
    def pmc(self):
        return self._pmc

    @property
    def arxiv(self):
        return self._arxiv

    @property
    def genre(self):
        return self._genre

    @property
    def title(self):
        return self._title

    @property
    def authors(self):
        return self._authors

    @property
    def year(self):
        return self._year

    @property
    def free_fulltext_host(self):
        return self._free_fulltext_host
