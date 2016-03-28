#!/usr/bin/env python
#
#  Copyright 2014 - 2016 The BCE Authors. All rights reserved.
#  Use of this source code is governed by a BSD-style license that can be
#  found in the license.txt file.
#

#
#  This file was copied and modified from SymPy source code.
#
#  Coding-Style exception:
#    This file follows SymPy's coding style. Don't apply BCE coding style
#    to this file.
#

import bce.parser.mexp.function as _mexp_function
import sympy.printing.codeprinter as _sympy_codeprinter
import sympy.printing.precedence as _sympy_precedence
import sympy.printing.str as _sympy_print_str
import sympy as _sympy


class _MEXPPrinter(_sympy_codeprinter.CodePrinter):
    """A printer to convert python expressions to strings of the text form."""

    #  Default settings.
    _default_settings = {
        "order": None,
        "full_prec": 'auto',
        "precision": 15,
        "human": True,
    }

    #  Collectors.
    _number_symbols = set()
    _not_supported = set()

    def __init__(self):
        """Initialize the printer."""

        _sympy_codeprinter.CodePrinter.__init__(self, {})

    #  Map doprint() method.
    doprint = _sympy_print_str.StrPrinter.doprint

    def _print_Pow(self, expr, rational=False):
        """Print a Pow object.

        :type rational: bool
        :param expr: The expression.
        :param rational: Is it a rational power.
        :rtype : str
        :return: The printed string.
        """

        #  Get the precedence.
        prec = _sympy_precedence.precedence(expr)

        #  Print.
        return '%s^%s' % (
            self.parenthesize(expr.base, prec),
            self.parenthesize(expr.exp, prec)
        )

    def _print_Mul(self, expr):
        """Print a Mul object.

        :param expr: The expression.
        :rtype : str
        :return: The printed string.
        """

        assert isinstance(expr, _sympy.Mul)

        #  Get the precedence.
        prec = _sympy_precedence.precedence(expr)

        #  Get commutative factors and non-commutative factors.
        c, nc = expr.args_cnc()

        #  Print.
        res = super(_MEXPPrinter, self)._print_Mul(expr.func(*c))
        if nc:
            res += '*'
            res += '^'.join(self.parenthesize(a, prec) for a in nc)

        return res

    def _print_Function(self, expr):
        """Print a Function object.

        :param expr: The expression.
        :rtype : str
        :return: The printed string.
        :raise RuntimeError: Raise if the function is not supported.
        """

        assert isinstance(expr, _sympy.Function)

        #  Check the function.
        fn_object = _mexp_function.find_sympy_function(expr.func.__name__)
        if fn_object is None:
            raise RuntimeError("Unsupported function: \"%s\"." % expr.func.__name__)
        if fn_object.get_argument_count() != len(expr.args):
            raise RuntimeError("Argument count mismatch.")

        #  Stringify the arguments.
        arg_text = ""
        for arg_id in range(0, len(expr.args)):
            arg_text += self.doprint(expr.args[arg_id])
            if arg_id + 1 != len(expr.args):
                arg_text += ","

        return "%s(%s)" % (fn_object.get_function_name(), arg_text)


def print_mexp(expr):
    """Print an expression to a text.

    :param expr: The expression.
    :rtype : str
    :return: The text.
    """

    return _MEXPPrinter().doprint(expr).replace(" ", "")
