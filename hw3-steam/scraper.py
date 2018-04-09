# Requirment Python 2.7
import re
import mechanize

from steam_store import steam_store_url
# from steam_community import steam_community_url, game_page
    
br = mechanize.Browser()
br.open(steam_store_url)

print br.title()

search_page = br.open(steam_store_url + '/search/?term=')
result_html = search_page.read()

print br.title()
print type(result_html)
