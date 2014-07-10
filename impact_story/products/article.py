from datetime import datetime
from product import Product


class Article(Product):
    def __init__(self, raw_product):
        Product.__init__(self, raw_product)
        bib_info = raw_product.get('biblio', {})
        self._parse_bib_info(bib_info)

    def _parse_bib_info(self, bib_info):
        self._issn = str(bib_info.get('issn', ""))
        self._journal = bib_info.get('journal', "")
        self._number = str(bib_info.get('number', ""))
        self._volume = str(bib_info.get('volume', ""))
        self._first_page = str(bib_info.get('first_page', ""))
        self._first_author = str(bib_info.get('first_author', ""))
        self._is_oa_journal = str(bib_info.get('is_oa_journal', ""))
        self._repository = str(bib_info.get('repository', ""))
        self._full_citation = str(bib_info.get('full_citation', ""))
        self._published_date = bib_info.get('published_date', None)
        if self._published_date:
            datetime.strptime(str(self._published_date), "%H:%M, %b %d, %Y")
        self._day = int(bib_info.get('day',0))
        self._month = str(bib_info.get('month', ""))
        self._full_citation_type = str(bib_info.get ('full_citation_type', ""))
        self._h1 = bib_info.get('h1', "")
        self._oai_id = str(bib_info.get('oai_id', ""))
        self._free_fulltext_url = str(bib_info.get('free_fulltext_url', ""))

    def __str__(self):
        return unicode("genre: " + str(self._genre)
                + "\ntitle: " + str(self._title)
                + "\nauthors: " + str(self._authors)
                + "\nissn: " + str(self._issn)
                + "\njournal: " + str(self._journal)
                + "\nnumber: " + str(self._number)
                + "\nvolume: " + str(self._volume)
                + "\nfirst_page: " + str(self._first_page)
                + "\nfirst_author: " + str(self._first_author)
                + "\nis_oa_journal: " + str(self._is_oa_journal)
                + "\nrepository: " + str(self._repository)
                + "\nfull_citation: " + str(self._full_citation)
                + "\npublished_date: " + str(self._published_date)
                + "\nday: " + str(self._day)
                + "\nmonth: " + str(self._month)
                + "\nyear: " + str(self._year)
                + "\nfull_citation_type: " + str(self._full_citation_type)
                + "\nh1: " + str(self._h1)
                + "\noai_id: " + str(self._oai_id)
                + "\nfree_fulltext_url: " + str(self._free_fulltext_url)
                + "\nfree_fulltext_host: " + str(self._free_fulltext_host)
                + "\nhas_metrics: " + str(self._has_metrics)
                + "\nmetrics: \n" + str(self._display_metrics) + "\n")

    @property
    def issn(self):
        return self._issn

    @property
    def journal(self):
        return self._journal

    @property
    def number(self):
        return self._number

    @property
    def volume(self):
        return self._volume

    @property
    def first_page(self):
        return self._first_page

    @property
    def first_author(self):
        return self._first_author
    @property
    def is_oa_journal(self):
        return self._is_oa_journal

    @property
    def repository(self):
        return self._repository

    @property
    def full_citation(self):
        return self._full_citation

    @property
    def published_date(self):
        return self._published_date

    @property
    def day(self):
        return self._day

    @property
    def month(self):
        return self._month

    @property
    def full_citation_type(self):
        return self._full_citation_type

    @property
    def h1(self):
        return self._h1

    @property
    def oai_id(self):
        return self._oai_id

    @property
    def free_fulltext_url(self):
        return self._free_fulltext_url

