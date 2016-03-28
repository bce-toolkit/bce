#!/usr/bin/env python
#
#  Copyright 2014 - 2016 The BCE Authors. All rights reserved.
#  Use of this source code is governed by a BSD-style license that can be
#  found in the license.txt file.
#


class ParserErrorWrapper(Exception):
    """Parser error."""

    pass


class LogicErrorWrapper(Exception):
    """Logic error."""

    pass


class InvalidCharacterException(Exception):
    """Invalid character exception."""

    pass


class SubstitutionErrorWrapper(Exception):
    """Substitution error."""

    pass
