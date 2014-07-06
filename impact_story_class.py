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

    '''
    def _check_changes(self, raw_dict):
        # check if JSON file was changed
        self._updated_dict(raw_dict["products"])

        if len(self._new_attributes) != 0:
            print "WARNING: changes found in JSON file - print new attributes"
            "\nIf you are interested in getting these attributes,"
            "\nfile a bug report, otherwise continue using the library"
        if len(self._new_attributes) == 0:
            self._parse_raw(raw_dict)


    # Method to find any changes in JSON file
    def _updated_dict(self, raw_dict):
        attribute_list = ['_tiid']

        for key in raw_dict:
            if key not in attribute_list:
                self._new_attributes.append(key)

            if type(raw_dict[key]) is dict or type(raw_dict[key]) is list:
                # recursive call on the sub-dict or list
                self._updated_dict(raw_dict[key])
    '''

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