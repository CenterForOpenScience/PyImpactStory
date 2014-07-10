from product import Product


class Unknown(Product):
    def __init__(self, raw_product):
        Product.__init__(self, raw_product)
        bib_info = raw_product.get('slides', {})
        self._parse_bib_info(bib_info)

    def _parse_bib_info(self, bib_info):
        self._free_fulltext_url = str(bib_info.get ('free_fulltext_url', ""))
        self._first_page = str(bib_info.get ('first_page', ""))
        self._first_author = str(bib_info.get ('first_author', ""))
        self._journal = str(bib_info.get ('journal', ""))
        self._number = str(bib_info.get ('number', ""))
        self._volume = str(bib_info.get ('volume', ""))

    def __str__(self):
        return unicode("genre: " + str(self._genre)
        + "\ntitle: " + str(self._title)
        + "\nauthors: " + str(self._authors)
        + "\nyear: " + str(self._year)
        + "\nfree_fulltext_host: " + str(self._free_fulltext_host)
        + "\nfree_fulltext_url: " + str(self._free_fulltext_url)
        + "\nfirst_page: " + str(self._first_page)
        + "\nfirst_author: " + str(self._first_author)
        + "\njournal: " + str(self._journal)
        + "\nnumber: " + str(self._number)
        + "\nvolume: " + str(self._volume)
        + "\nhas_metrics: " + str(self._has_metrics)
        + "\nmetrics: \n" + str(self._display_metrics) + "\n")

    @property
    def free_fulltext_url(self):
        return self._free_fulltext_url

    @property
    def first_page(self):
        return self._first_page

    @property
    def first_author(self):
        return self._first_author

    @property
    def journal(self):
        return self._journal

    @property
    def number(self):
        return self._number

    @property
    def volume(self):
        return self._volume
