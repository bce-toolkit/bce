#!/usr/bin/env python
#
#  Copyright 2014 - 2016 The BCE Authors. All rights reserved.
#  Use of this source code is governed by a BSD-style license that can be
#  found in the license.txt file.
#

import bce.parser.ast.molecule as _ast_base
import bce.parser.interface.molecule_parser as _ml_interface
import bce.parser.molecule.ast_bfs as _ast_bfs
import sympy as _sympy

_PROPERTY_KEY_SUBSTITUTION_ERROR_RAISED = "__bce.parser.molecule.ast_substitution_SubstitutionErrorRaised"


def _check_substituted_mexp(value):
    """Check the substituted math expression.

    :param value: The value math expression.
    :raise SubstituteError: Raise if the value is invalid.
    """

    if isinstance(value, _sympy.S.ComplexInfinity.__class__):
        raise _ml_interface.SubstituteError("Divided zero.")


def substitute_ast(root_node, subst_map):
    """Substitution an AST and save the substituted one to a new AST.

    :type root_node: bce.parser.ast.molecule.ASTNodeHydrateGroup | bce.parser.ast.molecule.ASTNodeMolecule
    :type subst_map: dict
    :param root_node: The root node of the origin AST.
    :param subst_map: The substitution map.
    :rtype : bce.parser.ast.molecule.ASTNodeHydrateGroup | bce.parser.ast.molecule.ASTNodeMolecule | None
    :return: The root node of the new AST.
    """

    #  Get the BFS order (from the leaves to the root).
    work_order = _ast_bfs.do_bfs(root_node, True)

    #  Initialize the substituted data container.
    substituted = {}
    """:type : dict[int, bce.parser.ast.molecule._ASTNodeBaseML | None]"""

    #  Iterate each node.
    for work_node in work_order:
        if work_node.is_hydrate_group():
            assert isinstance(work_node, _ast_base.ASTNodeHydrateGroup)

            #  Get and substitute the prefix number.
            pfx = work_node.get_prefix_number().subs(subst_map).simplify()
            _check_substituted_mexp(pfx)
            if pfx.is_zero:
                substituted[id(work_node)] = None
                continue

            #  Create a new hydrate group node.
            build_node = _ast_base.ASTNodeHydrateGroup()

            #  Set the prefix number.
            build_node.set_prefix_number(pfx)

            #  Iterate each child.
            for child_id in range(0, len(work_node)):
                #  Get child data.
                child_node = substituted[id(work_node[child_id])]

                if child_node is not None:
                    assert isinstance(child_node, _ast_base.ASTNodeMolecule)

                    #  Simulate raise an error if the child raised before.
                    if child_node.get_property(_PROPERTY_KEY_SUBSTITUTION_ERROR_RAISED, False):
                        build_node.set_property(_PROPERTY_KEY_SUBSTITUTION_ERROR_RAISED, True)

                    #  Link.
                    child_node.set_parent_node(build_node)
                    build_node.append_child(child_node)

            #  Eliminate the node if there is no content inside.
            if len(build_node) == 0:
                substituted[id(work_node)] = None
                continue

            #  Unpack the hydrate group if there is only 1 molecule in it.
            if len(build_node) == 1:
                #  Get the prefix number of the hydrate group.
                pfx = build_node.get_prefix_number()

                #  Unpack.
                build_node = build_node[0]
                assert isinstance(build_node, _ast_base.ASTNodeMolecule)

                #  Get the new prefix of the unpacked node.
                pfx = (pfx * build_node.get_prefix_number()).simplify()

                if pfx.is_zero:
                    #  Eliminate the node since the prefix is 0.
                    substituted[id(work_node)] = None
                else:
                    #  Set the parent node and prefix number of the unpacked node.
                    # noinspection PyTypeChecker
                    build_node.set_parent_node(None)
                    build_node.set_prefix_number(pfx)

                    #  Save.
                    substituted[id(work_node)] = build_node
            else:
                for child_id in range(0, len(build_node)):
                    #  Get the child node.
                    child_node = build_node[child_id]
                    assert isinstance(child_node, _ast_base.ASTNodeMolecule)

                    #  Check the prefix number of the child.
                    if child_node.get_prefix_number().simplify().is_negative:
                        build_node.set_property(_PROPERTY_KEY_SUBSTITUTION_ERROR_RAISED, True)
                        break

                #  Save.
                substituted[id(work_node)] = build_node
        elif work_node.is_molecule():
            assert isinstance(work_node, _ast_base.ASTNodeMolecule)

            #  Get and substitute the prefix number.
            pfx = work_node.get_prefix_number().subs(subst_map).simplify()
            _check_substituted_mexp(pfx)
            if pfx.is_zero:
                substituted[id(work_node)] = None
                continue

            #  Create a new molecule node.
            build_node = _ast_base.ASTNodeMolecule()

            #  Substitute the electronic count.
            substituted_charge = work_node.get_electronic_count().subs(subst_map).simplify()
            _check_substituted_mexp(substituted_charge)
            build_node.set_electronic_count(substituted_charge)

            #  Set the prefix number.
            build_node.set_prefix_number(pfx)

            #  Iterate each child.
            for child_id in range(0, len(work_node)):
                #  Get the child node.
                child_node = substituted[id(work_node[child_id])]

                if child_node is not None:
                    #  Raise an error if the child raised before.
                    if child_node.get_property(_PROPERTY_KEY_SUBSTITUTION_ERROR_RAISED, False):
                        build_node.set_property(_PROPERTY_KEY_SUBSTITUTION_ERROR_RAISED, True)

                    #  Link.
                    child_node.set_parent_node(build_node)
                    build_node.append_child(child_node)

            if len(build_node) == 0 and build_node.get_electronic_count().simplify().is_zero:
                #  Eliminate this node since there is no content inside and the electronic count is 0.
                substituted[id(work_node)] = None
            else:
                #  Save.
                substituted[id(work_node)] = build_node
        elif work_node.is_atom():
            assert isinstance(work_node, _ast_base.ASTNodeAtom)

            #  Initialize an atom node.
            build_node = _ast_base.ASTNodeAtom(work_node.get_atom_symbol())

            #  Get and substitute the suffix number.
            sfx = work_node.get_suffix_number().subs(subst_map).simplify()
            _check_substituted_mexp(sfx)

            #  Eliminate this node if the suffix number is 0.
            if sfx.is_zero:
                substituted[id(work_node)] = None
                continue

            if sfx.is_negative:
                build_node.set_property(_PROPERTY_KEY_SUBSTITUTION_ERROR_RAISED, True)

            #  Set the suffix number.
            build_node.set_suffix_number(sfx)

            #  Save.
            substituted[id(work_node)] = build_node
        elif work_node.is_parenthesis():
            assert isinstance(work_node, _ast_base.ASTNodeParenthesisWrapper)

            #  Get and substitute the suffix number.
            sfx = work_node.get_suffix_number().subs(subst_map).simplify()
            _check_substituted_mexp(sfx)

            #  Get the substituted inner data.
            inner_node = substituted[id(work_node.get_inner_node())]
            assert isinstance(inner_node, _ast_base.ASTNodeHydrateGroup) or \
                isinstance(inner_node, _ast_base.ASTNodeMolecule) or \
                inner_node is None

            #  Eliminate this node if the suffix number is zero or there is nothing inside.
            if sfx.is_zero or inner_node is None:
                substituted[id(work_node)] = None
                continue

            #  Create a new parenthesis wrapper node.
            build_node = _ast_base.ASTNodeParenthesisWrapper(inner_node)

            #  Link.
            inner_node.set_parent_node(build_node)

            #  Set the suffix number.
            build_node.set_suffix_number(sfx)

            if sfx.is_negative or inner_node.get_prefix_number().simplify().is_negative or \
                    inner_node.get_property(_PROPERTY_KEY_SUBSTITUTION_ERROR_RAISED, False):
                #  Raise an error since the suffix is negative or the prefix number or the
                #  inner node is negative or the child raised an error before.
                build_node.set_property(_PROPERTY_KEY_SUBSTITUTION_ERROR_RAISED, True)

            #  Save.
            substituted[id(work_node)] = build_node
        elif work_node.is_abbreviation():
            assert isinstance(work_node, _ast_base.ASTNodeAbbreviation)

            #  Create an abbreviation node.
            build_node = _ast_base.ASTNodeAbbreviation(work_node.get_abbreviation_symbol())

            #  Get and substitute the suffix number.
            sfx = work_node.get_suffix_number().subs(subst_map).simplify()
            _check_substituted_mexp(sfx)

            #  Eliminate this node if the suffix number is 0.
            if sfx.is_zero:
                substituted[id(work_node)] = None
                continue

            if sfx.is_negative:
                build_node.set_property(_PROPERTY_KEY_SUBSTITUTION_ERROR_RAISED, True)

            #  Set the suffix number.
            build_node.set_suffix_number(sfx)

            #  Save
            substituted[id(work_node)] = build_node
        else:
            raise RuntimeError("BUG: Unrecognized node.")

    #  Get the substituted root node data.
    new_root = substituted[id(root_node)]
    assert isinstance(new_root, _ast_base.ASTNodeHydrateGroup) or \
        isinstance(new_root, _ast_base.ASTNodeMolecule) or \
        new_root is None

    if new_root is not None:
        #  Raise an error if the root raised  error before.
        if new_root.get_property(_PROPERTY_KEY_SUBSTITUTION_ERROR_RAISED, False):
            raise _ml_interface.SubstituteError("An error occurred when do substitution on the molecule.")

        #  Set molecule status.
        new_root.set_status(root_node.get_status())

    #  Remove all "SubstitutionErrorRaised" property.
    for root_id in substituted:
        node = substituted[root_id]
        if node is not None and node.has_property(_PROPERTY_KEY_SUBSTITUTION_ERROR_RAISED):
            node.remove_property(_PROPERTY_KEY_SUBSTITUTION_ERROR_RAISED)

    return new_root
