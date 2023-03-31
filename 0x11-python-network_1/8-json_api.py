#!/usr/bin/python3
""" Sending a POST request with the letter as parameter """

import requests
from sys import argv

if __name__ == "__main__":
    try:
        data = argv[1]
    except IndexError:
        data = ""
    url = "http://0.0.0.0:5000/search_user"
    response = requests.post(url, {'q': data})
    header = response.headers['Content-Type']
    if header == 'application/json':
        my_dict = response.json()
        if my_dict:
            print(f'[{my_dict["id"]}] {my_dict["name"]}')
        else:
            print("No result")
    else:
        print("Not a valid JSON")
