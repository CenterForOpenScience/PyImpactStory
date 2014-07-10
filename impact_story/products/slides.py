from datetime import datetime
from product import Product


class Slides(Product):
    def __init__(self, raw_product):
        Product.__init__(self, raw_product)
        bib_info = raw_product.get('slides', {})
        self._parse_bib_info(bib_info)

    def _parse_bib_info(self, bib_info):
        self._repository = str(bib_info.get('repository', ""))
        self._username = str(bib_info.get('username', ""))
        self._published_date = bib_info.get('published_date', None)
        if self._published_date:
            datetime.strptime(str(self._published_date), "%Y-%m-%dT%H:%M:%SZ")

    def __str__(self):
        return unicode("genre: " + str(self._genre)
        + "\ntitle: " + str(self._title)
        + "\nauthors: " + str(self._authors)
        + "\nyear: " + str(self._year)
        + "\nfree_fulltext_host: " + str(self._free_fulltext_host)
        + "\nrepository: " + str(self._repository)
        + "\nusername: " + str(self._username)
        + "\npublished_date: " + str(self._published_date)
        + "\nhas_metrics: " + str(self._has_metrics)
        + "\nmetrics: \n" + str(self._display_metrics) + "\n")

    @property
    def repository(self):
        return self._repository

    @property
    def username(self):
        return self._username

    @property
    def published_date(self):
        return self._published_date
