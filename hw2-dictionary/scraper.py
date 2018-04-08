# Requirment Python 2.7
from robobrowser import RoboBrowser
from profile import email, passwd

# Create the browser session
dict_url = 'http://global.longmandictionaries.com'
bs = RoboBrowser(parser='lxml')
bs.open(dict_url)

# Login 
# You should set your email and password in 'profile.py'
form = bs.get_form()
form['email'].value = email
form['password'].value = passwd
bs.submit_form(form)
bs.open(dict_url + '/ldoce6/dictionary')
print bs
print bs.get_links()
