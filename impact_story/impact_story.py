import json
import requests
from products.article import Article
from products.dataset import Dataset
from products.figure import Figure
from products.slides import Slides
from products.unknown import Unknown
from products.webpage import Webpage
from products.video import Video
from products.software import Software

'''
ImpactStory
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

'''
To get ImpactStory profile data for a user,
instantiate ImpactStory object from url extension
(ImpactStory.from_id) or from JSON file (ImpactStory.from_file)
'''


class ImpactStory:
    def __init__(self, json_data):
        self._new_attributes = []
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

        self._raw_dict = json_data
        self._check_changes(self._raw_dict)
        self._parse_raw(self._raw_dict)

    def _check_changes(self, raw_dict):
        # check for changes in the JSON file
        self._updated_dict(raw_dict["products"])

        # notify user of any changes
        if len(self._new_attributes) != 0:
            new_attribute_str = "\n".join(self._new_attributes)

            print ("Impactstory has added the following information since this library was last updated."
                   + "\nIf you are interested in getting these attributes, "
                   + "file a bug report. Otherwise continue using the library:\n"
                   + str(new_attribute_str))

    # checks for keys added or removed from JSON
    def _updated_dict(self, raw):
        attribute_list = ["_tiid", "awardedness_score", "aliases", "has_new_metric", "currently_updating",
                  "has_percentiles", "is_true_product", "latest_diff_timestamp",
                  "metric_by_name", "has_metrics", "best_url", "url",
                  "github", "altmetric_com", "doi", "pmid","uuid", "pmc", "arxiv",
                  "biblio", "genre", "genre_plural", "display_genre_plural",
                  "title", "authors", "year", "free_fulltext_host", "published_date", "percentile",
                  "provenance_url","provider_name", "top_percentile", "metrics_raw_sum",
                  "update_status", "audience", "display_count", "display_interaction", "display_order",
                  "display_provider", "engagement_type", "has_new_metric", "hide_badge",
                  "interaction", "is_highly", "latest_nonzero_refresh_timestamp",
                  "metric_name", "issn", "journal", "number", "volume", "first_page",
                  "first_author", "is_oa_journal", "repository", "full_citation",
                  "published_date", "day", "month", "year", "full_citation_type",
                  "h1", "oai_id", "free_fulltext_url", "free_fulltext_host", "create_date",
                  "description","last_push_date", "owner", 'channel_title', "metrics", "tiid",
                  "display_title", "display_year", "display_authors", "markup", "is_heading",
                  "anchor", "icon","has_metrics", "host", "mendeley_discipline", "mendeley_discipline_str",
                  "collected_date", "diff_value", "is_refreshing", "last_modified", "calculated_genre",
                  "calculated_host", "removed", "has_diff", "created", "last_refresh_status",
                  "last_refresh_failure_message", "last_refresh_finished", "last_update_run", "value",
                  "drilldown_url", "finished_successful_refresh", "last_refresh_started",
                  "percentile_value_string", "provider", "fully_qualified_metric_name", "diff_window_length",
                  "username", "name", "id", "authors_literal", "date", "profile_id", "can_diff",
                  "milestone_just_reached", "window_start_snap"]

        # Check for keys added to the JSON file
        if type(raw) is list:
            for item in raw:
                if type(item) is dict or type(item) is list:
                    self._updated_dict(item)

        elif type(raw) is dict:
            for key in raw:
                if type(raw[key]) is dict or type(raw[key]) is list:
                    self._updated_dict(raw[key])

                else:
                    if key not in attribute_list and key not in self._new_attributes:
                        self._new_attributes.append(key)
        
    def _parse_raw(self, raw):
        self._parse_products(raw["products"])    

    def _parse_products(self, products):
        for product in products:             
            if '_tiid' in product:
                if product["genre"] == "article":
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

    @classmethod
    # use url extension from impactstory profile as id
    # e.g. SamanEhsan3939
    def from_id(cls, name):
        base_url = "https://impactstory.org/profile/"
        name = name.replace(" ", "")
        raw = requests.get(base_url + name + "?hide=markup,awards")

        if raw.status_code == 200:
            try:
                obj = ImpactStory(raw.json())
            except ValueError:
                raise ImpactStoryParseException(Exception.args)
        else:
            raise ImpactStoryHTTPException(raw.status_code, raw.text)

        return obj


    @classmethod
    def from_file(cls, json_file):
        if json_file.endswith('.json'):
            raw_json = open(json_file)
            try:
                raw_dict = json.load(raw_json)
                obj = ImpactStory(raw_dict)
                return obj
            except ValueError:
                    raise ImpactStoryParseException(Exception.args)
        else:
            print "File type is not JSON"

    @property
    def raw_dict(self):
        return self._raw_dict

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
