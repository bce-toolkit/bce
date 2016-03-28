#!/usr/bin/env python
#
#  Copyright 2014 - 2016 The BCE Authors. All rights reserved.
#  Use of this source code is governed by a BSD-style license that can be
#  found in the license.txt file.
#

import bce.base.stack as _adt_stack
import bce.locale.option as _l10n_opt
import bce.locale.registry as _l10n_reg
import bce.parser.cexp.error as _ce_error
import bce.parser.common.error as _cm_error
import bce.parser.common.token as _cm_token

#  Token types.
TOKEN_TYPE_OPERATOR = 1
TOKEN_TYPE_EQUAL = 2
TOKEN_TYPE_MOLECULE = 3
TOKEN_TYPE_END = 4

#  Token sub-types.
TOKEN_SUBTYPE_OPERATOR_PLUS = 1
TOKEN_SUBTYPE_OPERATOR_MINUS = 2
TOKEN_SUBTYPE_OPERATOR_SEPARATOR = 3


class Token(_cm_token.TokenBase):
    """Token class for chemical equation."""

    def __init__(self, symbol, token_type, token_subtype=None, idx=-1, pos=-1):
        """Initialize the token.

        :type symbol: str
        :type token_type: int
        :type idx: int
        :type pos: int
        :param symbol: The symbol.
        :param token_type: The token type (one of TOKEN_TYPE_*).
        :param token_subtype: The token sub-type (one of TOKEN_SUBTYPE_*).
        :param idx: The index.
        :param pos: The starting position.
        """

        self.__extra_pos = pos
        _cm_token.TokenBase.__init__(self, symbol, token_type, token_subtype, idx)

    def get_position(self):
        """Get the starting position of the token.

        :rtype : int
        :return: The starting position.
        """

        return self.__extra_pos

    def is_operator(self):
        """Get whether the token is an operator token.

        :rtype : bool
        :return: Return True if so.
        """

        return self.get_type() == TOKEN_TYPE_OPERATOR

    def is_operator_plus(self):
        """Get whether the token is a plus operator token.

        :rtype : bool
        :return: Return True if so.
        """

        if not self.is_operator():
            return False

        return self.get_subtype() == TOKEN_SUBTYPE_OPERATOR_PLUS

    def is_operator_minus(self):
        """Get whether the token is a minus operator token.

        :rtype : bool
        :return: Return True if so.
        """

        if not self.is_operator():
            return False

        return self.get_subtype() == TOKEN_SUBTYPE_OPERATOR_MINUS

    def is_operator_separator(self):
        """Get whether the token is a separator operator token.

        :rtype : bool
        :return: Return True if so.
        """

        if not self.is_operator():
            return False
        return self.get_subtype() == TOKEN_SUBTYPE_OPERATOR_SEPARATOR

    def is_equal(self):
        """Get whether the token is an equal('=') token.

        :rtype : bool
        :return: Return True if so.
        """

        return self.get_type() == TOKEN_TYPE_EQUAL

    def is_molecule(self):
        """Get whether the token is a molecule token.

        :rtype : bool
        :return: Return True if so.
        """

        return self.get_type() == TOKEN_TYPE_MOLECULE

    def is_end(self):
        """Get whether the token is an end token.

        :rtype : bool
        :return: Return True if so.
        """

        return self.get_type() == TOKEN_TYPE_END


def create_operator_plus_token(idx=-1, pos=-1):
    """Create a plus operator token.

    :type idx: int
    :type pos: int
    :param idx: The index.
    :param pos: The starting position.
    :rtype : Token
    :return: The created token.
    """

    return Token("+", TOKEN_TYPE_OPERATOR, TOKEN_SUBTYPE_OPERATOR_PLUS, idx, pos)


def create_operator_minus_token(idx=-1, pos=-1):
    """Create a minus operator token.

    :type idx: int
    :type pos: int
    :param idx: The index.
    :param pos: The starting position.
    :rtype : Token
    :return: The created token.
    """

    return Token("-", TOKEN_TYPE_OPERATOR, TOKEN_SUBTYPE_OPERATOR_MINUS, idx, pos)


def create_operator_separator_token(idx=-1, pos=-1):
    """Create a separator operator token.

    :type idx: int
    :type pos: int
    :param idx: The index.
    :param pos: The starting position.
    :rtype : Token
    :return: The created token.
    """

    return Token(";", TOKEN_TYPE_OPERATOR, TOKEN_SUBTYPE_OPERATOR_SEPARATOR, idx, pos)


def create_equal_token(idx=-1, pos=-1):
    """Create an equal operator token.

    :type idx: int
    :type pos: int
    :param idx: The index.
    :param pos: The starting position.
    :rtype : Token
    :return: The created token.
    """

    return Token("=", TOKEN_TYPE_EQUAL, None, idx, pos)


def create_molecule_token(symbol, idx=-1, pos=-1):
    """Create a molecule token.

    :type symbol: str
    :type idx: int
    :type pos: int
    :param symbol: The symbol.
    :param idx: The index.
    :param pos: The starting position.
    :rtype : Token
    :return: The created token.
    """

    return Token(symbol, TOKEN_TYPE_MOLECULE, None, idx, pos)


def create_end_token(idx=-1, pos=-1):
    """Create an end token.

    :type idx: int
    :type pos: int
    :param idx: The index.
    :param pos: The starting position.
    :rtype : Token
    :return: The created token.
    """

    return Token("", TOKEN_TYPE_END, None, idx, pos)


def tokenize(expression, options):
    """Tokenize a chemical equation.

    :type expression: str
    :type options: bce.option.Option
    :param expression: The chemical equation.
    :param options: The options.
    :rtype : list[Token]
    :return: The token list.
    """

    #  Get the language ID.
    lang_id = _l10n_opt.OptionWrapper(options).get_language_id()

    #  Initialize the result container.
    result = []

    #  Initialize the cursor.
    cursor = 0

    while cursor < len(expression):
        #  Get current character.
        cur_ch = expression[cursor]
        if cur_ch == "+":
            #  Add a plus token.
            result.append(create_operator_plus_token(len(result), cursor))

            #  Next position.
            cursor += 1
        elif cur_ch == "-":
            #  Add a minus token.
            result.append(create_operator_minus_token(len(result), cursor))

            #  Next position.
            cursor += 1
        elif cur_ch == ";":
            #  Add a separator token.
            result.append(create_operator_separator_token(len(result), cursor))

            #  Next position.
            cursor += 1
        elif cur_ch == "=":
            #  Add an equal sign token.
            result.append(create_equal_token(len(result), cursor))

            #  Next position.
            cursor += 1
        else:
            #  Initialize the stack.
            pm = _adt_stack.Stack()

            #  Initialize the searching cursor.
            search_pos = cursor

            #  Initialize the molecule symbol.
            molecule_symbol = ""

            while search_pos < len(expression):
                #  Get current character.
                search_ch = expression[search_pos]

                if search_ch in ["(", "[", "{", "<"]:
                    #  Emulate pushing operation.
                    pm.push(search_pos)

                    #  Add the character.
                    molecule_symbol += search_ch
                elif search_ch in [")", "]", "}", ">"]:
                    #  Raise an error if there is no left parenthesis in the stack.
                    if len(pm) == 0:
                        err = _cm_error.Error(
                            _ce_error.CEXP_PARENTHESIS_MISMATCH,
                            _l10n_reg.get_message(
                                lang_id,
                                "parser.cexp.error.parenthesis_mismatch.description"
                            ),
                            options
                        )
                        err.push_traceback(
                            expression,
                            search_pos,
                            search_pos,
                            _l10n_reg.get_message(
                                lang_id,
                                "parser.cexp.error.parenthesis_mismatch.left"
                            )
                        )
                        raise err

                    #  Emulate popping operation.
                    pm.pop()

                    #  Add the character.
                    molecule_symbol += search_ch
                elif search_ch in ["+", "-", ";", "="] and len(pm) == 0:
                    break
                else:
                    #  Add the character.
                    molecule_symbol += search_ch

                #  Move the searching cursor.
                search_pos += 1

            #  Raise an error if there are still some parentheses in the stack.
            if len(pm) != 0:
                err = _cm_error.Error(
                    _ce_error.CEXP_PARENTHESIS_MISMATCH,
                    _l10n_reg.get_message(
                        lang_id,
                        "parser.cexp.error.parenthesis_mismatch.description"
                    ),
                    options
                )

                while len(pm) != 0:
                    mismatched_pos = pm.pop()
                    err.push_traceback(
                        expression,
                        mismatched_pos,
                        mismatched_pos,
                        _l10n_reg.get_message(
                            lang_id,
                            "parser.cexp.error.parenthesis_mismatch.right"
                        )
                    )

                raise err

            #  Add a molecule token.
            result.append(create_molecule_token(molecule_symbol, len(result), cursor))

            #  Set the cursor.
            cursor = search_pos

    #  Add an end token.
    result.append(create_end_token(len(result), len(expression)))

    return result
