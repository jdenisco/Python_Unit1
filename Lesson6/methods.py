#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
#   file: methods
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
    def move(self, speed):
        print 'Swimming %s!' % speed
        print self.name + ' is moving ' + speed + '!'

myfish = Fish()

myfish.name = 'Spencer'
myfish.move('fast')
myfish.color = 'gold'

myotherfish = Fish()
myotherfish.name = 'Susan'
myotherfish.color = 'Blue'


