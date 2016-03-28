#!/usr/bin/env python
#
#  Copyright 2014 - 2016 The BCE Authors. All rights reserved.
#  Use of this source code is governed by a BSD-style license that can be
#  found in the license.txt file.
#


def check_input_expression_characters(expression):
    """Check whether characters of an expression are all valid.

    :type expression: str
    :rtype : bool
    :param expression: The expression.
    :return: True if all characters are valid.
    """

    #  Construct valid characters.
    valid_char = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz()[]{}+-*/^<>;.,="

    #  Check all characters.
    for ch in expression:
        if valid_char.find(ch) == -1:
            return False

    return True
