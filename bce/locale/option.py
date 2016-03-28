#!/usr/bin/env python
#
#  Copyright 2014 - 2016 The BCE Authors. All rights reserved.
#  Use of this source code is governed by a BSD-style license that can be
#  found in the license.txt file.
#

import bce.option as _opt
import locale as _locale

#  Option keys.
OPT_KEY_LOCALE_LANGUAGE_ID = "locale.language_id"


class OptionWrapper:
    """Option operations wrapper."""

    def __init__(self, opt):
        """Initialize the wrapper.

        :type opt: bce.option.Option
        :param opt: The option object.
        """

        self.__opt = opt

    def get_language_id(self):
        """Get the language ID.

        :rtype : str
        :return: The ID.
        """

        return self.__opt.get_option_value(OPT_KEY_LOCALE_LANGUAGE_ID)

    def set_language_id(self, language_id):
        """Set the language ID.

        :type language_id: str
        :param language_id: The ID.
        """

        self.__opt.set_option_value(OPT_KEY_LOCALE_LANGUAGE_ID, language_id)


def initialize_global_option():
    """Initialize global options."""

    _opt.register_option_pair(OPT_KEY_LOCALE_LANGUAGE_ID, _locale.getdefaultlocale()[0])
