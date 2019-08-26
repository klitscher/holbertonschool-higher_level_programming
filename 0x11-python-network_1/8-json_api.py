#!/usr/bin/python3
"""Script to send a post request"""

import sys
import requests


if __name__ == '__main__':
    if len(sys.argv) is not 2:
        letter = {'q': ""}
    else:
        letter = {'q': sys.argv[1]}
    url = 'http://0.0.0.0:5000/search_user'
    req = requests.post(url, data=letter)
    try:
        json = req.json()
        if len(json) == 0:
            print("No result")
        else:
            print('[{}] {}'.format(json.get('id'), json.get('name')))
    except ValueError:
        print("Not a valid JSON")
