#!/usr/bin/python3

"""
File: 1-write_file.py
Desctiption: This function writes to files
Author: B1ruk4
Date Created: Aug 5 2022
"""


def write_file(filename="", text=""):
    """
    takes a file  and writes to it
    """
    with open(filename, "w", encoding="utf8") as myfile:
        return (myfile.write(text))
