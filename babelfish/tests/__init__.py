#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2013 the BabelFish authors. All rights reserved.
# Use of this source code is governed by the 3-clause BSD license
# that can be found in the LICENSE file.
#

from __future__ import unicode_literals, print_function, division
from unittest import TestCase, TestLoader, TextTestRunner

def allTests(testClass):
    return TestLoader().loadTestsFromTestCase(testClass)
