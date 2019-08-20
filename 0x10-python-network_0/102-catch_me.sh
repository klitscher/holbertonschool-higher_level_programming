#!/bin/bash
# Grabs status code without a pipe
curl -sL -X PUT "$1" -d "user_id=98" -H "Origin: HolbertonSchool"
