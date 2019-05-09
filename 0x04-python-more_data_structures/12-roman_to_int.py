#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    if roman_string is None or isinstance(roman_string, str) is False:
        return 0
    if len(roman_string) < 1:
        return 0
    for i in roman_string:
        total += roman.get(i)
    return total
