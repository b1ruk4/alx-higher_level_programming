#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    for i in my_list:
        max_int = my_list[0]
        if my_list[i] > max_int:
            max_int = my_list[i]
        return (max_int)
