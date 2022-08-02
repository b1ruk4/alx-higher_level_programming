#!/usr/bin/python3
"""defining a function readfile"""


def read_file(filename=""):
    """the function takes filenam 
        print the content"""
    with open("{}".format(filename)) as myfile:
        print(myfile.read())
