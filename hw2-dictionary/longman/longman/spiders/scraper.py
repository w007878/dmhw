import re
import os

import scrapy
from scrapy import Spider
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule

from ..profile import email, passwd

class DictSpider(Spider):
    
    name = 'longman'
    allowed_domains = ['global.longmandictionaries.com']
    start_urls = ['http://global.longmandictionaries.com/auth/login']
    login_url = 'http://global.longmandictionaries.com/auth/login'
    
    def start_requests(self):
        yield scrapy.Request(self.login_url, callback=self.login, dont_filter=True)

    def login(self, response):
        formdata = {
            'email' : email,
            'password' : passwd,
            'submit' : 'Login'
        }
        return [scrapy.FormRequest.from_response(response, method='POST', 
            formdata=formdata, callback=self.logined_in, dont_filter=True)]

    def parse(self, response):
        filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)      
        
    def logined_in(self, response):
        lnk = 'http://global.longmandictionaries.com/home'
        return scrapy.Request(lnk, callback=self.parse, dont_filter=True)
        