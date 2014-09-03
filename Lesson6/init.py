#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
#   file: init
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
    def __init__(self, fish_name, color):
        self.name = fish_name
        self.color = color



myfish = Fish("Spencer", 'Gold')
print myfish.name
print myfish.color
