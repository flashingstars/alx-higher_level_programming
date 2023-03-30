#!/bin/bash
#send a request to a URL with curl and display the size of the response in bytes
curl -s -w '%{size_download}' -o /dev/null "$1"
