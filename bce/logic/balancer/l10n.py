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
            "balancer": {
                "error": {
                    "side_eliminated": {
                        "all": "All molecules in the chemical equation was eliminated.",
                        "left": "All molecules on the left side of the chemical equation was eliminated.",
                        "right": "All molecules on the right side of the chemical equation was eliminated."
                    },
                    "auto_arrange_with_multiple_answers": {
                        "description": "Can't balance chemical equations (with auto-correction form) that have " +
                                       "multiple answers."
                    },
                    "feature_disabled": {
                        "auto_arranging": "Auto-arranging feature has been disabled.",
                        "error_correction": "An correctable balancing error was found. But the error-correction " +
                                            "feature has been disabled."
                    }
                }
            }
        }
    }))

    #  Chinese-simplified translation.
    _l10n_reg.register_message_tree(_l10n_msgtree.ChineseSimplifiedMessageTree({
        "logic": {
            "balancer": {
                "error": {
                    "side_eliminated": {
                        "all": "该化学方程式中的所有分子都已被消去。",
                        "left": "该化学方程式中的等号左侧的所有分子都已被消去。",
                        "right": "该化学方程式中的等号右侧的所有分子都已被消去。"
                    },
                    "auto_arrange_with_multiple_answers": {
                        "description": "无法配平自动分界形式且包含多组解的化学方程式。"
                    },
                    "feature_disabled": {
                        "auto_arranging": "自动分界特性已被禁用。",
                        "error_correction": "发生了一个可纠正的配平错误，但纠错特性已被禁用。"
                    }
                }
            }
        }
    }))
