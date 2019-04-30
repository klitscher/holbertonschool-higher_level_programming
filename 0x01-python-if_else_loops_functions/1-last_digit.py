#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    modNum = number % 10
else:
    modNum = number % -10
str = "Last digit of"
str2 = "is less than 6 and not 0"
if modNum > 5:
    print("{} {:d} is {:d} and is greater than 5".format(str, number, modNum))
elif modNum == 0:
    print("{} {:d} is {:d} and is 0".format(str, number, modNum))
else:
    print("{} {:d} is {:d} and {}".format(str, number, modNum, str2))
