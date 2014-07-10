from datetime import datetime
from product import Product


class Figure(Product):
    def __init__(self, raw_product):
        Product.__init__(self, raw_product)
        bib_info = raw_product.get('biblio', {})
        self._parse_bib_info(bib_info)

    def _parse_bib_info(self, bib_info):
        self._published_date = bib_info.get ('published_date', None)
        if self._published_date:
            datetime.strptime(str(self._published_date), "%H:%M, %b %d, %Y")
        self._repository = str(bib_info.get('repository', ""))
        self._is_oa_journal = str(bib_info.get('is_oa_journal', ""))

    def __str__(self):
        return unicode("genre: " + str(self._genre)
                + "\ntitle: " + str(self._title)
                + "\nauthors: " + str(self._authors)
                + "\nyear: " + str(self._year)
                + "\nfree_fulltext_host: " + str(self._free_fulltext_host)
                + "\npublished_date: " + str(self._published_date)
                + "\nrepository: " + str(self._repository)
                + "\nis_oa_journal: " + str(self._is_oa_journal)
                + "\nhas_metrics: " + str(self._has_metrics)
                + "\nmetrics: \n" + str(self._display_metrics) + "\n")

    @property
    def published_date(self):
        return self._published_date

    @property
    def repository(self):
        return self._repository

    @property
    def is_oa_journal(self):
        return self._is_oa_journal

