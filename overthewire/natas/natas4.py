#!/usr/bin/env python3
# request with basic authentication

import requests
import re

username = 'natas4'
password = 'Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ'

#d define header settings referers
header_settings = {
    "Referer" : "http://natas5.natas.labs.overthewire.org/"
}

url = f'http://{username}.natas.labs.overthewire.org/'
#print (url)

response = requests.get(url, auth = (username, password), headers = header_settings)

print (response.text)
# het resultaat bevat het password

