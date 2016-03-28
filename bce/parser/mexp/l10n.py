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
            "mexp": {
                "error": {
                    "duplicated_decimal_dot": {
                        "description": "Duplicated decimal dot.",
                        "previous_dot": "Here's the previous decimal dot.",
                        "duplicated_dot": "Here's the duplicated decimal dot."
                    },
                    "protected_header": {
                        "description": "Used protected header.",
                        "message": "This symbol begins with the protected symbol header '$1'."
                    },
                    "unrecognized_token": {
                        "description": "Unrecognized token.",
                        "message": "This token can't be recognized."
                    },
                    "missing_operand": {
                        "description": "Missing operand.",
                        "left": "This operator has no left operand.",
                        "right": "This operator has no right operand."
                    },
                    "missing_operator": {
                        "description": "Missing operator.",
                        "multiply_before": "Missing a multiply operator before this token."
                    },
                    "unsupported_function": {
                        "description": "Unsupported function.",
                        "message": "The function '$1' hasn't been supported yet."
                    },
                    "no_content": {
                        "description": "No content.",
                        "in_parentheses": "There is no content between these parentheses.",
                        "in_argument": "This argument has no content."
                    },
                    "parenthesis_mismatch": {
                        "description": "Parenthesis mismatch.",
                        "left": "Missing left parenthesis matches with this parenthesis.",
                        "right": "Missing right parenthesis matches with this parenthesis.",
                        "incorrect": "Incorrect parenthesis, this parenthesis should be changed to '$1'."
                    },
                    "argument_count_mismatch": {
                        "description": "Argument count mismatch.",
                        "message": "This function requires $1 argument(s), but $2 argument(s) was/were provided."
                    },
                    "illegal_separator": {
                        "description": "Illegal argument separator.",
                        "message": "This argument separator was misplaced."
                    },
                    "divide_zero": {
                        "description": "Divide zero.",
                        "message": "The division is zero."
                    },
                    "domain_out_of_range": {
                        "description": "Domain is out of range.",
                        "message": "The value of the $1(st/nd/th) argument is out of its domain range."
                    }
                }
            }
        }
    }))

    #  Chinese-simplified translation.
    _l10n_reg.register_message_tree(_l10n_msgtree.ChineseSimplifiedMessageTree({
        "parser": {
            "mexp": {
                "error": {
                    "duplicated_decimal_dot": {
                        "description": "重复的小数点。",
                        "previous_dot": "这是上一个小数点。",
                        "duplicated_dot": "这是重复的小数点。"
                    },
                    "protected_header": {
                        "description": "使用了受保护的符号头.",
                        "message": "该符号使用了受保护的符号头 '$1'。"
                    },
                    "unrecognized_token": {
                        "description": "无法识别的记号。",
                        "message": "该记号无法被识别。"
                    },
                    "missing_operand": {
                        "description": "缺少操作数。",
                        "left": "该运算符没有左操作数。",
                        "right": "该运算符没有右操作数。"
                    },
                    "missing_operator": {
                        "description": "缺少操作符。",
                        "multiply_before": "该记号前面缺少一个乘号 (*)。"
                    },
                    "unsupported_function": {
                        "description": "不支持的函数。",
                        "message": "函数 '$1' 不被支持。"
                    },
                    "no_content": {
                        "description": "缺少内容。",
                        "in_parentheses": "该对括号内没有内容。",
                        "in_argument": "该参数缺少内容。"
                    },
                    "parenthesis_mismatch": {
                        "description": "括号不匹配。",
                        "left": "缺少与此括号相匹配的左括号。",
                        "right": "缺少与此括号相匹配的右括号。",
                        "incorrect": "不正确的括号，该括号应该为 '$1'。"
                    },
                    "argument_count_mismatch": {
                        "description": "参数个数不匹配。",
                        "message": "该函数需要 $1 个参数，但仅指定了 $2 个。"
                    },
                    "illegal_separator": {
                        "description": "非法的分隔符。",
                        "message": "该参数分隔符位于非法的位置。"
                    },
                    "divide_zero": {
                        "description": "除数为零。",
                        "message": "该除法的除数为零。"
                    },
                    "domain_out_of_range": {
                        "description": "定义域错误。",
                        "message": "第 $1 个参数的值超出了它的定义域。"
                    }
                }
            }
        }
    }))
