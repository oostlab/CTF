#!/usr/bin/env python3
# request with basic authentication

# vuln: php xor

import requests
import re

username = 'natas11'
password = 'U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK'

url = f'http://{username}.natas.labs.overthewire.org/'
#print (url)

session = requests.Session()
response = requests.get(url, auth = (username, password))
# response = requests.post(url, auth = (username, password))


print (response.text)
#print (re.findall(" natas8 is (.*)", response.text)[0])
# pw DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe
