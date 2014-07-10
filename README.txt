============
ImpactStory
============

Python library for ImpactStory. This tool parses the provided JSON file for a given Impactstory user in order to extract
bibliographic information and metric data for each of their professional "Products". ImpactStory defines a "Product"
as any one article, dataset, figure, slideshow, software, video, webpage, or "unknown" (product with genre not
previously listed) that a user has produced throughout their career and added to their ImpactStory profile. As
previously stated, this library enables the extraction of these "products" and their bibliographic and
metric information.

To access product information for an Impactstory user::

    from impact_story import ImpactStory

Create an ImpactStory object from either the JSON file or directly from the user's url extension::

    username = ImpactStory.from_file(file.json)
    username = ImpactStory.from_id("HeatherPiwowar")

Products are sorted into lists based on product type. Thus, to access product and product information by type::

    article_list = user.articles
    article = article_list[0]

To access specific bibliographic information for any given product such as its title, published date or author::

    article.title
    article.published_date
    article.authors


To access metric information for any given product, such as its audience or engagement type (e.g. number of views):

    metric_list = article.metrics
    metric = metric_list[0]
    metric.audience
    metric.engagement_type



