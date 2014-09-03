#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
#   file: Fish
#   date: 2014-09-02
#   author: jdenisco
#   email: james.denisco@genesys.com
#
# Copyright © 2014 jdenisco <james.denisco@genesys.com>
#

"""
Description:
"""

class Fish:
    breathes_in_water = True
    skin = 'scales'


myfish = Fish()
print myfish.skin

if myfish.breathes_in_water:
    print 'Glug glug'

