#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Copyright 2014 - 2016 The BCE Authors. All rights reserved.
#  Use of this source code is governed by a BSD-style license that can be
#  found in the license.txt file.
#

import bce.locale.registry as _l10n_reg
import bce.locale.tree as _l10n_msgtree


def setup_localization():
    """Setup localization messages."""

    #  English translation.
    _l10n_reg.register_message_tree(_l10n_msgtree.EnglishMessageTree({
        "logic": {
            "common": {
                "error": {
                    "header": "A logic error occurred (Code: $1):",
                    "description": "Description:"
                }
            }
        }
    }))

    #  Chinese-simplified translation.
    _l10n_reg.register_message_tree(_l10n_msgtree.ChineseSimplifiedMessageTree({
        "logic": {
            "common": {
                "error": {
                    "header": "逻辑错误 (错误代码: $1):",
                    "description": "错取解释："
                }
            }
        }
    }))
