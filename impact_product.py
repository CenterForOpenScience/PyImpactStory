import requests
import json 

# Last Updated 
# generic object type for all impact story "products" (i.e. articles, datasets, slides, etc.)
class Product:
    def __init__(self, raw_product):
        self._tiid = raw_product.get('_tiid', None)
        self._awardedness_score = raw_product.get('awardedness_score', None)
        
        #double-check alias data structure to ensure correct parsing!!!
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
        
        if (str(self._has_metrics).lower() == "true"):
            self._parse_metrics(raw_product.get('metrics', None))
    
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
        self._free_fulltext_host = bib_info.get('published_date', None)
             
    def _parse_metrics(self, metrics):
        for metric in metrics:
            self._metrics.append(Metric(metric))

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
        return ("genre: " + str(self._genre)  
        + "\ntitle: " + str(self._title) + 
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
        + "\nfree_fulltext_url: " + str(self_free_fulltext_url)
        + "\nfree_fulltext_host: " + str(self._free_fulltext_host)
        + "\nhas_metrics: " + str(self._has_metrics)
        + "\nmetrics: " + str(self._metrics))
        
class Metric:
    def __init__(self, raw_metrics):
        self._audience = raw_metrics.get('audience', None)
        self._display_count = raw_metrics.get('display_count', None)
        self._display_interaction = raw_metrics.get('display_interaction', None)
        self._display_order = raw_metrics.get('display_order', None)
        self._display_provider = raw_metrics.get('display_provider', None) 
        self._engagement_type = raw_metrics.get('engagement_type', None) 
        self._has_new_metric = raw_metrics.get('has_new_metric', None) 
        self._hide_badge = raw_metrics.get('hide_badge', None)
        historical_values = raw_metrics.get('historical_values', None)
        self._collected_date = historical_values.get('current', None).get('collected_date') 
        previous_date = historical_values.get('previous', None).get('collected_date', None) 
        previous_value = historical_values.get('previous', None).get('raw', None) 
        self._previous_value = (previous_date, previous_value)
        self._interaction = raw_metrics.get('interaction', None)
        self._is_highly = raw_metrics.get('_is_highly', None)
        self._latest_nonzero_refresh_timestamp = raw_metrics.get('latest_nonzero_refresh_timestamp', None)
        self._metric_name= raw_metrics.get('metric_name', None)
        
        # Percentiles includes CI95_lower, CI95_upper, estimate_lower,  
        # estimate_upper, refset, refset_storage_verb, indexed by, 
        # and top_percent
        self._percentiles = raw_metrics.get('percentiles', {})
        self._provenance_url = raw_metrics.get('provenance_url', None)
        self._provider_name = raw_metrics.get('provider_name', None)
        self._top_percentile = raw_metrics.get('top_percentile', None)
        self._metrics_raw_sum = raw_metrics.get('metrics_raw_sum', None)
        self._update_status = raw_metrics.get('update_status', None)
        
    def __str__(self):
        return ("audience: " + str(self._audience)
        + "\ndisplay_count: " + str(self._display_count)
        + "\ndisplay_interaction: " + str(self._display_interaction)
        + "\ndisplay_order: " + str(self._display_order)
        + "\ndisplay_provider: " + str(self._display_provider)
        + "\nengagement_type: " + str(self._engagement_type)
        + "\nhas_new_metric: " + str(self._has_new_metric)
        + "\nhide_badge: " + str(self._hide_badge)
        + "\ncollected_date: " + str(self._collected_date) 
        + "\nprevious_value: " + str(self._previous_value)
        + "\ninteraction: " + str(self._interaction)
        + "\nis_highly: " + str(self._is_highly)
        + "\nlatest_nonzero_refresh_timestamp: " + str(self._latest_nonzero_refresh_timestamp)
        + "\nmetric_name: " + str(self._metric_name))
        
class Dataset(Product):
    def __init__(self, raw_product):
        Product.__init__(self, raw_product)
        bib_info = raw_product.get('biblio', {})
        self._parse_bib_info(bib_info)
        
    def _parse_bib_info(self, bib_info): 
        self._published_date = bib_info.get('published_date', None)
        self._repository = bib_info.get('repository', None)
        self._is_oa_journal = bib_info.get('is_oa_journal', None)
   
    # Check if you can access both Dataset attributes as well as
    # those inherited from Product 
    def __str__(self):
        return ("genre: " + str(self._genre) 
        + "\ntitle: " + str(self._title)
        + "\nauthors: " + str(self._authors) 
        + "\nyear: " + str(self._year)
        + "\nfree_fulltext_host: " + str(self._free_fulltext_host)
        + "\npublished_date: " + str(self._published_date)
        + "\nrepository: " + str(self._repository)
        + "\nis_oa_journal: " + str(self._is_oa_journal)
        + "\nhas_metrics: " + str(self._has_metrics)
        + "\nmetrics: " + str(self._metrics))

class Figure(Product):
    def __init__(self, raw_product):
        Product.__init__(self, raw_product)
        bib_info = raw_product.get('biblio', {})
        self._parse_bib_info(bib_info)
        
    def _parse_bib_info(self, bib_info):   
        self._published_date = bib_info.get ('published_date', None)
        self.repository = bib_info.get ('repository', None)
        self.is_oa_journal = bib_info.get ('is_oa_journal', None)         
    
    def __str__(self):
        return ("genre: " + str(self._genre) 
        + "\ntitle: " + str(self._title)
        + "\nauthors: " + str(self._authors) 
        + "\nyear: " + str(self._year)
        + "\nfree_fulltext_host: " + str(self._free_fulltext_host)
        + "\npublished_date: " + str(self._published_date)
        + "\nrepository: " + str(self._repository)
        + "\nis_oa_journal: " + str(self._is_oa_journal)
        + "\nhas_metrics: " + str(self._has_metrics)
        + "\nmetrics: " + str(self._metrics))

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
        self.repository = bib_info.get ('repository', None)
        self.username = bib_info.get ('username', None)
        self.published_date = bib_info.get ('published_date', None)

    def __str__(self):
        return ("genre: " + str(self._genre) 
        + "\ntitle: " + str(self._title)
        + "\nauthors: " + str(self._authors) 
        + "\nyear: " + str(self._year)
        + "\nfree_fulltext_host: " + str(self._free_fulltext_host)
        + "\nrepository: " + str(self._repository)
        + "\nusername: " + str(self._username)
        + "\npublished_date: " + str(self._published_date)
        + "\nhas_metrics: " + str(self._has_metrics)
        + "\nmetrics: " + str(self._metrics))
    
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
        return ("genre: " + str(self._genre) 
        + "\ntitle: " + str(self._title)
        + "\nauthors: " + str(self._authors) 
        + "\nyear: " + str(self._year)
        + "\nfree_fulltext_host: " + str(self._free_fulltext_host)
        + "\ncreate_date: " + str(self.create_date)
        + "\ndescription: " + str(self.description)
        + "\nlast_push_date: " + str(self.last_push_date)
        + "\nowner: " + str(self.owner)
        + "\nhas_metrics: " + str(self._has_metrics)
        + "\nmetrics: " + str(self._metrics))
    
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
        return ("genre: " + str(self._genre) 
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
        + "\nmetrics: " + str(self._metrics))

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
        return ("genre: " + str(self._genre) 
        + "\ntitle: " + str(self._title)
        + "\nauthors: " + str(self._authors) 
        + "\nyear: " + str(self._year)
        + "\nfree_fulltext_host: " + str(self._free_fulltext_host)
        + "\npublished_date: " + str(self._published_date)
        + "\nrepository: " + str(self._repository)
        + "\nchannel_title: " + str(self._channel_title)
        + "\nhas_metrics: " + str(self._has_metrics)
        + "\nmetrics: " + str(self._metrics))

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
        return ("genre: " + str(self._genre) 
        + "\ntitle: " + str(self._title)
        + "\nauthors: " + str(self._authors) 
        + "\nyear: " + str(self._year)
        + "\nfree_fulltext_host: " + str(self._free_fulltext_host)
        + "\nhas_metrics: " + str(self._has_metrics)
        + "\nmetrics: " + str(self._metrics))
        