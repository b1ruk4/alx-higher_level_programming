#!/usr/bin/python3
"""
    File: 0-read_file.py
    Description: This function reads files.
    Author: B1ruk4
    Date: Aug 5 2022
"""


"""defining a function read_file"""


def read_file(filename=""):
    """the function takes file
        print the content
      Args:
        filename(any): name of the file

    """
    
    with open(filename, encoding="utf-8") as myfile:
        print(myfile.read(), end="")
