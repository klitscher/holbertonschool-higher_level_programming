#!/usr/bin/python3
"""Script to send a search request to a star wars api"""

import sys
import requests


if __name__ == '__main__':
    search = {'search': sys.argv[1]}
    url = 'https://swapi.co/api/people/'
    req = requests.get(url, params=search)
    json = req.json()
    results = json.get('results')
    print("Number of results: {}".format(json.get('count')))
    for res in results:
        print(res.get('name'))
