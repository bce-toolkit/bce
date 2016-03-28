#!/usr/bin/env python
#
#  Copyright 2014 - 2016 The BCE Authors. All rights reserved.
#  Use of this source code is governed by a BSD-style license that can be
#  found in the license.txt file.
#

import sympy as _sympy


def convert_int_string_to_rational(symbol):
    """Convert a string that contains an integer to SymPy's internal integer type.

    :type symbol: str
    :param symbol: The string.
    :return: Converted value.
    """

    return _sympy.Integer(int(symbol))


def convert_float_string_to_rational(symbol):
    """Convert a string that contains a float number to SymPy's internal Rational type.

    :type symbol: str
    :param symbol: The string.
    :return: Converted value.
    """

    #  Find the position of decimal dot.
    dot_pos = symbol.find(".")

    #  Get the value of its numerator and denominator.
    numerator = int(symbol[:dot_pos] + symbol[dot_pos + 1:])
    denominator = 10 ** (len(symbol) - 1 - dot_pos)

    return _sympy.Rational(numerator, denominator)
