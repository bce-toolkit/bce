#!/usr/bin/env python
#
#  Copyright 2014 - 2016 The BCE Authors. All rights reserved.
#  Use of this source code is governed by a BSD-style license that can be
#  found in the license.txt file.
#

import bce.locale.option as _l10n_opt
import bce.locale.registry as _l10n_reg
import bce.parser.common.token as _cm_token
import bce.parser.common.error as _cm_error
import bce.parser.interface.option as _interface_opt
import bce.parser.molecule.error as _ml_error
import sympy as _sympy

#  Token types.
TOKEN_TYPE_SYMBOL = 1
TOKEN_TYPE_OPERAND = 2
TOKEN_TYPE_HYDRATE_DOT = 3
TOKEN_TYPE_PARENTHESIS = 4
TOKEN_TYPE_ABBREVIATION = 5
TOKEN_TYPE_STATUS = 6
TOKEN_TYPE_ELECTRONIC = 7
TOKEN_TYPE_END = 8

#  Token sub-types.
#  (For operands)
TOKEN_SUBTYPE_INTEGER = 1
TOKEN_SUBTYPE_MEXP = 2

#  (For parentheses)
TOKEN_SUBTYPE_PARENTHESIS_LEFT = 1
TOKEN_SUBTYPE_PARENTHESIS_RIGHT = 2

#  (For status)
TOKEN_SUBTYPE_AQUEOUS = 1
TOKEN_SUBTYPE_GAS = 2
TOKEN_SUBTYPE_LIQUID = 3
TOKEN_SUBTYPE_SOLID = 4

#  (For electronics)
TOKEN_SUBTYPE_EL_BEGIN = 1
TOKEN_SUBTYPE_EL_END = 2
TOKEN_SUBTYPE_EL_FLAG_POSITIVE = 3
TOKEN_SUBTYPE_EL_FLAG_NEGATIVE = 4


class Token(_cm_token.TokenBase):
    """Token class for molecule."""

    def __init__(self, symbol, token_type, token_subtype=None, idx=-1, pos=-1):
        """Initialize the class.

        :type symbol: str
        :type token_type: int
        :type idx: int
        :type pos: int
        :param symbol: The symbol.
        :param token_type: The token type.
        :param token_subtype: The token sub-type.
        :param idx: The index.
        :param pos: The starting position.
        """

        self.__extra_pos = pos
        self.__extra_ev_mexp = None
        self.__extra_el = None
        _cm_token.TokenBase.__init__(self, symbol, token_type, token_subtype, idx)

    def get_position(self):
        """Get the starting position of the token in origin expression.

        :rtype : int
        :return: The position.
        """

        return self.__extra_pos

    def is_symbol(self):
        """Get whether the token is a symbol token.

        :rtype : bool
        :return: Return True if the token is a symbol token.
        """

        return self.get_type() == TOKEN_TYPE_SYMBOL

    def is_operand(self):
        """Get whether the token is an operand token.

        :rtype : bool
        :return: Return True if the token is an operand token.
        """

        return self.get_type() == TOKEN_TYPE_OPERAND

    def is_integer_operand(self):
        """Get whether the token is an integer operand token.

        :rtype : bool
        :return: Return True if the token is an integer operand token.
        """

        if not self.is_operand():
            return False

        return self.get_subtype() == TOKEN_SUBTYPE_INTEGER

    def is_mexp_operand(self):
        """Get whether the token is a MEXP operand token.

        :rtype : bool
        :return: Return True if the token is a MEXP operand token.
        """

        if not self.is_operand():
            return False

        return self.get_subtype() == TOKEN_SUBTYPE_MEXP

    def is_hydrate_dot(self):
        """Get whether the token is a dot token.

        :rtype : bool
        :return: Return True if the token is a dot token.
        """

        return self.get_type() == TOKEN_TYPE_HYDRATE_DOT

    def is_parenthesis(self):
        """Get whether the token is a parenthesis token.

        :rtype : bool
        :return: Return True if the token is a parenthesis token.
        """

        return self.get_type() == TOKEN_TYPE_PARENTHESIS

    def is_left_parenthesis(self):
        """Get whether the token is a left parenthesis token.

        :rtype : bool
        :return: Return True if the token is a left parenthesis token.
        """

        if not self.is_parenthesis():
            return False

        return self.get_subtype() == TOKEN_SUBTYPE_PARENTHESIS_LEFT

    def is_right_parenthesis(self):
        """Get whether the token is a right parenthesis token.

        :rtype : bool
        :return: Return True if the token is a right parenthesis token.
        """

        if not self.is_parenthesis():
            return False

        return self.get_subtype() == TOKEN_SUBTYPE_PARENTHESIS_RIGHT

    def is_abbreviation(self):
        """Get whether the token is an abbreviation token.

        :rtype : bool
        :return: Return True if the token is an abbreviation token.
        """

        return self.get_type() == TOKEN_TYPE_ABBREVIATION

    def set_evaluated_mexp(self, ev_value):
        """Set the evaluated MEXP value of this token.

        :param ev_value: The value.
        """

        self.__extra_ev_mexp = ev_value

    def get_evaluated_mexp(self):
        """Get the evaluated MEXP value of the token.

        :return: The value.
        """

        return self.__extra_ev_mexp

    def is_status(self):
        """Get whether the token is a status descriptor.

        :rtype : bool
        :return: Whether the token is a status descriptor.
        """

        return self.get_type() == TOKEN_TYPE_STATUS

    def is_aqueous_status(self):
        """Get whether the token is an aqueous status descriptor.

        :rtype : bool
        :return: Whether the token is an aqueous status descriptor.
        """

        if not self.is_status():
            return False

        return self.get_subtype() == TOKEN_SUBTYPE_AQUEOUS

    def is_gas_status(self):
        """Get whether the token is a gas status descriptor.

        :rtype : bool
        :return: Whether the token is a gas status descriptor.
        """

        if not self.is_status():
            return False

        return self.get_subtype() == TOKEN_SUBTYPE_GAS

    def is_liquid_status(self):
        """Get whether the token is a liquid status descriptor.

        :rtype : bool
        :return: Whether the token is a liquid status descriptor.
        """

        if not self.is_status():
            return False

        return self.get_subtype() == TOKEN_SUBTYPE_LIQUID

    def is_solid_status(self):
        """Get whether the token is a solid status descriptor.

        :rtype : bool
        :return: Whether the token is a solid status descriptor.
        """

        if not self.is_status():
            return False

        return self.get_subtype() == TOKEN_SUBTYPE_SOLID

    def is_electronic(self):
        """Get whether the token is an electronic token.

        :rtype : bool
        :return: True if so. Otherwise, return False.
        """

        return self.get_type() == TOKEN_TYPE_ELECTRONIC

    def get_operand_value(self):
        """Get the value of the operand token.

        :return: The value.
        """

        if self.is_mexp_operand():
            return self.get_evaluated_mexp()
        else:
            return _sympy.Integer(int(self.get_symbol()))

    def is_electronic_begin(self):
        """Get whether the token is an electronic begin parenthesis token.

        :rtype : bool
        :return: True if so. Otherwise, return False.
        """

        if not self.is_electronic():
            return False

        return self.get_subtype() == TOKEN_SUBTYPE_EL_BEGIN

    def is_electronic_end(self):
        """Get whether the token is an electronic end parenthesis token.

        :rtype : bool
        :return: True if so. Otherwise, return False.
        """

        if not self.is_electronic():
            return False

        return self.get_subtype() == TOKEN_SUBTYPE_EL_END

    def is_electronic_positive_flag(self):
        """Get whether the token is a positive electronic flag token.

        :rtype : bool
        :return: True if so. Otherwise, return False.
        """

        if not self.is_electronic():
            return False

        return self.get_subtype() == TOKEN_SUBTYPE_EL_FLAG_POSITIVE

    def is_electronic_negative_flag(self):
        """Get whether the token is a negative electronic flag token.

        :rtype : bool
        :return: True if so. Otherwise, return False.
        """

        if not self.is_electronic():
            return False

        return self.get_subtype() == TOKEN_SUBTYPE_EL_FLAG_NEGATIVE

    def is_end(self):
        """Get whether the token is an end token.

        :rtype : bool
        :return: True if so. Otherwise, return False.
        """

        return self.get_type() == TOKEN_TYPE_END

    def set_position(self, new_position):
        """Set the position.

        :param new_position: The new position.
        """

        self.__extra_pos = new_position


def create_symbol_token(symbol, idx=-1, pos=-1):
    """Create an atom symbol token.

    :type symbol: str
    :type idx: int
    :type pos: int
    :param symbol: The symbol.
    :param idx: The index.
    :param pos: The starting position.
    :rtype : Token
    :return: The created token.
    """

    return Token(symbol, TOKEN_TYPE_SYMBOL, None, idx, pos)


def create_integer_operand_token(symbol, idx=-1, pos=-1):
    """Create an integer token.

    :type symbol: str
    :type idx: int
    :type pos: int
    :param symbol: The symbol.
    :param idx: The index.
    :param pos: The starting position.
    :rtype : Token
    :return: The created token.
    """

    return Token(symbol, TOKEN_TYPE_OPERAND, TOKEN_SUBTYPE_INTEGER, idx, pos)


def create_mexp_operand_token(symbol, value, idx=-1, pos=-1):
    """Create a math expression token.

    :type symbol: str
    :type idx: int
    :type pos: int
    :param symbol: The symbol.
    :param value: The evaluated value of the expression.
    :param idx: The index.
    :param pos: The starting position.
    :rtype : Token
    :return: The created token.
    """

    r = Token(symbol, TOKEN_TYPE_OPERAND, TOKEN_SUBTYPE_MEXP, idx, pos)
    r.set_evaluated_mexp(value)

    return r


def create_hydrate_dot_token(idx=-1, pos=-1):
    """Create a dot token.

    :type idx: int
    :type pos: int
    :param idx: The index.
    :param pos: The starting position.
    :rtype : Token
    :return: The created token.
    """

    return Token(".", TOKEN_TYPE_HYDRATE_DOT, None, idx, pos)


def create_left_parenthesis_token(idx=-1, pos=-1):
    """Create a left parenthesis token.

    :type idx: int
    :type pos: int
    :param idx: The index.
    :param pos: The starting position.
    :rtype : Token
    :return: The created token.
    """

    return Token("(", TOKEN_TYPE_PARENTHESIS, TOKEN_SUBTYPE_PARENTHESIS_LEFT, idx, pos)


def create_right_parenthesis_token(idx=-1, pos=-1):
    """Create a right parenthesis token.

    :type idx: int
    :type pos: int
    :param idx: The index.
    :param pos: The starting position.
    :rtype : Token
    :return: The created token.
    """

    return Token(")", TOKEN_TYPE_PARENTHESIS, TOKEN_SUBTYPE_PARENTHESIS_RIGHT, idx, pos)


def create_abbreviation_token(symbol, idx=-1, pos=-1):
    """Create an abbreviation token.

    :type symbol: str
    :type idx: int
    :type pos: int
    :param symbol: The symbol.
    :param idx: The index.
    :param pos: The starting position.
    :rtype : Token
    :return: The created token.
    """

    return Token(symbol, TOKEN_TYPE_ABBREVIATION, None, idx, pos)


def create_aqueous_status_token(idx=-1, pos=-1):
    """Create an aqueous status descriptor token.

    :type idx: int
    :type pos: int
    :param idx: The index.
    :param pos: The starting position.
    :rtype : Token
    :return: The created token.
    """

    return Token("(aq)", TOKEN_TYPE_STATUS, TOKEN_SUBTYPE_AQUEOUS, idx, pos)


def create_gas_status_token(idx=-1, pos=-1):
    """Create a gas status descriptor.

    :type idx: int
    :type pos: int
    :param idx: The index.
    :param pos: The starting position.
    :rtype : Token
    :return: The created token.
    """

    return Token("(g)", TOKEN_TYPE_STATUS, TOKEN_SUBTYPE_GAS, idx, pos)


def create_liquid_status_token(idx=-1, pos=-1):
    """Create a liquid status descriptor token.

    :type idx: int
    :type pos: int
    :param idx: The index.
    :param pos: The starting position.
    :rtype : Token
    :return: The created token.
    """

    return Token("(l)", TOKEN_TYPE_STATUS, TOKEN_SUBTYPE_LIQUID, idx, pos)


def create_solid_status_token(idx=-1, pos=-1):
    """Create a solid status descriptor token.

    :type idx: int
    :type pos: int
    :param idx: The index.
    :param pos: The starting position.
    :rtype : Token
    :return: The created token.
    """

    return Token("(s)", TOKEN_TYPE_STATUS, TOKEN_SUBTYPE_SOLID, idx, pos)


def create_electronic_begin_token(idx=-1, pos=-1):
    """Create an electronic begin parenthesis token.

    :type idx: int
    :type pos: int
    :param idx: The index.
    :param pos: The starting position.
    :rtype : Token
    :return: The created token.
    """

    return Token("<", TOKEN_TYPE_ELECTRONIC, TOKEN_SUBTYPE_EL_BEGIN, idx, pos)


def create_end_token(idx=-1, pos=-1):
    """Create an end token.

    :type idx: int
    :type pos: int
    :param idx: The index.
    :param pos: The position.
    :rtype : Token
    :return: The created token.
    """

    return Token("", TOKEN_TYPE_END, None, idx, pos)


def create_electronic_end_token(idx=-1, pos=-1):
    """Create an electronic end parenthesis token.

    :type idx: int
    :type pos: int
    :param idx: The index.
    :param pos: The starting position.
    :rtype : Token
    :return: The created token.
    """

    return Token(">", TOKEN_TYPE_ELECTRONIC, TOKEN_SUBTYPE_EL_END, idx, pos)


def create_positive_electronic_flag_token(idx=-1, pos=-1):
    """Create a positive electronic flag token.

    :type idx: int
    :type pos: int
    :param idx: The index.
    :param pos: The starting position.
    :rtype : Token
    :return: The created token.
    """

    return Token("e+", TOKEN_TYPE_ELECTRONIC, TOKEN_SUBTYPE_EL_FLAG_POSITIVE, idx, pos)


def create_negative_electronic_flag_token(idx=-1, pos=-1):
    """Create a negative electronic flag token.

    :type idx: int
    :type pos: int
    :param idx: The index.
    :param pos: The starting position.
    :rtype : Token
    :return: The created token.
    """

    return Token("e-", TOKEN_TYPE_ELECTRONIC, TOKEN_SUBTYPE_EL_FLAG_NEGATIVE, idx, pos)


def tokenize(expression, options, mexp_protected_header_enabled=False, mexp_protected_header_prefix="X"):
    """Tokenize a molecule expression.

    :type expression: str
    :type options: bce.option.Option
    :type mexp_protected_header_enabled: bool
    :type mexp_protected_header_prefix: str
    :param expression: The expression.
    :param options: The options.
    :param mexp_protected_header_enabled: Whether the MEXP protected headers are enabled.
    :param mexp_protected_header_prefix: The prefix of the MEXP protected headers.
    :rtype : list[Token]
    :return: The token list.
    :raise bce.parser.common.error.Error: Raise when a parser error occurred.
    """

    #  Initialize.
    lang_id = _l10n_opt.OptionWrapper(options).get_language_id()
    if_opt = _interface_opt.OptionWrapper(options)
    result = []
    cur_pos = 0
    end_pos = len(expression)

    while cur_pos < end_pos:
        cur_ch = expression[cur_pos]

        #  Read a integer token if current character is a digit.
        if cur_ch.isdigit():
            #  Search for the next non-digit character.
            search_pos = cur_pos + 1
            search_end = end_pos

            while search_pos < end_pos:
                search_ch = expression[search_pos]

                if not search_ch.isdigit():
                    search_end = search_pos
                    break

                #  Go to next searching position.
                search_pos += 1

            #  Create an integer token.
            result.append(create_integer_operand_token(expression[cur_pos:search_end], len(result), cur_pos))

            #  Go to next position.
            cur_pos = search_end

            continue

        #  Read an atom symbol if current character is a upper-case alphabet.
        if cur_ch.isupper():
            #  Search for next non-lower-case character.
            search_pos = cur_pos + 1
            search_end = end_pos

            while search_pos < end_pos:
                if not expression[search_pos].islower():
                    search_end = search_pos
                    break

                #  Go to next searching position.
                search_pos += 1

            #  Create a symbol token.
            result.append(create_symbol_token(expression[cur_pos:search_end], len(result), cur_pos))

            #  Go to next position.
            cur_pos = search_end

            continue

        #  Read a hydrate-dot token if current character is a dot.
        if cur_ch == ".":
            #  Create a dot token.
            result.append(create_hydrate_dot_token(len(result), cur_pos))

            #  Go to next position.
            cur_pos += 1

            continue

        if expression.startswith("(g)", cur_pos):
            #  Create a status descriptor token.
            result.append(create_gas_status_token(len(result), cur_pos))

            #  Go to next position.
            cur_pos += 3

            continue

        if expression.startswith("(l)", cur_pos):
            #  Create a status descriptor token.
            result.append(create_liquid_status_token(len(result), cur_pos))

            #  Go to next position.
            cur_pos += 3

            continue

        if expression.startswith("(s)", cur_pos):
            #  Create a status descriptor token.
            result.append(create_solid_status_token(len(result), cur_pos))

            #  Go to next position.
            cur_pos += 3

            continue

        if expression.startswith("(aq)", cur_pos):
            #  Create a status descriptor token.
            result.append(create_aqueous_status_token(len(result), cur_pos))

            #  Go to next position.
            cur_pos += 4

            continue

        #  Read a normal left parenthesis if current character is '('.
        if cur_ch == "(":
            #  Create a left parenthesis token.
            result.append(create_left_parenthesis_token(len(result), cur_pos))

            #  Go to next position.
            cur_pos += 1

            continue

        #  Read a normal right parenthesis if current character is ')'.
        if cur_ch == ")":
            #  Create a right parenthesis token.
            result.append(create_right_parenthesis_token(len(result), cur_pos))

            #  Go to next position.
            cur_pos += 1

            continue

        #  Read a abbreviation if current character is '['.
        if cur_ch == "[":
            #  Find the ']'.
            search_end = -1
            search_pos = cur_pos + 1

            while search_pos < end_pos:
                if expression[search_pos] == "]":
                    search_end = search_pos + 1
                    break

                #  Go to next searching position.
                search_pos += 1

            #  Raise an error if we can't find the ']'.
            if search_end == -1:
                err = _cm_error.Error(
                    _ml_error.MOLECULE_PARENTHESIS_MISMATCH,
                    _l10n_reg.get_message(
                        lang_id,
                        "parser.molecule.error.parenthesis_mismatch.description"
                    ),
                    options
                )
                err.push_traceback(
                    expression,
                    cur_pos,
                    cur_pos,
                    _l10n_reg.get_message(
                        lang_id,
                        "parser.molecule.error.parenthesis_mismatch.right"
                    )
                )
                raise err

            #  Create an abbreviation token.
            result.append(create_abbreviation_token(expression[cur_pos:search_end], len(result), cur_pos))

            #  Go to next position.
            cur_pos = search_end

            continue

        #  Read a math expression if current character is '{'.
        if cur_ch == "{":
            #  Simulate a parenthesis stack to find the end '}'.
            p_mexp = 0

            #  Searching the end '}'.
            search_end = -1
            search_pos = cur_pos + 1

            while search_pos < end_pos:
                search_ch = expression[search_pos]

                if search_ch == "(" or search_ch == "[" or search_ch == "{":
                    #  If current character is a left parenthesis, push it onto the stack.
                    p_mexp += 1
                elif search_ch == ")" or search_ch == "]" or search_ch == "}":
                    #  When we meet a right parenthesis and there's no left parenthesis in the stack.
                    #  The parenthesis we met should be the end '}'.
                    if p_mexp == 0:
                        #  Raise an error if the parenthesis isn't '}'.
                        if search_ch != "}":
                            err = _cm_error.Error(
                                _ml_error.MOLECULE_PARENTHESIS_MISMATCH,
                                _l10n_reg.get_message(
                                    lang_id,
                                    "parser.molecule.error.parenthesis_mismatch.description"
                                ),
                                options
                            )
                            err.push_traceback(
                                expression,
                                search_pos,
                                search_pos,
                                _l10n_reg.get_message(
                                    lang_id,
                                    "parser.molecule.error.parenthesis_mismatch.incorrect",
                                    replace_map={
                                        "$1": "}"
                                    }
                                )
                            )
                            raise err

                        #  Set the end position.
                        search_end = search_pos + 1

                        break

                    #  Pop the parenthesis off from the stack.
                    p_mexp -= 1
                else:
                    pass

                #  Go to next searching position.
                search_pos += 1

            #  Raise an error if we can't find the end '}'.
            if search_end == -1:
                err = _cm_error.Error(
                    _ml_error.MOLECULE_PARENTHESIS_MISMATCH,
                    _l10n_reg.get_message(
                        lang_id,
                        "parser.molecule.error.parenthesis_mismatch.description"
                    ),
                    options
                )
                err.push_traceback(
                    expression,
                    cur_pos,
                    cur_pos,
                    _l10n_reg.get_message(
                        lang_id,
                        "parser.molecule.error.parenthesis_mismatch.right"
                    )
                )
                raise err

            #  Raise an error if the math expression has no content.
            if cur_pos + 2 == search_end:
                err = _cm_error.Error(
                    _ml_error.MOLECULE_NO_CONTENT,
                    _l10n_reg.get_message(
                        lang_id,
                        "parser.molecule.error.no_content.description"
                    ),
                    options
                )
                err.push_traceback(
                    expression,
                    cur_pos,
                    cur_pos + 1,
                    _l10n_reg.get_message(
                        lang_id,
                        "parser.molecule.error.no_content.inside"
                    )
                )
                raise err

            #  Get the expression.
            mexp_expr = expression[cur_pos:search_end]

            #  Evaluate the expression.
            try:
                ev_value = if_opt.get_mexp_parser().parse(
                    mexp_expr,
                    options,
                    protected_header_enabled=mexp_protected_header_enabled,
                    protected_header_prefix=mexp_protected_header_prefix
                )
            except _cm_error.Error as err:
                err.push_traceback(
                    expression,
                    cur_pos,
                    search_end - 1,
                    _l10n_reg.get_message(
                        lang_id,
                        "parser.molecule.error.parsing_mexp.message"
                    )
                )
                raise err

            #  Create a math expression token.
            result.append(create_mexp_operand_token(mexp_expr, ev_value, len(result), cur_pos))

            #  Go to next position.
            cur_pos = search_end

            continue

        if cur_ch == "<":
            #  Create an electronic begin parenthesis token.
            result.append(create_electronic_begin_token(len(result), cur_pos))

            #  Go to next position.
            cur_pos += 1

            continue

        if cur_ch == ">":
            #  Create an electronic begin parenthesis token.
            result.append(create_electronic_end_token(len(result), cur_pos))

            #  Go to next position.
            cur_pos += 1

            continue

        if expression.startswith("e+", cur_pos):
            #  Create a positive electronic flag token.
            result.append(create_positive_electronic_flag_token(len(result), cur_pos))

            #  Go to next position.
            cur_pos += 2

            continue

        if expression.startswith("e-", cur_pos):
            #  Create a negative electronic flag token.
            result.append(create_negative_electronic_flag_token(len(result), cur_pos))

            #  Go to next position.
            cur_pos += 2

            continue

        #  Raise an error if current character can't be tokenized.
        err = _cm_error.Error(
            _ml_error.MOLECULE_UNRECOGNIZED_TOKEN,
            _l10n_reg.get_message(
                lang_id,
                "parser.molecule.error.unrecognized_token.description"
            ),
            options
        )
        err.push_traceback(
            expression,
            cur_pos,
            cur_pos,
            _l10n_reg.get_message(
                lang_id,
                "parser.molecule.error.unrecognized_token.message"
            )
        )
        raise err

    #  Add an end token.
    result.append(create_end_token(len(result), len(expression)))

    return result
