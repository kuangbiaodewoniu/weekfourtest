# -*- coding: utf-8 -*-
import scrapy
from getshiyanlougithub.items import RepositoriesItem


class ShiyanlougithunSpider(scrapy.Spider):
    name = 'shiyanlougithun'
    allowed_domains = ['github.com/shiyanlou']

    @property
    def start_urls(self):
        url_templates = 'https://github.com/shiyanlou?page={}&tab=repositories'
        return (url_templates.format(i) for i in range(1, 5))

    def parse(self, response):
        for repository in response.css('li[itemtype="http://schema.org/Code"]'):
            item = RepositoriesItem({
                'name': repository.css('a[itemprop="name codeRepository"]::text').re_first('\S+'),
                'update_time': repository.css('relative-time::attr("datetime")').extract_first()
            })
            yield item
