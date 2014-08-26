#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
#   file: Exception_Handling1
#   date: 2014-08-25
#   author: jdenisco
#   email: jimd@jdenisco.com
#
# Copyright © 2014 jdenisco <jimd@jdenisco.com>
#

"""
Description:
"""

import sys

try:
    f = open('intergers.txt')
    s = f.readline()
    i = int(s.strip())
#except IOError as (errno, strerror):
#    print "I/O error({0}): {1}".format(errno, strerror)
#except ValueError:
#    print "No valid integer in line."
except (IOError, ValueError):
    print "An I/O error or a ValueError occurrred"
except:
    print "Unexpected error:", sys.exc_info()[0]
    raise

