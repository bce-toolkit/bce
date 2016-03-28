#!/usr/bin/env python
#
#  Copyright 2014 - 2016 The BCE Authors. All rights reserved.
#  Use of this source code is governed by a BSD-style license that can be
#  found in the license.txt file.
#

import bce.parser.interface.option as _interface_opt
import bce.parser.molecule.implementation as _ml_impl
import bce.parser.molecule.l10n as _ml_l10n
import bce.parser.molecule.option as _ml_opt


def initialize_module():
    """Initialize the module."""

    #  Initialize the global option.
    _ml_opt.initialize_global_option()

    #  Setup the localization module.
    _ml_l10n.setup_localization()

    #  Register the parser implementation.
    _interface_opt.register_default_molecule_parser(_ml_impl.MoleculeParserImplementation())
