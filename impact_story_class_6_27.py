import requests 
import json

STATIC_URL = "https://impactstory.org/profile/"

# Impact Story Class --> should be combined with impact_product
class ImpactStory:
    def __init__(self, name):
        self._articles = [] 
        self._datasets = []
        self._figures = []
        self._slides = [] 
        self._software = []
        self._unknown = []
        self._videos = [] 
        self._webpages = []
        
        name = name.replace(" ", "")
        raw = requests.get(STATIC_URL + name + "?hide=markup,awards")
        self._parse_raw(raw.json())
        
        
    def _parse_raw(self, raw):
        self._parse_products(raw["products"])    

    def _parse_products(self, products):
        for product in products:             
            biblio = product.get("biblio", None)
            if (biblio):
                if (product["biblio"]["genre"] == "article"):
                    self._articles.append(Article(product))          
        
                elif (product["biblio"]["genre"] == "dataset"):
                    self._datasets.append(Dataset(product))

                elif (product["biblio"]["genre"] == "figure"):
                    self._figures.append(Figure(product))

                elif (product["biblio"]["genre"] == "slides"):
                    self._slides.append(Slides(product))

                elif (product["biblio"]["genre"] == "software"):
                    self._software.append(Software(product))

                elif (product["biblio"]["genre"] == "unknown"):
                    self._unknown.append(Unknown(product))

                elif (product["biblio"]["genre"] == "video"):
                    self._videos.append(Video(product))

                elif (product["biblio"]["genre"] == "webpage"):
                    self._webpages.append(Webpage(product))

                else:
                    print "No products found"

    @property
    def articles(self):
        return self._articles  

    @property
    def datasets(self):
        return self._datasets
    
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

    # consider adding methods that get the names of each item in the product lists 
    def article_titles(self):
        article_titles = []
        for article in self._articles:
            article_titles.append(str(article.title))
        return article_titles

Hey what's up Saman???
