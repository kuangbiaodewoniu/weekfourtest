# !usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
@author:dandan.zheng 
@file: PageFollowing_2.py 
@time: 2018/04/09 
"""
import scrapy

class PageFollowing_2(scrapy.Spider):

    name = 'PageFollowing_2'

    @property
    def start_urls(self):
        url = 'https://www.shiyanlou.com/courses/63'
        return [url]

    def parse(self, response):
        # 返回文章标题和作者
        yield {
            'name': response.xpath('//h4[@class="course-infobox-title"]/span/text()').extract_first(),
            'author': response.xpath('//div[@class="mooc-info"]/div[@class="name"]/strong/text()').extract_first()
        }

        for url in response.xpath('//div[@class="sidebox-body course-content"]/a/@href'):
            yield response.follow(url=url, callback=self.parse)