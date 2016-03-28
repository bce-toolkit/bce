#!/usr/bin/env python
#
#  Copyright 2014 - 2016 The BCE Authors. All rights reserved.
#  Use of this source code is governed by a BSD-style license that can be
#  found in the license.txt file.
#

import copy as _copy

#  The option template.
_OPTION_TEMPLATE = {}


def register_option_pair(key, default_value):
    """Register an option pair (key => default value).

    :type key: str
    :param key: The option key.
    :param default_value: The default option value.
    """

    _OPTION_TEMPLATE[key] = default_value


class Option:
    """The option."""

    def __init__(self):
        """Initialize the object."""

        #  Copy options from the template.
        self.__opt = _copy.deepcopy(_OPTION_TEMPLATE)

    def has_option(self, key):
        """Get whether a key of an option is valid.

        :type key: str
        :param key: The option key.
        :return: True if so.
        """

        return key in self.__opt

    def __assert_option(self, key):
        """Assert a key of an option exists.

        :type key: str
        :param key: The option key.
        :raise KeyError: Raise this exception if the key is invalid.
        """

        if not self.has_option(key):
            raise KeyError("No such option.")

    def get_option_value(self, key):
        """Get the value of an option.

        :type key: str
        :param key: The option key.
        :return: The value of the option.
        """

        #  Check the key.
        self.__assert_option(key)

        #  Get and return the value.
        return self.__opt[key]

    def set_option_value(self, key, value):
        """Set the value of an option.

        :type key: str
        :param key: The option key.
        :param value: The option value.
        """

        #  Check the key.
        self.__assert_option(key)

        #  Set the value.
        self.__opt[key] = value
