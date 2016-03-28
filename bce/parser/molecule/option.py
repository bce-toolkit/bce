#!/usr/bin/env python
#
#  Copyright 2014 - 2016 The BCE Authors. All rights reserved.
#  Use of this source code is governed by a BSD-style license that can be
#  found in the license.txt file.
#

import bce.option as _opt

#  Option keys.
OPT_KEY_ABBREVIATION_MAPPING = "parser.molecule.abbreviation_mapping"


class OptionWrapper:
    """Option operations wrapper."""

    def __init__(self, opt):
        """Initialize the wrapper.

        :type opt: bce.option.Option
        :param opt: The option object.
        """

        self.__opt = opt

    def get_abbreviation_mapping(self):
        """Get the abbreviation mapping.

        :rtype : dict[str, str]
        :return: The mapping.
        """

        return self.__opt.get_option_value(OPT_KEY_ABBREVIATION_MAPPING)

    def set_abbreviation_mapping(self, mapping):
        """Set the abbreviation mapping.

        :type mapping: dict[str, str]
        :param mapping: The mapping.
        """

        self.__opt.set_option_value(OPT_KEY_ABBREVIATION_MAPPING, mapping)


def initialize_global_option():
    """Initialize global options."""

    _opt.register_option_pair(OPT_KEY_ABBREVIATION_MAPPING, {})
