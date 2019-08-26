#!/usr/bin/python3
"""Takes in a string and sends a search request to the Star Wars API"""


import requests
import sys

r = requests.get('https://swapi.co/api/people/?search={}'.format(sys.argv[1]))
print('Number of results: {}'.format(r.json()['count']))
for res in r.json()['results']:
    print(res['name'])
