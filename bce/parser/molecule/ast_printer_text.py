#!/usr/bin/env python
#
#  Copyright 2014 - 2016 The BCE Authors. All rights reserved.
#  Use of this source code is governed by a BSD-style license that can be
#  found in the license.txt file.
#

import bce.math.constant as _math_cst
import bce.parser.ast.molecule as _ml_ast_base
import bce.parser.interface.printer as _interface_printer
import bce.parser.molecule.ast_bfs as _ml_ast_bfs


def _print_operand(operand_value, mexp_parser):
    """Print an operand.

    :type mexp_parser: bce.parser.interface.mexp_parser.MathExpressionParserInterface
    :param operand_value: The value of the operand (must be simplified).
    :param mexp_parser: The math expression parser.
    :rtype : str
    :return: The printed expression.
    """

    if operand_value.is_Integer:
        if operand_value == _math_cst.ONE:
            return ""
        else:
            return str(operand_value)
    else:
        return "{%s}" % mexp_parser.print_out(
            operand_value,
            printer_type=_interface_printer.PRINTER_TYPE_TEXT
        )


def _print_electronic(charge, mexp_parser):
    """Print an electronic charge value.

    :type mexp_parser: bce.parser.interface.mexp_parser.MathExpressionParserInterface
    :param charge: The charge value (must be simplified).
    :param mexp_parser: The math expression parser.
    :rtype : str
    :return: The printed expression.
    """

    #  Print the positivity part.
    if charge.is_negative:
        charge = -charge
        positivity = "e-"
    else:
        positivity = "e+"

    #  Print the charge part and do combination.
    return "<%s%s>" % (_print_operand(charge, mexp_parser), positivity)


def _print_suffix(node, mexp_parser):
    """Print the suffix part of specified node.

    :type node: bce.parser.ast.molecule._ASTNodeWithSuffix
    :type mexp_parser: bce.parser.interface.mexp_parser.MathExpressionParserInterface
    :param node: The node.
    :param mexp_parser: The math expression parser.
    :rtype : str
    :return: The printed expression.
    """

    #  Initialize the result.
    ret = ""

    #  Print the suffix number part if has.
    sfx = node.get_suffix_number().simplify()
    if not sfx.is_zero:
        ret += _print_operand(sfx, mexp_parser)

    return ret


def print_ast(root_node, mexp_parser):
    """Print an AST to text.

    :type root_node: bce.parser.ast.molecule.ASTNodeHydrateGroup | bce.parser.ast.molecule.ASTNodeMolecule
    :type mexp_parser: bce.parser.interface.mexp_parser.MathExpressionParserInterface
    :param root_node: The root node of the AST.
    :param mexp_parser: The math expression parser.
    :rtype : str
    :return: The printed expression.
    """

    #  Get the printing order.
    work_order = _ml_ast_bfs.do_bfs(root_node, True)

    #  Initialize the printing result container.
    printed = {}

    for work_node in work_order:
        if work_node.is_hydrate_group():
            assert isinstance(work_node, _ml_ast_base.ASTNodeHydrateGroup)

            #  Print the prefix number part.
            pfx = work_node.get_prefix_number().simplify()
            if pfx != _math_cst.ONE:
                model = _print_operand(pfx, mexp_parser) + "(%s)"
            else:
                model = "%s"

            #  Print children nodes.
            inner = printed[id(work_node[0])]
            for child_id in range(1, len(work_node)):
                inner += "." + printed[id(work_node[child_id])]

            #  Save printing result.
            printed[id(work_node)] = model % inner
        elif work_node.is_molecule():
            assert isinstance(work_node, _ml_ast_base.ASTNodeMolecule)

            #  Print the prefix number part.
            pfx = work_node.get_prefix_number().simplify()
            build = _print_operand(pfx, mexp_parser)

            #  Print children nodes.
            for child_id in range(0, len(work_node)):
                build += printed[id(work_node[child_id])]

            #  Print the electronic part.
            el_charge = work_node.get_electronic_count().simplify()
            if not el_charge.is_zero:
                build += _print_electronic(el_charge, mexp_parser)

            #  Save printing result.
            printed[id(work_node)] = build
        elif work_node.is_atom():
            assert isinstance(work_node, _ml_ast_base.ASTNodeAtom)

            #  Print and save the result.
            printed[id(work_node)] = work_node.get_atom_symbol() + _print_suffix(work_node, mexp_parser)
        elif work_node.is_parenthesis():
            assert isinstance(work_node, _ml_ast_base.ASTNodeParenthesisWrapper)

            #  Print and save the result.
            printed[id(work_node)] = "(%s)%s" % (
                printed[id(work_node.get_inner_node())],
                _print_suffix(work_node, mexp_parser)
            )
        elif work_node.is_abbreviation():
            assert isinstance(work_node, _ml_ast_base.ASTNodeAbbreviation)

            #  Print and save the result.
            printed[id(work_node)] = "[%s]%s" % (
                work_node.get_abbreviation_symbol(),
                _print_suffix(work_node, mexp_parser)
            )
        else:
            raise RuntimeError("BUG: Unhandled AST node type.")

    #  Post process - add status.
    post_process = printed[id(root_node)]
    if root_node.is_gas_status():
        post_process += "(g)"
    elif root_node.is_liquid_status():
        post_process += "(l)"
    elif root_node.is_solid_status():
        post_process += "(s)"
    elif root_node.is_aqueous_status():
        post_process += "(aq)"
    else:
        pass

    return post_process
