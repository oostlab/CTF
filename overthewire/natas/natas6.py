#!/usr/bin/env python3
# request with basic authentication

import requests
import re

username = 'natas6'
password = 'aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1'

url = f'http://{username}.natas.labs.overthewire.org/'
#print (url)

#d define header settings referers
#header_settings = {
#    "Referer" : "http://natas5.natas.labs.overthewire.org/"
#}
# cookies = {"loggedin": "1"}

response = requests.post(url, data = { "secret" : "FOEIUWGHFEEUHOFUOIU", "submit" : "submit"}, auth = (username, password))
# session = requests.Session()
# response = session.get(url, auth = (username, password), cookies = cookies)

print (response.text)
print (re.findall(" natas7 is (.*)", response.text)[0])                                                                 
# password natas7 7z3hEENjQtflzgnT29q7wAvMNfZdh0i9