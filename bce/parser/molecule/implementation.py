#!/usr/bin/env python
#
#  Copyright 2014 - 2016 The BCE Authors. All rights reserved.
#  Use of this source code is governed by a BSD-style license that can be
#  found in the license.txt file.
#

import bce.parser.interface.molecule_parser as _ml_interface
import bce.parser.interface.printer as _interface_printer
import bce.parser.molecule.token as _ml_token
import bce.parser.molecule.ast_generator as _ml_ast_generator
import bce.parser.molecule.ast_parser as _ml_ast_parser
import bce.parser.molecule.ast_printer_mathml as _ml_ast_printer_mathml
import bce.parser.molecule.ast_printer_text as _ml_ast_printer_text
import bce.parser.molecule.ast_substitution as _ml_ast_substitution


class MoleculeParserImplementation(_ml_interface.MoleculeParserInterface):
    """Implementation of molecule parser."""

    def __init__(self):
        """Initialize."""

        _ml_interface.MoleculeParserInterface.__init__(self)

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

        #  Tokenize.
        token_list = _ml_token.tokenize(
            expression,
            options,
            mexp_protected_header_enabled=mexp_protected_header_enabled,
            mexp_protected_header_prefix=mexp_protected_header_prefix
        )
        
        #  Generate the AST.
        ast_root = _ml_ast_generator.generate_ast(expression, token_list, options)

        return ast_root

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

        return _ml_ast_parser.parse_ast(
            expression,
            ast_root,
            option,
            mexp_protected_header_enabled=mexp_protected_header_enabled,
            mexp_protected_header_prefix=mexp_protected_header_prefix
        )

    def substitute(self, ast_root, substitute_map=None):
        """Substitute a ast_root.

        :type ast_root: bce.parser.ast.molecule.ASTNodeMolecule | bce.parser.ast.molecule.ASTNodeHydrateGroup
        :type substitute_map: dict | None
        :param ast_root: The ast_root.
        :param substitute_map: The substitution map.
        :rtype : bce.parser.ast.molecule.ASTNodeMolecule | bce.parser.ast.molecule.ASTNodeHydrateGroup | None
        :return: The substituted AST root node.
        """

        return _ml_ast_substitution.substitute_ast(
            ast_root,
            substitute_map
        )

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

        if printer_type == _interface_printer.PRINTER_TYPE_TEXT:
            return _ml_ast_printer_text.print_ast(
                ast_root,
                mexp_parser
            )
        elif printer_type == _interface_printer.PRINTER_TYPE_MATHML:
            return _ml_ast_printer_mathml.print_ast(
                ast_root,
                mexp_parser,
                mexp_protected_header_enabled=mexp_protected_header_enabled,
                mexp_protected_header_prefix=mexp_protected_header_prefix
            )
        else:
            raise RuntimeError("BUG: Unhandled printer type.")
