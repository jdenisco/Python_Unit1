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


