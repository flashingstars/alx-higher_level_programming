#!/bin/bash
#A script to delete request passed as first argument and displays the body of the response
curl -sX DELETE "$1"
