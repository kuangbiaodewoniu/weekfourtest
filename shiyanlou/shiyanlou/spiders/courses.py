# -*- coding: utf-8 -*-
import scrapy
from shiyanlou.items import CourseItem


class CoursesSpider(scrapy.Spider):
    name = 'courses'
    allowed_domains = ['shiyanlou.com']

    @property
    def start_urls(self):
        url_template = 'https://www.shiyanlou.com/courses/?category=all&course_type=all&fee=all&tag=all&page={}'
        return (url_template.format(i) for i in range(1, 25))

    def parse(self, response):
        for course in response.css('a.course-box'):
            item = CourseItem({
                'name': course.css('div.course-name::text').extract_first(),
                'desc': course.css('div.course-desc::text').extract_first(),
                'users': course.xpath('.//span[contains(@class, "pull-left")]/text()[2]').re_first('[^\d]*(\d*)[^\d]*')
            })
            yield item

