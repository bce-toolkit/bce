#!/usr/bin/env python
#
#  Copyright 2014 - 2016 The BCE Authors. All rights reserved.
#  Use of this source code is governed by a BSD-style license that can be
#  found in the license.txt file.
#


class TokenBase:
    """Basic token class."""

    def __init__(self, symbol, token_type, token_subtype, idx):
        """Initialize the object.

        :type symbol: str
        :type token_type: int
        :type token_subtype: int
        :type idx: int
        :param symbol: The symbol.
        :param token_type: The token type.
        :param token_subtype: The token sub-type.
        :param idx: The index.
        """

        self.__sym = symbol
        self.__type = token_type
        self.__subtype = token_subtype
        self.__idx = idx

    def get_symbol(self):
        """Get the symbol.

        :rtype : str
        :return: The symbol.
        """

        return self.__sym

    def get_type(self):
        """Get the token type.

        :rtype : int
        :return: The token type.
        """

        return self.__type

    def get_subtype(self):
        """Get the token sub-type.

        :rtype : int
        :return: The token sub-type.
        """

        return self.__subtype

    def get_index(self):
        """Get the index.

        :rtype : int
        :return: The index.
        """

        return self.__idx

    def set_index(self, new_index):
        """Set the index.

        :param new_index: The new index.
        """

        self.__idx = new_index


def untokenize(token_list):
    """Untokenize a token list to its origin expression.

    :type token_list: list[TokenBase]
    :param token_list: The token list.
    :rtype : str
    :return: The origin expression.
    """

    #  Initialize the expression.
    expr = ""

    #  Append the symbol of each item of the token list.
    for token in token_list:
        expr += token.get_symbol()

    return expr
