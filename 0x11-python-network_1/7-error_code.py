#!/usr/bin/python3
"""Takes in a URL, sends a request to the URL and
displays the body of the response"""

import requests
from sys import argv
if __name__ == "__main__":
    r = requests.get(argv[1])
    status = r.status_code
    if status >= 400:
        print("Error code: {}".format(status))
    else:
        print(r.text)
