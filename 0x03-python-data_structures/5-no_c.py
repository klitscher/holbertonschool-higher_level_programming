#!/usr/bin/python3
def no_c(my_string):
    l = list(my_string)
    if l.count('c') > 0:
        l.remove('c')
    if l.count('C') > 0:
        l.remove('C')
    str_list = "".join(l)
    return str_list
