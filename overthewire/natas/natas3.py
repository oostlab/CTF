#!/usr/bin/env python3
# request with basic authentication

import requests
import re

username = 'natas3'
password = 'sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14'

#url = f'http://{username}.natas.labs.overthewire.org/robots.txt'
url = f'http://{username}.natas.labs.overthewire.org/s3cr3t/users.txt'
#print (url)

response = requests.get(url, auth = (username, password))

print (response.text)
# het resultaat bevat het password

