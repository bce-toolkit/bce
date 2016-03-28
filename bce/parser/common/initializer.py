#!/usr/bin/env python
#
#  Copyright 2014 - 2016 The BCE Authors. All rights reserved.
#  Use of this source code is governed by a BSD-style license that can be
#  found in the license.txt file.
#

import bce.parser.common.l10n as _l10n


def initialize_module():
    """Initialize the module."""

    _l10n.setup_localization()
