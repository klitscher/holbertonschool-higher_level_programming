#!/bin/bash
# Sends a url request, displays the response
curl -sI "$1" | grep 'Content-Length' | cut -d ' ' -f 2
