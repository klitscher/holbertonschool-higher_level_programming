#!/bin/bash
# Adds a custome header to request
curl -s "$1" -H "X-HolbertonSchool-User-Id: 98"
