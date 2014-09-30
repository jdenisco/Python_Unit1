#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
#   file: FizzBuzzRefactor
#   date: 2014-09-02
#   author: jdenisco
#   email: jimd@jdenisco.com
#
# Copyright © 2014 jdenisco <jimd@jdenisco.com>
#

"""
Description:
FizzBuzz using functions
Refactor
Thinkful Lesson 4 
    Fizz Buzz
"""

import sys


def even(dividend, divisor):
    """ Is dividend evenly divisible by divisor """

    if dividend % divisor == 0:
        return True
    else:
        return False


def fizzbuzz(upperlimit=100):
    """ Run FizzBizz up to upperlimit """
    for i in range(1, upperlimit+1):
        if even(i, 3) is True:
            if even(i, 5) is True:
                print('FizzBuzz')
            else:
                print('Fizz')
        elif even(i, 5) is True:
            print('Buzz')
        else:
            print(i)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        upperlimit = int(sys.argv[1])
        fizzbuzz(upperlimit)
    else:
        fizzbuzz()

# Lets see if we can get number from command line.
#if len(sys.argv) > 1:
#    number = int(sys.argv[1])
#else:
#    number = int(raw_input("Please enter a number for me to count to: "))

#while number >= 100 or not number > 0:
#    print('Please enter a value less then or equal to 100')
##    number = int(raw_input('Please re-enter number you would like to count to: '))
