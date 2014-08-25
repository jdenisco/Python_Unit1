#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
#   file: Exception_Handling
#   date: 2014-08-25
#   author: jdenisco
#   email: james.denisco@genesys.com
#
# Copyright © 2014 jdenisco <james.denisco@genesys.com>
#

"""
Description:
"""


while True:
    try:
        n = raw_input("Please enter an integer: ")
        n = int(n)
        break
    except ValueError:
        print("No valid integer! Please try again ...")
print "Great, you successfully entered an integer!"

