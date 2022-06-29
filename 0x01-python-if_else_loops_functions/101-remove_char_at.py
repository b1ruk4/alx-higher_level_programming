#!/usr/bin/python3
def remove_char_at(str, n):
    lett = ""
    i = 0
    for c in str:
        if c != n:
            lett += c
        i += 1
    return lett
