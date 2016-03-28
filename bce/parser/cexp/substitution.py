#!/usr/bin/env python
#
#  Copyright 2014 - 2016 The BCE Authors. All rights reserved.
#  Use of this source code is governed by a BSD-style license that can be
#  found in the license.txt file.
#

import bce.math.constant as _math_cst
import bce.parser.common.error as _cm_error
import bce.parser.interface.cexp_parser as _cexp_interface
import bce.parser.interface.molecule_parser as _ml_interface
import bce.parser.interface.option as _interface_opt
import sympy as _sympy


def _check_substituted_mexp(value):
    """Check the substituted math expression.

    :param value: The value math expression.
    :raise SubstituteError: Raise this error if the value is invalid.
    """

    if isinstance(value, _sympy.S.ComplexInfinity.__class__):
        raise _cexp_interface.SubstituteError("Divided zero.")


def substitute_cexp(cexp_object, substitute_map, options):
    """Do substitution on a chemical equation.

    :type cexp_object: bce.parser.interface.cexp_parser.ChemicalEquation
    :type substitute_map: dict
    :type options: bce.option.Option
    :param cexp_object: The chemical equation object.
    :param substitute_map: The substitution map.
    :param options: The options.
    :rtype : bce.parser.interface.cexp_parser.ChemicalEquation
    :return: The substituted chemical equation.
    """

    if cexp_object.get_left_item_count() == 0 or cexp_object.get_right_item_count() == 0:
        raise _cexp_interface.SubstituteError("Unsupported form.")

    #  Wrap the interface options.
    if_opt = _interface_opt.OptionWrapper(options)

    #  Get the molecule parser.
    ml_parser = if_opt.get_molecule_parser()

    #  Initialize an empty chemical equation.
    new_ce = _cexp_interface.ChemicalEquation()

    #  Process left items.
    for idx in range(0, cexp_object.get_left_item_count()):
        #  Get the item.
        item = cexp_object.get_left_item(idx)

        #  Get and substitute the AST.
        try:
            ast_root = ml_parser.substitute(item.get_molecule_ast(), substitute_map)
        except _ml_interface.SubstituteError:
            raise _cexp_interface.SubstituteError("Can't substitute sub-molecule.")

        #  Substitute the origin coefficient.
        item_coeff = item.get_coefficient().subs(substitute_map).simplify()
        _check_substituted_mexp(item_coeff)

        if ast_root is None:
            continue

        #  Get and substitute the coefficient.
        coeff = (item_coeff * ast_root.get_prefix_number()).simplify()
        _check_substituted_mexp(coeff)

        #  Clear the prefix number of the AST.
        ast_root.set_prefix_number(_math_cst.ONE)

        #  Re-parse the AST.
        try:
            #  Re-parse.
            atom_dict = ml_parser.parse_ast(
                "-",
                ast_root,
                options,
                mexp_protected_header_enabled=False
            )

            #  Add the substituted item.
            new_ce.append_left_item(item.get_operator_id(), coeff, ast_root, atom_dict)
        except _cm_error.Error:
            raise _cexp_interface.SubstituteError("Re-parse error.")

    #  Process right items.
    for idx in range(0, cexp_object.get_right_item_count()):
        #  Get the item.
        item = cexp_object.get_right_item(idx)

        #  Get and substitute the AST.
        try:
            ast_root = ml_parser.substitute(item.get_molecule_ast(), substitute_map)
        except _ml_interface.SubstituteError:
            raise _cexp_interface.SubstituteError("Can't substitute sub-molecule.")

        #  Substitute the origin coefficient.
        item_coeff = item.get_coefficient().subs(substitute_map).simplify()
        _check_substituted_mexp(item_coeff)

        if ast_root is None:
            continue

        #  Get and substitute the coefficient.
        coeff = (item_coeff * ast_root.get_prefix_number()).simplify()
        _check_substituted_mexp(coeff)

        #  Clear the prefix number of the AST.
        ast_root.set_prefix_number(_math_cst.ONE)

        try:
            #  Re-parse.
            atom_dict = ml_parser.parse_ast(
                "-",
                ast_root,
                options,
                mexp_protected_header_enabled=False
            )

            #  Add the substituted item.
            new_ce.append_right_item(item.get_operator_id(), coeff, ast_root, atom_dict)
        except _cm_error.Error:
            raise _cexp_interface.SubstituteError("Re-parse error.")

    #  Remove items with coefficient 0.
    new_ce.remove_items_with_coefficient_zero()

    #  Move items that have negative coefficient to another side.
    new_ce.move_items_with_negative_coefficient_to_another_side()

    #  Integerize the coefficients.
    new_ce.coefficients_integerize()

    #  Check.
    if new_ce.get_left_item_count() == 0 or new_ce.get_right_item_count() == 0:
        raise _cexp_interface.SubstituteError("Side(s) eliminated.")

    return new_ce
