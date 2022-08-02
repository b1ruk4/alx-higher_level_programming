#!/usr/bin/python3
"""Defining a function read file"""


def read_file(filename=""):
    """takes the file name and prints it out"""
    with open("{}".format(filename, encode="utf=8") as filename:
            filename.read()

print(filename.read())
            
