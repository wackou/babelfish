#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2013 the BabelFish authors. All rights reserved.
# Use of this source code is governed by the 3-clause BSD license
# that can be found in the LICENSE file.
#

from __future__ import unicode_literals, print_function, division
from babelfish import UnicodeMixin


class Language(UnicodeMixin):
    """This class represents a human language.

    You can initialize it with pretty much anything, as it knows conversion
    from ISO-639 2-letter and 3-letter codes, English and French names.

    You can also distinguish languages for specific countries, such as
    Portuguese and Brazilian Portuguese.

    There are various properties on the language object that give you the
    representation of the language for a specific usage, such as .alpha3
    to get the ISO 3-letter code, or .opensubtitles to get the OpenSubtitles
    language code.


    >>> Language('fr')
    Language(French)

    >>> Language('eng').french_name
    'anglais'

    >>> Language('pt(br)').country.name
    'Brazil'

    >>> Language('Español (Latinoamérica)').country.name
    'Latin America'

    >>> Language('Spanish (Latin America)') == Language('Español (Latinoamérica)')
    True

    >>> Language('zz', strict=False).name
    'Undetermined'

    >>> Language('pt(br)').opensubtitles
    'pob'

    """

    def __init__(self, language, country=None, strict=False, scheme=None):
        """Check in IETF recommendation whether:
          - country should be named region or sth else (eg: Latin America is not a country)

        :param bool strict: if strict=True, raise ValueError on unknown language
                            if strict=False, return Language(Undetermined)

        """
        raise NotImplementedError


    @property
    def alpha2(self):
        raise NotImplementedError

    @property
    def alpha3(self):
        raise NotImplementedError

    @property
    def terminological(self):
        """See http://en.wikipedia.org/wiki/ISO_639-2#B_and_T_codes for a more
        detailed description."""
        raise NotImplementedError

    @property
    def name(self):
        raise NotImplementedError

    @property
    def french_name(self):
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



    ## Should be dealt with as a plugin
    @property
    def opensubtitles(self):
        raise NotImplementedError

    ## Should be dealt with as a plugin
    @property
    def tmdb(self):
        raise NotImplementedError
