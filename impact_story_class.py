import json
import requests
from impact_product import Article
from impact_product import Dataset
from impact_product import Figure
from impact_product import Slides
from impact_product import Unknown
from impact_product import Webpage
from impact_product import Video
from impact_product import Software


STATIC_URL = "https://impactstory.org/profile/"

'''
ImpactStory Class 
Retrieves JSON file from ImpactStory user profile,
converts JSON to python dict, parses "projects" 
dict & instantiates "project" objects (i.e. articles, datasets, figures) 
'''


class ImpactStoryException(Exception):
    pass


class ImpactStoryHTTPException(ImpactStoryException):
    def __init__(self, status_code, message):
        self.status_code = status_code
        self.msg = message


class ImpactStoryParseException(ImpactStoryException):
    pass


class ImpactStory:
    def __init__(self, name):
        #self._attribute_list = []
        self._new_attributes = []
        self._unused_attributes = []
        self._articles = [] 
        self._datasets = []
        self._figures = []
        self._slides = [] 
        self._software = []
        self._unknown = []
        self._videos = [] 
        self._webpages = []
        self._all = {'articles': self._articles, 
                     'datasets': self._datasets,
                     'figures': self._figures,
                     'slides': self._slides,
                     'software': self._software,
                     'unknown': self._unknown,
                     'videos': self._videos, 
                     'webpages': self._webpages
                     } 
        
        name = name.replace(" ", "")
        raw = requests.get(STATIC_URL + name + "?hide=markup,awards")
        raw_dict = raw.json()

        if raw.status_code == 200:
            try:
                #self._check_changes(raw_dict)
                self._parse_raw(raw.json())
            except ValueError:
                raise ImpactStoryParseException(Exception.args)
        else:
            raise ImpactStoryHTTPException(raw.status_code, raw.text)

     def _check_changes(self, raw_dict):
        # iterate through product list to check for any changes
        for item in raw_dict["products"]:
            self._updated_dict(item)

        # notify user of any changes
        if len(self._new_attributes) != 0:
            print "WARNING: changes found in JSON file - print new attributes" \
                  + "\nIf you are interested in getting these attributes,"\
                  + "\nfile a bug report, otherwise continue using the library"
        if len(self._unused_attributes) != 0:
            print "The following attributes could not be found: " #list keys

    # checks for keys added or removed from JSON
    def _updated_dict(self, raw_dict):
        attribute_list = ["tiid", "awardedness", "article", "dataset", "figure", "slides",\
                  "software", "unknown", "video", "webpage", "currently_updating",\
                  "has_percentiles", "is_true_product", "latest_diff_timestamp", \
                  "metric_by_name", "has_metric","published_date", "best_url" "url",\
                  "github", "altmetric_com", "doi", "pmid","uuid", "pmc", "arxiv",\
                  "genre", "title", "authors", "year", "percentiles", "provenance_url",\
                  "provider_name", "top_percentile", "metrics_raw_sum", "update_status",\
                  "audience", "display_count", "display_interaction", "display_order",\
                  "display_provider", "engagement_type", "has_new_metric", "hide_badge",\
                  "interaction", "is_highly", "latest_nonzero_refresh_timestamp",\
                  "metric_name", "genre", "journal", "number", "volume", "first_page",\
                  "first_author: ", "is_oa_journal: ", "repository", "full_citation", \
                  "published_date: ", "day", "month", "year", "full_citation_type",\
                  "h1", "oai_id" + "free_fulltext_url", "free_fulltext_host", "create_date", \
                  "description","last_push_date", "owner", 'channel_title']

        # Check for keys added to the JSON file
        for attribute in raw_dict:
            if type(attribute) is dict:
                self._updated_dict(attribute)

            else:
                if attribute not in attribute_list and attribute not in self._new_attributes:
                    self._new_attributes.append(attribute)

                if type(raw_dict[attribute]) is dict or type(raw_dict[attribute]) is list:
                    # recursive call on the sub-dict or list
                    self._updated_dict(raw_dict[attribute])

        '''
        # Check for keys removed from the JSON file
        for item in attribute_list:
            if item not in raw_dict.keys():
                item.append(self._unused_keys)
        '''
        
    def _parse_raw(self, raw):
        self._parse_products(raw["products"])    

    def _parse_products(self, products):
        for product in products:             
            if '_tiid' in product:
                if product[""]["genre"] == "article":
                    self._articles.append(Article(product))          
        
                elif product["genre"] == "dataset":
                    self._datasets.append(Dataset(product))

                elif product["genre"] == "figure":
                    self._figures.append(Figure(product))

                elif product["genre"] == "slides":
                    self._slides.append(Slides(product))

                elif product["genre"] == "software":
                    self._software.append(Software(product))

                elif product["genre"] == "unknown":
                    self._unknown.append(Unknown(product))

                elif product["genre"] == "video":
                    self._videos.append(Video(product))

                elif product["genre"] == "webpage":
                    self._webpages.append(Webpage(product))

                else:
                    print ("End of Profile")

    @property
    def articles(self):
        return self._articles  

    @property
    def datasets(self):
        return self._datasets
    
    @property
    def figures(self):
        return self._figures

    @property
    def slides(self):
        return self._slides  

    @property
    def software(self):
        return self._software
    
    @property
    def unknown(self):
        return self._unknown 

    @property
    def videos(self):
        return self._videos
    
    @property
    def webpages(self):
        return self._webpages

    @property 
    def all(self):
        return self._all