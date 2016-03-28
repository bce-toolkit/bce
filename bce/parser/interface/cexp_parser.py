#!/usr/bin/env python
#
#  Copyright 2014 - 2016 The BCE Authors. All rights reserved.
#  Use of this source code is governed by a BSD-style license that can be
#  found in the license.txt file.
#

import bce.math.constant as _math_constant
import bce.parser.interface.printer as _interface_printer
import sympy as _sympy

#  Operators.
OPERATOR_PLUS = 1
OPERATOR_MINUS = 2


class SubstituteError(Exception):
    """Chemical equation substitution error."""

    pass


class ChemicalEquationItem:
    """Class for containing the item of chemical equation."""

    def __init__(self, operator_id, coefficient, molecule_ast, atoms_dictionary):
        """Initialize the class.

        :type operator_id: int
        :type molecule_ast: bce.parser.ast.molecule.ASTNodeHydrateGroup | bce.parser.ast.molecule.ASTNodeMolecule
        :type atoms_dictionary: dict
        :param operator_id: The operator ID.
        :param coefficient: The coefficient before the molecule.
        :param molecule_ast: The root node of the AST of the molecule (without coefficient).
        :param atoms_dictionary: The parsed atom dictionary (without coefficient).
        """

        self.__op = operator_id
        self.__co = coefficient
        self.__ast = molecule_ast
        self.__ad = atoms_dictionary

    def get_operator_id(self):
        """Get the operator ID.

        :rtype : int
        :return: The ID.
        """

        return self.__op

    def set_operator_id(self, new_id):
        """Set the operator ID.

        :type new_id: int
        :param new_id: The ID.
        """

        self.__op = new_id

    def is_operator_plus(self):
        """Get whether the operator before the molecule is plus.

        :rtype : bool
        :return: True if so. Otherwise, return False.
        """

        return self.__op == OPERATOR_PLUS

    def is_operator_minus(self):
        """Get whether the operator before the molecule is minus.

        :rtype : bool
        :return: True if so. Otherwise, return False.
        """

        return self.__op == OPERATOR_MINUS

    def get_coefficient(self):
        """Get the coefficient before the molecule.

        :return: The coefficient.
        """

        return self.__co

    def set_coefficient(self, new_coefficient):
        """Set the coefficient before the molecule.

        :param new_coefficient: The coefficient.
        """

        self.__co = new_coefficient

    def get_molecule_ast(self):
        """Get the root node of the AST of the molecule.

        :rtype : bce.parser.ast.molecule.ASTNodeHydrateGroup | bce.parser.ast.molecule.ASTNodeMolecule
        :return: The node.
        """

        return self.__ast

    def set_molecule_ast(self, new_ast):
        """Set the root node of the AST of the molecule.

        :type new_ast: bce.parser.ast.molecule.ASTNodeHydrateGroup | bce.parser.ast.molecule.ASTNodeMolecule
        :param new_ast:
        """

        self.__ast = new_ast

    def get_atoms_dictionary(self):
        """Get the atoms dictionary.

        :rtype : dict
        :return: The dictionary.
        """

        return self.__ad

    def set_atoms_dictionary(self, new_dict):
        """Set the atoms dictionary.

        :type new_dict: dict
        :param new_dict: The new dictionary.
        """

        self.__ad = new_dict


class ChemicalEquation:
    """Class for containing and operating one chemical equation."""

    def __init__(self):
        """Initialize the class."""

        self.__left_items = []
        """:type : list[ChemicalEquationItem]"""
        self.__right_items = []
        """:type : list[ChemicalEquationItem]"""

    def __len__(self):
        """Get the count of chemicals.

        :rtype : int
        :return: The count.
        """

        return self.get_left_item_count() + self.get_right_item_count()

    def append_left_item(self, operator_id, coefficient, molecule_ast, atoms_dictionary):
        """Append an item to the left side of the equal sign.

        :type operator_id: int
        :type molecule_ast: bce.parser.ast.molecule.ASTNodeHydrateGroup | bce.parser.ast.molecule.ASTNodeMolecule
        :type atoms_dictionary: dict
        :param operator_id: The operator ID.
        :param coefficient: The coefficient before the molecule.
        :param molecule_ast: The root node of the AST of the molecule (without coefficient).
        :param atoms_dictionary: The atoms dictionary (without coefficient).
        """

        self.__left_items.append(ChemicalEquationItem(operator_id, coefficient, molecule_ast, atoms_dictionary))

    def append_right_item(self, operator_id, coefficient, molecule_ast, atoms_dictionary):
        """Append an item to the right side of the equal sign.

        :type operator_id: int
        :type molecule_ast: bce.parser.ast.molecule.ASTNodeHydrateGroup | bce.parser.ast.molecule.ASTNodeMolecule
        :type atoms_dictionary: dict
        :param operator_id: The operator ID.
        :param coefficient: The coefficient before the molecule.
        :param molecule_ast: The root node of the AST of the molecule (without coefficient).
        :param atoms_dictionary: The atoms dictionary (without coefficient).
        """

        self.__right_items.append(ChemicalEquationItem(operator_id, coefficient, molecule_ast, atoms_dictionary))

    def get_left_item_count(self):
        """Get the count of the items on the left side of the equal sign.

        :rtype : int
        :return: The count.
        """

        return len(self.__left_items)

    def get_right_item_count(self):
        """Get the count of the items on the right side of the equal sign.

        :rtype : int
        :return: The count.
        """

        return len(self.__right_items)

    def pop_left_item(self, idx):
        """Pop an item from the left side of the equal sign.

        :type idx: int
        :param idx: The index.
        :rtype : ChemicalEquationItem
        :return: The item.
        """

        return self.__left_items.pop(idx)

    def pop_right_item(self, idx):
        """Pop an item from the right side of the equal sign.

        :type idx: int
        :param idx: The index.
        :rtype : ChemicalEquationItem
        :return: The item.
        """

        return self.__right_items.pop(idx)

    def get_left_item(self, idx):
        """Get an item from the left side of the equal sign.

        :type idx: int
        :param idx: The index.
        :rtype : ChemicalEquationItem
        :return: The item.
        """

        return self.__left_items[idx]

    def get_right_item(self, idx):
        """Get an item from the right side of the equal sign.

        :type idx: int
        :param idx: The index.
        :rtype : ChemicalEquationItem
        :return: The item.
        """

        return self.__right_items[idx]

    def set_left_item(self, idx, new_item):
        """Set the item on the left side of the equal sign.

        :type idx: int
        :type new_item: ChemicalEquationItem
        :param idx: The index.
        :param new_item: The new item.
        """

        self.__left_items[idx] = new_item

    def set_right_item(self, idx, new_item):
        """Set the item on the right side of the equal sign.

        :type idx: int
        :type new_item: ChemicalEquationItem
        :param idx: The index.
        :param new_item: The new item.
        """

        self.__right_items[idx] = new_item

    def remove_items_with_coefficient_zero(self):
        """Remove items that have coefficient 0."""

        #  Process left items.
        for idx in range(len(self.__left_items) - 1, -1, -1):
            if self.__left_items[idx].get_coefficient().simplify().is_zero:
                self.__left_items.pop(idx)

        #  Process right items.
        for idx in range(len(self.__right_items) - 1, -1, -1):
            if self.__right_items[idx].get_coefficient().simplify().is_zero:
                self.__right_items.pop(idx)

    def move_items_with_negative_coefficient_to_another_side(self):
        """Move items with negative coefficient to another side of the equal sign."""

        #  Initialize new items container.
        new_left_items = []
        """:type : list[ChemicalEquationItem]"""
        new_right_items = []
        """:type : list[ChemicalEquationItem]"""

        #  Process left items.
        for item in self.__left_items:
            #  Get the coefficient.
            coeff = item.get_coefficient().simplify()
            if coeff.is_negative:
                #  Move side.
                item.set_coefficient(-coeff)
                new_right_items.append(item)
            else:
                #  Keep origin side.
                new_left_items.append(item)

        #  Process right items.
        for item in self.__right_items:
            #  Get the coefficient.
            coeff = item.get_coefficient().simplify()

            if coeff.is_negative:
                #  Move side.
                item.set_coefficient(-coeff)
                new_left_items.append(item)
            else:
                #  Keep origin side.
                new_right_items.append(item)

        #  Save results.
        self.__left_items = new_left_items
        self.__right_items = new_right_items

    def coefficients_integerize(self):
        """Transform coefficients to integers if it could be done."""

        #  Get the list that contains all items.
        all_items = self.__left_items + self.__right_items

        #  Initialize the LCM of denominators as 1.
        denom_lcm = _math_constant.ONE

        #  Process left items.
        for item in all_items:
            #  Get the coefficient.
            coeff = item.get_coefficient().simplify()

            #  Get the denominator.
            nd = coeff.as_numer_denom()
            nd_denom = nd[1].simplify()

            #  Calculate.
            if nd_denom.is_Integer:
                denom_lcm = _sympy.lcm(denom_lcm, nd_denom)

        #  Let all coefficients multiply with the LCM value.
        for item in all_items:
            item.set_coefficient(item.get_coefficient() * denom_lcm)

        #  Initialize the GCD of numerators.
        numer_gcd = None
        use_numer_gcd = True

        for item in all_items:
            #  Get the coefficient.
            coeff = item.get_coefficient().simplify()

            #  Get the numerator.
            nd = coeff.as_numer_denom()
            nd_numer = nd[0].simplify()

            #  Calculate.
            if nd_numer.is_Integer and not nd_numer.is_zero:
                if numer_gcd is None:
                    numer_gcd = nd_numer
                else:
                    numer_gcd = _sympy.gcd(nd_numer, numer_gcd)
            else:
                use_numer_gcd = False
                break

        #  Let all coefficients divide by the GCD value if the GCD value is available.
        if use_numer_gcd and numer_gcd is not None:
            for item in all_items:
                item.set_coefficient((item.get_coefficient() / numer_gcd).simplify())

    def flip(self):
        """Flip the left items and the right items."""

        tmp = self.__left_items
        self.__left_items = self.__right_items
        self.__right_items = tmp


class ChemicalEquationParserInterface:
    """Interface for chemical equation parsers."""

    def __init__(self):
        """Initialize."""

        pass

    # noinspection PyMethodMayBeStatic
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
        :rtype : ChemicalEquation
        :return: The chemical equation object.
        """

        raise RuntimeError("parse() method should be overrided.")

    # noinspection PyMethodMayBeStatic
    def substitute(self, cexp_object, options, substitute_map=None):
        """Substitute a chemical equation.

        :type cexp_object: ChemicalEquation
        :type substitute_map: dict | None
        :param cexp_object: The chemical equation object.
        :param substitute_map: The substitution map.
        :rtype : ChemicalEquation
        :return: The substituted chemical equation object.
        """

        raise RuntimeError("substitute() method should be overrided.")

    # noinspection PyMethodMayBeStatic
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

        :type cexp_object: ChemicalEquation
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

        raise RuntimeError("BUG: print_out() method should be overrided.")
