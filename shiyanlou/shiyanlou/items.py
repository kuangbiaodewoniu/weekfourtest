# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CourseItem(scrapy.Item):
    name = scrapy.Field()
    desc = scrapy.Field()
    users = scrapy.Field()


class UserItem(scrapy.Item):
    username = scrapy.Field()
    userlevel = scrapy.Field()
    joindate = scrapy.Field()
