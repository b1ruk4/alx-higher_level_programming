#!/usr/bin/python3
"""defining add_integer"""
def add_integer(a, b=98):
    """this function adds to integers and returns the sum"""

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError('b must be an integer')
     if a is None or (type(a) is not int and type(a) is not float):
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if type(a) in [float] or type(b) in [float]:
        a = int(round(a, 0))
        b = int(round(b, 0))
    return int(a) + int(b)
