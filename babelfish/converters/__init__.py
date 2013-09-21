# -*- coding: utf-8 -*-
#
# Copyright (c) 2013 the BabelFish authors. All rights reserved.
# Use of this source code is governed by the 3-clause BSD license
# that can be found in the LICENSE file.
#
from collections import defaultdict
from operator import attrgetter
from pkg_resources import iter_entry_points
from ..exceptions import NoConverterError


__all__ = ['CONVERTERS', 'Converter', 'load_converters', 'register_converter']

CONVERTERS = {}


class Converter(object):
    from_code = 'alpha3'

    def convert(self, from_code, country=None):
        raise NotImplementedError

    def reverse(self, code):
        raise NotImplementedError


def load_converters(force_reload=False):
    for ep in iter_entry_points(__name__):
        if force_reload or ep.name not in CONVERTERS:
            CONVERTERS[ep.name] = ep.load()()


def register_converter(name, converter):
    CONVERTERS[name] = converter()
