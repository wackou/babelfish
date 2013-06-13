#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2013 the BabelFish authors. All rights reserved.
# Use of this source code is governed by the 3-clause BSD license
# that can be found in the LICENSE file.
#

from __future__ import unicode_literals, print_function, division
from babelfish import UnicodeMixin


class Country(UnicodeMixin):
    """This class represents a country.

    You can initialize it with pretty much anything, as it knows conversion
    from ISO-3166 2-letter and 3-letter codes, and an English name.

    Check in IETF recommendation whether:
    - country should be named region or sth else (eg: Latin America is not a country)
    """

    def __init__(self, country, strict=False):
        """
        :param bool strict: if strict=True, raise ValueError on unknown language
                            if strict=False, return Language(Undetermined)
        """
        raise NotImplementedError


    @property
    def alpha2(self):
        raise NotImplementedError

    @property
    def name(self):
        raise NotImplementedError


    def __hash__(self):
        raise NotImplementedError

    def __eq__(self, other):
        raise NotImplementedError

    def __ne__(self, other):
        return not self == other

    def __nonzero__(self):
        raise NotImplementedError

    def __unicode__(self):
        raise NotImplementedError

    def __repr__(self):
        raise NotImplementedError
