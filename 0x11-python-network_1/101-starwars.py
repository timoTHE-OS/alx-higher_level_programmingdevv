#!/usr/bin/python3
"""Takes in a string and sends a search request to the Star Wars API"""

if __name__ == "__main__":
    import requests
    import sys

    r = requests.get('https://swapi.co/api/people/?search={}'
                     .format(sys.argv[1])).json()
    print('Number of results: {}'.format(r.get('count')))
    results = []
    results = results + r.get('results')
    while r.get('next') is not None:
        res = requests.get(r.get('next')).json()
        results = results + res.get('results')

    for res in results:
        print(res.get('name'))
