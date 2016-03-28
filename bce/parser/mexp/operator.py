#!/usr/bin/env python
#
#  Copyright 2014 - 2016 The BCE Authors. All rights reserved.
#  Use of this source code is governed by a BSD-style license that can be
#  found in the license.txt file.
#


class OperatorAssociativity:
    """Enumeration class for the associativity of operators."""

    Left = 1
    Right = 2


class OperatorItem:
    """Class for description an math operator."""

    def __init__(self, symbol, precedence, associativity, required_left_op, required_right_op):
        """Initialize the class with specific operator symbol, precedence and associativity.

        :type symbol: str
        :type precedence: int
        :type associativity: int
        :type required_left_op: bool
        :type required_right_op: bool
        :param symbol: The symbol.
        :param precedence: The precedence.
        :param associativity: The associativity.
        """

        self.__sym = symbol
        self.__pd = precedence
        self.__assoc = associativity
        self.__req_left_op = required_left_op
        self.__req_right_op = required_right_op

    def get_symbol(self):
        """Get the symbol of the operator.

        :rtype : str
        :return: The symbol.
        """

        return self.__sym

    def get_precedence(self):
        """Get the precedence of the operator.

        :rtype : int
        :return: The precedence.
        """

        return self.__pd

    def get_associativity(self):
        """Get the associativity of the operator.

        :rtype : int
        :return: The associativity.
        """

        return self.__assoc

    def is_left_associative(self):
        """Get whether the operator is left-associative.

        :rtype : bool
        :return: Return True if the operator is left-associative.
        """

        return self.__assoc == OperatorAssociativity.Left

    def is_right_associative(self):
        """Get whether the operator is right-associative.

        :rtype : bool
        :return: Return True if the operator is right-associative.
        """

        return self.__assoc == OperatorAssociativity.Right

    def is_required_left_operand(self):
        """Get whether the operator requires left operand.

        :rtype : bool
        :return: Return True if the left operand is required.
        """

        return self.__req_left_op

    def is_required_right_operand(self):
        """Get whether the operator requires right operand.

        :rtype : bool
        :return: Return True if the right operand is required.
        """

        return self.__req_right_op


#  Operators.
OPERATORS = [
    OperatorItem("^", 5, OperatorAssociativity.Right, True, True),
    OperatorItem("-", 4, OperatorAssociativity.Right, False, True),
    OperatorItem("*", 3, OperatorAssociativity.Left, True, True),
    OperatorItem("/", 3, OperatorAssociativity.Left, True, True),
    OperatorItem("+", 2, OperatorAssociativity.Left, True, True),
    OperatorItem("-", 2, OperatorAssociativity.Left, True, True),
]

#  The ID of operators.
OPERATOR_POW_ID = 0
OPERATOR_NEGATIVE_ID = 1
OPERATOR_MULTIPLY_ID = 2
OPERATOR_DIVIDE_ID = 3
OPERATOR_PLUS_ID = 4
OPERATOR_MINUS_ID = 5
