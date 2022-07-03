#!/usr/bin/python3
def no_c(my_string):
    rm_char = 'c', 'C'
    for i in rm_char:
        my_string = my_string.replace(i, '')
    return my_string
