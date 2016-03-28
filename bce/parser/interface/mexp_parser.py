#!/usr/bin/env python
#
#  Copyright 2014 - 2016 The BCE Authors. All rights reserved.
#  Use of this source code is governed by a BSD-style license that can be
#  found in the license.txt file.
#

import bce.parser.interface.printer as _interface_printer


class MathExpressionParserInterface:
    """Interface for math expression parsers."""

    def __init__(self):
        """Initialize."""

        pass

    # noinspection PyMethodMayBeStatic
    def parse(self, expression, options, protected_header_enabled=False, protected_header_prefix="X"):
        """Parse an expression.

        :type expression: str
        :type options: bce.option.Option
        :type protected_header_enabled: bool
        :type protected_header_prefix: str
        :param expression: The expression.
        :param options: The options.
        :param protected_header_enabled: Whether the protected headers are enabled.
        :param protected_header_prefix: The prefix of the protected headers.
        :return: The calculated value.
        """

        raise RuntimeError("parse() method should be overrided.")

    # noinspection PyMethodMayBeStatic
    def substitute(self, value, substitute_map=None):
        """Substitute a value.

        :type substitute_map: dict | None
        :param value: The value.
        :param substitute_map: The substitution map.
        :return: The substituted value.
        """

        raise RuntimeError("substitute() method should be overrided.")

    # noinspection PyMethodMayBeStatic
    def print_out(
            self,
            value,
            printer_type=_interface_printer.PRINTER_TYPE_TEXT,
            protected_header_enabled=False,
            protected_header_prefix="X"
    ):
        """Print a value.

        :type printer_type: int
        :type protected_header_enabled: bool
        :type protected_header_prefix: str
        :param value: The value.
        :param printer_type: The printer type.
        :param protected_header_enabled: Whether the protected headers are enabled.
        :param protected_header_prefix: The prefix of the protected headers.
        :rtype : str | bce.dom.mathml.all.Base
        :return: The printed string or MathML object.
        """

        raise RuntimeError("print_out() method should be overrided.")
