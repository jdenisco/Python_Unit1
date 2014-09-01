#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
#   file: built-in
#   date: 2014-08-31
#   author: jdenisco
#   email: james.denisco@genesys.com
#
# Copyright © 2014 jdenisco <james.denisco@genesys.com>
#

"""
Description:
"""

def distance_from_zero(s):
    if  isinstance(s, int) or isinstance(s, float):
        return abs(s)
    else:
        return 'Nope'


print (distance_from_zero(10))
print (distance_from_zero(1.0))
print (distance_from_zero(1.110))
print (distance_from_zero('a'))
print (distance_from_zero('True'))


