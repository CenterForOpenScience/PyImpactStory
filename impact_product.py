'''
Generic object type for all impactstory products
extended by Article, Dataset, Figure, Slides, 
Software, Video, Website & Unknown. 
'''

class Product:
    def __init__(self, raw_product):
        self._tiid = raw_product.get('_tiid', None)
        self._awardedness_score = raw_product.get('awardedness_score', None)
        
        # parsed aliases 
        aliases = raw_product.get('aliases', {})
        self._parse_aliases(aliases)
        
        # parsed bibliographic information 
        bib_info = raw_product.get('biblio', {})
        self._parse_product_bib(bib_info)
        
        # parsed metrics
        self._currently_updating = raw_product.get('currently_updating', None)
        self._has_new_metric = raw_product.get('has_new_metric', None)
        self._has_percentiles = raw_product.get('has_percentiles', None)
        self._is_true_product = raw_product.get('is_true_product', None)
        self._latest_diff_timestamp = raw_product.get('latest_diff_timestamp', None)
        self._metric_by_name = raw_product.get('metric_by_name', {})
        self._metrics = []
        self._has_metrics = raw_product.get('has_metrics', None) 
        
        if str(self._has_metrics).lower() == "true":
            self._parse_metrics(raw_product.get('metrics', None))
        
        self._display_metrics = []
        self.display_metrics()
        
    def _parse_aliases(self, alias):
        self._best_url = alias.get('best_url', None)
        self._url = alias.get('url', None)
        self._github = alias.get('github', None)
        self._altmetric_com = alias.get('altmetric_com', None)
        self._doi = alias.get('doi', None)
        self._pmid = alias.get('pmid', None)
        self._uuid = alias.get('uuid', None)
        self._pmc = alias.get('pmc', None)
        self._arxiv = alias.get('arxiv', None)
        
    def _parse_product_bib(self, bib_info): 
        self._genre = bib_info.get('genre', None)
        self._title = bib_info.get('title', None) 
        self._authors = bib_info.get('authors', None)
        self._year = bib_info.get('year', None)
        self._free_fulltext_host = bib_info.get('free_fulltext_host', None)
    
    def _parse_metrics(self, metrics):
        for metric in metrics:
            self._metrics.append(Metric(metric))
    '''
    Creates a list of metrics represented as strings 
    Used in Project subclasses to display metric info
    '''
    def display_metrics(self): 
        for metric in self._metrics:
            self._display_metrics.append(str(metric))
        self._display_metrics = "\n".join(self._display_metrics)
        return self._display_metrics
    

    @property
    def tiid(self):
        return self._tiid
    
    @property
    def awardedness_score(self):
        return self._awardedness_score

    @property 
    def currently_updating(self):
        return self._currently_updating

    @property
    def has_metrics(self):
        return self._has_metrics

    @property 
    def has_new_metric(self):
        return self._has_new_metric
    
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
    def has_percentiles(self):
        return self._has_percentiles
    
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
        self._audience = raw_metrics.get('audience', None)
        self._diff_value = raw_metrics.get('diff_value', None)
        self._diff_window_length = raw_metrics.get('diff_window_length', None)
        self._display_count = raw_metrics.get('display_count', None)
        self._display_interaction = raw_metrics.get('display_interaction', None)
        self._display_order = raw_metrics.get('display_order', None)
        self._display_provider = raw_metrics.get('display_provider', None) 
        self._engagement_type = raw_metrics.get('engagement_type', None) 
        self._fully_qualified_metric_name= raw_metrics.get('fully_qualified_metric_name', None)
        self._has_new_metric = raw_metrics.get('has_new_metric', None)
        self._hide_badge = raw_metrics.get('hide_badge', None)
        self._interaction = raw_metrics.get('interaction', None)
        self._is_highly = raw_metrics.get('is_highly', None)
        self._latest_nonzero_refresh_timestamp = raw_metrics.get('latest_nonzero_refresh_timestamp', None)

        # previous metric values
        most_recent_snap = raw_metrics.get('most_recent_snap', None)
        self._last_collected_date = most_recent_snap.get('collected_date', None)
        self._last_value = most_recent_snap.get('value', None)
        self._drilldown_url = most_recent_snap.get('drilldown_url')

        self._percentile = raw_metrics.get('percentile', {})

        #self._provenance_url = raw_metrics.get('provenance_url', None)
        self._provider_name = raw_metrics.get('provider_name', None)
        #self._top_percentile = raw_metrics.get('top_percentile', None)
        #self._metrics_raw_sum = raw_metrics.get('metrics_raw_sum', None)
        #self._update_status = raw_metrics.get('update_status', None)


    def __str__(self):
        return ("\naudience: " + str(self._audience)
                + "\ndisplay_count: " + str(self._display_count)
                + "\ndisplay_interaction: " + str(self._display_interaction)
                + "\ndisplay_order: " + str(self._display_order)
                + "\ndisplay_provider: " + str(self._display_provider)
                + "\nengagement_type: " + str(self._engagement_type)
                + "\nhas_new_metric: " + str(self._has_new_metric)
                + "\nhide_badge: " + str(self._hide_badge)
                + "\ninteraction: " + str(self._interaction)
                + "\nis_highly: " + str(self._is_highly)
                + "\nlatest_nonzero_refresh_timestamp: " + str(self._latest_nonzero_refresh_timestamp)
                + "\nmetric_name: " + str(self._metric_name))

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
    def has_new_metric(self):
        return self._has_new_metric
        
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
    def metric_name(self):
        return self._metric_name 
        
    @property 
    def percentiles(self):
        return self._percentiles
        
    @property 
    def provenance_url(self):
        return self._provenance_url 
        
    @property 
    def provider_name(self):
        return self._provider_name
        
    @property 
    def top_percentile(self):
        return self._top_percentile 
        
    @property 
    def metrics_raw_sum(self):
        return self._metrics_raw_sum 
        
    @property 
    def update_status(self):
        return self._update_status
 
    
class Article(Product):
    def __init__(self, raw_product):
        Product.__init__(self, raw_product)
        bib_info = raw_product.get('biblio', {})
        self._parse_bib_info(bib_info)
        
    def _parse_bib_info(self, bib_info): 
        self._issn = bib_info.get ('issn', None)
        self._journal = bib_info.get ('journal', None)
        self._number = bib_info.get ('number', None)
        self._volume = bib_info.get('volume', None)
        self._first_page = bib_info.get ('first_page', None)
        self._first_author = bib_info.get ('first_author', None)
        self._is_oa_journal = bib_info.get ('is_oa_journal', None)
        self._repository = bib_info.get ('repository', None)                                                 
        self._full_citation = bib_info.get ('full_citation', None)
        self._published_date = bib_info.get('published_date', None)
        self._day = bib_info.get ('day', None)
        self._month = bib_info.get ('month', None)
        self._full_citation_type = bib_info.get ('full_citation_type', None)
        self._h1 = bib_info.get ('h1', None)
        self._oai_id = bib_info.get ('oai_id', None)
        self._free_fulltext_url = bib_info.get('free_fulltext_url', None)
    
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
                + "\nmetrics: \n" + self._display_metrics + "\n")
        
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
        self._repository = bib_info.get('repository', None)
        self._is_oa_journal = bib_info.get('is_oa_journal', None)

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
                + "\nmetrics: \n" + self._display_metrics + "\n")
        
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
        self._repository = bib_info.get ('repository', None)
        self._is_oa_journal = bib_info.get ('is_oa_journal', None)         
    
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
                + "\nmetrics: \n" + self._display_metrics + "\n")

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
        self._repository = bib_info.get ('repository', None)
        self._username = bib_info.get ('username', None)
        self._published_date = bib_info.get ('published_date', None)
    
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
        + "\nmetrics: \n" + self._display_metrics + "\n")
    
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
        self._description = bib_info.get('description', None)
        self._last_push_date = bib_info.get('last_push_date', None)
        self._owner = bib_info.get('owner', None)
    
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
        + "\nmetrics: \n" + self._display_metrics + "\n")
    
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
        self._free_fulltext_url = bib_info.get ('free_fulltext_url', None)
        self._first_page = bib_info.get ('first_page', None)
        self._first_author = bib_info.get ('first_author', None)
        self._journal = bib_info.get ('journal', None)
        self._number = bib_info.get ('number', None)
        self._volume = bib_info.get ('volume', None)
    
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
        + "\nmetrics: \n" + self._display_metrics + "\n")

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
        self._repository = bib_info.get('repository', None)
        self._channel_title = bib_info.get('channel_title', None)
  
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
        + "\nmetrics: \n" + self._display_metrics + "\n")

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
        + "\nmetrics: \n" + self._display_metrics + "\n")
        
