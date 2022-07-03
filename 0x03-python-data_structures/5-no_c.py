#!/usr/bin/python3
def no_c(my_string):
    rm_char = 'c', 'C'
    my_string = ''.join(i for i in my_string if not i in rm_char)
    return my_string
