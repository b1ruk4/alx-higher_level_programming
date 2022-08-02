#!/usr/bin/python3
"""defining a function readfile"""


def read_file(filename=""):
    """the function takes filen
        print the content"""
    with open("{}".format(filename), encoding="utf-8)) as myfile:
        print(myfile.read(), end="")
