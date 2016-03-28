#!/usr/bin/env python
#
#  Copyright 2014 - 2016 The BCE Authors. All rights reserved.
#  Use of this source code is governed by a BSD-style license that can be
#  found in the license.txt file.
#

import bce.locale.initializer as _locale_init
import bce.logic.balancer.initializer as _logic_bce_init
import bce.logic.common.initializer as _logic_cm_init
import bce.parser.common.initializer as _parser_cm_init
import bce.parser.cexp.initializer as _parser_cexp_init
import bce.parser.mexp.initializer as _parser_mexp_init
import bce.parser.molecule.initializer as _parser_ml_init

#
#  Initialize all sub modules.
#

#  Initialize locale module.
_locale_init.initialize_module()

#  Initialize logic modules.
_logic_cm_init.initialize_module()
_logic_bce_init.initialize_module()

#  Initialize parser modules.
_parser_cm_init.initialize_module()
_parser_mexp_init.initialize_module()
_parser_ml_init.initialize_module()
_parser_cexp_init.initialize_module()
