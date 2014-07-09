from datetime import datetime

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


class Metric:
    def __init__(self, raw_metrics):
        self._audience = str(raw_metrics.get('audience', ""))
        self._display_count = int(raw_metrics.get('display_count', 0))
        self._display_interaction = str(raw_metrics.get('display_interaction', ""))
        self._display_order = int(raw_metrics.get('display_order', 0))
        self._display_provider = str(raw_metrics.get('display_provider', ""))
        self._engagement_type = str(raw_metrics.get('engagement_type', ""))
        self._hide_badge = bool(raw_metrics.get('hide_badge', False))
        self._interaction = str(raw_metrics.get('interaction', ""))
        self._is_highly = bool(raw_metrics.get('is_highly', False))
        self._latest_nonzero_refresh_timestamp = raw_metrics.get('latest_nonzero_refresh_timestamp', None)
        if self._latest_nonzero_refresh_timestamp:
            datetime.strptime(str(self._latest_nonzero_refresh_timestamp), "%Y-%m-%dT%H:%M:%S.%f")

        self._percentile_value_string = raw_metrics.get('percentile_value_string', None)
        self._provider_name = str(raw_metrics.get('provider_name', ""))
        self._diff_value = raw_metrics.get('diff_value', None)
        self._diff_window_length = raw_metrics.get('diff_window_length', None)
        self._drilldown_url = str(raw_metrics.get('drilldown_url', ""))
        self._fully_qualified_metric_name = str(raw_metrics.get('fully_qualified_metric_name', ""))
        self._percentile = raw_metrics.get('percentile', None)
        if self._percentile:
            self._parse_percentiles(self._percentile)

        # unique attributes in most_recent_snap
        self._most_recent_snap = dict(raw_metrics.get('most_recent_snap', {}))
        self._collected_date = self._most_recent_snap.get('collected_date', None)
        if self._collected_date:
            datetime.strptime(str(self._collected_date), "%Y-%m-%dT%H:%M:%S.%f")
        self._value = self._most_recent_snap.get('value', None) #can be int or list

    def _parse_percentiles(self, percentiles):
        self._host = str(percentiles.get('host', ""))
        self._mendeley_discipline = percentiles.get('mendeley_discipline', None)
        self._provider = str(percentiles.get('provider', ""))

    def __str__(self):
        return ("\naudience: " + str(self._audience)
                + "\ndisplay_count: " + str(self._display_count)
                + "\ndisplay_interaction: " + str(self._display_interaction)
                + "\ndisplay_order: " + str(self._display_order)
                + "\ndisplay_provider: " + str(self._display_provider)
                + "\nengagement_type: " + str(self._engagement_type)
                + "\nhide_badge: " + str(self._hide_badge)
                + "\ninteraction: " + str(self._interaction)
                + "\nis_highly: " + str(self._is_highly)
                + "\nlatest_nonzero_refresh_timestamp: "
                + str(self._latest_nonzero_refresh_timestamp)
                + "\npercentile: " + str(self._percentile)
               	+ "\npercentile_value_string: " + str(self._percentile_value_string)
                + "\nprovider_name: " + str(self._provider_name)
                + "\ndiff_value: " + str(self._diff_value)
                + "\ndiff_window_length: " + str(self._diff_window_length)
                + "\ndrilldown_url: " + str(self._drilldown_url)
                + "\nfully_qualified_metric_name: " + str(self._fully_qualified_metric_name)
                + "\nlast_collected_date: " + str(self._collected_date)
                + "\nvalue: " + str(self._value))

    @property
    def audience(self):
        return self._audience

    @property
    def display_count(self):
        return self._display_count

    @property
    def display_interaction(self):
        return self._display_interaction

    @property
    def display_order(self):
        return self._display_order

    @property
    def display_provider(self):
        return self._display_provider

    @property
    def engagement_type(self):
        return self._engagement_type

    @property
    def hide_badge(self):
        return self._hide_badge

    @property
    def interaction(self):
        return self._interaction

    @property
    def is_highly(self):
        return self._is_highly

    @property
    def latest_nonzero_refresh_timestamp(self):
        return self._latest_nonzero_refresh_timestamp

    @property
    def host(self):
        return self._host

    @property
    def mendeley_discipline(self):
        return self._mendeley_discipline

    @property
    def provider(self):
        return self._provider

    @property
    def percentile_value_string(self):
        return self._percentile_value_string

    @property
    def provider_name(self):
        return self._provider_name

    @property
    def diff_value(self):
        return self._diff_value

    @property
    def diff_window_length(self):
        return self._diff_window_length

    @property
    def drilldown_url(self):
        return self._drilldown_url

    @property
    def fully_qualified_metric_name(self):
        return self._fully_qualified_metric_name

    @property
    def last_collected_date(self):
        return self._collected_date

    # number of [interaction] in [host]
    @property
    def value(self):
        return self._value

    @property
    def most_recent_snap(self):
        return self._most_recent_snap

    @property
    def percentile(self):
        return self._percentile


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


class Dataset(Product):
    def __init__(self, raw_product):
        Product.__init__(self, raw_product)
        bib_info = raw_product.get('biblio', {})
        self._parse_bib_info(bib_info)

    def _parse_bib_info(self, bib_info):
        self._published_date = bib_info.get('published_date', None)
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
            datetime.strptime(str(self._published_date), "%H:%M, %b %d, %Y")

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


class Software(Product):
    def __init__(self, raw_product):
        Product.__init__(self, raw_product)
        bib_info = raw_product.get('biblio', {})
        self._parse_bib_info(bib_info)

    def _parse_bib_info(self, bib_info):
        self._create_date = bib_info.get('create_date', None)
        if self._create_date:
            datetime.strptime(str(self._create_date), "%Y-%m-%dT%H:%M:%S.%f")

        self._description = str(bib_info.get('description', ""))
        self._last_push_date = bib_info.get('last_push_date', None)
        if self._last_push_date:
            datetime.strptime(str(self._last_push_date), "%Y-%m-%dT%H:%M:%S.%f")
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


class Video(Product):
    def __init__(self, raw_product):
        Product.__init__(self, raw_product)
        bib_info = raw_product.get('biblio', {})
        self._parse_bib_info(bib_info)

    def _parse_bib_info(self, bib_info):
        self._published_date = bib_info.get('published_date', None)
        if self._published_date:
            datetime.strptime(str(self._published_date), "%H:%M, %b %d, %Y")
        self._repository = str(bib_info.get('repository', ""))
        self._channel_title = str(bib_info.get('channel_title', ""))

    def __str__(self):
        return unicode("genre: " + str(self._genre)
        + "\ntitle: " + str(self._title)
        + "\nauthors: " + str(self._authors)
        + "\nyear: " + str(self._year)
        + "\nfree_fulltext_host: " + str(self._free_fulltext_host)
        + "\npublished_date: " + str(self._published_date)
        + "\nrepository: " + str(self._repository)
        + "\nchannel_title: " + str(self._channel_title)
        + "\nhas_metrics: " + str(self._has_metrics)
        + "\nmetrics: \n" + str(self._display_metrics) + "\n")

    @property
    def published_date(self):
        return self._published_date

    @property
    def repository(self):
        return self._repository

    @property
    def channel_title(self):
        return self._channel_title


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
