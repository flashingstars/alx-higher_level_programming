#!/usr/bin/python3
""" Retrieving a header from a get request """

import requests
from sys import argv

if __name__ == "__main__":
    response = requests.get(argv[1])
    print(response.headers["X-Request-Id"])
