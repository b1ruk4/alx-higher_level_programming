#!/usr/bin/python3
def no_c(my_string):
    rm = 'c', 'C'
    copy = [x for x in my_string if not x in rm]
    return ("".join(copy))
