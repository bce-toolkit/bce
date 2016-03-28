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
            "molecule": {
                "error": {
                    "parenthesis_mismatch": {
                        "description": "Parenthesis mismatch.",
                        "left": "Missing left parenthesis matches with this parenthesis.",
                        "right": "Missing right parenthesis matches with this parenthesis.",
                        "incorrect": "Incorrect parenthesis, this parenthesis should be changed to '$1'."
                    },
                    "no_content": {
                        "description": "No content.",
                        "before": "There is no content before this position.",
                        "after": "There is no content after this position.",
                        "inside": "There is no content inside."
                    },
                    "parsing_mexp": {
                        "message": "An error occurred when parsing and evaluating this math expression."
                    },
                    "parsing_abbreviation": {
                        "origin": "An error occurred when parsing the abbreviation.",
                        "expand": "An error occurred when parsing the expanded expression."
                    },
                    "unrecognized_token": {
                        "description": "Unrecognized token.",
                        "message": "This token is unexpected."
                    },
                    "unexpected_token": {
                        "description": "Unexpected token.",
                        "electronic_suffix": "Expect positivity descriptor(e+/e-) or an integer here.",
                        "electronic_end": "Expect a '>' here.",
                        "electronic_misplaced": "Misplaced status descriptor. It should be put at the end of the " +
                                                "molecule.",
                        "other": "This token is unexpected."
                    },
                    "domain_error": {
                        "description": "Domain error.",
                        "prefix": "The prefix operand shouldn't be less than or equal to zero.",
                        "electronic_charge": "The electronic charge shouldn't be less than or equal to zero.",
                        "suffix": "The suffix operand shouldn't be less than or equal to zero."
                    },
                    "exceed_operand": {
                        "description": "Exceed operand.",
                        "prefix": "The prefix operand is exceed and it should be removed.",
                        "electronic_charge": "The charge is exceed and it should be removed.",
                        "suffix": "The suffix operand is exceed and it should be removed."
                    },
                    "element_eliminated": {
                        "description": "Element eliminated.",
                        "message": "Element '$1' was eliminated."
                    },
                    "unsupported_abbreviation": {
                        "description": "Unsupported abbreviation.",
                        "message": "The abbreviation is unsupported."
                    }
                }
            }
        }
    }))

    #  Chinese-simplified translation.
    _l10n_reg.register_message_tree(_l10n_msgtree.ChineseSimplifiedMessageTree({
        "parser": {
            "molecule": {
                "error": {
                    "parenthesis_mismatch": {
                        "description": "括号不匹配。",
                        "left": "缺少与此括号相匹配的左括号。",
                        "right": "缺少与此括号相匹配的右括号。",
                        "incorrect": "不正确的括号，该括号应该为 '$1'。"
                    },
                    "no_content": {
                        "description": "缺少内容。",
                        "before": "该位置之前缺少内容。",
                        "after": "该位置之后缺少内容。",
                        "inside": "缺少内部内容。"
                    },
                    "parsing_mexp": {
                        "message": "在解析该数学表达式时发生错误。"
                    },
                    "parsing_abbreviation": {
                        "origin": "在解析该缩写时发生错误。",
                        "expand": "在解析该展开式时发生错误。"
                    },
                    "unrecognized_token": {
                        "description": "无法识别的记号。",
                        "message": "该记号无法被识别。"
                    },
                    "unexpected_token": {
                        "description": "未期望的记号。",
                        "electronic_suffix": "这里被期望是一个电荷正负性描述符 (e+/e-) 或一个整数。",
                        "electronic_end": "这里被期望是一个 '>'。",
                        "electronic_misplaced": "状态描述符位置不正确。它应该被放到分子表达式的最后。",
                        "other": "该符号未被期望。"
                    },
                    "domain_error": {
                        "description": "定义域错误。",
                        "prefix": "该前缀数不应该小于等于零。",
                        "electronic_charge": "该电量描述符的数值不应该小于等于零。",
                        "suffix": "该后缀数不应该小于等于零。"
                    },
                    "exceed_operand": {
                        "description": "多余的操作数",
                        "prefix": "该前缀操作数是多余的，它应当被删除。",
                        "electronic_charge": "该电量描述符是多余的，它应当被删除。",
                        "suffix": "该后缀操作数是多余的，它应当被删除。"
                    },
                    "element_eliminated": {
                        "description": "元素被消去。",
                        "message": "元素 '$1' 被消去。"
                    },
                    "unsupported_abbreviation": {
                        "description": "不支持的缩写。",
                        "message": "该所写不被支持。"
                    }
                }
            }
        }
    }))
