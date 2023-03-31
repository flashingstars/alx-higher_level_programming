#!/usr/bin/python3
# A script to open a URL

from urllib.request import urlopen

if __name__ == "__main__":
    with urlopen("https://alx-intranet.hbtn.io/status") as f:
        body = f.read()
    print('Body response:')
    print(f'    - type: {type(body)}')
    print(f'    - content: {body}')
    print(f'    - utf8 content: {body.decode("utf-8")}')
