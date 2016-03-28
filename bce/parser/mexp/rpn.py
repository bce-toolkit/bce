#!/usr/bin/env python
#
#  Copyright 2014 - 2016 The BCE Authors. All rights reserved.
#  Use of this source code is governed by a BSD-style license that can be
#  found in the license.txt file.
#

import bce.base.stack as _adt_stack
import bce.locale.option as _l10n_opt
import bce.locale.registry as _l10n_reg
import bce.parser.common.error as _cm_error
import bce.parser.mexp.error as _mexp_errors
import bce.parser.mexp.function as _mexp_functions
import bce.utils.sympy_converter as _util_sympy_cnv
import sympy as _sympy


def calculate_rpn(expression, rpn_token_list, options):
    """Calculate the value of a RPN token list.

    :type expression: str
    :type rpn_token_list: list[bce.parser.mexp.token.Token]
    :type options: bce.option.Option
    :param expression: The expression.
    :param rpn_token_list: The RPN token list.
    :param options: The options.
    :return: The calculated value.
    """

    #
    #  This routine implements the postfix algorithm.
    #

    #  Get the language ID.
    lang_id = _l10n_opt.OptionWrapper(options).get_language_id()

    #  Initialize the operand stack.
    calc_stack = _adt_stack.Stack()

    for token in rpn_token_list:
        if token.is_integer_operand():
            #  Convert the symbol to integer and push it onto the stack.
            calc_stack.push(_util_sympy_cnv.convert_int_string_to_rational(token.get_symbol()))
        elif token.is_float_operand():
            #  Convert the symbol to float and push it onto the stack.
            calc_stack.push(_util_sympy_cnv.convert_float_string_to_rational(token.get_symbol()))
        elif token.is_symbol_operand():
            #  Create a math symbol and push it onto the stack.
            calc_stack.push(_sympy.Symbol(token.get_symbol()))
        elif token.is_plus_operator():
            #  Get two operands.
            num2 = calc_stack.pop()
            num1 = calc_stack.pop()

            #  Calculate.
            result = (num1 + num2).simplify()

            #  Push the result onto the stack.
            calc_stack.push(result)
        elif token.is_minus_operator():
            #  Get two operands.
            num2 = calc_stack.pop()
            num1 = calc_stack.pop()

            #  Calculate.
            result = (num1 - num2).simplify()

            #  Do minus and push the result onto the stack.
            calc_stack.push(result)
        elif token.is_multiply_operator():
            #  Get two operands.
            num2 = calc_stack.pop()
            num1 = calc_stack.pop()

            #  Calculate.
            result = (num1 * num2).simplify()

            #  Push the result onto the stack.
            calc_stack.push(result)
        elif token.is_divide_operator():
            #  Get two operands.
            num2 = calc_stack.pop()
            num1 = calc_stack.pop()

            #  Simplify before checking.
            num2 = num2.simplify()

            #  Raise an error if the rhs equals to zero.
            if num2.is_zero:
                err = _cm_error.Error(
                    _mexp_errors.MEXP_RPN_EVALUATION_DIVIDE_ZERO,
                    _l10n_reg.get_message(
                        lang_id,
                        "parser.mexp.error.divide_zero.description"
                    ),
                    options
                )
                err.push_traceback(
                    expression,
                    token.get_position(),
                    token.get_position() + len(token.get_symbol()) - 1,
                    _l10n_reg.get_message(
                        lang_id,
                        "parser.mexp.error.divide_zero.message"
                    )
                )
                raise err

            #  Calculate.
            result = (num1 / num2).simplify()

            #  Push the result onto the stack.
            calc_stack.push(result)
        elif token.is_pow_operator():
            #  Get two operands.
            num2 = calc_stack.pop()
            num1 = calc_stack.pop()

            #  Simplify before checking.
            num1 = num1.simplify()
            num2 = num2.simplify()

            #  For a ^ b, when b < 0, a != 0.
            if num2.is_negative and num1.is_zero:
                err = _cm_error.Error(
                    _mexp_errors.MEXP_RPN_EVALUATION_DIVIDE_ZERO,
                    _l10n_reg.get_message(
                        lang_id,
                        "parser.mexp.error.divide_zero.description"
                    ),
                    options
                )
                err.push_traceback(
                    expression,
                    token.get_position(),
                    token.get_position() + len(token.get_symbol()) - 1,
                    _l10n_reg.get_message(
                        lang_id,
                        "parser.mexp.error.divide_zero.message"
                    )
                )
                raise err

            #  Calculate.
            result = (num1 ** num2).simplify()

            #  Push the result onto the stack.
            calc_stack.push(result)
        elif token.is_negative_operator():
            #  Get an operand.
            num1 = calc_stack.pop()

            #  Calculate.
            result = (-num1).simplify()

            #  Push the result onto the stack.
            calc_stack.push(result)
        elif token.is_function():
            #  Get the function object.
            fn_object = _mexp_functions.find_function(token.get_symbol())
            if fn_object is None:
                raise RuntimeError("BUG: Function object is None.")

            #  Build the arguments list.
            arguments = []
            for i in range(0, fn_object.get_argument_count()):
                arguments.insert(0, calc_stack.pop())

            #  Invoke.
            error_code, result = fn_object.invoke(arguments)

            #  Handle the error code and the result.
            if error_code == _mexp_functions.ERROR_SUCCESS:
                #  Push the result onto the stack.
                calc_stack.push(result)
            elif error_code == _mexp_functions.ERROR_ARGUMENT_COUNT:
                raise RuntimeError("BUG: Incorrect argument count.")
            elif error_code == _mexp_functions.ERROR_DOMAIN:
                #  Get the ID of the out-of-ranged argument.
                assert isinstance(result, dict)
                arg_id = result["argument"]
                assert isinstance(arg_id, int)

                #  Raise an error.
                err = _cm_error.Error(
                    _mexp_errors.MEXP_RPN_EVALUATION_DOMAIN_OUT_OF_RANGE,
                    _l10n_reg.get_message(
                        lang_id,
                        "parser.mexp.error.domain_out_of_range.description"
                    ),
                    options
                )
                err.push_traceback(
                    expression,
                    token.get_position(),
                    token.get_position() + len(token.get_symbol()) - 1,
                    _l10n_reg.get_message(
                        lang_id,
                        "parser.mexp.error.domain_out_of_range.message",
                        replace_map={
                            "$1": str(arg_id + 1)
                        }
                    )
                )
                raise err
            else:
                raise RuntimeError("BUG: Unhandled error code.")
        else:
            raise RuntimeError("BUG: Invalid token type.")

    #  If there are more than one operands in the stack, raise a runtime error. But generally,
    #  we shouldn't get this error because we have checked the whole expression when tokenizing.
    if len(calc_stack) > 1:
        raise RuntimeError("BUG: Too many items in the stack after calculation.")

    return calc_stack.top()
