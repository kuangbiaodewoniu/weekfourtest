# -*- coding: utf-8 -*-
import scrapy
from images.items import CourseImageItem


class CourseImageSpider(scrapy.Spider):
    name = 'course_image'
    allowed_domains = ['shiyanlou.com/courses']
    start_urls = ['http://shiyanlou.com/courses/']

    def parse(self, response):
        yield CourseImageItem({
            'image_urls': response.xpath('//div[@class="course-img"]/img/@src').extract()
        })
