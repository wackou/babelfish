#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2013 the BabelFish authors. All rights reserved.
# Use of this source code is governed by the 3-clause BSD license
# that can be found in the LICENSE file.
#
from setuptools import setup, find_packages


setup(name='babelfish',
    version='0.1-dev',
    license='BSD',
    description='A module for working with languages and countries',
    long_description=open('README.rst').read() + '\n\n' + open('CHANGES').read(),
    keywords='babelfish language country locale',
    url='https://github.com/wackou/babelfish',
    author='Nicolas Wack',
    author_email='wackou@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    package_data={'babelfish': ['iso-639-3.tab', 'iso-3166-1.txt']},
    classifiers=['Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Topic :: Multimedia :: Video',
        'Topic :: Software Development :: Libraries :: Python Modules'],
    test_suite='babelfish.tests.suite',
    entry_points={'babelfish.converters': ['alpha2 = babelfish.converters.alpha2:Alpha2Converter',
                                           'alpha3b = babelfish.converters.alpha3b:Alpha3BConverter',
                                           'name = babelfish.converters.name:NameConverter',
                                           'opensubtitles = babelfish.converters.opensubtitles:OpenSubtitlesConverter']})
