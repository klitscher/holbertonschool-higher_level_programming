#!/usr/bin/python3
"""Script to send a request to github api"""

import sys
import requests


if __name__ == '__main__':
    url = 'https://api.github.com/user'
    req = requests.get(url, auth=(sys.argv[1], sys.argv[2]))
    result = req.json()
    print(result.get('id'))
