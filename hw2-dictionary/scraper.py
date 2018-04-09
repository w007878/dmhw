# Requirment Python 2.7
import re
import mechanize
from profile import email, passwd

# Create the browser session
dict_url = 'http://global.longmandictionaries.com'
br = mechanize.Browser()
br.open(dict_url)
print br.title()

# Login 
# You should set your email and password in 'profile.py'
# form = bs.get_form()

br.select_form(nr=0)
br['email'] = email
br['password'] = passwd
br.form.controls[3].items[0].selected = True
br.submit()

br.open(dict_url + '/ldoce6/advanced_search')
print br.viewing_html()

br.select_form(nr=0)
print br.form
br.
# bs.open(dict_url + '/ldoce6/dictionary')

# print bs
# print bs.get_form()
# print bs.get_links()
# 
