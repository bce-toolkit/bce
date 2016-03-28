#!/usr/bin/env python
#
#  Copyright 2014 - 2016 The BCE Authors. All rights reserved.
#  Use of this source code is governed by a BSD-style license that can be
#  found in the license.txt file.
#

import bce.locale.option as _l10n_opt
import bce.locale.registry as _l10n_reg


class Error(Exception):
    """Logic error."""

    def __init__(self, error_code, description, options):
        """Initialize the class with specific error code, description and
        detail note.

        :type error_code: str
        :type description: str
        :type options: bce.option.Option
        :param error_code: An integer that contains the error code.
        :param description: The description.
        :param options: The options.
        """

        self.__error_code = error_code
        self.__description = description
        self.__opt = options

    def get_error_code(self):
        """Get the error code.

        :rtype : str
        :return: The error code.
        """

        return self.__error_code

    def get_description(self):
        """Get the description.

        :rtype : str
        :return: The description.
        """

        return self.__description

    def to_string(self, left_margin=0, indent=4):
        """Present the error in a human-readable text.

        :type left_margin: int
        :type indent: int
        :param left_margin: The left margin value.
        :param indent: The indent value.
        :rtype : str
        :return: The formatted string.
        """

        #  Wrap the locale options.
        lang_id = _l10n_opt.OptionWrapper(self.__opt).get_language_id()

        #  Write header.
        s = " " * left_margin + _l10n_reg.get_message(
            lang_id,
            "logic.common.error.header",
            replace_map={
                "$1": self.get_error_code()
            }
        ) + "\n\n"

        #  Write description.
        s += " " * left_margin + _l10n_reg.get_message(
            lang_id,
            "logic.common.error.description"
        ) + "\n\n"
        s += " " * (left_margin + indent) + self.get_description()

        return s
