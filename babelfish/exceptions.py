# -*- coding: utf-8 -*-
#
# Copyright (c) 2013 the BabelFish authors. All rights reserved.
# Use of this source code is governed by the 3-clause BSD license
# that can be found in the LICENSE file.
#


class BabelfishError(Exception):
    pass


class ConverterError(BabelfishError):
    pass


class NoConversionError(ConverterError):
    pass


class NoConverterError(ConverterError):
    pass
