#!/usr/bin/python3
"""
File: 2-append_write.py
Description: appendes to existing file
Author: b1ruk4
Date Created: Aug 5 2022
"""

def append_write(filename="", text=""):
    """
    This function appends a string to existing file
    """


    with open(filename, 'a', encoding="utf8") as myfile:
        return myfile.write(text)
