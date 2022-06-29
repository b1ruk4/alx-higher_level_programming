#!/usr/bin/python3
def uppercase(str):
    string = ''
    for str in string:
        if ord(char) >= 97 and ord(char)<= 122:
            return(ord(char) - 32)
            string += "%c" % char
        else:
            return ord(char)
    print("{:s}".format(string))
