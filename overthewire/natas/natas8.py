#!/usr/bin/env python3
# request with basic authentication

# http://natas8.natas.labs.overthewire.org

# vuln: Base64

import requests
import re

username = 'natas8'
password = 'DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe'

url = f'http://{username}.natas.labs.overthewire.org/'
print (url)

url = f'http://{username}.natas.labs.overthewire.org/'

session = requests.Session()
# response = session.get(url, auth=(username, password))
response = session.post(url, data = {"secret": "oubWYf2kBq", "submit" : "submit"}, auth=(username, password))
content = response.text

print(content)

# result:
# Access granted. The password for natas9 is W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl
