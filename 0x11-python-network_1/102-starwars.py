#!/usr/bin/python3
"""Script to send a search request to a star wars api"""

import sys
import requests


if __name__ == '__main__':
    search = {'search': sys.argv[1]}
    url = 'https://swapi.co/api/people/'
    req = requests.get(url, params=search)
    json = req.json()
    print("Number of results: {}".format(json.get('count')))
    while True:
        json = req.json()
        results = json.get('results')
        for res in results:
            print(res.get('name'))
            film_list = res.get('films')
            for film_url in film_list:
                new_req = requests.get(film_url).json()
                print("\t{}".format(new_req.get('title')))
        next_page = json.get('next')
        if next_page is None:
            break
        req = requests.get(next_page)
