#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
#   file: if
#   date: 2014-08-20
#   author: jdenisco
#   email: jimd@jdenisco.com
#
# Copyright © 2014 jdenisco <jimd@jdenisco.com>
#

"""
Description:
"""

number = 23
guess = int(raw_input('Enter an integer : '))

if guess == number:
    # New block starts here
    print 'Congratulations you guessed it.'
    print '(but you do not win any prizes!)'
    # block ends
elif guess < number:
    # another block
    print 'No, it us a little higher than that'
else:
    print 'No, it is a little lower than that'

print 'Done'