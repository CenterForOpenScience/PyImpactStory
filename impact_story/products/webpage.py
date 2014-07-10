from product import Product


class Webpage(Product):
    def __init__(self, raw_product):
        Product.__init__(self, raw_product)

    def __str__(self):
        return unicode("genre: " + str(self._genre)
        + "\ntitle: " + str(self._title)
        + "\nauthors: " + str(self._authors)
        + "\nyear: " + str(self._year)
        + "\nfree_fulltext_host: " + str(self._free_fulltext_host)
        + "\nhas_metrics: " + str(self._has_metrics)
        + "\nmetrics: \n" + str(self._display_metrics) + "\n")