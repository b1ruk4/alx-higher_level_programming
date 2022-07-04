#!/usr/bin/python3
def no_c(my_string):
    rm = ""
    for x in my_string:
        if x != 'c' and x != 'C':
            rm += x
    return (rm)
