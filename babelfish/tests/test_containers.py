#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2013 the BabelFish authors. All rights reserved.
# Use of this source code is governed by the 3-clause BSD license
# that can be found in the LICENSE file.
#
from __future__ import unicode_literals, print_function, division
from babelfish import Language, Country
from babelfish.test import allTests
from unittest import TestCase, TextTestRunner


class LanguageListTestCase(TestCase):
    def test_list_contains(self):
        languages = list([Language('fr'), Language('en-US'), Language('en-GB')])
        self.assertTrue(Language('fr') in languages)
        self.assertTrue(Language('en-US') in languages)
        self.assertTrue(Language('en') not in languages)
        self.assertTrue(Language('fr-BE') not in languages)

    def test_language_list_contains(self):
        languages = language_list(['fr', 'en-US', 'en-GB'])
        self.assertTrue(Language('fr') in languages)
        self.assertTrue(Language('en-US') in languages)
        self.assertTrue(Language('en') not in languages)
        self.assertTrue(Language('fr-BE') in languages)

    def test_list_index(self):
        languages = [Language('fr'), Language('en-US'), Language('en-GB')]
        self.assertTrue(languages.index(Language('fr')) == 0)
        self.assertTrue(languages.index(Language('en-US')) == 1)
        self.assertTrue(languages.index(Language('en-GB')) == 2)
        with self.assertRaises(ValueError):
            languages.index(Language('fr-BE'))

    def test_language_list_index(self):
        languages = language_list(['fr', 'en-US', 'en-GB'])
        self.assertTrue(languages.index(Language('fr')) == 0)
        self.assertTrue(languages.index(Language('en-US')) == 1)
        self.assertTrue(languages.index(Language('en-GB')) == 2)
        self.assertTrue(languages.index(Language('fr-BE')) == 0)


class LanguageSetTestCase(TestCase):
    def test_set_contains(self):
        languages = set([Language('fr'), Language('en-US'), Language('en-GB')])
        self.assertTrue(Language('fr') in languages)
        self.assertTrue(Language('en-US') in languages)
        self.assertTrue(Language('en') not in languages)
        self.assertTrue(Language('fr-BE') not in languages)

    def test_language_set_contains(self):
        languages = language_set(['fr', 'en-US', 'en-GB'])
        self.assertTrue(Language('fr') in languages)
        self.assertTrue(Language('en-US') in languages)
        self.assertTrue(Language('en') not in languages)
        self.assertTrue(Language('fr-BE') in languages)

    def test_language_set_intersect(self):
        languages = language_set(['fr', 'en-US', 'en-GB'])
        self.assertTrue(len(languages & language_set([Language('en')])) == 2)
        self.assertTrue(len(language_set([Language('en')]) & languages) == 2)
        self.assertTrue(len(languages & language_set([Language('fr')])) == 1)

    def test_language_set_substract(self):
        languages = language_set(['fr', 'en-US', 'en-GB'])
        self.assertTrue(len(languages - language_set(['en'])) == 1)
        self.assertTrue(len(languages - language_set(['en-US'])) == 2)
        self.assertTrue(len(languages - language_set(['en-US', 'fr'])) == 1)



suite = allTests(TestLanguage)

if __name__ == '__main__':
    TextTestRunner(verbosity=2).run(suite)
