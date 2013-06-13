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
import io


class TestLanguage(TestCase):

    ############################################################################
    # formerly guessit tests

    def check_languages(self, languages, scheme=None):
        for lang1, lang2 in languages.items():
            self.assertEqual(Language(lang1, scheme=scheme),
                             Language(lang2, scheme=scheme))

    def test_addic7ed(self):
        languages = {'English': 'en',
                     'English (US)': 'en',
                     'English (UK)': 'en',
                     'Italian': 'it',
                     'Portuguese': 'pt',
                     'Portuguese (Brazilian)': 'pt',
                     'Romanian': 'ro',
                     'Español (Latinoamérica)': 'es',
                     'Español (España)': 'es',
                     'Spanish (Latin America)': 'es',
                     'Español': 'es',
                     'Spanish': 'es',
                     'Spanish (Spain)': 'es',
                     'French': 'fr',
                     'Greek': 'el',
                     'Arabic': 'ar',
                     'German': 'de',
                     'Croatian': 'hr',
                     'Indonesian': 'id',
                     'Hebrew': 'he',
                     'Russian': 'ru',
                     'Turkish': 'tr',
                     'Swedish': 'se',
                     'Czech': 'cs',
                     'Dutch': 'nl',
                     'Hungarian': 'hu',
                     'Norwegian': 'no',
                     'Polish': 'pl',
                     'Persian': 'fa'}

        self.check_languages(languages)

    def test_subswiki(self):
        languages = {'English (US)': 'en', 'English (UK)': 'en', 'English': 'en',
                     'French': 'fr', 'Brazilian': 'po', 'Portuguese': 'pt',
                     'Español (Latinoamérica)': 'es', 'Español (España)': 'es',
                     'Español': 'es', 'Italian': 'it', 'Català': 'ca'}

        self.check_languages(languages)

    def test_tvsubtitles(self):
        languages = {'English': 'en', 'Español': 'es', 'French': 'fr', 'German': 'de',
                     'Brazilian': 'br', 'Russian': 'ru', 'Ukrainian': 'ua', 'Italian': 'it',
                     'Greek': 'gr', 'Arabic': 'ar', 'Hungarian': 'hu', 'Polish': 'pl',
                     'Turkish': 'tr', 'Dutch': 'nl', 'Portuguese': 'pt', 'Swedish': 'sv',
                     'Danish': 'da', 'Finnish': 'fi', 'Korean': 'ko', 'Chinese': 'cn',
                     'Japanese': 'jp', 'Bulgarian': 'bg', 'Czech': 'cz', 'Romanian': 'ro'}

        self.check_languages(languages)

    def test_opensubtitles(self):
        opensubtitles_langfile = file_in_same_dir(__file__, 'opensubtitles_languages_2012_05_09.txt')
        langs = [ l.strip().split('\t') for l in io.open(opensubtitles_langfile, encoding='utf-8') ][1:]
        for lang in langs:
            # check that we recognize the opensubtitles language code correctly
            # and that we are able to output this code from a language
            self.assertEqual(lang[0], Language(lang[0], scheme='opensubtitles').opensubtitles)
            if lang[1]:
                # check we recognize the opensubtitles 2-letter code correctly
                self.check_languages({lang[0]: lang[1]}, scheme='opensubtitles')

    def test_tmdb(self):
        # examples from http://api.themoviedb.org/2.1/language-tags
        for lang in ['en-US', 'en-CA', 'es-MX', 'fr-PF']:
            self.assertEqual(lang, Language(lang).tmdb)


    def test_subtitulos(self):
        languages = {'English (US)': 'en', 'English (UK)': 'en', 'English': 'en',
                     'French': 'fr', 'Brazilian': 'po', 'Portuguese': 'pt',
                     'Español (Latinoamérica)': 'es', 'Español (España)': 'es',
                     'Español': 'es', 'Italian': 'it', 'Català': 'ca'}

        self.check_languages(languages)

    def test_thesubdb(self):
        languages = {'af': 'af', 'cs': 'cs', 'da': 'da', 'de': 'de', 'en': 'en', 'es': 'es', 'fi': 'fi',
                     'fr': 'fr', 'hu': 'hu', 'id': 'id', 'it': 'it', 'la': 'la', 'nl': 'nl', 'no': 'no',
                     'oc': 'oc', 'pl': 'pl', 'pt': 'pt', 'ro': 'ro', 'ru': 'ru', 'sl': 'sl', 'sr': 'sr',
                     'sv': 'sv', 'tr': 'tr'}

        self.check_languages(languages)

    def test_language_object(self):
        self.assertEqual(len(list(set([Language('qwerty'), Language('asdf')]))), 1)
        d = { Language('qwerty'): 7 }
        d[Language('asdf')] = 23
        self.assertEqual(d[Language('qwerty')], 23)

    def test_exceptions(self):
        self.assertEqual(Language('br'), Language('pt(br)'))

        # languages should be equal regardless of country
        self.assertEqual(Language('br'), Language('pt'))

        self.assertEqual(Language('unknown'), Language('und'))



    ############################################################################
    # formerly subliminal tests

    def test_attrs(self):
        language = Language('French')
        self.assertTrue(language.alpha2 == 'fr')
        self.assertTrue(language.alpha3 == 'fre')
        self.assertTrue(language.terminologic == 'fra')
        self.assertTrue(language.name == 'French')
        self.assertTrue(language.french_name == u'français')

    def test_eq(self):
        language = Language('French')
        self.assertTrue(language == Language('fr'))
        self.assertTrue(language == Language('fre'))
        self.assertTrue(language == Language('fra'))
        self.assertTrue(language == Language('Français'))

    def test_ne(self):
        self.assertTrue(Language('French') != Language('en'))

    def test_in(self):
        self.assertTrue(Language('Portuguese (BR)') in Language('Portuguese - Brazil'))
        self.assertTrue(Language('Portuguese (BR)') in Language('Portuguese'))
        self.assertTrue(Language('Portuguese') not in Language('Portuguese (BR)'))

    def test_with_country(self):
        self.assertTrue(Language('Portuguese (BR)').country == Country('Brazil'))
        self.assertTrue(Language('pt_BR').country == Country('Brazil'))
        self.assertTrue(Language('fr - France').country == Country('France'))
        self.assertTrue(Language('fra', country='FR').country == Country('France'))
        self.assertTrue(Language('fra', country=Country('FRA')).country == Country('France'))

    def test_eq_with_country(self):
        self.assertTrue(Language('Portuguese (BR)') == Language('Portuguese - Brazil'))
        self.assertTrue(Language('English') == Language('en'))

    def test_ne_with_country(self):
        self.assertTrue(Language('Portuguese') != Language('Portuguese (BR)'))
        self.assertTrue(Language('English (US)') != Language('English (GB)'))

    def test_hash(self):
        self.assertTrue(hash(Language('French')) == hash('fre'))

    def test_missing(self):
        with self.assertRaises(ValueError):
            Language('zzz')


suite = allTests(TestLanguage)

if __name__ == '__main__':
    TextTestRunner(verbosity=2).run(suite)
