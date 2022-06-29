#!/usr/bin/python3
def fizzbuzz():
    for number in range(1, 101):
        if (number % 3 == 0  and number % 5 == 0):
            print("%s%s" % ("fizzbuzz", end=' ')
        elif (number % 3 == 0):
            print("%s" % ("fizz", end=' ')
        elif (number % 5 == 0):
            print("%s" % ("buzz", end=' ')
        else:
            print("%d" % (number), end=' ')
