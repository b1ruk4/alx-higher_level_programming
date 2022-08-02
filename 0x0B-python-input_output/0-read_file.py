#!/usr/bin/python3
"""defining a function readfile"""


def read_file(filename=""):
    """the function takes filena 
        print the content"""
    with open(filename, encoding="utf-8)) as myfile:
        print(myfile.read(), end="")
