#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
#   file: FizzBuzz
#   date: 2014-08-30
#   author: jdenisco
#   email: james.denisco@genesys.com
#
# Copyright © 2014 jdenisco <james.denisco@genesys.com>
#

"""
Description:
Thinkful Lesson 4 
    Fizz Buzz
    V1
"""

number = int(raw_input("Please enter a number for me to count to: "))

if number > 100:
    print('Please enter a value less then or equal to 100')
    number = int(raw_input('Please re-enter number you would like to count to: '))
    

for i in range( 1, number+1):
    if i % 3 == 0:
        if i % 5 == 0:
            print("Fizz Buzz")
        else:
            print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
     print(i)
    


