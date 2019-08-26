#!/usr/bin/python3
"""Script to send a request to github api"""

import sys
import requests


if __name__ == '__main__':
    url = 'https://api.github.com/repos/{}/{}/commits'.format(
        sys.argv[2], sys.argv[1])
    req = requests.get(url)
    result = req.json()
    for i in range(10):
        sha = result[i].get('sha')
        commit = result[i].get('commit')
        author = commit.get('author')
        name = author.get('name')
        print("{}: {}".format(sha, name))
