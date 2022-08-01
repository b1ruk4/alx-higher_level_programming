#!/usr/bin/python3
"""defining an object attribute lookup function"""


def lookup(obj):
    """Returns a list of all the available methodes"""
    return(dir(obj))
