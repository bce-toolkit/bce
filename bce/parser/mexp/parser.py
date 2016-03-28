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
import bce.parser.mexp.operator as _mexp_operators
import bce.parser.mexp.token as _mexp_token


class _RPNProcessor:
    """RPN processor for the MEXP parser."""

    def __init__(self):
        """Initialize the processor with empty operator stack and RPN token list."""

        self.__op_stack = _adt_stack.Stack()
        self.__rpn = []

    def clear(self):
        """Clear the operator stack and RPN token list."""

        self.__op_stack = _adt_stack.Stack()
        self.__rpn = []

    def add_operand(self, operand_token):
        """Process an operand token.

        :type operand_token: bce.parser.mexp.token.Token
        :param operand_token: The operand token.
        """

        self.__rpn.append(operand_token)

    def add_operator(self, operator_token):
        """Process an operator token.

        :type operator_token: bce.parser.mexp.token.Token
        :param operator_token: The operator token.
        """

        #  Get the operator of the token.
        op1 = _mexp_operators.OPERATORS[operator_token.get_subtype()]

        while True:
            if len(self.__op_stack) == 0:
                break

            #  Stop popping if the top item of the stack isn't an operator.
            top_op = self.__op_stack.top()
            if not top_op.is_operator():
                break

            #  Get the operator on the top of the stack.
            op2 = _mexp_operators.OPERATORS[top_op.get_subtype()]

            if (op1.is_left_associative() and op1.get_precedence() <= op2.get_precedence()) or \
                    (op1.is_right_associative() and op1.get_precedence() < op2.get_precedence()):
                self.__rpn.append(top_op)
                self.__op_stack.pop()
            else:
                break

        #  Push current token to the operator stack.
        self.__op_stack.push(operator_token)

    def add_function(self, function_token):
        """Process a function token.

        :type function_token: bce.parser.mexp.token.Token
        :param function_token: The function token.
        """

        self.__op_stack.push(function_token)

    def add_separator(self):
        """Process a separator token."""

        while True:
            top_op = self.__op_stack.top()
            if top_op.is_left_parenthesis():
                break
            self.__rpn.append(top_op)
            self.__op_stack.pop()

    def add_left_parenthesis(self, parenthesis_token):
        """Process a left parenthesis.

        :type parenthesis_token: bce.parser.mexp.token.Token
        :param parenthesis_token:
        """

        self.__op_stack.push(parenthesis_token)

    def add_right_parenthesis(self):
        """Process a right parenthesis."""

        while True:
            #  Get the top item of the stack.
            top_op = self.__op_stack.top()

            #  Stop popping if the top item of the stack is not a left parenthesis.
            if top_op.is_left_parenthesis():
                break

            #  Pop the token off from the stack and push it onto the RPN token list.
            self.__rpn.append(top_op)
            self.__op_stack.pop()

        #  Pop the left parenthesis off from the stack.
        self.__op_stack.pop()

        if len(self.__op_stack) != 0 and self.__op_stack.top().is_function():
            self.__rpn.append(self.__op_stack.pop())

    def finalize(self):
        """Pop all items off from the stack and push them to the RPN token list."""

        while len(self.__op_stack) != 0:
            self.__rpn.append(self.__op_stack.pop())

    def direct_add_token_to_rpn(self, token):
        """Add a token to the RPN token list directly.

        :type token: bce.parser.mexp.token.Token
        :param token: The token.
        """

        self.__rpn.append(token)

    def direct_push_item_onto_stack(self, item):
        """Push an item onto the stack directly.

        :type item: bce.parser.mexp.token.Token
        :param item: The item.
        """

        self.__op_stack.push(item)

    def direct_pop_item_from_stack(self):
        """Pop an item off from the stack and return it directly.

        :rtype : bce.parser.mexp.token.Token
        :return: The item.
        """

        return self.__op_stack.pop()

    def get_stack_item_count(self):
        """Get the item count of the stack.

        :rtype : int
        :return: The item count.
        """

        return len(self.__op_stack)

    def get_stack_top_item(self):
        """Get the top item of the stack.

        :rtype : bce.parser.mexp.token.Token
        :return: The item.
        """

        return self.__op_stack.top()

    def get_rpn(self):
        """Get the RPN token list.

        :rtype : list[bce.parser.mexp.token.Token]
        :return: The list.
        """

        return self.__rpn


class _ParenthesisStackItem:
    """Parenthesis state class for MEXP parser."""

    def __init__(self, symbol, token_id, is_in_fn, cur_argc, req_argc, prev_sep_pos):
        """Initialize the item.

        :type symbol: str
        :type token_id: int
        :type is_in_fn: bool
        :type cur_argc: int
        :type req_argc: int
        :type prev_sep_pos: int
        :param symbol: The symbol of the left parenthesis.
        :param token_id: The token ID.
        :param is_in_fn: Whether it's in function state now.
        :param cur_argc: Current argument count.
        :param req_argc: Required argument count.
        :param prev_sep_pos: Previous separator position.
        """

        self.__sym = symbol
        self.__token_id = token_id
        self.__is_in_fn = is_in_fn
        self.__cur_argc = cur_argc
        self.__req_argc = req_argc
        self.__prev_sep_pos = prev_sep_pos

    def get_symbol(self):
        """Get the symbol of the left parenthesis.

        :rtype : str
        :return: The symbol.
        """

        return self.__sym

    def is_in_function(self):
        """Get whether it's in function state.

        :rtype : bool
        :return: Whether it's in function state.
        """

        return self.__is_in_fn

    def get_current_argument_count(self):
        """Get current argument count.

        :rtype : int
        :return: The count.
        """

        return self.__cur_argc

    def get_required_argument_count(self):
        """Get required argument count.

        :rtype : int
        :return: The count.
        """

        return self.__req_argc

    def get_previous_separator_position(self):
        """Get the position of previous separator.

        :rtype : int
        :return: The position.
        """

        return self.__prev_sep_pos

    def get_token_id(self):
        """Get the token ID.

        :rtype : int
        :return: The token ID.
        """

        return self.__token_id


def _check_left_operand(expression, token_list, token_id, options):
    """Check the left operand.

    :type expression: str
    :type token_list: list[bce.parser.mexp.token.Token]
    :type token_id: int
    :type options: bce.option.Option
    :param expression: (The same as the variable in parse_to_rpn() routine.)
    :param token_list: (The same as the variable in parse_to_rpn() routine.)
    :param token_id: (The same as the variable in parse_to_rpn() routine.)
    :param options: (The same as the variable in parse_to_rpn() routine.)
    :raise bce.parser.common.error.Error: Raise when there's no left operand.
    """

    raise_err = False
    if token_id == 0:
        raise_err = True
    else:
        prev_tok = token_list[token_id - 1]
        if not (prev_tok.is_right_parenthesis() or prev_tok.is_operand()):
            raise_err = True

    if raise_err:
        #  Get the language ID.
        lang_id = _l10n_opt.OptionWrapper(options).get_language_id()

        #  Raise the error.
        err_pos = token_list[token_id].get_position()
        err = _cm_error.Error(
            _mexp_errors.MEXP_MISSING_OPERAND,
            _l10n_reg.get_message(
                lang_id,
                "parser.mexp.error.missing_operand.description"
            ),
            options
        )
        err.push_traceback(
            expression,
            err_pos,
            err_pos,
            _l10n_reg.get_message(
                lang_id,
                "parser.mexp.error.missing_operand.left"
            )
        )
        raise err


def _check_right_operand(expression, token_list, token_id, options):
    """Check the right operand.

    :type expression: str
    :type token_list: list[bce.parser.mexp.token.Token]
    :type token_id: int
    :type options: bce.option.Option
    :param expression: (The same as the variable in parse_to_rpn() routine.)
    :param token_list: (The same as the variable in parse_to_rpn() routine.)
    :param token_id: (The same as the variable in parse_to_rpn() routine.)
    :param options: (The same as the variable in parse_to_rpn() routine.)
    :raise _cm_error.Error: Raise when there's no right operand.
    """

    raise_err = False
    if token_id + 1 == len(token_list):
        raise_err = True
    else:
        next_tok = token_list[token_id + 1]
        if not (next_tok.is_left_parenthesis() or next_tok.is_operand() or next_tok.is_function()):
            raise_err = True

    if raise_err:
        #  Get the language ID.
        lang_id = _l10n_opt.OptionWrapper(options).get_language_id()

        #  Raise the error.
        err_pos = token_list[token_id].get_position()
        err = _cm_error.Error(
            _mexp_errors.MEXP_MISSING_OPERAND,
            _l10n_reg.get_message(
                lang_id,
                "parser.mexp.error.missing_operand.description"
            ),
            options
        )
        err.push_traceback(
            expression,
            err_pos,
            err_pos,
            _l10n_reg.get_message(
                lang_id,
                "parser.mexp.error.missing_operand.right"
            )
        )
        raise err


def parse_to_rpn(expression, token_list, options, protected_header_enabled=False, protected_header_prefix="X"):
    """Parse an infix math expression to RPN.

    :type expression: str
    :type token_list: list[bce.parser.mexp.token.Token]
    :type options: bce.option.Option
    :type protected_header_enabled: bool
    :type protected_header_prefix: str
    :param expression: The infix math expression.
    :param token_list: The tokenized infix math expression.
    :param options: The options.
    :param protected_header_enabled: Whether the protected headers are enabled.
    :param protected_header_prefix: The prefix of the protected headers.
    :rtype : list[bce.parser.mexp.token.Token]
    :return: The RPN token list.
    :raise bce.parser.common.error.Error: Raise when a parser error occurred.
    """

    #  Initialize
    lang_id = _l10n_opt.OptionWrapper(options).get_language_id()
    token_id = 0
    token_count = len(token_list)
    rpn = _RPNProcessor()
    current_argc = 0
    required_argc = 0
    prev_separator_position = -1
    parenthesis_mapping = {
        ")": "(",
        "]": "[",
        "}": "{"
    }
    parenthesis_stack = _adt_stack.Stack()
    in_function = False

    while token_id < token_count:
        #  Get current token.
        token = token_list[token_id]

        #  Get previous token.
        if token_id != 0:
            prev_tok = token_list[token_id - 1]
        else:
            prev_tok = None

        if token.is_operand():
            if token.is_symbol_operand():
                #  Check the protected header.
                if protected_header_enabled and token.get_symbol().startswith(protected_header_prefix):
                    err = _cm_error.Error(
                        _mexp_errors.MEXP_USE_PROTECTED_HEADER,
                        _l10n_reg.get_message(
                            lang_id,
                            "parser.mexp.error.protected_header.description"
                        ),
                        options
                    )
                    err.push_traceback(
                        expression,
                        token.get_position(),
                        token.get_position() + len(token.get_symbol()) - 1,
                        _l10n_reg.get_message(
                            lang_id,
                            "parser.mexp.error.protected_header.message"
                        ),
                        replace_map={
                            "$1": protected_header_prefix
                        }
                    )
                    raise err

            if prev_tok is not None:
                if prev_tok.is_right_parenthesis():
                    if token.is_symbol_operand():
                        #  Do completion:
                        #    ([expr])[unknown] => ([expr])*[unknown]
                        #
                        #  For example:
                        #    (3-y)x => (3-y)*x
                        rpn.add_operator(_mexp_token.create_multiply_operator_token())
                    else:
                        #  Numeric parenthesis suffix was not supported.
                        #
                        #  For example:
                        #    (x-y)3
                        #         ^
                        #         Requires a '*' before this token.
                        err = _cm_error.Error(
                            _mexp_errors.MEXP_MISSING_OPERATOR,
                            _l10n_reg.get_message(
                                lang_id,
                                "parser.mexp.error.missing_operator.description"
                            ),
                            options
                        )
                        err.push_traceback(
                            expression,
                            token.get_position(),
                            token.get_position() + len(token.get_symbol()) - 1,
                            _l10n_reg.get_message(
                                lang_id,
                                "parser.mexp.error.missing_operator.multiply_before"
                            )
                        )
                        raise err

                if prev_tok.is_operand():
                    #  Do completion:
                    #    [number][symbol] => [number]*[symbol]
                    #
                    #  For example:
                    #    4x => 4*x
                    rpn.add_operator(_mexp_token.create_multiply_operator_token())

            #  Process the token.
            rpn.add_operand(token)

            #  Go to next token.
            token_id += 1

            continue
        elif token.is_function():
            #  Raise an error if the function is unsupported.
            if _mexp_functions.find_function(token.get_symbol()) is None:
                err = _cm_error.Error(
                    _mexp_errors.MEXP_FUNCTION_UNSUPPORTED,
                    _l10n_reg.get_message(
                        lang_id,
                        "parser.mexp.error.unsupported_function.description"
                    ),
                    options
                )
                err.push_traceback(
                    expression,
                    token.get_position(),
                    token.get_position() + len(token.get_symbol()) - 1,
                    _l10n_reg.get_message(
                        lang_id,
                        "parser.mexp.error.unsupported_function.message"
                    ),
                    replace_map={
                        "$1": token.get_symbol()
                    }
                )
                raise err

            if prev_tok is not None and (prev_tok.is_operand() or prev_tok.is_right_parenthesis()):
                #  Do completion:
                #    [num][fn] => [num]*[fn]
                #
                #  For example:
                #    4pow(2,3) => 4*pow(2,3)
                rpn.add_operator(_mexp_token.create_multiply_operator_token())

            #  Process the token.
            rpn.add_function(token)

            #  Go to next token.
            token_id += 1

            continue
        elif token.is_operator():
            #  Get the operator.
            op = _mexp_operators.OPERATORS[token.get_subtype()]

            #  Check operands.
            if op.is_required_left_operand():
                _check_left_operand(expression, token_list, token_id, options)

            if op.is_required_right_operand():
                _check_right_operand(expression, token_list, token_id, options)

            #  Process the token.
            rpn.add_operator(token)

            #  Go to next token.
            token_id += 1

            continue
        elif token.is_left_parenthesis():
            #  Save state.
            parenthesis_stack.push(_ParenthesisStackItem(
                token.get_symbol(),
                token_id,
                in_function,
                current_argc,
                required_argc,
                prev_separator_position
            ))

            current_argc = 0
            prev_separator_position = token_id

            #  Set function state and get required argument count.
            if prev_tok is not None and prev_tok.is_function():
                #  Mark the flag.
                in_function = True

                #  Get the function object.
                fn_object = _mexp_functions.find_function(prev_tok.get_symbol())
                if fn_object is None:
                    raise RuntimeError("BUG: Function object is None.")

                #  Get the required argument count.
                required_argc = fn_object.get_argument_count()
            else:
                #  Clear the flag.
                in_function = False
                required_argc = 0

            if prev_tok is not None and (prev_tok.is_right_parenthesis() or prev_tok.is_operand()):
                #  Do completion
                #    [lp][expr][rp][lp][expr][rp] => [lp][expr][rp]*[lp][expr][rp]
                #
                #  For example:
                #    (2+3)(4+2) => (2+3)*(4+2)
                rpn.add_operator(_mexp_token.create_multiply_operator_token())

            #  Process the token.
            rpn.add_left_parenthesis(token)

            #  Go to next token.
            token_id += 1

            continue
        elif token.is_right_parenthesis():
            #  Raise an error if there's no content between two separators.
            if prev_separator_position + 1 == token_id:
                err = _cm_error.Error(
                    _mexp_errors.MEXP_NO_CONTENT,
                    _l10n_reg.get_message(
                        lang_id,
                        "parser.mexp.error.no_content.description"
                    ),
                    options
                )
                if prev_tok.is_left_parenthesis():
                    err.push_traceback(
                        expression,
                        prev_tok.get_position(),
                        token.get_position(),
                        _l10n_reg.get_message(
                            lang_id,
                            "parser.mexp.error.no_content.in_parentheses"
                        )
                    )
                else:
                    err.push_traceback(
                        expression,
                        prev_tok.get_position(),
                        token.get_position(),
                        _l10n_reg.get_message(
                            lang_id,
                            "parser.mexp.error.no_content.in_argument"
                        )
                    )

                raise err

            #  Raise an error if there's no left parenthesis to be matched with.
            if len(parenthesis_stack) == 0:
                err = _cm_error.Error(
                    _mexp_errors.MEXP_PARENTHESIS_MISMATCH,
                    _l10n_reg.get_message(
                        lang_id,
                        "parser.mexp.error.parenthesis_mismatch.description"
                    ),
                    options
                )
                err.push_traceback(
                    expression,
                    token.get_position(),
                    token.get_position(),
                    _l10n_reg.get_message(
                        lang_id,
                        "parser.mexp.error.parenthesis_mismatch.left"
                    )
                )
                raise err

            #  Get the top item of the stack.
            p_item = parenthesis_stack.pop()

            #  Get the symbol of the parenthesis matches with current token.
            p_matched_sym = parenthesis_mapping[token.get_symbol()]

            #  Raise an error if the parenthesis was mismatched.
            if p_matched_sym != p_item.get_symbol():
                err = _cm_error.Error(
                    _mexp_errors.MEXP_PARENTHESIS_MISMATCH,
                    _l10n_reg.get_message(
                        lang_id,
                        "parser.mexp.error.parenthesis_mismatch.description"
                    ),
                    options
                )
                err.push_traceback(
                    expression,
                    token.get_position(),
                    token.get_position(),
                    _l10n_reg.get_message(
                        lang_id,
                        "parser.mexp.error.parenthesis_mismatch.incorrect"
                    ),
                    replace_map={
                        "$1": p_matched_sym
                    }
                )
                raise err

            if in_function:
                current_argc += 1

                #  Raise an error if the argument count was not matched.
                if current_argc != required_argc:
                    fn_token = token_list[p_item.get_token_id() - 1]

                    err = _cm_error.Error(
                        _mexp_errors.MEXP_FUNCTION_ARGUMENT_COUNT_MISMATCH,
                        _l10n_reg.get_message(
                            lang_id,
                            "parser.mexp.error.argument_count_mismatch.description"
                        ),
                        options
                    )
                    err.push_traceback(
                        expression,
                        fn_token.get_position(),
                        fn_token.get_position() + len(fn_token.get_symbol()) - 1,
                        _l10n_reg.get_message(
                            lang_id,
                            "parser.mexp.error.argument_count_mismatch.message"
                        ),
                        {
                            "$1": str(required_argc),
                            "$2": str(current_argc)
                        }
                    )
                    raise err

            #  Restore state.
            in_function = p_item.is_in_function()
            current_argc = p_item.get_current_argument_count()
            required_argc = p_item.get_required_argument_count()
            prev_separator_position = p_item.get_previous_separator_position()

            #  Process the token.
            rpn.add_right_parenthesis()

            #  Go to next token.
            token_id += 1

            continue
        elif token.is_separator():
            #  Raise an error if we're not in function now.
            if not in_function:
                err = _cm_error.Error(
                    _mexp_errors.MEXP_ILLEGAL_ARGUMENT_SEPARATOR,
                    _l10n_reg.get_message(
                        lang_id,
                        "parser.mexp.error.illegal_separator.description"
                    ),
                    options
                )
                err.push_traceback(
                    expression,
                    token.get_position(),
                    token.get_position(),
                    _l10n_reg.get_message(
                        lang_id,
                        "parser.mexp.error.illegal_separator.message"
                    )
                )
                raise err

            #  Raise an error if there's no content between two separators.
            if prev_separator_position + 1 == token_id:
                err = _cm_error.Error(
                    _mexp_errors.MEXP_NO_CONTENT,
                    _l10n_reg.get_message(
                        lang_id,
                        "parser.mexp.error.no_content.description"
                    ),
                    options
                )
                err.push_traceback(
                    expression,
                    prev_tok.get_position(),
                    token.get_position(),
                    _l10n_reg.get_message(
                        lang_id,
                        "parser.mexp.error.no_content.in_argument"
                    )
                )
                raise err

            #  Save separator position.
            prev_separator_position = token_id

            #  Increase argument counter.
            current_argc += 1

            #  Process the token.
            rpn.add_separator()

            #  Go to next token.
            token_id += 1

            continue
        else:
            raise RuntimeError("Never reach this condition.")

    #  Raise an error if there are still some left parentheses in the stack.
    if len(parenthesis_stack) != 0:
        err = _cm_error.Error(
            _mexp_errors.MEXP_PARENTHESIS_MISMATCH,
            _l10n_reg.get_message(
                lang_id,
                "parser.mexp.error.parenthesis_mismatch.description"
            ),
            options
        )
        while len(parenthesis_stack) != 0:
            p_item = parenthesis_stack.pop()
            p_token = token_list[p_item.get_token_id()]
            err.push_traceback(
                expression,
                p_token.get_position(),
                p_token.get_position(),
                _l10n_reg.get_message(
                    lang_id,
                    "parser.mexp.error.parenthesis_mismatch.right"
                )
            )
        raise err

    #  Pop all items off from the stack and push them onto the RPN token list.
    rpn.finalize()

    #  Return the RPN token list.
    return rpn.get_rpn()
