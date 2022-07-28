#!/usr/bin/python3

import unittest
from 6-max_integer import max_integer

class TestMaxInteger(unittest.TestCase):
    def test_integer(self):
      """Testes if the function prints the same output"""
        self.assertAlmostEqual(max_integer[1, 5, 0, 9], 9)
        self.assertAlmostEqual(max_integer[0, 00, 0, 0], 0)


    def test_value(self):
        """testes if what the list can and cann't do"""
        self.assertRaises(ValueError, 'a')
        self.assertRaises(ValueError, a)
    

    def test_type(self):
        """testes for type of value in list"""
        self.assertRaises(TypeError, max_integer[2+s, 5j, 0])
        self.arrestRaises(TypeError, max_integer[a, b, c, None, "and"]
      
        
