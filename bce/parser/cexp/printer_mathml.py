#!/usr/bin/env python
#
#  Copyright 2014 - 2016 The BCE Authors. All rights reserved.
#  Use of this source code is governed by a BSD-style license that can be
#  found in the license.txt file.
#

import bce.dom.mathml.all as _mathml
import bce.parser.interface.printer as _interface_printer


def print_cexp(
        cexp_object,
        molecule_parser,
        mexp_parser,
        mexp_protected_header_enabled=False,
        mexp_protected_header_prefix="X"
):
    """Print the chemical equation.

    :type cexp_object: bce.parser.interface.cexp_parser.ChemicalEquation
    :type molecule_parser: bce.parser.interface.molecule_parser.MoleculeParserInterface
    :type mexp_parser: bce.parser.interface.mexp_parser.MathExpressionParserInterface
    :type mexp_protected_header_enabled: bool
    :type mexp_protected_header_prefix: str
    :param cexp_object: The chemical equation object.
    :param molecule_parser: The molecule parser.
    :param mexp_parser: The math expression parser.
    :param mexp_protected_header_enabled: Whether the MEXP protected headers are enabled.
    :param mexp_protected_header_prefix: The prefix of the MEXP protected headers.
    :rtype : bce.dom.mathml.all.Base
    :return: The printed MathML.
    """

    assert cexp_object.get_left_item_count() != 0 and cexp_object.get_right_item_count() != 0

    #  Initialize an empty CE expression.
    r = _mathml.RowComponent()

    #  Process items on left side.
    for idx in range(0, cexp_object.get_left_item_count()):
        #  Get the item.
        item = cexp_object.get_left_item(idx)

        #  Insert operator.
        if item.is_operator_plus():
            if len(r) != 0:
                r.append_object(_mathml.OperatorComponent(_mathml.OPERATOR_PLUS))

        if item.is_operator_minus():
            r.append_object(_mathml.OperatorComponent(_mathml.OPERATOR_MINUS))

        #  Get the AST root node.
        ast_root = item.get_molecule_ast()

        #  Backup the prefix number.
        origin_coefficient = ast_root.get_prefix_number()

        #  Set the prefix to the balanced coefficient.
        ast_root.set_prefix_number(item.get_coefficient() * origin_coefficient)

        #  Print the molecule.
        r.append_object(molecule_parser.print_out(
            ast_root,
            mexp_parser,
            mexp_protected_header_enabled=mexp_protected_header_enabled,
            mexp_protected_header_prefix=mexp_protected_header_prefix,
            printer_type=_interface_printer.PRINTER_TYPE_MATHML
        ))

        #  Restore the prefix number.
        ast_root.set_prefix_number(origin_coefficient)

    #  Insert '='.
    r.append_object(_mathml.OperatorComponent(_mathml.OPERATOR_EQUAL))

    #  Mark whether processing molecule is the first molecule on right side.
    r_is_first = True

    #  Process items on right side.
    for idx in range(0, cexp_object.get_right_item_count()):
        #  Get the item.
        item = cexp_object.get_right_item(idx)

        #  Insert operator.
        if item.is_operator_plus():
            if not r_is_first:
                r.append_object(_mathml.OperatorComponent(_mathml.OPERATOR_PLUS))

        if item.is_operator_minus():
            r.append_object(_mathml.OperatorComponent(_mathml.OPERATOR_MINUS))

        #  Get the AST root node.
        ast_root = item.get_molecule_ast()

        #  Backup the prefix number.
        origin_coefficient = ast_root.get_prefix_number()

        #  Set the prefix to the balanced coefficient.
        ast_root.set_prefix_number(item.get_coefficient() * origin_coefficient)

        #  Print the molecule.
        r.append_object(molecule_parser.print_out(
            ast_root,
            mexp_parser,
            mexp_protected_header_enabled=mexp_protected_header_enabled,
            mexp_protected_header_prefix=mexp_protected_header_prefix,
            printer_type=_interface_printer.PRINTER_TYPE_MATHML
        ))

        #  Restore the prefix number.
        ast_root.set_prefix_number(origin_coefficient)

        #  Switch off the mark.
        r_is_first = False

    return r
