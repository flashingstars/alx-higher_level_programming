#!/usr/bin/python3
""" using an api with auth"""

import requests
import sys

if __name__ == "__main__":
    # Replace with your own GitHub username and personal access token
    username = sys.argv[1]
    password = sys.argv[2]

    # Set up the API endpoint and headers
    url = 'https://api.github.com/user'
    headers = {
        'Accept': 'application/vnd.github.v3+json'
    }

    # Authenticate using Basic Authentication with personal access token
    auth = (username, password)

    # Make the API request
    response = requests.get(url, headers=headers, auth=auth)
    print(response.json().get("id"))
