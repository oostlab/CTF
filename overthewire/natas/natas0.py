#!/usr/bin/env python3
# request with basic authentication

import requests
import re

username = 'natas0'
password = 'natas0'

url = f'http://{username}.natas.labs.overthewire.org'



#print (url)
response = requests.get(url, auth = (username, password))

print (response.text)

# de response bevat de gevraagde password
# Via regular expressie filteren we het wachtwoord
password_list = re.findall("<!--The password for natas1 is (.*) -->", response.text)

# initialize an empty string
str1 = " " 
    
# return string  
new_password = str1.join(password_list)


print(new_password)