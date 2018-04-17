# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FedrevjobsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #description = scrapy.Field()
    job_pageurl = scrapy.Field()
    job_title = scrapy.Field()
    job_id = scrapy.Field()
    job_location = scrapy.Field()
    job_keyword = scrapy.Field()
    job_category = scrapy.Field()
    date_posted = scrapy.Field()