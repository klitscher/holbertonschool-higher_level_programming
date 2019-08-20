#!/bin/bash
# Sends a post request
curl -s -X POST "$1" -d "email=hr@holbertonschool.com&subject=I will always be here for PLD"
