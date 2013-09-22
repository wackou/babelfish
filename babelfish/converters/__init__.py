# Copyright (c) 2013 the BabelFish authors. All rights reserved.
# Use of this source code is governed by the 3-clause BSD license
# that can be found in the LICENSE file.
#
from collections import defaultdict
from operator import attrgetter
from pkg_resources import iter_entry_points
from ..exceptions import NoConverterError

__all__ = ['Converter']


class Converter(object):
    def convert(self, from_code, country=None):
        raise NotImplementedError

    def reverse(self, code):
        raise NotImplementedError
