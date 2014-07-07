import requests 
from impact_product import Article
from impact_product import Dataset
from impact_product import Figure
from impact_product import Slides
from impact_product import Software
from impact_product import Unknown
from impact_product import Video
from impact_product import Webpage


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
    def __init__(self, status_code, msg):
        self.status_code = status_code
        self.msg = msg


class ImpactStoryParseException(ImpactStoryException):
    pass


class ImpactStory:
    def __init__(self, name):
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
                self._parse_raw(raw_dict)
            except ValueError as exception:
                raise ImpactStoryParseException(exception.message)
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
        attribute_list = ['_tiid', 'awardedness_score','aliases', 'best_url', 'url',
        'github', 'altmetric_com', 'doi', 'pmid', 'uuid', 'pmc', 'arxiv', 'biblio', 'genre',
        'title', 'authors']

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

        for key in raw_dict:
            if key not in attribute_list:
                self._new_attributes.append(key)

            if type(raw_dict[key]) is dict or type(raw_dict[key]) is list:
                # recursive call on the sub-dict or list
                self._updated_dict(raw_dict[key])

        # Check for keys removed from the JSON file
        for item in attribute_list:
            if item not in raw_dict.keys():
                item.append(self._unused_attributes)

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
                    print "End of Profile"

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