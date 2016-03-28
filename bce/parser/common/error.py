#!/usr/bin/env python
#
#  Copyright 2014 - 2016 The BCE Authors. All rights reserved.
#  Use of this source code is governed by a BSD-style license that can be
#  found in the license.txt file.
#

import bce.locale.option as _l10n_opt
import bce.locale.registry as _l10n_reg


class TracebackItem:
    """Traceback description container class."""

    def __init__(self, expression, start_pos, end_pos, text):
        """Initialize the class.

        :type expression: str
        :type start_pos: int
        :type end_pos: int
        :type text: str
        :param expression: The expression.
        :param start_pos: The starting position.
        :param end_pos: The end position.
        :param text: The error message.
        """

        self.__expr = expression
        self.__s_pos = start_pos
        self.__e_pos = end_pos
        self.__txt = text

    def get_expression(self):
        """Get the expression.

        :rtype : str
        :return: The expression.
        """

        return self.__expr

    def get_start_position(self):
        """Get the starting position.

        :rtype : int
        :return: The position.
        """

        return self.__s_pos

    def get_end_position(self):
        """Get the ending position.

        :rtype : int
        :return: The position.
        """

        return self.__e_pos

    def get_text(self):
        """Get the error message text.

        :rtype : str
        :return: The text.
        """

        return self.__txt

    def to_string(self, left_margin=0, underline_char="^"):
        """Convert the item to human-readable form(string).

        :type left_margin: int
        :type underline_char: str
        :param left_margin: The count of left margin spaces.
        :param underline_char: The underline character.
        :return: The converted string.
        """

        left_margin_str = " " * left_margin
        start_pos_margin_str = " " * self.__s_pos

        return "%s%s\n%s%s%s\n%s%s%s" % (
            left_margin_str,
            self.__expr,
            left_margin_str,
            start_pos_margin_str,
            underline_char * (self.__e_pos - self.__s_pos + 1),
            left_margin_str,
            start_pos_margin_str,
            self.__txt
        )


class Error(Exception):
    """Parser error class."""

    def __init__(self, error_code, description, options):
        """Initialize the class with specific error code and description.

        :type error_code: str
        :type description: str
        :type options: bce.option.Option
        :param error_code: The error code.
        :param description: The description.
        :param options: The options.
        """

        self.__err_code = error_code
        self.__description = description
        self.__traceback = []
        self.__opt = options

    def get_error_code(self):
        """Get the error code.

        :rtype : str
        :return: The error code.
        """

        return self.__err_code

    def get_description(self):
        """Get the description.

        :rtype : str
        :return: The description.
        """

        return self.__description

    def get_traceback_count(self):
        """Get the count of traceback items.

        :rtype : int
        :return: The count.
        """

        return len(self.__traceback)

    def push_traceback_raw(self, item):
        """Push a traceback item onto the stack.

        :type item: TracebackItem
        :param item: The traceback item.
        """

        self.__traceback.append(item)

    def push_traceback(self, expression, start_pos, end_pos, msg, replace_map=None):
        """Create an instance of TracebackItem class with specified arguments and
        push the item onto the stack.

        :type expression: str
        :type start_pos: int
        :type end_pos: int
        :type msg: str
        :type replace_map: dict | None
        :param expression: The expression.
        :param start_pos: The starting position.
        :param end_pos: The end position.
        :param msg: The message.
        :param replace_map: The replace map.
        """

        if replace_map is None:
            replace_map = {}

        #  Push.
        self.push_traceback_raw(TracebackItem(
            expression,
            start_pos,
            end_pos,
            _l10n_reg.apply_replace_map(msg, replace_map)
        ))

    def pop_traceback(self):
        """Pop off a item from the traceback stack and return it.

        :rtype : TracebackItem
        :return: The top item of the stack.
        """

        return self.__traceback.pop()

    def to_string(self, left_margin=0, indent=4):
        """Present the error in a human-readable form(string).

        :type left_margin: int
        :type indent: int
        :param left_margin: The left margin value.
        :param indent: The indent spaces count.
        :rtype : str
        :return: The formatted string.
        """

        #  Get the language ID.
        lang_id = _l10n_opt.OptionWrapper(self.__opt).get_language_id()

        #  Write header.
        s = " " * left_margin + _l10n_reg.get_message(
            lang_id,
            "parser.common.error.header",
            replace_map={
                "$1": self.get_error_code()
            }
        ) + "\n\n"

        #  Write description.
        s += " " * left_margin + _l10n_reg.get_message(
            lang_id,
            "parser.common.error.description"
        ) + "\n\n"
        s += " " * (left_margin + indent) + self.__description

        #  Write traceback items if have.
        if len(self.__traceback) != 0:
            #  Write traceback header.
            s += "\n\n" + " " * left_margin + _l10n_reg.get_message(
                lang_id,
                "parser.common.error.traceback"
            )

            #  Write all traceback items.
            i = len(self.__traceback) - 1
            while i >= 0:
                s += "\n\n" + self.__traceback[i].to_string(left_margin + indent, "^")
                i -= 1

        return s
