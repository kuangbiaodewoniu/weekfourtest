# !usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
@author:dandan.zheng 
@file: login.py 
@time: 2018/04/09 
"""

import scrapy

class Login(scrapy.Spider):
    name = 'login_spider'

    start_urls = ['https://www.shiyanlou.com/login']

    def parse(self, response):
        """
        模拟登录的核心就在这里，scrapy 会下载 start_urls 里的登录页面，将 response 传到这里，
        然后调用 FormRequest 模拟构造一个 POST 登录请求。
        FormRequest 继承自 Request，所以 Request 的参数对它适用。
        FormRequest 的方法 from_response 用于快速构建 FormRequest 对象。
        from_response 方法会从第一步返回的 response 中获取请求的 url、form 表单信息等等，
        我们只需要指定必要的表单数据和回调函数就可以了。
        """
        csrf_token = response.xpath('//input[@id="csrf_token"]/@value').extract_first()
        self.logger.info(csrf_token)
        return scrapy.FormRequest.from_response(
            # 第一个参数必须传入上一步返回的 response
            response,
            # 以字典结构传入表单数据
            formdata={
                'csrf_token': csrf_token,
                'login': 'chababy@qq.com',
                'password': '@WSX3edc',
            },
            # 指定回调函数
            callback=self.after_login
        )

    def after_login(self, response):
        # 登录之后的代码和普通的 scrapy 爬虫一样，构造 Request，指定 callback ...
        return [scrapy.Request(url='https://www.shiyanlou.com/user/708913/', callback=self.parse_after_login)]

    def parse_after_login(self, response):
        return {
            'username': response.css('span.username::text').extract_first()
        }
