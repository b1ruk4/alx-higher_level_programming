#!/usr/bin/python3
"""defining a function read_file"""


def read_file(filename=""):
    """the function takes filen
        print the content

    Args:
        filename(any): name of the file

    """
    with open(filename, encoding="utf-8) as myfile:
        print(myfile.read(), end="")
