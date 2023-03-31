#!/usr/bin/python3
""" Sending a http request with header data """

from urllib import request, parse
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    value = {"email": argv[2]}
    header = parse.urlencode(value).encode()
    with request.urlopen(request.Request(url, header)) as response:
        print(response.read().decode("utf-8"))
