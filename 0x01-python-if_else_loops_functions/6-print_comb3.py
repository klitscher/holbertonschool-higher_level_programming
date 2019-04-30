#!/usr/bin/python3
for i in range(1, 10):
    for j in range(i, 10):
        if (i-1) == 8 and j == 9:
            print("{:d}{:d}".format((i-1), j))
        else:
            print("{:d}{:d}, ".format((i-1), j), end="")
