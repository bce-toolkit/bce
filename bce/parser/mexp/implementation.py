#!/usr/bin/env python
#
#  Copyright 2014 - 2016 The BCE Authors. All rights reserved.
#  Use of this source code is governed by a BSD-style license that can be
#  found in the license.txt file.
#

import bce.parser.interface.mexp_parser as _mexp_interface
import bce.parser.interface.printer as _interface_printer
import bce.parser.mexp.token as _mexp_token
import bce.parser.mexp.parser as _mexp_parser
import bce.parser.mexp.printer_mathml as _mexp_printer_mathml
import bce.parser.mexp.printer_text as _mexp_printer_text
import bce.parser.mexp.rpn as _mexp_rpn


class MathExpressionParserImplementation(_mexp_interface.MathExpressionParserInterface):
    """Implementation of math expression parser."""

    def __init__(self):
        """Initialize the object."""

        _mexp_interface.MathExpressionParserInterface.__init__(self)

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

        #  Tokenize.
        token_list = _mexp_token.tokenize(expression, options)

        #  Convert the token list to a RPN token list.
        rpn_token_list = _mexp_parser.parse_to_rpn(
            expression,
            token_list,
            options,
            protected_header_enabled=protected_header_enabled,
            protected_header_prefix=protected_header_prefix
        )

        #  Evaluate.
        result = _mexp_rpn.calculate_rpn(expression, rpn_token_list, options)

        return result

    def substitute(self, value, substitute_map=None):
        """Substitute a value.

        :type substitute_map: dict | None
        :param value: The value.
        :param substitute_map: The substitution map.
        :return: The substituted value.
        """

        if substitute_map is None:
            substitute_map = {}

        return value.subs(substitute_map)

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

        if printer_type == _interface_printer.PRINTER_TYPE_TEXT:
            return _mexp_printer_text.print_mexp(value)
        elif printer_type == _interface_printer.PRINTER_TYPE_MATHML:
            return _mexp_printer_mathml.print_mexp(
                value,
                protected_header_enabled=protected_header_enabled,
                protected_header_prefix=protected_header_prefix
            )
        else:
            raise RuntimeError("BUG: Unhandled printer type.")
