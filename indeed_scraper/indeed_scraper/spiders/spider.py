# import urllib2
# from bs4 import BeautifulSoup
import scrapy


class Spider(scrapy.Spider):
    name = "indeed"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.indeed.com/jobs?q=security&l="
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2] + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)

	# url = "http://www.indeed.com/jobs?q=security&l="
	# page = urllib2.urlopen(url)
	# soup = BeautifulSoup(page)
	# jobs = soup.find_all("div", class_="result")

