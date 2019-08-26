#!/usr/bin/python3
"""Takes in a URL, sends a request to the URL and displays the value of the
X-Request-Id variable found in the header of the response"""


import urllib.request
import sys

with urllib.request.urlopen(sys.argv[1]) as response:
    head = response.info().__dict__
    header = [x[1] for x in head['_headers'] if x[0] == 'X-Request-Id']
    print(header[0])
