#!/usr/bin/env python
from __future__ import unicode_literals, print_function
import babelfish

print(babelfish.Language.from_opensubtitles('pob'))
for language, country in [('fra', None), ('por', 'BR')]:
    l = babelfish.Language(language, country)
    print(l, l.country, l.alpha3, l.alpha2, l.alpha3b, l.opensubtitles)
