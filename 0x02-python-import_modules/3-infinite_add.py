#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    length = len(argv) - 1
    total = 0
    if length == 0:
        print("{:d}".format(length))
    elif length == 1:
        print("{:d}".format(argv[length]))
    else:
        for i in range(1, length + 1):
            total = total + int(argv[i])
        print("{:d}".format(total))
