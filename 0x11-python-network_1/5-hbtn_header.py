#!/usr/bin/python3
"""Script to get a url and display the value of a header"""

import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    req = requests.get(url)
    print(req.headers.get('x-request-id'))
