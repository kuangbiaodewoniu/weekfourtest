# -*- coding: utf-8 -*-
import scrapy
from pages.items import MultiPageItem


class MutipageSpider(scrapy.Spider):
    name = 'mutipage'
    # allowed_domains = ['shiyanlou.com/courses']
    start_urls = ['http://shiyanlou.com/courses/']

    def parse(self, response):
        # 图片，名称，作者
        for course in response.css('a.course-box'):
            item = MultiPageItem()
            item['name'] = course.css('div.course-name::text').extract_first()
            item['pic'] = course.xpath('//div[@class="course-img"]/img/@src').extract_first()
            url = course.xpath('./@href').extract_first()
            request = scrapy.Request(response.urljoin(url), callback=self.parse_author)
            request.meta['item'] = item
            yield request

    def parse_author(self, response):
        item = response.meta['item']
        item['author'] = response.xpath('//div[@class="mooc-info"]/div[@class="name"]/strong/text()').extract_first()
        yield item