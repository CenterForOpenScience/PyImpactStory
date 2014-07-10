from datetime import datetime
from product import Product


class Software(Product):
    def __init__(self, raw_product):
        Product.__init__(self, raw_product)
        bib_info = raw_product.get('biblio', {})
        self._parse_bib_info(bib_info)

    def _parse_bib_info(self, bib_info):
        self._create_date = bib_info.get('create_date', None)
        if self._create_date:
            datetime.strptime(str(self._create_date), "%Y-%m-%dT%H:%M:%SZ")

        self._description = str(bib_info.get('description', ""))
        self._last_push_date = bib_info.get('last_push_date', None)
        if self._last_push_date:
            datetime.strptime(str(self._last_push_date), "%Y-%m-%dT%H:%M:%SZ")
        self._owner = str(bib_info.get('owner', ""))

    def __str__(self):
        return unicode("genre: " + str(self._genre)
        + "\ntitle: " + str(self._title)
        + "\nauthors: " + str(self._authors)
        + "\nyear: " + str(self._year)
        + "\nfree_fulltext_host: " + str(self._free_fulltext_host)
        + "\ncreate_date: " + str(self._create_date)
        + "\ndescription: " + str(self._description)
        + "\nlast_push_date: " + str(self._last_push_date)
        + "\nowner: " + str(self._owner)
        + "\nhas_metrics: " + str(self._has_metrics)
        + "\nmetrics: \n" + str(self._display_metrics) + "\n")

    @property
    def create_date(self):
        return self._create_date

    @property
    def desription(self):
        return self._description

    @property
    def last_push_date(self):
        return self._last_push_date

    @property
    def owner(self):
        return self._owner


