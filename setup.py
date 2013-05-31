#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# BabelFish - A module for working with languages and countries
# Copyright (c) 2013 Antoine Bertin <diaoulael@gmail.com>
# Copyright (c) 2013 Nicolas Wack <wackou@gmail.com>
#
# BabelFish is free software; you can redistribute it and/or modify it under
# the terms of the Lesser GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# BabelFish is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# Lesser GNU General Public License for more details.
#
# You should have received a copy of the Lesser GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

from setuptools import setup
import os
import babelfish


here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
NEWS = open(os.path.join(here, 'NEWS.rst')).read()

requires = []


args = dict(name = 'babelfish',
            version = babelfish.__version__,
            description = 'A module for working with languages and countries.',
            long_description = README + '\n\n' + NEWS,
            # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
            classifiers = [ 'Development Status :: 2 - Pre-Alpha',
                            'License :: OSI Approved :: BSD License',
                            'Operating System :: OS Independent',
                            'Intended Audience :: Developers',
                            'Programming Language :: Python :: 2',
                            'Programming Language :: Python :: 2.7',
                            'Programming Language :: Python :: 3',
                            'Programming Language :: Python :: 3.3',
                            'Topic :: Software Development :: Libraries :: Python Modules'
                            ],
            keywords = 'babelfish language country locale python library',
            author = 'Nicolas Wack',
            author_email = 'wackou@gmail.com',
            url = 'http://babelfish.readthedocs.org/',
            license = 'BSD',
            packages = [ 'babelfish', 'babelfish.test' ],
            include_package_data=True,
            install_requires = requires,
            entry_points=entry_points,
            #extras_require = { 'language_detection':  ['guess-language>=0.2'] },
            test_suite = 'babelfish.test'
            )


setup(**args)
