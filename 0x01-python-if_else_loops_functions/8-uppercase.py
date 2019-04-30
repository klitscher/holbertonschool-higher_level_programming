#!/usr/bin/python3
def uppercase(str):
    length = len(str)
    for i in range(0, length):
        j = str[i]
        if ord(j) >= ord('a') and ord(j) <= ord('z'):
            j = chr(ord(j) - 32)
        print("{}".format(j), end="")
    print("")
