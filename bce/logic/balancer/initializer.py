#!/usr/bin/env python
#
#  Copyright 2014 - 2016 The BCE Authors. All rights reserved.
#  Use of this source code is governed by a BSD-style license that can be
#  found in the license.txt file.
#

import bce.logic.balancer.l10n as _l10n
import bce.logic.balancer.option as _option


def initialize_module():
    """Initialize the module."""

    #  Initialize the global option.
    _option.initialize_global_option()

    #  Setup the localization module.
    _l10n.setup_localization()
