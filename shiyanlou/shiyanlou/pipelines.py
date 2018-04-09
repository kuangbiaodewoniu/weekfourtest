# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from sqlalchemy.orm import sessionmaker
from shiyanlou.Models import Course, engine, User
from shiyanlou.items import CourseItem


class ShiyanlouPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item, CourseItem):
            self.course_process_item(item, spider)
        else:
            self.user_process_item(item, spider)
        return item

    def course_process_item(self, item, spider):
        item['users'] = int(item['users'])
        self.session.add(Course(**item))

    def user_process_item(self, item, spider):
        self.session.add(User(**item))

    def open_spider(self, spider):
        """ 在爬虫被开启的时候，创建数据库 session
        """
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def close_spider(self, spider):
        self.session.commit()
        self.session.close()

