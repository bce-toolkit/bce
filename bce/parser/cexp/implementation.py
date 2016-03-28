#!/usr/bin/env python
#
#  Copyright 2014 - 2016 The BCE Authors. All rights reserved.
#  Use of this source code is governed by a BSD-style license that can be
#  found in the license.txt file.
#

import bce.parser.cexp.token as _cexp_token
import bce.parser.cexp.parser as _cexp_parser
import bce.parser.cexp.substitution as _cexp_substitution
import bce.parser.interface.cexp_parser as _cexp_interface
import bce.parser.interface.printer as _interface_printer
import bce.parser.cexp.printer_mathml as _cexp_printer_mathml
import bce.parser.cexp.printer_text as _cexp_printer_text


class ChemicalEquationParserImplementation(_cexp_interface.ChemicalEquationParserInterface):
    """Implementation of chemical equation parser."""
    
    def __init__(self):
        """Initialize."""

        _cexp_interface.ChemicalEquationParserInterface.__init__(self)

    def parse(self, expression, option, mexp_protected_header_enabled=False, mexp_protected_header_prefix="X"):
        """Parse a chemical equation.

        :type expression: str
        :type option: bce.option.Option
        :type mexp_protected_header_enabled: bool
        :type mexp_protected_header_prefix: str
        :param expression: The chemical equation.
        :param option: The options.
        :param mexp_protected_header_enabled: Whether the protected headers are enabled.
        :param mexp_protected_header_prefix: The prefix of the protected headers.
        :rtype : bce.parser.interface.cexp_parser.ChemicalEquation
        :return: The chemical equation object.
        """

        #  Tokenize.
        token_list = _cexp_token.tokenize(expression, option)

        #  Parse.
        cexp_object = _cexp_parser.parse(
            expression,
            token_list,
            option,
            mexp_protected_header_enabled=mexp_protected_header_enabled,
            mexp_protected_header_prefix=mexp_protected_header_prefix
        )

        return cexp_object

    def substitute(self, cexp_object, option, substitute_map=None):
        """Substitute a chemical equation.

        :type cexp_object: bce.parser.interface.cexp_parser.ChemicalEquation
        :type substitute_map: dict | None
        :param cexp_object: The chemical equation object.
        :param substitute_map: The substitution map.
        :rtype : bce.parser.interface.cexp_parser.ChemicalEquation
        :return: The substituted chemical equation object.
        """

        return _cexp_substitution.substitute_cexp(cexp_object, substitute_map, option)

    def print_out(
            self,
            cexp_object,
            molecule_parser,
            mexp_parser,
            mexp_protected_header_enabled=False,
            mexp_protected_header_prefix="X",
            printer_type=_interface_printer.PRINTER_TYPE_TEXT
    ):
        """Print a chemical equation.

        :type cexp_object: bce.parser.interface.cexp_parser.ChemicalEquation
        :type molecule_parser: bce.parser.interface.molecule_parser.MoleculeParserInterface
        :type mexp_parser: bce.parser.interface.mexp_parser.MathExpressionParserInterface
        :type mexp_protected_header_enabled: bool
        :type mexp_protected_header_prefix: str
        :type printer_type: int
        :param cexp_object: The chemical equation object.
        :param molecule_parser: The molecule parser.
        :param mexp_parser: The math expression parser.
        :param mexp_protected_header_enabled: Whether the MEXP protected headers are enabled.
        :param mexp_protected_header_prefix: The prefix of the MEXP protected headers.
        :param printer_type: The printer type.
        :rtype : str | bce.dom.mathml.all.Base
        :return: The printed string or MathML object.
        """

        if printer_type == _interface_printer.PRINTER_TYPE_TEXT:
            return _cexp_printer_text.print_cexp(cexp_object, molecule_parser, mexp_parser)
        elif printer_type == _interface_printer.PRINTER_TYPE_MATHML:
            return _cexp_printer_mathml.print_cexp(
                cexp_object,
                molecule_parser,
                mexp_parser,
                mexp_protected_header_enabled=mexp_protected_header_enabled,
                mexp_protected_header_prefix=mexp_protected_header_prefix
            )
        else:
            raise RuntimeError("BUG: Unhandled printer type.")
