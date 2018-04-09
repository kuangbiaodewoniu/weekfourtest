# -*- coding: utf-8 -*-

import scrapy
from shiyanlou.items import UserItem


class UsersSpider(scrapy.Spider):
    name = 'users'

    @property
    def start_urls(self):
        url_template = 'https://www.shiyanlou.com/user/{}/'
        return (url_template.format(i) for i in range(1, 293620))

    def parse(self, response):
        item = UserItem({
            'username': response.css('span.username::text').extract_first(),
            'userlevel': response.css('span.user-level::text').extract_first(),
            'joindate': response.css('span.join-date::text').extract_first(),
        })
        yield item
