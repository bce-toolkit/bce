#!/usr/bin/env python
#
#  Copyright 2014 - 2016 The BCE Authors. All rights reserved.
#  Use of this source code is governed by a BSD-style license that can be
#  found in the license.txt file.
#

import bce.math.constant as _math_constant
import bce.parser.ast.base as _ast_base

#  AST node types.
AST_TYPE_HYDRATE_GROUP = 1
AST_TYPE_MOLECULE = 2
AST_TYPE_ATOM = 3
AST_TYPE_PARENTHESIS = 4
AST_TYPE_ABBREVIATION = 5

#  Molecule status.
STATUS_GAS = 1
STATUS_LIQUID = 2
STATUS_SOLID = 3
STATUS_AQUEOUS = 4


class _ASTNodeBaseML(_ast_base.ASTNodeBase):
    """Base class for molecule AST nodes."""

    def __init__(self, node_type, parent_node=None):
        """Initialize the node.

        :type node_type: int
        :type parent_node: _ASTNodeBaseML
        :param node_type: The node type identifier.
        :param parent_node: The parent node.
        """

        _ast_base.ASTNodeBase.__init__(self, node_type)
        self.set_parent_node(parent_node)

    def is_hydrate_group(self):
        """Get whether the node is a hydrate group.

        :rtype : bool
        :return: True if so. Otherwise, return False.
        """

        return self.get_node_type() == AST_TYPE_HYDRATE_GROUP

    def is_molecule(self):
        """Get whether the node is a single molecule.

        :rtype : bool
        :return: True if so. Otherwise, return False.
        """

        return self.get_node_type() == AST_TYPE_MOLECULE

    def is_atom(self):
        """Get whether the node is an atom.

        :rtype : bool
        :return: True if so. Otherwise, return False.
        """

        return self.get_node_type() == AST_TYPE_ATOM

    def is_parenthesis(self):
        """Get whether the node is a parenthesis wrapper.

        :rtype : bool
        :return: True if so. Otherwise, return False.
        """

        return self.get_node_type() == AST_TYPE_PARENTHESIS

    def is_abbreviation(self):
        """Get whether the node is an abbreviation descriptor.

        :rtype : bool
        :return: True if so. Otherwise, return False.
        """

        return self.get_node_type() == AST_TYPE_ABBREVIATION


class _ASTNodeWithPrefix(_ast_base.ASTNodeBase):
    """Protocols for nodes which have prefix number."""

    def get_prefix_number(self):
        """Get the prefix number.

        :return: The number.
        """

        return self.get_property("prefix", _math_constant.ONE)

    def set_prefix_number(self, value):
        """Set the prefix number.

        :param value: The number.
        """

        self.set_property("prefix", value)


class _ASTNodeWithSuffix(_ast_base.ASTNodeBase):
    """Protocols for nodes which have suffix number and electronics."""

    def get_suffix_number(self):
        """Get the suffix number.

        :return: The number.
        """

        return self.get_property("suffix_number", _math_constant.ONE)

    def set_suffix_number(self, value):
        """Set the suffix number.

        :param value: The number.
        """

        self.set_property("suffix_number", value)


class _ASTNodeWithRightParenthesis(_ast_base.ASTNodeBase):
    """Protocols for nodes which have to save the position of its right parenthesis."""

    def set_right_parenthesis_position(self, pos):
        """Set the position of the right parenthesis.

        :type pos: int
        :param pos: The position.
        """

        self.set_property("right_parenthesis_position", pos)

    def get_right_parenthesis_position(self):
        """Get the position of the right parenthesis.

        :rtype : int
        :return: The position.
        """

        return self.get_property("right_parenthesis_position", -1)


class _ASTNodeWithStatus(_ast_base.ASTNodeBase):
    """Protocols for nodes which have to save status."""

    def clear_status(self):
        """Clear molecule status."""

        self.set_status(None)

    def set_status(self, status_id):
        """Set molecule status.

        :type status_id: int | None
        :param status_id: The status identifier.
        """

        self.set_property("status_id", status_id)

    def get_status(self):
        """Get molecule status.

        :rtype : int | None
        :return: The status identifier.
        """

        return self.get_property("status_id", None)

    def is_undefined_status(self):
        """Get whether the substance status is undefined.

        :rtype : bool
        :return: True if so.
        """

        return self.get_status() is None

    def is_gas_status(self):
        """Get whether the substance status is gas.

        :rtype : bool
        :return: True if so.
        """

        return self.get_status() == STATUS_GAS

    def is_liquid_status(self):
        """Get whether the substance status is liquid.

        :rtype : bool
        :return: True if so.
        """

        return self.get_status() == STATUS_LIQUID

    def is_solid_status(self):
        """Get whether the substance status is solid.

        :rtype : bool
        :return: True if so.
        """

        return self.get_status() == STATUS_SOLID

    def is_aqueous_status(self):
        """Get whether the substance status is aqueous.

        :rtype : bool
        :return: True if so.
        """

        return self.get_status() == STATUS_AQUEOUS


class ASTNodeHydrateGroup(_ASTNodeBaseML, _ASTNodeWithPrefix, _ASTNodeWithStatus):
    """AST node class for hydrate groups."""

    def __init__(self, parent_node=None):
        """Initialize the node.

        :type parent_node: _ASTNodeBaseML
        :param parent_node: The parent node.
        """

        _ASTNodeBaseML.__init__(self, AST_TYPE_HYDRATE_GROUP, parent_node)


class ASTNodeMolecule(_ASTNodeBaseML, _ASTNodeWithPrefix, _ASTNodeWithStatus):
    """AST node class for molecules."""

    def __init__(self, parent_node=None):
        """Initialize the node.

        :type parent_node: _ASTNodeBaseML
        :param parent_node: The parent node.
        """

        _ASTNodeBaseML.__init__(self, AST_TYPE_MOLECULE, parent_node)

    def set_electronic_count(self, value):
        """Set the electronic count.

        :param value: The new count.
        """

        self.set_property("electronic_count", value)

    def get_electronic_count(self):
        """Get the electronic count.

        :return: The count.
        """

        return self.get_property("electronic_count", _math_constant.ZERO)


class ASTNodeAtom(_ASTNodeBaseML, _ASTNodeWithSuffix):
    """AST node class for atoms."""

    def __init__(self, atom_symbol, parent_node=None):
        """Initialize the node.

        :type atom_symbol: str
        :type parent_node: _ASTNodeBaseML
        :param atom_symbol: The atom symbol.
        :param parent_node: The parent node.
        """

        _ASTNodeBaseML.__init__(self, AST_TYPE_ATOM, parent_node)
        self.set_property("atom_symbol", atom_symbol)

    def get_atom_symbol(self):
        """Get the atom symbol.

        :rtype : str
        :return: The symbol.
        """

        return self.get_property("atom_symbol")


class ASTNodeParenthesisWrapper(_ASTNodeBaseML, _ASTNodeWithSuffix, _ASTNodeWithRightParenthesis):
    """AST node class for parenthesis wrappers."""

    def __init__(self, inner_node, parent_node=None):
        """Initialize the node.

        :type inner_node: _ASTNodeBaseML
        :type parent_node: _ASTNodeBaseML
        :param inner_node: The inner node to be wrapped.
        :param parent_node: The parent node.
        """

        _ASTNodeBaseML.__init__(self, AST_TYPE_PARENTHESIS, parent_node)
        self.set_property("inner_node", inner_node)

    def get_inner_node(self):
        """Get the inner node.

        :rtype : _ASTNodeBaseML
        :return: The node.
        """

        return self.get_property("inner_node")

    def set_inner_node(self, new_node):
        """Set the inner node.

        :type new_node: _ASTNodeBaseML
        :param new_node: The node.
        """

        self.set_property("inner_node", new_node)


class ASTNodeAbbreviation(_ASTNodeBaseML, _ASTNodeWithSuffix, _ASTNodeWithRightParenthesis):
    """AST node class for abbreviation descriptors."""

    def __init__(self, abbreviation_symbol, parent_node=None):
        """Initialize the node.

        :type abbreviation_symbol: str
        :type parent_node: _ASTNodeBaseML
        :param abbreviation_symbol: The symbol of the abbreviation.
        :param parent_node: The parent node.
        """

        _ASTNodeBaseML.__init__(self, AST_TYPE_ABBREVIATION, parent_node)
        self.set_property("abbr_symbol", abbreviation_symbol)

    def get_abbreviation_symbol(self):
        """Get the abbreviation symbol.

        :rtype : str
        :return: The symbol.
        """

        return self.get_property("abbr_symbol")
