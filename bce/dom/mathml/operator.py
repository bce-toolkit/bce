#!/usr/bin/env python
#
#  Copyright 2014 - 2016 The BCE Authors. All rights reserved.
#  Use of this source code is governed by a BSD-style license that can be
#  found in the license.txt file.
#

import bce.dom.mathml.base as _base
import bce.dom.mathml.types as _types

OPERATOR_PLUS = 1000
OPERATOR_MINUS = 1001
OPERATOR_MULTIPLY = 1002
OPERATOR_DOT = 1003
OPERATOR_LEFT_PARENTHESIS = 1004
OPERATOR_RIGHT_PARENTHESIS = 1005
OPERATOR_EQUAL = 1006
OPERATOR_SEPARATOR = 1007


class OperatorComponent(_base.Base):
    """Operator component."""

    def __init__(self, operator_id):
        """Initialize the operator component.

        :type operator_id: int
        :param operator_id: The operator ID.
        """

        _base.Base.__init__(self, _types.COMPONENT_TYPE_OPERATOR)
        self.__op_id = operator_id

    def set_operator_id(self, operator_id):
        """Set the ID of the operator.

        :type operator_id: int
        :param operator_id: The operator ID.
        """

        self.__op_id = operator_id

    def get_operator_id(self):
        """Get the ID of the operator.

        :rtype : int
        :return: The operator ID.
        """

        return self.__op_id

    def _get_operator_symbol(self):
        """Get the serialized MathML symbol of the operator.

        :rtype : str
        :return: The serialized symbol.
        :raise ValueError: Raise this error if the operator type is invalid.
        """

        if self.__op_id == OPERATOR_PLUS:
            return "+"
        elif self.__op_id == OPERATOR_MINUS:
            return "&#x2212;"
        elif self.__op_id == OPERATOR_MULTIPLY:
            return "&#xD7;"
        elif self.__op_id == OPERATOR_DOT:
            return "&#x22C5;"
        elif self.__op_id == OPERATOR_LEFT_PARENTHESIS:
            return "("
        elif self.__op_id == OPERATOR_RIGHT_PARENTHESIS:
            return ")"
        elif self.__op_id == OPERATOR_EQUAL:
            return "="
        elif self.__op_id == OPERATOR_SEPARATOR:
            return ","
        else:
            raise ValueError("Invalid operator ID.")

    def is_plus(self):
        """Get whether the operator is a plus operator.

        :rtype : bool
        :return: Whether the operator is a plus operator.
        """

        return self.__op_id == OPERATOR_PLUS

    def is_minus(self):
        """Get whether the operator is a minus operator.

        :rtype : bool
        :return: Whether the operator is a minus operator.
        """

        return self.__op_id == OPERATOR_MINUS

    def is_multiply(self):
        """Get whether the operator is a multiply operator.

        :rtype : bool
        :return: Whether the operator is a multiply operator.
        """

        return self.__op_id == OPERATOR_MULTIPLY

    def is_dot(self):
        """Get whether the operator is a dot.

        :rtype : bool
        :return: Whether the operator is a dot.
        """

        return self.__op_id == OPERATOR_DOT

    def is_left_parenthesis(self):
        """Get whether the operator is a left parenthesis.

        :rtype : bool
        :return: Whether the operator is a left parenthesis.
        """

        return self.__op_id == OPERATOR_LEFT_PARENTHESIS

    def is_right_parenthesis(self):
        """Get whether the operator is a right parenthesis.

        :rtype : bool
        :return: Whether the operator is a right parenthesis.
        """

        return self.__op_id == OPERATOR_RIGHT_PARENTHESIS

    def is_equal(self):
        """Get whether the operator is an equal.

        :rtype : bool
        :return: Whether the operator is an equal.
        """

        return self.__op_id == OPERATOR_EQUAL

    def is_separator(self):
        """Get whether the operator is a separator.

        :rtype : bool
        :return: Whether the operator is a separator.
        """

        return self.__op_id == OPERATOR_SEPARATOR

    def to_string(self, indent=0):
        """Serialize the component to string.

        :type indent: int
        :param indent: The indent space count.
        :rtype : str
        :return: The serialized string.
        """

        return " " * indent + "<mo>" + self._get_operator_symbol() + "</mo>"
