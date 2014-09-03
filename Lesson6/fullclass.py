#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
#   file: fullclass
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
    def __init__(self, fish_name, fish_color):
        self.name = fish_name
        self.color = fish_color
    def move(self, speed):
        print self.name + ' is moving ' + speed + '!'
    
spencer = Fish('Spencer', 'Gold')
spencer.move('slowly')
