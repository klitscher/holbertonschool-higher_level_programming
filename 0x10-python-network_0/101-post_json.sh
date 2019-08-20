#!/bin/bash
# Post a json file
curl -sH "Content-Type: application/json" -d @"$2" "$1"
