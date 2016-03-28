#!/usr/bin/env python
#
#  Copyright 2014 - 2016 The BCE Authors. All rights reserved.
#  Use of this source code is governed by a BSD-style license that can be
#  found in the license.txt file.
#

import bce.parser.interface.option as _interface_opt
import bce.parser.mexp.implementation as _mexp_impl
import bce.parser.mexp.l10n as _mexp_l10n


def initialize_module():
    """Initialize the module."""

    #  Setup the localization module.
    _mexp_l10n.setup_localization()

    #  Register the parser implementation.
    _interface_opt.register_default_mexp_parser(_mexp_impl.MathExpressionParserImplementation())
