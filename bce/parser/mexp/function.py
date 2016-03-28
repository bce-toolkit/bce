#!/usr/bin/env python
#
#  Copyright 2014 - 2016 The BCE Authors. All rights reserved.
#  Use of this source code is governed by a BSD-style license that can be
#  found in the license.txt file.
#

import sympy as _sympy

#  Error codes.
ERROR_SUCCESS = 0
ERROR_ARGUMENT_COUNT = 1
ERROR_DOMAIN = 2


#
#  Base class.
#
class _MathFunctionBase:
    """Base class for all math function classes."""

    def __init__(self, function_name, sympy_function_name, argument_count):
        """Initialize the object.

        :type function_name: str
        :type sympy_function_name: str | None
        :type argument_count: int
        :param function_name: The function name.
        :param sympy_function_name: The function name in SymPy.
        :param argument_count: The argument count.
        """

        self.__func_name = function_name
        self.__sympy_func_name = sympy_function_name
        self.__argc = argument_count

    def get_function_name(self):
        """Get the function name.

        :rtype : str
        :return: The function name.
        """

        return self.__func_name

    def get_sympy_function_name(self):
        """Get the function name in SymPy.

        :rtype : str | None
        :return: The function name.
        """

        return self.__sympy_func_name

    def get_argument_count(self):
        """Get the argument count.

        :rtype : int
        :return: The argument count.
        """

        return self.__argc

    # noinspection PyMethodMayBeStatic
    def invoke(self, arguments):
        """Invoke the function.

        :type arguments: list
        :param arguments: The arguments.
        :rtype : (int, object)
        :return: A tuple contains the error code and the detailed result.
        """

        raise RuntimeError("invoke() method should be overrided.")


#
#  Implementations.
#
class MathFunctionPower(_MathFunctionBase):
    """Implementation of math function pow(x, y)."""

    def __init__(self):
        """Initialize the object."""

        _MathFunctionBase.__init__(self, "pow", None, 2)

    def invoke(self, arguments):
        """Invoke the function.

        :type arguments: list
        :param arguments: The arguments.
        :rtype : (int, object)
        :return: A tuple contains the error code and the detailed result.
        """

        #  Check the argument count.
        if self.get_argument_count() != len(arguments):
            return (
                ERROR_ARGUMENT_COUNT,
                {
                    "required": self.get_argument_count(),
                    "actual": len(arguments)
                }
            )

        #  Get the base and the exponent.
        base_value = arguments[0].simplify()
        exp_value = arguments[1].simplify()

        #  Check the domain.
        if base_value.is_zero and exp_value.is_negative:
            return (
                ERROR_DOMAIN,
                {
                    "argument": 1
                }
            )

        #  Calculate.
        result = (base_value ** exp_value).simplify()

        return (
            ERROR_SUCCESS,
            result
        )


class MathFunctionSquareRoot(_MathFunctionBase):
    """Implementation of math function pow(x, y)."""

    def __init__(self):
        """Initialize the object."""

        _MathFunctionBase.__init__(self, "sqrt", "sqrt", 1)

    def invoke(self, arguments):
        """Invoke the function.

        :type arguments: list
        :param arguments: The arguments.
        :rtype : (int, object)
        :return: A tuple contains the error code and the detailed result.
        """

        #  Check the argument count.
        if self.get_argument_count() != len(arguments):
            return (
                ERROR_ARGUMENT_COUNT,
                {
                    "required": self.get_argument_count(),
                    "actual": len(arguments)
                }
            )

        #  Get the base.
        base_value = arguments[0].simplify()

        #  Check the domain.
        if base_value.is_negative:
            return (
                ERROR_DOMAIN,
                {
                    "argument": 0
                }
            )

        #  Calculate.
        result = _sympy.sqrt(base_value).simplify()

        return (
            ERROR_SUCCESS,
            result
        )

#
#  Registry.
#
AVAILABLE_FUNCTIONS = [
    MathFunctionPower(),
    MathFunctionSquareRoot()
]


def find_function(function_name):
    """Find a function.

    :type function_name: str
    :param function_name: The function name.
    :rtype : _MathFunctionBase | None
    :return: The function object. (Return None if the function can't be found.)
    """

    for function_obj in AVAILABLE_FUNCTIONS:
        assert isinstance(function_obj, _MathFunctionBase)
        if function_obj.get_function_name() == function_name:
            return function_obj

    return None


def find_sympy_function(function_name):
    """Find a function with its function name in SymPy.

    :type function_name: str
    :param function_name: The function name.
    :rtype : _MathFunctionBase | None
    :return: The function object. (Return None if the function can't be found.)
    """

    for function_obj in AVAILABLE_FUNCTIONS:
        assert isinstance(function_obj, _MathFunctionBase)
        if function_obj.get_function_name() == function_name:
            return function_obj

    return None
