#!/bin/bash
# Grabs status code without a pipe
curl -s -o /dev/null -w %{http_code} "$1"
