#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import requests
url = 'https://notify-api.line.me/api/notify'
token = 'YOUR-SECRET-TOKENS'
headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+token}
msg = 'YOUR WEB SERVER LINE Notify'
r = requests.post(url, headers=headers, data = {'message':msg})
print r.text
