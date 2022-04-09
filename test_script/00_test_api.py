#!/bin/python3
import requests
import json

#API_URL = 'http://azure.rogermz.com:3000/'
API_URL = 'http://0.0.0.0:3000/saludo/RogerMZ'

# Test POST request
response = requests.request("GET", API_URL)

print(response.status_code)
print(response.text)

if response.status_code != 200:
    print('Se activo fail')
    exit(1)

