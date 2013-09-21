# -*- coding: utf-8 -*-
#
# Copyright (c) 2013 the BabelFish authors. All rights reserved.
# Use of this source code is governed by the 3-clause BSD license
# that can be found in the LICENSE file.
#
from __future__ import unicode_literals
from pkg_resources import resource_stream  # @UnresolvedImport
from .converters import CONVERTERS
from .country import Country


__all__ = ['LANGUAGES', 'Language']


LANGUAGES = set()
with resource_stream('babelfish', 'iso-639-3.tab') as f:
    f.readline()
    for l in f:
        (alpha3, _, _, _, _, _, _, _) = l.decode('utf-8').split('\t')
        LANGUAGES.add(alpha3)


class Language(object):
    """A human language

    A human language is composed of a language part following the ISO-639
    standard and can be country-specific as per the ISO-3166 standard.

    The :class:`Language` is extensible with plug-ins to support custom
    language conversions. Refer to the `plug-ins`__ section for more details.

    >>> Language('fra')
    <Language fra>

    >>> Language('ara').alpha2
    'ar'

    >>> Language('por', 'BR').opensubtitles
    'pob'

    """
    def __init__(self, language, country=None):
        if language not in LANGUAGES:
            raise ValueError('{} is not a valid language'.format(language))
        self.alpha3 = language
        self.country = None
        if isinstance(country, Country):
            self.country = country
        elif isinstance(country, (str, unicode)):
            self.country = Country(country)

    def __getattr__(self, name):
        if name not in CONVERTERS:
            raise AttributeError
        return CONVERTERS[name].convert(self.alpha3, self.country.alpha2 if self.country is not None else None)

    def __hash__(self):
        if self.country is None:
            return hash(self.alpha3)
        return hash(self.alpha3 + '-' + self.country.alpha2)

    def __eq__(self, other):
        return self.alpha3 == other.alpha3 and self.country == other.country

    def __ne__(self, other):
        return not self == other

    def __unicode__(self):
        return self.alpha3

    def __repr__(self):
        return '<Language {}>'.format(self.name)
