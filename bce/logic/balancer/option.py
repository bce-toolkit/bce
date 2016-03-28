#!/usr/bin/env python
#
#  Copyright 2014 - 2016 The BCE Authors. All rights reserved.
#  Use of this source code is governed by a BSD-style license that can be
#  found in the license.txt file.
#

import bce.option as _opt

#  Option keys.
OPT_KEY_ERROR_CORRECTION_ENABLED = "logic.balancer.feature.error_correction"
OPT_KEY_AUTO_SIDE_ARRANGING_ENABLED = "logic.balancer.feature.auto_side_arrange"


class OptionWrapper:
    """Option operations wrapper."""

    def __init__(self, opt):
        """Initialize the wrapper.

        :type opt: bce.option.Option
        :param opt: The option object.
        """

        self.__opt = opt

    def enable_error_correction_feature(self, enabled=True):
        """Enable or disable the error-correction feature.

        :type enabled: bool
        :param enabled: True if the feature is to be enabled.
        """

        self.__opt.set_option_value(OPT_KEY_ERROR_CORRECTION_ENABLED, enabled)

    def is_error_correction_feature_enabled(self):
        """Get whether the error-correction feature is enabled.

        :rtype : bool
        :return: True if enabled.
        """

        return self.__opt.get_option_value(OPT_KEY_ERROR_CORRECTION_ENABLED)

    def enable_auto_side_arranging_feature(self, enabled=True):
        """Enable or disable the auto-side-arranging feature.

        :type enabled: bool
        :param enabled: True if the feature is to be enabled.
        """

        self.__opt.set_option_value(OPT_KEY_AUTO_SIDE_ARRANGING_ENABLED, enabled)

    def is_auto_side_arranging_feature_enabled(self):
        """Get whether the auto-side-arranging feature is enabled.

        :rtype : bool
        :return: True if enabled.
        """

        return self.__opt.get_option_value(OPT_KEY_AUTO_SIDE_ARRANGING_ENABLED)


def initialize_global_option():
    """Initialize global options."""

    _opt.register_option_pair(OPT_KEY_ERROR_CORRECTION_ENABLED, True)
    _opt.register_option_pair(OPT_KEY_AUTO_SIDE_ARRANGING_ENABLED, True)
