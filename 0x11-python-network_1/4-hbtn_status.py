#!/usr/bin/python3
""" Using request to fetch https://alx-intranet.hbtn.io/status """

import requests

if __name__ == "__main__":
    response = requests.get("https://alx-intranet.hbtn.io/status").text
    print("Body response:")
    print(f'    - type: {type(response)}')
    print(f'    - content: {response}')
