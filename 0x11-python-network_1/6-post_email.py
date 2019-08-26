#!/usr/bin/python3
"""Script to send a Post request with request"""

import requests
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    email = {'email': sys.argv[2]}
    req = requests.post(url, data=email)
    print(req.text)
