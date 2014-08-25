#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
#   file: else
#   date: 2014-08-25
#   author: jdenisco
#   email: james.denisco@genesys.com
#
# Copyright © 2014 jdenisco <james.denisco@genesys.com>
#

"""
Description:
"""
import sys
file_name = sys.argv[1]
text = []
try:
    fh = open(file_name, 'r')
except IOError:
    print 'cannot open', file_name
else:
    text = fh.readlines()
    fh.close()

if text:
    print text[100]
