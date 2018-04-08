# Requirment Python 2.7
import robobrowser import RoboBrowser
from profile import email, passwd

dict_url = 'http://global.longmandictionaries.com'
bs = RoboBrowser()
bs.open(dict_url)

form = bs.get_form()
form['email'] = email
form['password'] = passwd

