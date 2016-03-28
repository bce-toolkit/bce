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
        "shell": {
            "console": {
                "error": {
                    "invalid_character": {
                        "description": "Found invalid character(s) in the expression."
                    },
                    "invalid_unknown_header": {
                        "description": "Invalid unknown header."
                    },
                    "file_reading_error": {
                        "description": "Can't read file \"$1\"."
                    },
                    "file_corrupted": {
                        "description": "Corrupted file \"$1\"."
                    }
                },
                "command": {
                    "header": "BCE - Chemical Equation Balancer",
                    "output_mathml": "Show output in MathML format.",
                    "disable_banner": "Disable the start-up banner.",
                    "disable_bundled_abbreviations": "Disable bundled abbreviations.",
                    "disable_error_correction": "Disable the error-correction feature.",
                    "disable_auto_arranging": "Disable the auto-arranging feature.",
                    "unknown_header": "Set the header of unknown symbols.",
                    "load_abbreviations_file": "Load extra abbreviations from specified file.",
                    "language": "Set the software language." +
                                "(Available: \"en_US\" [English(US)], \"zh_CN\", \"zh_Hans\" [Simplified Chinese])",
                    "show_version": "Show the software version."
                },
                "application": {
                    "banner": "BCE V$1.$2.$3",
                    "copyright": "Copyright (C) 2014 - 2015 The BCE Authors. All rights reserved.",
                    "version": "bce-$1.$2.$3"
                }
            }
        }
    }))

    #  Chinese-simplified translation.
    _l10n_reg.register_message_tree(_l10n_msgtree.ChineseSimplifiedMessageTree({
        "shell": {
            "console": {
                "error": {
                    "invalid_character": {
                        "description": "表达式中存在无效字符。"
                    },
                    "invalid_unknown_header": {
                        "description": "无效的未知量符号前缀。"
                    },
                    "file_reading_error": {
                        "description": "无法读取文件 \"$1\"。"
                    },
                    "file_corrupted": {
                        "description": "文件 \"$1\" 已损坏。"
                    }
                },
                "command": {
                    "header": "BCE - 化学方程式配平程序",
                    "output_mathml": "将结果显示为 MathML 格式。",
                    "disable_banner": "禁用启动时标语。",
                    "disable_bundled_abbreviations": "禁用自带的各种缩写符号。",
                    "disable_error_correction": "禁用自动纠错特性。",
                    "disable_auto_arranging": "禁用自动分界特性。",
                    "unknown_header": "设置系统未知量符号前缀。",
                    "load_abbreviations_file": "从指定文件中读取额外(非自带的)的缩写符号。",
                    "language": "设置软件语言。" +
                                "(可用选项: \"en_US\" [英语(美国)], \"zh_CN\", \"zh_Hans\" [中文(简体)])",
                    "version": "显示软件版本。"
                },
                "application": {
                    "banner": "BCE V$1.$2.$3",
                    "copyright": "版权所有 (C) 2014 - 2015 BCE 的作者，保留所有权利。",
                    "version": "bce-$1.$2.$3"
                }
            }
        }
    }))
