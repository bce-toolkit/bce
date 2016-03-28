#!/usr/bin/env python
#
#  Copyright 2014 - 2016 The BCE Authors. All rights reserved.
#  Use of this source code is governed by a BSD-style license that can be
#  found in the license.txt file.
#

import bce.option as _opt

#  Option keys.
OPT_KEY_MEXP_PARSER_IMPLEMENTATION = "parser.implementation.mexp"
OPT_KEY_MOLECULE_PARSER_IMPLEMENTATION = "parser.implementation.molecule"
OPT_KEY_CEXP_PARSER_IMPLEMENTATION = "parser.implementation.cexp"


class OptionWrapper:
    """Option operations wrapper."""

    def __init__(self, opt):
        """Initialize the wrapper.

        :type opt: bce.option.Option
        :param opt: The options.
        """

        self.__opt = opt

    def get_mexp_parser(self):
        """Get the MEXP parser.

        :rtype : bce.parser.interface.mexp_parser.MathExpressionParserInterface
        :return: The parser implementation.
        """

        return self.__opt.get_option_value(OPT_KEY_MEXP_PARSER_IMPLEMENTATION)

    def set_mexp_parser(self, parser_impl):
        """Set the MEXP parser.

        :type parser_impl: bce.parser.interface.mexp_parser.MathExpressionParserInterface
        :param parser_impl: The parser implementation.
        """

        self.__opt.set_option_value(OPT_KEY_MEXP_PARSER_IMPLEMENTATION, parser_impl)

    def get_molecule_parser(self):
        """Get the molecule parser.

        :rtype : bce.parser.interface.molecule_parser.MoleculeParserInterface
        :return: The parser implementation.
        """

        return self.__opt.get_option_value(OPT_KEY_MOLECULE_PARSER_IMPLEMENTATION)

    def set_molecule_parser(self, parser_impl):
        """Set the molecule parser.

        :type parser_impl: bce.parser.interface.molecule_parser.MoleculeParserInterface
        :param parser_impl: The parser implementation.
        """

        self.__opt.set_option_value(OPT_KEY_MOLECULE_PARSER_IMPLEMENTATION, parser_impl)

    def get_cexp_parser(self):
        """Get the CEXP parser.

        :rtype : bce.parser.interface.cexp_parser.ChemicalEquationParserInterface
        :return: The parser implementation.
        """

        return self.__opt.get_option_value(OPT_KEY_CEXP_PARSER_IMPLEMENTATION)

    def set_cexp_parser(self, parser_impl):
        """Set the CEXP parser.

        :type parser_impl: bce.parser.interface.cexp_parser.ChemicalEquationParserInterface
        :param parser_impl: The parser implementation.
        """

        self.__opt.set_option_value(OPT_KEY_CEXP_PARSER_IMPLEMENTATION, parser_impl)


def register_default_mexp_parser(parser_impl):
    """Register default MEXP parser.

    :type parser_impl: bce.parser.interface.mexp_parser.MathExpressionParserInterface
    :param parser_impl: The parser implementation.
    """

    _opt.register_option_pair(OPT_KEY_MEXP_PARSER_IMPLEMENTATION, parser_impl)


def register_default_molecule_parser(parser_impl):
    """Register default molecule parser.

    :type parser_impl: bce.parser.interface.molecule_parser.MoleculeParserInterface
    :param parser_impl: The parser implementation.
    """

    _opt.register_option_pair(OPT_KEY_MOLECULE_PARSER_IMPLEMENTATION, parser_impl)


def register_default_cexp_parser(parser_impl):
    """Register the default CEXP parser.

    :type parser_impl: bce.parser.interface.cexp_parser.ChemicalEquationParserInterface
    :param parser_impl: The parser implementation.
    """

    _opt.register_option_pair(OPT_KEY_CEXP_PARSER_IMPLEMENTATION, parser_impl)
