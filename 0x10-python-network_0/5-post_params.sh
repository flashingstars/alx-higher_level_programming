#!/bin/bash
#POST request with email and subject as variables sent to the URL displaying the response
curl -s -X POST -d "email=test@gmail.com&subject=I will be here for PLD" "$1"
