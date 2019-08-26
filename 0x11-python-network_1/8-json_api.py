#!/usr/bin/python3
"""Takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter"""

import requests
import sys

q = sys.argv[1] if len(sys.argv) > 1 else ""
r = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
if r.json() == {}:
    print('No result')
else:
    try:
        dic = r.json()
        print("[{}] {}".format(dic['id'], dic['name']))
    except ValueError:
        print('Not a valid JSON')
