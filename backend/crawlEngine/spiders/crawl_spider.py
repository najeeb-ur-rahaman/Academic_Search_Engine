import scrapy, datetime
from elasticsearch import Elasticsearch
import urllib.parse

# Password for the 'elastic' user generated by Elasticsearch
ELASTIC_PASSWORD = "p5iqqHyCAebVnHYOrkWqhJNi"

# Found in the 'Manage Deployment' page
CLOUD_ID = "Search_engine:dXMtY2VudHJhbDEuZ2NwLmNsb3VkLmVzLmlvJDg1ODQ1MWEzYTQwMTQwMzI5ODVlMjRiNDVkYjdhYmVmJGVhZjRhYjczMWE5NzQ4MTZiZGMxYmZkYmE0NDU3MDdj"

# Create the client instance
client = Elasticsearch(
    cloud_id=CLOUD_ID,
    basic_auth=("elastic", ELASTIC_PASSWORD)
)

class spiderCrawling(scrapy.Spider):
    name = "academic"
    allowed_domains = ['eric.ed.gov']
    start_urls = ["https://eric.ed.gov/?q=source%3a%22higher+education%22"]
    
    # rules = (
    #     Rule(LinkExtractor(allow="higher+education"), callback="parse_item"),
    # )
    
    def parse(self, response):
        for journal in response.css("div.r_i"):
            client.index(
                index='academic',
                document={
                    "url": urllib.parse.urljoin("https://eric.ed.gov/" , journal.css(".r_t a::attr(href)").get()),
                    "title": journal.css(".r_t a::text").get(),
                    "authors": journal.css(".r_a::text").get(),
                    'datetime' : datetime.datetime.now()
                })
        next_page = response.xpath('//div[@style="text-align:left;float:left"]/a/@href').getall()
        if next_page[-1] is not None:
            print(next_page)
            yield response.follow(next_page[-1], callback=self.parse)