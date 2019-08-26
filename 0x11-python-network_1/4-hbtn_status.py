#!/usr/bin/python3
"""Script to get a url with requests"""

import requests


if __name__ == '__main__':
    req = requests.get('https://intranet.hbtn.io/status')
    req.encoding = 'utf-8'
    print('Body response:')
    print('\t- type: {}'.format(type(req.text)))
    print('\t- content: {}'.format(req.text))
