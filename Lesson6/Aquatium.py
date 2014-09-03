#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
#   file: Aquatium
#   date: 2014-09-02
#   author: jdenisco
#   email: james.denisco@genesys.com
#
# Copyright © 2014 jdenisco <james.denisco@genesys.com>
#

"""
Description:
"""


class Aquarium(object):
    fish = []

    def __init__(self, fish):
        self.fish = fish

    def feed(self, food):
        for fish in self.fish:
            fish.eat(food)


class Fish(object):
    color = "Blue"

    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print self.name + " is eating " + food + "!"


class Goldfish(Fish):
    color = "Gold"


class Flounder(Fish):
    pass


my_fish = [Goldfish("Spencer"), Goldfish("Vladimir"), Flounder("Susan")]
my_aquarium = Aquarium(my_fish)
my_aquarium.feed('flakes')
for fish in my_aquarium.fish:
    print fish.name
