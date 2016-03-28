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

import bce.dom.mathml.all as _mathml
import bce.parser.mexp.function as _mexp_function
# noinspection PyProtectedMember
from sympy.core.function import _coeff_isneg
import sympy.printing.precedence as _sympy_precedence
import sympy.printing.printer as _sympy_printer
import sympy as _sympy


# noinspection PyMethodMayBeStatic,PyPep8Naming
class _MathMLPrinter(_sympy_printer.Printer):
    """Print SymPy expression to MathML."""

    #  Default settings.
    _default_settings = {
        "order": None,
        "encoding": "utf-8"
    }

    def __init__(self, settings=None, protected_header_enabled=False, protected_header_prefix="X"):
        """Initialize the printer.

        :type protected_header_enabled: bool
        :type protected_header_prefix: str
        :param settings: The settings.
        :param protected_header_enabled: Whether the protected headers are enabled.
        :param protected_header_prefix: The prefix of the protected headers.
        """

        #  Initialize the super class.
        _sympy_printer.Printer.__init__(self, settings)

        #  Save protected-header settings.
        self.__ph_enabled = protected_header_enabled
        self.__ph_prefix = protected_header_prefix

    def doprint(self, expr):
        """Do printing.

        :param expr: The expression.
        :rtype : bce.dom.mathml.all.Base
        :return: The printed MathML object.
        """

        return _sympy_printer.Printer._print(self, expr)

    def _print_Mul(self, expr):
        """Print a Mul object.

        :param expr: The expression.
        :rtype : bce.dom.mathml.all.Base
        :return: The printed MathML object.
        """

        assert isinstance(expr, _sympy.Mul)

        # noinspection PyProtectedMember
        if _coeff_isneg(expr):
            x = _mathml.RowComponent()
            x.append_object(_mathml.OperatorComponent(_mathml.OPERATOR_MINUS))
            x.append_object(self._print_Mul(-expr))
            return x

        PREC = _sympy_precedence.precedence(expr)

        from sympy.simplify import fraction
        numer, denom = fraction(expr)

        if denom is not _sympy.S.One:
            return _mathml.FractionComponent(self._print(numer), self._print(denom))

        coeff, terms = expr.as_coeff_mul()
        if coeff is _sympy.S.One and len(terms) == 1:
            #  Since the negative coefficient has been handled, I don't
            #  thing a coeff of 1 can remain
            if _sympy_precedence.precedence(terms[0]) < PREC:
                #  Return the argument with parentheses around.
                tmp_node = _mathml.RowComponent()
                tmp_node.append_object(_mathml.OperatorComponent(_mathml.OPERATOR_LEFT_PARENTHESIS))
                tmp_node.append_object(self._print(terms[0]))
                tmp_node.append_object(_mathml.OperatorComponent(_mathml.OPERATOR_RIGHT_PARENTHESIS))

                return tmp_node
            else:
                #  Return the argument only.
                return self._print(terms[0])

        if self.order != "old":
            # noinspection PyProtectedMember
            terms = _sympy.Mul._from_args(terms).as_ordered_factors()

        #  Build result row element(node).
        x = _mathml.RowComponent()

        if coeff != 1:
            if _sympy_precedence.precedence(coeff) < PREC:
                #  Insert the coefficient number with parentheses around.
                x.append_object(_mathml.OperatorComponent(_mathml.OPERATOR_LEFT_PARENTHESIS))
                x.append_object(self._print(coeff))
                x.append_object(_mathml.OperatorComponent(_mathml.OPERATOR_RIGHT_PARENTHESIS))
            else:
                #  Insert the coefficient number only.
                x.append_object(self._print(coeff))

            #  Insert a multiply operator.
            if not terms[0].is_Symbol:
                x.append_object(_mathml.OperatorComponent(_mathml.OPERATOR_MULTIPLY))

        terms_len = len(terms)
        for term_id in range(0, terms_len):
            cur_term = terms[term_id]
            if _sympy_precedence.precedence(cur_term) < PREC:
                x.append_object(_mathml.OperatorComponent(_mathml.OPERATOR_LEFT_PARENTHESIS))
                x.append_object(self._print(cur_term))
                x.append_object(_mathml.OperatorComponent(_mathml.OPERATOR_RIGHT_PARENTHESIS))
            else:
                x.append_object(self._print(cur_term))
            if term_id + 1 != terms_len and not cur_term.is_Symbol:
                x.append_object(_mathml.OperatorComponent(_mathml.OPERATOR_MULTIPLY))

        return x

    def _print_Add(self, expr, order=None):
        """Print a Add object.

        :param expr: The expression.
        :rtype : bce.dom.mathml.all.Base
        :return: The printed MathML object.
        """

        assert isinstance(expr, _sympy.Add)

        args = self._as_ordered_terms(expr, order=order)
        PREC = _sympy_precedence.precedence(expr)
        dt = _mathml.RowComponent()
        args_len = len(args)

        #  Iterator each part.
        for arg_id in range(0, args_len):
            cur_arg = args[arg_id]
            if cur_arg.is_negative:
                #  Get the negative number.
                neg_arg = -cur_arg

                #  Get the precedence.
                CUR_PREC = _sympy_precedence.precedence(neg_arg)

                #  Add a '-' operator.
                dt.append_object(_mathml.OperatorComponent(_mathml.OPERATOR_MINUS))

                # noinspection PyProtectedMember
                if CUR_PREC < PREC or (_coeff_isneg(neg_arg) and arg_id != 0):
                    #  Insert the argument with parentheses around.
                    dt.append_object(_mathml.OperatorComponent(_mathml.OPERATOR_LEFT_PARENTHESIS))
                    dt.append_object(self._print(neg_arg))
                    dt.append_object(_mathml.OperatorComponent(_mathml.OPERATOR_RIGHT_PARENTHESIS))
                else:
                    #  Insert the argument only.
                    dt.append_object(self._print(neg_arg))
            else:
                #  Add a '+' operator if the argument is not the first one.
                if arg_id != 0:
                    dt.append_object(_mathml.OperatorComponent(_mathml.OPERATOR_PLUS))

                #  Get the precedence.
                CUR_PREC = _sympy_precedence.precedence(cur_arg)

                # noinspection PyProtectedMember
                if CUR_PREC < PREC or (_coeff_isneg(cur_arg) and arg_id != 0):
                    #  Insert the argument with parentheses around.
                    dt.append_object(_mathml.OperatorComponent(_mathml.OPERATOR_LEFT_PARENTHESIS))
                    dt.append_object(self._print(cur_arg))
                    dt.append_object(_mathml.OperatorComponent(_mathml.OPERATOR_RIGHT_PARENTHESIS))
                else:
                    #  Insert the argument only.
                    dt.append_object(self._print(cur_arg))

        return dt

    def _print_Rational(self, e):
        """Print a Rational object.

        :param e: The expression.
        :rtype : bce.dom.mathml.all.Base
        :return: The printed MathML object.
        """

        assert isinstance(e, _sympy.Rational)

        if e.q == 1:
            #  Don't do division if the denominator is 1.
            return _mathml.NumberComponent(str(e.p))

        return _mathml.FractionComponent(
            _mathml.NumberComponent(str(e.p)),
            _mathml.NumberComponent(str(e.q))
        )

    def _print_Symbol(self, sym):
        """Print a Symbol object.

        :param sym: The expression.
        :rtype : bce.dom.mathml.all.Base
        :return: The printed MathML object.
        """

        assert isinstance(sym, _sympy.Symbol)

        if self.__ph_enabled and sym.name.startswith(self.__ph_prefix):
            return _mathml.SubComponent(
                _mathml.TextComponent(self.__ph_prefix.lower()),
                _mathml.TextComponent(sym.name[len(self.__ph_prefix):])
            )
        else:
            return _mathml.TextComponent(sym.name)

    def _print_Pow(self, e):
        """Print a Pow object.

        :param e: The expression.
        :rtype : bce.dom.mathml.all.Base
        :return: The printed MathML object.
        """

        assert isinstance(e, _sympy.Pow)
        PREC = _sympy_precedence.precedence(e)

        if e.exp.is_Rational and e.exp.p == 1:
            #  If the exponent is like {1/x}, do SQRT operation if x is 2, otherwise, do 
            #  root operation.
            printed_base = self._print(e.base)

            if e.exp.q != 2:
                #  Do root operation.
                root = _mathml.RootComponent(printed_base, _mathml.NumberComponent(str(e.exp.q)))
            else:
                #  Do SQRT operation.
                root = _mathml.SquareRootComponent(printed_base)

            return root

        if e.exp.is_negative:
            if e.exp.is_Integer and e.exp == _sympy.Integer(-1):
                final_node = _mathml.FractionComponent(
                    _mathml.NumberComponent("1"),
                    self._print(e.base)
                )
            else:
                #  frac{1, base ^ |exp|}
                neg_exp = -e.exp

                #  Get node for the base.
                if _sympy_precedence.precedence(e.base) < PREC:
                    base_node = _mathml.RowComponent()
                    base_node.append_object(_mathml.OperatorComponent(_mathml.OPERATOR_LEFT_PARENTHESIS))
                    base_node.append_object(self._print(e.base))
                    base_node.append_object(_mathml.OperatorComponent(_mathml.OPERATOR_RIGHT_PARENTHESIS))
                else:
                    base_node = self._print(e.base)

                #  Get node for the exponent.
                if _sympy_precedence.precedence(neg_exp) < PREC:
                    exp_node = _mathml.RowComponent()
                    exp_node.append_object(_mathml.OperatorComponent(_mathml.OPERATOR_LEFT_PARENTHESIS))
                    exp_node.append_object(self._print(neg_exp))
                    exp_node.append_object(_mathml.OperatorComponent(_mathml.OPERATOR_RIGHT_PARENTHESIS))
                else:
                    exp_node = neg_exp

                final_node = _mathml.FractionComponent(
                    _mathml.NumberComponent("1"),
                    _mathml.SuperComponent(base_node, exp_node)
                )

            return final_node

        #  Get node for the base.
        if _sympy_precedence.precedence(e.base) < PREC:
            base_node = _mathml.RowComponent()
            base_node.append_object(_mathml.OperatorComponent(_mathml.OPERATOR_LEFT_PARENTHESIS))
            base_node.append_object(self._print(e.base))
            base_node.append_object(_mathml.OperatorComponent(_mathml.OPERATOR_RIGHT_PARENTHESIS))
        else:
            base_node = self._print(e.base)

        return _mathml.SuperComponent(
            base_node,
            self._print(e.exp)
        )

    def _print_Function(self, e):
        """Print a Function object.

        :param e: The expression.
        :rtype : bce.dom.mathml.all.Base
        :return: The printed MathML object.
        """

        assert isinstance(e, _sympy.Function)

        #  Check the function.
        fn_object = _mexp_function.find_sympy_function(e.func.__name__)
        if fn_object is None:
            raise RuntimeError("Unsupported function: \"%s\"." % e.func.__name__)
        if fn_object.get_argument_count() != len(e.args):
            raise RuntimeError("Argument count mismatch.")

        #  Build the node.
        node = _mathml.RowComponent()
        node.append_object(_mathml.TextComponent(fn_object.get_function_name()))
        node.append_object(_mathml.OperatorComponent(_mathml.OPERATOR_LEFT_PARENTHESIS))
        for arg_id in range(0, len(e.args)):
            arg_value = e.args[arg_id]
            node.append_object(self.doprint(arg_value))
            if arg_id + 1 != len(e.args):
                node.append_object(_mathml.OperatorComponent(_mathml.OPERATOR_SEPARATOR))
        node.append_object(_mathml.OperatorComponent(_mathml.OPERATOR_RIGHT_PARENTHESIS))

        return node

    def _print_Number(self, e):
        """Print a Number object.

        :param e: The expression.
        :rtype : bce.dom.mathml.all.Base
        :return: The printed MathML object.
        """

        assert isinstance(e, _sympy.Number)

        return _mathml.NumberComponent(str(e))

    def _print_int(self, p):
        """Print an int object.

        :param p: The expression.
        :rtype : bce.dom.mathml.all.Base
        :return: The printed MathML object.
        """

        assert isinstance(p, int)

        return _mathml.NumberComponent(str(p))


def print_mexp(expr, protected_header_enabled=False, protected_header_prefix="X", **settings):
    """Print an expression to a MathML object.

    :type protected_header_enabled: bool
    :type protected_header_prefix: str
    :param expr: The expression.
    :param protected_header_enabled: Whether the protected headers are enabled.
    :param protected_header_prefix: The prefix of the protected headers.
    :param settings: The settings.
    :rtype : bce.dom.mathml.all.Base
    :return: The printed MathML object.
    """

    # noinspection PyProtectedMember
    return _MathMLPrinter(
        settings,
        protected_header_enabled=protected_header_enabled,
        protected_header_prefix=protected_header_prefix
    ).doprint(_sympy.sympify(expr))
