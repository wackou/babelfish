#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2013 the BabelFish authors. All rights reserved.
# Use of this source code is governed by the 3-clause BSD license
# that can be found in the LICENSE file.
#

from __future__ import unicode_literals, print_function, division

__version__ = '0.1-dev'
__all__ = []

# Do python3 detection before importing any other module, to be sure that
# it will then always be available
# with code from http://lucumr.pocoo.org/2011/1/22/forwards-compatible-python/
import sys

if sys.version_info[0] >= 3:
    PY3, PY2 = True, False
    unicode_text_type = str
    native_text_type = str
    base_text_type = str
    class UnicodeMixin(object):
        __str__ = lambda x: x.__unicode__()

else:
    PY3, PY2 = False, True
    __all__ = [ str(s) for s in __all__ ] # fix imports for python2
    unicode_text_type = unicode
    native_text_type = str
    base_text_type = basestring
    class UnicodeMixin(object):
        __str__ = lambda x: unicode(x).encode('utf-8')
