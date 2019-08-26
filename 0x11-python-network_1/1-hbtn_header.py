#!/usr/bin/python3
"""Takes in a URL, sends a request to the URL and displays the value of the
X-Request-Id variable found in the header of the response"""


if __name__ == "__main__":
    import urllib.request
    import sys

    with urllib.request.urlopen(sys.argv[1]) as response:
        head = response.info().__dict__
        headers = head.get('_headers')
        h = [x[1] for x in headers if x[0] == 'X-Request-Id']
        print(h[0])
