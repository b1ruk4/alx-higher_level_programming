#!/usr/bin/python3
def remove_char_at(str, n):
    string = ""
    i = 0
    for char in range(str):
        if char != n:
            string += i
        i += 1
    return string
