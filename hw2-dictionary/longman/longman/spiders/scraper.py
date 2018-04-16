import re
import os, sys
import time
import lxml, html
from Queue import Queue

import scrapy
from scrapy import Spider
from scrapy.linkextractors.sgml import SgmlLinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import selenium

from ..profile import email, passwd
from ..profile import IELTS_words
from ..select import word, pos, meaning

print os.getcwd()

IELTS_path = '../IELTS/IELTSWordList'
valid_pos = [' verb', ' adverb', ' adjective', ' noun', 'verb', 'adverb', 'adjective', 'noun']


class DictSpider(Spider):
    
    name = 'longman'
    allowed_domains = ['global.longmandictionaries.com']
    start_urls = ['http://global.longmandictionaries.com/auth/login']
    login_url = 'http://global.longmandictionaries.com/auth/login'
    search_url = 'http://global.longmandictionaries.com/dict_search/entry_for_alpha_key/ldoce6/'

    now = -1
    wl0 = IELTS_words(IELTS_path)
    had = {}
    q = Queue()
    
    def start_requests(self):
        for word in DictSpider.wl0:
            DictSpider.had[word] = True
            
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
        # Load all IELTS words
        return scrapy.Request(self.search_url, callback=self.parse, dont_filter=True)
        
    def parse(self, response):
        selector = scrapy.Selector(response)

        wd = word(selector)
        if wd:
                
            flag = False
            for p in pos(selector):
                flag = flag or (p in valid_pos)

            if flag:
                DictSpider.had[wd[0]] = True

                meaning_list = []
                for w in meaning(selector):
                    meaning_list.extend(w.split())

                for w in meaning_list:
                    if not (w in DictSpider.had):
                        DictSpider.had[w] = True
                        DictSpider.had[w + '_1'] = True
                        DictSpider.had[w + '_2'] = True
                        DictSpider.had[w + '_3'] = True
                        DictSpider.wl0.append(w)                    
                        DictSpider.wl0.append(w + '_1')                    
                        DictSpider.wl0.append(w + '_2')                    
                        DictSpider.wl0.append(w + '_3')                    
                yield {
                    'word' : word(selector),
                    'POS' : pos(selector),
                    'meaning' : meaning(selector) 
                }

        if DictSpider.now + 1 < len(DictSpider.wl0):
            DictSpider.now = DictSpider.now + 1
            theword = DictSpider.wl0[DictSpider.now]
            
            formdata = {
                'alpha_key' : theword,
                'name' : ''
            }
            yield scrapy.FormRequest(
                url=response.url, method='POST', formdata=formdata, 
                callback=self.parse, dont_filter=True
            )
