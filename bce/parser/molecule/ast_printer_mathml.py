#!/usr/bin/env python
#
#  Copyright 2014 - 2016 The BCE Authors. All rights reserved.
#  Use of this source code is governed by a BSD-style license that can be
#  found in the license.txt file.
#

import bce.math.constant as _math_constant
import bce.parser.interface.printer as _interface_printer
import bce.parser.ast.molecule as _ml_ast_base
import bce.parser.molecule.ast_bfs as _ml_ast_bfs
import bce.dom.mathml.all as _mathml


def _print_operand(
        value,
        need_wrapping,
        mexp_parser,
        mexp_protected_header_enabled=False,
        mexp_protected_header_prefix="X"
):
    """Print an operand.

    :type need_wrapping: bool
    :type mexp_parser: bce.parser.interface.mexp_parser.MathExpressionParserInterface
    :type mexp_protected_header_enabled: bool
    :type mexp_protected_header_prefix: str
    :param value: The operand value.
    :param need_wrapping: Set to True if you need to wrap the expression when it is neither an integer nor a symbol.
    :param mexp_parser: The math expression parser.
    :param mexp_protected_header_enabled: Whether the MEXP protected headers are enabled.
    :param mexp_protected_header_prefix: The prefix of the MEXP protected headers.
    :rtype : bce.dom.mathml.all.Base
    :return: The printed MathML node.
    """

    #  Simplify.
    value = value.simplify()

    if value.is_Integer:
        return _mathml.NumberComponent(str(value))
    else:
        if need_wrapping and not (value.is_Integer or value.is_Symbol):
            #  Use a pair of parentheses to wrap the printed expression.
            r = _mathml.RowComponent()
            r.append_object(_mathml.OperatorComponent(_mathml.OPERATOR_LEFT_PARENTHESIS))
            r.append_object(mexp_parser.print_out(
                value,
                printer_type=_interface_printer.PRINTER_TYPE_MATHML,
                protected_header_enabled=mexp_protected_header_enabled,
                protected_header_prefix=mexp_protected_header_prefix
            ))
            r.append_object(_mathml.OperatorComponent(_mathml.OPERATOR_RIGHT_PARENTHESIS))
            return r
        else:
            return mexp_parser.print_out(
                value,
                printer_type=_interface_printer.PRINTER_TYPE_MATHML,
                protected_header_enabled=mexp_protected_header_enabled,
                protected_header_prefix=mexp_protected_header_prefix
            )


def _print_super_electronic(
        charge,
        mexp_parser,
        mexp_protected_header_enabled=False,
        mexp_protected_header_prefix="X"
):
    """Print electronic charge value.

    :type mexp_parser: bce.parser.interface.mexp_parser.MathExpressionParserInterface
    :type mexp_protected_header_enabled: bool
    :type mexp_protected_header_prefix: str
    :param charge: The charge number.
    :param mexp_parser: The math expression parser.
    :param mexp_protected_header_enabled: Whether the MEXP protected headers are enabled.
    :param mexp_protected_header_prefix: The prefix of the MEXP protected headers.
    :rtype : bce.dom.mathml.all.Base
    :return: The printed MathML node.
    """

    #  Print the positivity part.
    if charge.is_negative:
        charge = -charge
        positivity = _mathml.OperatorComponent(_mathml.OPERATOR_MINUS)
    else:
        positivity = _mathml.OperatorComponent(_mathml.OPERATOR_PLUS)

    #  Simplify.
    charge = charge.simplify()

    if charge == _math_constant.ONE:
        return positivity
    else:
        #  Initialize a row component to contain the printing result.
        r = _mathml.RowComponent()

        #  Print the charge part.
        r.append_object(_print_operand(
            charge,
            True,
            mexp_parser,
            mexp_protected_header_enabled=mexp_protected_header_enabled,
            mexp_protected_header_prefix=mexp_protected_header_prefix
        ))

        #  Add the positivity flag.
        r.append_object(positivity)

        return r


def _print_suffix(
        main_dom,
        node,
        mexp_parser,
        mexp_protected_header_enabled=False,
        mexp_protected_header_prefix="X"
):
    """Print suffix part of specified node.

    :type node: bce.parser.ast.molecule._ASTNodeWithSuffix
    :type mexp_parser: bce.parser.interface.mexp_parser.MathExpressionParserInterface
    :type mexp_protected_header_enabled: bool
    :type mexp_protected_header_prefix: str
    :param main_dom: The main DOM node.
    :param node: The AST node.
    :param mexp_parser: The math expression parser.
    :param mexp_protected_header_enabled: Whether the MEXP protected headers are enabled.
    :param mexp_protected_header_prefix: The prefix of the MEXP protected headers.
    :rtype : bce.dom.mathml.all.Base
    :return: The printed MathML node.
    """

    #  Print the suffix number part.
    sfx = node.get_suffix_number().simplify()
    if sfx != _math_constant.ONE:
        sfx_dom = _print_operand(
            sfx,
            False,
            mexp_parser,
            mexp_protected_header_enabled=mexp_protected_header_enabled,
            mexp_protected_header_prefix=mexp_protected_header_prefix
        )
    else:
        sfx_dom = None

    #  Do combination and return.
    if sfx_dom is None:
        return main_dom
    else:
        return _mathml.SubComponent(main_dom, sfx_dom)


def print_ast(
        root_node,
        mexp_parser,
        mexp_protected_header_enabled=False,
        mexp_protected_header_prefix="X"
):
    """Print an AST to BCE expression.

    :type root_node: bce.parser.ast.molecule.ASTNodeHydrateGroup | bce.parser.ast.molecule.ASTNodeMolecule
    :type mexp_parser: bce.parser.interface.mexp_parser.MathExpressionParserInterface
    :type mexp_protected_header_enabled: bool
    :type mexp_protected_header_prefix: str
    :param root_node: The root node of the AST.
    :param mexp_parser: The math expression parser.
    :param mexp_protected_header_enabled: Whether the MEXP protected headers are enabled.
    :param mexp_protected_header_prefix: The prefix of the MEXP protected headers.
    :rtype : bce.dom.mathml.all.Base
    :return: The printed expression.
    """

    #  Get the printing order.
    work_order = _ml_ast_bfs.do_bfs(root_node, True)

    #  Initialize the printed result container.
    printed = {}

    for work_node in work_order:
        if work_node.is_hydrate_group():
            assert isinstance(work_node, _ml_ast_base.ASTNodeHydrateGroup)

            #  Initialize a row component to contain the printing result.
            build = _mathml.RowComponent()

            #  Print the prefix number part.
            pfx = work_node.get_prefix_number().simplify()
            if pfx != _math_constant.ONE:
                build.append_object(_print_operand(
                    pfx,
                    True,
                    mexp_parser,
                    mexp_protected_header_enabled=mexp_protected_header_enabled,
                    mexp_protected_header_prefix=mexp_protected_header_prefix
                ))
                build.append_object(_mathml.OperatorComponent(_mathml.OPERATOR_LEFT_PARENTHESIS))
                surround = True
            else:
                surround = False

            #  Print children nodes.
            build.append_object(printed[id(work_node[0])])
            for child_id in range(1, len(work_node)):
                build.append_object(_mathml.OperatorComponent(_mathml.OPERATOR_DOT))
                build.append_object(printed[id(work_node[child_id])])

            #  Complete the surrounding parentheses if the flag was marked.
            if surround:
                build.append_object(_mathml.OperatorComponent(_mathml.OPERATOR_RIGHT_PARENTHESIS))

            #  Save printing result.
            printed[id(work_node)] = build
        elif work_node.is_molecule():
            assert isinstance(work_node, _ml_ast_base.ASTNodeMolecule)

            #  Initialize a row component to contain the printing result.
            build = _mathml.RowComponent()

            #  Print the prefix number part.
            pfx = work_node.get_prefix_number().simplify()
            if pfx != _math_constant.ONE:
                build.append_object(_print_operand(
                    pfx,
                    True,
                    mexp_parser,
                    mexp_protected_header_enabled=mexp_protected_header_enabled,
                    mexp_protected_header_prefix=mexp_protected_header_prefix
                ))

            #  Print children nodes.
            for child_id in range(0, len(work_node)):
                build.append_object(printed[id(work_node[child_id])])

            el_charge = work_node.get_electronic_count().simplify()
            if not el_charge.is_zero:
                if len(work_node) == 0:
                    build.append_object(_mathml.SuperComponent(
                        _mathml.TextComponent("e"),
                        _print_super_electronic(
                            el_charge,
                            mexp_parser,
                            mexp_protected_header_enabled=mexp_protected_header_enabled,
                            mexp_protected_header_prefix=mexp_protected_header_prefix
                        )
                    ))
                else:
                    #  Find the innermost row component.
                    innermost = build
                    while innermost[-1].is_row():
                        innermost = innermost[-1]

                    #  Fetch the last item.
                    last_item = innermost[-1]

                    #  Add the electronic.
                    if last_item.is_sub():
                        assert isinstance(last_item, _mathml.SubComponent)
                        last_item = _mathml.SubAndSuperComponent(
                            last_item.get_main_object(),
                            last_item.get_sub_object(),
                            _print_super_electronic(
                                el_charge,
                                mexp_parser,
                                mexp_protected_header_enabled=mexp_protected_header_enabled,
                                mexp_protected_header_prefix=mexp_protected_header_prefix
                            )
                        )
                    else:
                        last_item = _mathml.SuperComponent(
                            last_item,
                            _print_super_electronic(
                                el_charge,
                                mexp_parser,
                                mexp_protected_header_enabled=mexp_protected_header_enabled,
                                mexp_protected_header_prefix=mexp_protected_header_prefix
                            )
                        )

                    #  Save the modified item.
                    innermost[-1] = last_item

            #  Save printing result.
            printed[id(work_node)] = build
        elif work_node.is_atom():
            assert isinstance(work_node, _ml_ast_base.ASTNodeAtom)

            #  Print and save the result.
            printed[id(work_node)] = _print_suffix(
                _mathml.TextComponent(work_node.get_atom_symbol()),
                work_node,
                mexp_parser,
                mexp_protected_header_enabled=mexp_protected_header_enabled,
                mexp_protected_header_prefix=mexp_protected_header_prefix
            )
        elif work_node.is_parenthesis():
            assert isinstance(work_node, _ml_ast_base.ASTNodeParenthesisWrapper)

            #  Initialize a row component to contain the printing result.
            build = _mathml.RowComponent()

            #  Print.
            build.append_object(_mathml.OperatorComponent(_mathml.OPERATOR_LEFT_PARENTHESIS))
            build.append_object(printed[id(work_node.get_inner_node())])
            build.append_object(_print_suffix(
                _mathml.OperatorComponent(_mathml.OPERATOR_RIGHT_PARENTHESIS),
                work_node,
                mexp_parser,
                mexp_protected_header_enabled=mexp_protected_header_enabled,
                mexp_protected_header_prefix=mexp_protected_header_prefix
            ))

            #  Save printing result.
            printed[id(work_node)] = build
        elif work_node.is_abbreviation():
            assert isinstance(work_node, _ml_ast_base.ASTNodeAbbreviation)

            #  Print and save the result.
            printed[id(work_node)] = _print_suffix(
                _mathml.TextComponent("[%s]" % work_node.get_abbreviation_symbol()),
                work_node,
                mexp_parser,
                mexp_protected_header_enabled=mexp_protected_header_enabled,
                mexp_protected_header_prefix=mexp_protected_header_prefix
            )
        else:
            raise RuntimeError("BUG: Unhandled AST node type.")

    #  Post process - add status.
    post_process = printed[id(root_node)]
    if root_node.get_status() is not None:
        if not post_process.is_row():
            tmp = _mathml.RowComponent()
            tmp.append_object(post_process)
            post_process = tmp
        post_process.append_object(_mathml.OperatorComponent(_mathml.OPERATOR_LEFT_PARENTHESIS))
        if root_node.get_status() == _ml_ast_base.STATUS_GAS:
            post_process.append_object(_mathml.TextComponent("g"))
        elif root_node.get_status() == _ml_ast_base.STATUS_LIQUID:
            post_process.append_object(_mathml.TextComponent("l"))
        elif root_node.get_status() == _ml_ast_base.STATUS_SOLID:
            post_process.append_object(_mathml.TextComponent("s"))
        elif root_node.get_status() == _ml_ast_base.STATUS_AQUEOUS:
            post_process.append_object(_mathml.TextComponent("aq"))
        else:
            raise RuntimeError("BUG: No such status.")
        post_process.append_object(_mathml.OperatorComponent(_mathml.OPERATOR_RIGHT_PARENTHESIS))

    return printed[id(root_node)]
