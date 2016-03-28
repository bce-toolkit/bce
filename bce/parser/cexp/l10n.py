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
            "cexp": {
                "error": {
                    "parenthesis_mismatch": {
                        "description": "Parenthesis mismatch.",
                        "left": "Missing left parenthesis matches with this parenthesis.",
                        "right": "Missing right parenthesis matches with this parenthesis."
                    },
                    "mixed_form": {
                        "description": "Mixed form.",
                        "message": "The chemical equation mixed normal form and auto-arranging form."
                    },
                    "empty_expression": {
                        "description": "Empty expression."
                    },
                    "no_content": {
                        "description": "No content.",
                        "operator_between": "There is no content between these two operators.",
                        "operator_before": "There is no content before this operator.",
                        "operator_after": "There is no content after this operator."
                    },
                    "parsing_molecule": {
                        "message": "An error occurred when parsing the molecule."
                    },
                    "duplicated_equal_sign": {
                        "description": "Duplicated equal sign.",
                        "previous": "Here's the previous equal sign.",
                        "duplicated": "Here's the duplicated one."
                    },
                    "only_one_molecule": {
                        "description": "Only one molecule.",
                        "message": "There is only one molecule in the chemical equation."
                    },
                    "no_equal_sign": {
                        "description": "No equal sign.",
                        "message": "There is no equal sign in this chemical equation."
                    }
                }
            }
        }
    }))

    #  Chinese-simplified translation.
    _l10n_reg.register_message_tree(_l10n_msgtree.ChineseSimplifiedMessageTree({
        "parser": {
            "cexp": {
                "error": {
                    "parenthesis_mismatch": {
                        "description": "括号不匹配。",
                        "left": "缺少与此括号相匹配的左括号。",
                        "right": "缺少与此括号相匹配的右括号。",
                    },
                    "mixed_form": {
                        "description": "混合形式。",
                        "message": "该化学方程式同时包含了一般形式和自动分界形式。"
                    },
                    "empty_expression": {
                        "description": "空表达式。"
                    },
                    "no_content": {
                        "description": "缺少内容。",
                        "operator_between": "这两个操作符之间缺少内容。",
                        "operator_before": "该操作符之前缺少内容。",
                        "operator_after": "该操作符之后缺少内容。"
                    },
                    "parsing_molecule": {
                        "message": "在解析该分子式时发生错误。"
                    },
                    "duplicated_equal_sign": {
                        "description": "重复的等号。",
                        "previous": "这是上一个等号。",
                        "duplicated": "这是重复的等号。"
                    },
                    "only_one_molecule": {
                        "description": "单分子方程。",
                        "message": "该化学方程式中仅包含一个分子。"
                    },
                    "no_equal_sign": {
                        "description": "无等号。",
                        "message": "该化学方程式中无等号。"
                    }
                }
            }
        }
    }))
