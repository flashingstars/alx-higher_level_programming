#!/usr/bin/python3
""" Retrieving a header from a urllib request """

from urllib.request import urlopen
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    with urlopen(url) as response:
        header = response.getheader("X-Request-Id")
    print(header)
