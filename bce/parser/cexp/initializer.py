#!/usr/bin/env python
#
#  Copyright 2014 - 2016 The BCE Authors. All rights reserved.
#  Use of this source code is governed by a BSD-style license that can be
#  found in the license.txt file.
#

import bce.parser.cexp.implementation as _cexp_impl
import bce.parser.cexp.l10n as _cexp_l10n
import bce.parser.interface.option as _interface_opt


def initialize_module():
    """Initialize the module."""

    #  Setup the localization module.
    _cexp_l10n.setup_localization()

    #  Register the parser implementation.
    _interface_opt.register_default_cexp_parser(_cexp_impl.ChemicalEquationParserImplementation())
