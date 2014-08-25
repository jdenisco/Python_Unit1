#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
#   file: Exception_Handling2
#   date: 2014-08-25
#   author: jdenisco
#   email: james.denisco@genesys.com
#
# Copyright © 2014 jdenisco <james.denisco@genesys.com>
#

"""
Description:
"""
try:
    x = float(raw_input("Your number: "))
    inverse = 1.0 / x
except ValueError:
    print "You should have given either an int or a float"
except ZeroDivisionError:
    print "Infinity"
finally:
    print("There may or may not have been an exception.")
