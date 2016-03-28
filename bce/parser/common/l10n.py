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
        "parser": {
            "common": {
                "error": {
                    "header": "A parser error occurred (Code: $1):",
                    "description": "Description:",
                    "traceback": "Traceback:"
                }
            }
        }
    }))

    #  Chinese-simplified translation.
    _l10n_reg.register_message_tree(_l10n_msgtree.ChineseSimplifiedMessageTree({
        "parser": {
            "common": {
                "error": {
                    "header": "解释表达式发生错误 (错误代码: $1):",
                    "description": "错取解释：",
                    "traceback": "错误追踪："
                }
            }
        }
    }))
