# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class IndeedScraperItem(scrapy.Item):
    title = scrappy.Filed()
    description = scrappy.Filed()
    blurb = scrappy.Filed()
    location = scrappy.Filed()
   
