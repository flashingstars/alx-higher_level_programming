#!/usr/bin/python3
""" Displaying the body of the response with error code if status is >= 400 """

import requests
from sys import argv

if __name__ == "__main__":
    try:
        response = requests.get(argv[1])
        error = response.raise_for_status()
        if not error:
            print(response.text)
    except requests.exceptions.HTTPError as err:
        if response.status_code >= 400:
            print(f'Error code: {response.status_code}')
            print(type(response.status_code))
