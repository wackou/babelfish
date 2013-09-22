# -*- coding: utf-8 -*-
#
# Copyright (c) 2013 the BabelFish authors. All rights reserved.
# Use of this source code is governed by the 3-clause BSD license
# that can be found in the LICENSE file.
#
from __future__ import unicode_literals
from functools import partial
from pkg_resources import resource_stream, iter_entry_points  # @UnresolvedImport
from .country import Country

__all__ = ['CONVERTERS', 'reload_converters', 'LANGUAGES', 'Language', 'register_converter', 'unregister_converter']


LANGUAGES = set()
with resource_stream('babelfish', 'iso-639-3.tab') as f:
    f.readline()
    for l in f:
        (alpha3, _, _, _, _, _, _, _) = l.decode('utf-8').split('\t')
        LANGUAGES.add(alpha3)

CONVERTERS = {}


def reload_converters():
    CONVERTERS.clear()
    for ep in iter_entry_points('babelfish.converters'):
        if ep.name not in CONVERTERS:
            CONVERTERS[ep.name] = ep.load()()


class LanguageMeta(type):
    def __init__(cls, name, bases, attrs):
        reload_converters()

        def fromcode(cls, code, converter):
            return cls(*CONVERTERS[converter].reverse(code))

        for converter_name in CONVERTERS.keys():
            setattr(cls, 'from' + converter_name, classmethod(partial(fromcode, converter=converter_name)))
        return super(LanguageMeta, cls).__init__(name, bases, attrs)


class Language(object):
    """A human language

    A human language is composed of a language part following the ISO-639
    standard and can be country-specific as per the ISO-3166 standard.

    The :class:`Language` is extensible with plug-ins to support custom
    language conversions. Refer to the `plug-ins`__ section for more details.

    >>> Language('fra')
    <Language French>

    >>> Language('ara').alpha2
    'ar'

    >>> Language('por', 'BR').opensubtitles
    'pob'

    """
    __metaclass__ = LanguageMeta

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
        if self.country is not None:
            return '<Language {}, country={}>'.format(self.name, self.country.name)
        return '<Language {}>'.format(self.name)


def register_converter(name, converter):
    CONVERTERS[name] = converter()

    def fromcode(cls, code, converter):
        return cls(*CONVERTERS[converter].reverse(code))
    setattr(Language, 'from' + name, classmethod(partial(fromcode, converter=name)))


def unregister_converter(name):
    if name not in CONVERTERS:
        raise ValueError('{} is not a converter'.format(name))
    del CONVERTERS[name]
    delattr(Language, 'from' + name)
