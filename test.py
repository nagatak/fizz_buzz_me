#!/usr/bin/env python

import unittest
from fizz_buzz import fizz_buzz

class TestFizzBuzz(unittest.TestCase):

    def test_fizz_buzz_1(self):
        actual = fizz_buzz(1)
        expected = '1'
        self.assertEqual(actual, expected)

    def test_fizz_buzz_2(self):
        actual = fizz_buzz(2)
        expected = '2'
        self.assertEqual(actual, expected)

    def test_fizz_buzz_3(self):
        actual = fizz_buzz(3)
        expected = 'fizz'
        self.assertEqual(actual, expected)

    def test_fizz_buzz_5(self):
        actual = fizz_buzz(5)
        expected = 'buzz'
        self.assertEqual(actual, expected)

    def test_fizz_buzz_15(self):
        actual = fizz_buzz(15)
        expected = 'fizzbuzz'
        self.assertEqual(actual, expected)

    def test_fizz_buzz_45(self):
        actual = fizz_buzz(45)
        expected = 'fizzbuzz'
        self.assertEqual(actual, expected)

    def test_fizz_buzz_11654(self):
        actual = fizz_buzz(11654)
        expected = '11654'
        self.assertEqual(actual, expected)

    def test_fizz_buzz_11655(self):
        actual = fizz_buzz(11655)
        expected = 'fizzbuzz'
        self.assertEqual(actual, expected)


##########################

if __name__ == '__main__':
    unittest.main()
