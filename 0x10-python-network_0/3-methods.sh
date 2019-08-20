#!/bin/bash
# Sends displays all http methods accepted
curl -is -X OPTIONS "$1" | grep 'Allow' | cut -d ' ' -f 2,3,4
