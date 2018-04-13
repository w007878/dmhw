import re
import os
import time
import lxml, html

import scrapy
from scrapy import Spider
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
import selenium

from ..profile import email, passwd
from ..select import word, pos, meaning

class DictSpider(Spider):
    
    name = 'longman'
    allowed_domains = ['global.longmandictionaries.com']
    start_urls = ['http://global.longmandictionaries.com/auth/login']
    login_url = 'http://global.longmandictionaries.com/auth/login'
    search_url = 'http://global.longmandictionaries.com/dict_search/entry_for_alpha_key/ldoce6/'
    
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

    def logined_in(self, response):
        lnk = 'http://global.longmandictionaries.com/ldoce6/dictionary'
        return scrapy.Request(lnk, callback=self.parse, dont_filter=True)

    def parse(self, response):
        yield scrapy.Request(response.url, callback=self.parse_word, dont_filter=True)

    def write(self, response):
        filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)      
        selector = scrapy.Selector(response)
        print 'The Word:'
        for name in word(selector):
            print name, '\n'
        print 'The POS:'
        for p in pos(selector):
            print p
        print '\nThe meanings:'
        for d in meaning(selector):
            print d,'\n'
        
    def parse_word(self, response):
        formdata = {
            'alpha_key' : 'abandon_1',
            'name' : ''
        }
        return [scrapy.FormRequest(
            url=self.search_url, method='POST', formdata=formdata, 
            callback=self.write, dont_filter=True
        )]
        