#!/usr/bin/env python3
# request with basic authentication

# vuln: Local file inclusion

import requests
import re

username = 'natas8'
password = 'DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe'

url = f'http://{username}.natas.labs.overthewire.org/'
#print (url)

#d define header settings referers
#header_settings = {
#    "Referer" : "http://natas5.natas.labs.overthewire.org/"
#}
# cookies = {"loggedin": "1"}

response = requests.get(url, auth = (username, password))
# session = requests.Session()
# response = session.get(url, auth = (username, password), cookies = cookies)

print (response.text)
#print (re.findall(" natas8 is (.*)", response.text)[0])                                                                 
# pw DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe
