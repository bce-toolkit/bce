#!/usr/bin/env python
#
#  Copyright 2014 - 2016 The BCE Authors. All rights reserved.
#  Use of this source code is governed by a BSD-style license that can be
#  found in the license.txt file.
#

import bce.parser.interface.printer as _interface_printer


class SubstituteError(Exception):
    """Molecule substitution error."""

    pass


class MoleculeParserInterface:
    """Interface for math expression parsers."""

    def __init__(self):
        """Initialize."""

        pass

    # noinspection PyMethodMayBeStatic
    def parse_expression(
            self,
            expression,
            options,
            mexp_protected_header_enabled=False,
            mexp_protected_header_prefix="X"
    ):
        """Parse an expression.

        :type expression: str
        :type options: bce.option.Option
        :type mexp_protected_header_enabled: bool
        :type mexp_protected_header_prefix: str
        :param expression: The expression.
        :param options: The options.
        :param mexp_protected_header_enabled: Whether the MEXP protected headers are enabled.
        :param mexp_protected_header_prefix: The prefix of the MEXP protected headers.
        :rtype : bce.parser.ast.molecule.ASTNodeMolecule | bce.parser.ast.molecule.ASTNodeHydrateGroup
        :return: The root node of the AST.
        """

        raise RuntimeError("parse_expression() method should be overrided.")

    # noinspection PyMethodMayBeStatic
    def parse_ast(
            self,
            expression,
            ast_root,
            option,
            mexp_protected_header_enabled=False,
            mexp_protected_header_prefix="X"
    ):
        """Parse an AST.

        :type expression: str
        :type ast_root: bce.parser.ast.molecule.ASTNodeMolecule | bce.parser.ast.molecule.ASTNodeHydrateGroup
        :type option: bce.option.Option
        :type mexp_protected_header_enabled: bool
        :type mexp_protected_header_prefix: str
        :param expression: The expression.
        :param ast_root: The root node of the AST.
        :param option: The options.
        :param mexp_protected_header_enabled: Whether the MEXP protected headers are enabled.
        :param mexp_protected_header_prefix: The prefix of the MEXP protected headers.
        :rtype : dict
        :return: The parsed element dictionary.
        """

        raise RuntimeError("parse_ast() method should be overrided.")

    # noinspection PyMethodMayBeStatic
    def substitute(self, ast_root, substitute_map=None):
        """Substitute a ast_root.

        :type ast_root: bce.parser.ast.molecule.ASTNodeMolecule | bce.parser.ast.molecule.ASTNodeHydrateGroup
        :type substitute_map: dict | None
        :param ast_root: The ast_root.
        :param substitute_map: The substitution map.
        :rtype : bce.parser.ast.molecule.ASTNodeMolecule | bce.parser.ast.molecule.ASTNodeHydrateGroup | None
        :return: The substituted AST root node.
        """

        raise RuntimeError("substitute() method should be overrided.")

    # noinspection PyMethodMayBeStatic
    def print_out(
            self,
            ast_root,
            mexp_parser,
            mexp_protected_header_enabled=False,
            mexp_protected_header_prefix="X",
            printer_type=_interface_printer.PRINTER_TYPE_TEXT
    ):
        """Print a molecule.

        :type ast_root: bce.parser.ast.molecule.ASTNodeMolecule | bce.parser.ast.molecule.ASTNodeHydrateGroup
        :type mexp_parser: bce.parser.interface.mexp_parser.MathExpressionParserInterface
        :type mexp_protected_header_enabled: bool
        :type mexp_protected_header_prefix: str
        :type printer_type: int
        :param ast_root: The AST root.
        :param printer_type: The printer type.
        :param mexp_parser: The math expression parser.
        :param mexp_protected_header_enabled: Whether the MEXP protected headers are enabled.
        :param mexp_protected_header_prefix: The prefix of the MEXP protected headers.
        :rtype : str | bce.dom.mathml.all.Base
        :return: The printed string or MathML object.
        """

        raise RuntimeError("print_out() method should be overrided.")
